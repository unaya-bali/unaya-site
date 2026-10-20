// Étape 2 : Midtrans appelle cette adresse quand le statut d'un paiement change.
// Réglage Midtrans : Settings > Payment > Notification URL = https://<site>/api/pay/notify
// On vérifie la signature, on reconfirme le statut auprès de Midtrans, puis on informe Beds24 (notify.php).
import { apiBase, midAuth, sha512hex } from '../../../lib/pay.js';

export async function onRequestPost({ request, env }) {
  if (!env.MIDTRANS_SERVER_KEY || !env.BEDS24_GATEWAY_KEY) return new Response('not configured', { status: 500 });
  let n;
  try { n = await request.json(); } catch { return new Response('bad json', { status: 400 }); }
  const { order_id = '', status_code = '', gross_amount = '', signature_key = '' } = n;
  const expected = await sha512hex(order_id + status_code + gross_amount + env.MIDTRANS_SERVER_KEY);
  if (expected !== signature_key) return new Response('bad signature', { status: 403 });

  const m = /^UNAYA-(\d+)-/.exec(order_id);
  if (!m) return new Response('ok'); // transaction qui ne vient pas du site : ignorée
  const bookId = m[1];

  // Double contrôle : on redemande le statut à Midtrans.
  const s = await fetch(`${apiBase(env)}/v2/${encodeURIComponent(order_id)}/status`, { headers: { Authorization: midAuth(env), Accept: 'application/json' } });
  if (!s.ok) return new Response('status check failed', { status: 502 });
  const st = await s.json();
  const paid = st.transaction_status === 'settlement' || (st.transaction_status === 'capture' && st.fraud_status === 'accept');
  if (!paid) return new Response('ok'); // en attente, expiré ou refusé : rien à faire

  const amount = Math.round(parseFloat(st.gross_amount));
  const body = new URLSearchParams({
    key: env.BEDS24_GATEWAY_KEY,
    bookid: bookId,
    status: '1',
    amount: String(amount),
    description: `Paiement Midtrans (${st.payment_type || 'en ligne'}) ${order_id}`,
    txnid: st.transaction_id || order_id,
  });
  const b = await fetch('https://api.beds24.com/custompaymentgateway/notify.php', { method: 'POST', body });
  const txt = (await b.text()).trim();
  if (!b.ok || txt) return new Response('beds24: ' + txt.slice(0, 200), { status: 502 }); // Midtrans réessaiera
  return new Response('ok');
}
