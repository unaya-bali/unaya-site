// Étape 2 : Midtrans appelle cette adresse quand le statut d'un paiement change.
// Réglage Midtrans : Settings > Payment > Notification URL = https://<site>/api/pay/notify
// On vérifie la signature, on reconfirme le statut auprès de Midtrans, puis on informe Beds24 (notify.php).
// Une fois la signature vérifiée, on répond TOUJOURS 200 à Midtrans (même si Beds24 refuse, ex. paiement déjà
// enregistré ou réservation annulée) : l'erreur est journalisée et, si Resend est configuré, envoyée par e-mail.
import { apiBase, midAuth, sha512hex, beds24Paid, payFail } from '../../../lib/pay.js';

export async function onRequestPost({ request, env }) {
  if (!env.MIDTRANS_SERVER_KEY) return new Response('not configured', { status: 500 });
  let n;
  try { n = await request.json(); } catch { return new Response('bad json', { status: 400 }); }
  const order_id = String(n.order_id || ''), status_code = String(n.status_code || ''), gross_amount = String(n.gross_amount || '');
  const expected = await sha512hex(order_id + status_code + gross_amount + env.MIDTRANS_SERVER_KEY);
  if (expected !== String(n.signature_key || '')) return new Response('bad signature', { status: 403 });

  // Signature valide : à partir d'ici, réponse 200 quoi qu'il arrive.
  try {
    const m = /^UNAYA-(\d+)-/.exec(order_id);
    if (!m) return ok('ignored: not a site order');
    const bookId = m[1];

    // Double contrôle : on redemande le statut à Midtrans.
    const s = await fetch(`${apiBase(env)}/v2/${encodeURIComponent(order_id)}/status`, { headers: { Authorization: midAuth(env), Accept: 'application/json' } });
    if (!s.ok) return await fail(env, order_id, 'Midtrans status check HTTP ' + s.status);
    const st = await s.json();
    const paid = st.transaction_status === 'settlement' || (st.transaction_status === 'capture' && st.fraud_status === 'accept');
    if (!paid) return ok('no action: ' + st.transaction_status);

    const amount = Math.round(parseFloat(st.gross_amount));
    const err = await beds24Paid(env, bookId, amount, `Paiement Midtrans (${st.payment_type || 'en ligne'}) ${order_id}`, st.transaction_id || order_id);
    if (err) return await fail(env, order_id, err);
    return ok('beds24 updated');
  } catch (e) {
    return await fail(env, order_id, 'Exception: ' + (e && e.message));
  }
}

function ok(msg) { return new Response(msg, { status: 200 }); }

function fail(env, orderId, msg) { return payFail(env, 'Midtrans', orderId, msg); }
