// Outils communs au paiement Midtrans <-> Beds24.
// Variables Cloudflare (Settings > Variables et secrets) — à saisir par vous, jamais dans le code :
//   MIDTRANS_SERVER_KEY   (Secret)  clé serveur Midtrans (Sandbox pour les tests, Production ensuite)
//   MIDTRANS_ENV          "sandbox" (défaut) ou "production"
//   BEDS24_GATEWAY_KEY    (Secret)  même valeur que le champ « Key » de la Passerelle personnalisée Beds24
//   BEDS24_REFRESH_TOKEN  (Secret)  jeton API Beds24 v2 (lecture des réservations) — sert à vérifier le montant
//   DEPOSIT_PERCENT       acompte demandé en % du total (défaut 30)
//   TEST_AMOUNT           (mode sandbox sans API Beds24) montant fictif en IDR, défaut 100000
//   PAY_PROVIDER          "midtrans" (défaut) ou "xendit" — prestataire utilisé pour les nouveaux paiements
//   XENDIT_SECRET_KEY     (Secret)  clé API secrète Xendit (clé de test xnd_development_… puis clé live)
//   XENDIT_CALLBACK_TOKEN (Secret)  « Verification token » des callbacks Xendit (Settings > Webhooks)

export const isProd = env => (env.MIDTRANS_ENV || 'sandbox') === 'production';
export const snapUrl = env => isProd(env) ? 'https://app.midtrans.com/snap/v1/transactions' : 'https://app.sandbox.midtrans.com/snap/v1/transactions';
export const apiBase = env => isProd(env) ? 'https://api.midtrans.com' : 'https://api.sandbox.midtrans.com';
export const midAuth = env => 'Basic ' + btoa(env.MIDTRANS_SERVER_KEY + ':');

export async function sha512hex(s) {
  const buf = await crypto.subtle.digest('SHA-512', new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

// Lit une réservation via l'API Beds24 v2 (renvoie null si non configurée ou introuvable).
export async function getBooking(env, bookId) {
  if (!env.BEDS24_REFRESH_TOKEN) return null;
  const t = await fetch('https://beds24.com/api/v2/authentication/token', { headers: { refreshToken: env.BEDS24_REFRESH_TOKEN } });
  if (!t.ok) throw new Error('Beds24 token ' + t.status);
  const { token } = await t.json();
  const r = await fetch('https://beds24.com/api/v2/bookings?id=' + encodeURIComponent(bookId), { headers: { token } });
  if (!r.ok) throw new Error('Beds24 booking ' + r.status);
  const j = await r.json();
  return (j.data && j.data[0]) || null;
}

export const UNAYA_PROPS = new Set(['359816', '359817', '359818']);

export function page(lang, title, msg, status = 200) {
  const back = lang === 'en' ? '/' : '/fr/';
  const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title><link rel="stylesheet" href="/assets/css/site.css"></head><body><main><section style="max-width:760px;margin:0 auto;padding:72px 24px"><img src="/assets/logos/unaya-management-horizontal.svg" alt="Unaya Management" style="height:40px;margin-bottom:40px"><h1 style="font-family:'Cormorant Garamond',serif;font-weight:400;font-size:44px;color:#3F2A3A;margin:0 0 16px">${title}</h1><p>${msg}</p><p><a href="${back}">← ${lang === 'en' ? 'Back to home' : "Retour à l'accueil"}</a></p></section></main></body></html>`;
  return new Response(html, { status, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
}

export const provider = env => (env.PAY_PROVIDER || 'midtrans').toLowerCase() === 'xendit' ? 'xendit' : 'midtrans';
export const xenAuth = env => 'Basic ' + btoa(env.XENDIT_SECRET_KEY + ':');

// Enregistre un paiement dans Beds24 (passerelle personnalisée). Renvoie '' si OK, sinon le message d'erreur.
export async function beds24Paid(env, bookId, amount, description, txnid) {
  if (!env.BEDS24_GATEWAY_KEY) return 'BEDS24_GATEWAY_KEY manquante';
  const body = new URLSearchParams({ key: env.BEDS24_GATEWAY_KEY, bookid: String(bookId), status: '1', amount: String(Math.round(amount)), description, txnid });
  const b = await fetch('https://api.beds24.com/custompaymentgateway/notify.php', { method: 'POST', body });
  const txt = (await b.text()).trim();
  return (!b.ok || txt) ? `Beds24 HTTP ${b.status}: ${txt.slice(0, 300)}` : '';
}

// Alerte e-mail (Resend) quand un paiement reçu n'a pas pu être reporté dans Beds24. Répond toujours 200.
export async function payFail(env, provName, orderId, msg) {
  console.log('[pay]', provName, orderId, msg);
  try {
    if (env.RESEND_API_KEY) {
      await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({
          from: env.FORM_FROM || 'Site Unaya <site@unayabali.com>',
          to: [env.FORM_TO || 'info@unayabali.com'],
          subject: `[Paiement] À vérifier — ${orderId}`,
          text: `Paiement ${provName} reçu mais Beds24 n'a pas été mis à jour automatiquement.\n\nCommande : ${orderId}\nDétail : ${msg}\n\nVérifiez la réservation dans Beds24 et ajoutez le paiement à la main si nécessaire.`,
        }),
      });
    }
  } catch (e) { /* l'alerte ne doit jamais bloquer la réponse */ }
  return new Response('received; follow-up needed: ' + msg, { status: 200 });
}
