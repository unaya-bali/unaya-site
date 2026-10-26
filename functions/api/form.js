// Cloudflare Pages Function : reçoit les formulaires du site et les envoie par e-mail via Resend.
// Variables à définir dans Cloudflare Pages > Settings > Environment variables :
//   RESEND_API_KEY  (clé API Resend — à saisir par vous, jamais dans le code)
//   FORM_TO         (destinataire, ex. info@unayabali.com)
//   FORM_FROM       (expéditeur vérifié dans Resend, ex. "Site Unaya <site@unayabali.com>")
export async function onRequestPost({ request, env }) {
  const data = await request.formData();
  const lang = data.get('lang') === 'en' ? 'en' : 'fr';
  const thanks = lang === 'en' ? '/thank-you/' : '/fr/merci/';
  // Anti-spam : champ caché rempli = robot
  if (data.get('site_web')) return Response.redirect(new URL(thanks, request.url), 303);
  // Anti-spam 2 : le formulaire doit avoir été rempli dans un vrai navigateur (jeton posé par site.js, au moins 3 s)
  const t0 = Number(data.get('t_ok') || 0);
  if (!t0 || Date.now() - t0 < 3000) return Response.redirect(new URL(thanks, request.url), 303);
  // Anti-spam 3 : fausse adresse imitant notre domaine (ex. search-unayabali.com) = arnaque
  const mail = String(data.get('e_mail') || data.get('email') || '').toLowerCase();
  const dom = mail.split('@')[1] || '';
  if (dom.includes('unayabali') && dom !== 'unayabali.com') return Response.redirect(new URL(thanks, request.url), 303);
  const msgAll = [...data.values()].map(String).join(' ').toLowerCase();
  const spammy = /(search ?index|searchregister|seo |backlink|rank(ing)? (on|in) google|crypto|casino|bitcoin|guest post)/.test(msgAll);

  const svc = data.get('service_demande');
  const formName = svc ? `Service voyageur — ${svc} (${lang})` : String(data.get('form-name') || 'formulaire');
  const skip = new Set(['form-name', 'site_web', 'lang', 't_ok']);
  const rows = [];
  for (const [k, v] of data.entries()) {
    if (skip.has(k)) continue;
    const val = String(v).slice(0, 5000);
    rows.push(`<tr><td style="padding:6px 12px;color:#5A3552;vertical-align:top"><b>${esc(k)}</b></td><td style="padding:6px 12px">${esc(val).replace(/\n/g, '<br>')}</td></tr>`);
  }
  const replyTo = String(data.get('e_mail') || data.get('email') || '');
  const html = `<div style="font-family:Arial,sans-serif;color:#2E2429"><h2 style="color:#3F2A3A">Nouvelle demande — ${esc(formName)}</h2><table style="border-collapse:collapse">${rows.join('')}</table><p style="color:#8B5A46">Envoyé depuis unayabali.com</p></div>`;

  if (!env.RESEND_API_KEY) return new Response('Formulaire non configuré (RESEND_API_KEY manquante).', { status: 500 });
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: env.FORM_FROM || 'Site Unaya <site@unayabali.com>',
      to: [env.FORM_TO || 'info@unayabali.com'],
      subject: `${spammy ? '[Spam probable] ' : ''}[Site] ${formName}`,
      html,
      ...(replyTo.includes('@') ? { reply_to: replyTo } : {}),
    }),
  });
  if (!r.ok) return new Response(lang === 'en' ? 'Sorry, your message could not be sent. Please email info@unayabali.com.' : "Désolé, votre message n'a pas pu être envoyé. Écrivez-nous à info@unayabali.com.", { status: 502 });
  return Response.redirect(new URL(thanks, request.url), 303);
}
function esc(s) { return s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
