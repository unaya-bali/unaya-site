// Callback Xendit (facture payée). Réglage Xendit : Settings > Webhooks > « Invoices paid »
//   URL = https://unayabali.com/api/pay/xendit   ; le « Verification token » va dans la variable XENDIT_CALLBACK_TOKEN.
// On vérifie le jeton, on redemande la facture à Xendit (double contrôle), puis on informe Beds24.
// Une fois le jeton vérifié, on répond TOUJOURS 200 (sinon Xendit réessaie) ; les erreurs partent par e-mail.
import { xenAuth, beds24Paid, payFail } from '../../../lib/pay.js';

export async function onRequestPost({ request, env }) {
  if (!env.XENDIT_SECRET_KEY || !env.XENDIT_CALLBACK_TOKEN) return new Response('not configured', { status: 500 });
  if (request.headers.get('x-callback-token') !== env.XENDIT_CALLBACK_TOKEN) return new Response('bad token', { status: 403 });
  let n;
  try { n = await request.json(); } catch { return new Response('bad json', { status: 400 }); }
  const ext = String(n.external_id || '');
  try {
    const m = /^UNAYA-(\d+)-/.exec(ext);
    if (!m) return ok('ignored: not a site order');
    const s = await fetch(`https://api.xendit.co/v2/invoices/${encodeURIComponent(String(n.id || ''))}`, { headers: { Authorization: xenAuth(env) } });
    if (!s.ok) return await payFail(env, 'Xendit', ext, 'Xendit invoice check HTTP ' + s.status);
    const inv = await s.json();
    if (inv.external_id !== ext) return await payFail(env, 'Xendit', ext, 'external_id différent');
    if (!['PAID', 'SETTLED'].includes(String(inv.status))) return ok('no action: ' + inv.status);
    const amount = Number(inv.paid_amount || inv.amount || 0);
    const err = await beds24Paid(env, m[1], amount, `Paiement Xendit (${inv.payment_method || inv.payment_channel || 'en ligne'}) ${ext}`, String(inv.id || ext));
    if (err) return await payFail(env, 'Xendit', ext, err);
    return ok('beds24 updated');
  } catch (e) {
    return await payFail(env, 'Xendit', ext, 'Exception: ' + (e && e.message));
  }
}
function ok(msg) { return new Response(msg, { status: 200 }); }
