// Outils communs au paiement Midtrans <-> Beds24.
// Variables Cloudflare (Settings > Variables et secrets) — à saisir par vous, jamais dans le code :
//   MIDTRANS_SERVER_KEY   (Secret)  clé serveur Midtrans (Sandbox pour les tests, Production ensuite)
//   MIDTRANS_ENV          "sandbox" (défaut) ou "production"
//   BEDS24_GATEWAY_KEY    (Secret)  même valeur que le champ « Key » de la Passerelle personnalisée Beds24
//   BEDS24_REFRESH_TOKEN  (Secret)  jeton API Beds24 v2 (lecture des réservations) — sert à vérifier le montant
//   DEPOSIT_PERCENT       acompte minimum en % du total (défaut 30)

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
