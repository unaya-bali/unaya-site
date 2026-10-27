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
  // Case anti-robot Cloudflare Turnstile (active dès que TURNSTILE_SECRET est défini dans Cloudflare)
  if (env.TURNSTILE_SECRET) {
    const fd = new FormData();
    fd.append('secret', env.TURNSTILE_SECRET);
    fd.append('response', String(data.get('cf-turnstile-response') || ''));
    const ip = request.headers.get('CF-Connecting-IP'); if (ip) fd.append('remoteip', ip);
    const v = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', { method: 'POST', body: fd }).then(r => r.json()).catch(() => ({ success: false }));
    if (!v.success) return new Response(lang === 'en' ? 'Please tick the anti-robot box, then send the form again.' : 'Merci de cocher la case anti-robot, puis renvoyez le formulaire.', { status: 400, headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
  }
  const msgAll = [...data.values()].map(String).join(' ').toLowerCase();
  const spammy = /(search ?index|searchregister|seo |backlink|rank(ing)? (on|in) google|crypto|casino|bitcoin|guest post)/.test(msgAll);

  const svc = data.get('service_demande');
  const isEstim = data.get('type_demande') === 'estimation';
  const pick = (re) => { for (const [k, v] of data.entries()) if (re.test(k) && typeof v === 'string' && v) return v; return ''; };
  const formName = isEstim ? `Estimation revenus — ${pick(/^(zone|area)$/)} · ${pick(/chambres|bedrooms/)} ch. · ${pick(/^(e_mail|email)$/)} (${lang})`
    : svc ? `Service voyageur — ${svc} (${lang})` : String(data.get('form-name') || 'formulaire');
  const skip = new Set(['form-name', 'site_web', 'lang', 't_ok', 'cf-turnstile-response', 'type_demande']);
  const rows = [];
  const attachments = [];
  let attBytes = 0;
  for (const [k, v] of data.entries()) {
    if (skip.has(k)) continue;
    if (typeof v === 'object' && v && 'arrayBuffer' in v) {
      // Fichier joint (photos de la demande d'estimation) : 5 fichiers / 10 Mo maximum
      if (!v.size || attachments.length >= 5 || attBytes + v.size > 10 * 1024 * 1024) continue;
      attBytes += v.size;
      const buf = new Uint8Array(await v.arrayBuffer());
      let bin = ''; for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
      attachments.push({ filename: String(v.name || `photo-${attachments.length + 1}.jpg`).slice(0, 100), content: btoa(bin) });
      continue;
    }
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
      subject: `${spammy ? '[Spam probable] ' : ''}${isEstim ? '[Estimation revenus]' : '[Site]'} ${formName}`,
      html: attachments.length ? html.replace('</table>', `</table><p>${attachments.length} photo(s) en pièce jointe.</p>`) : html,
      ...(attachments.length ? { attachments } : {}),
      ...(replyTo.includes('@') ? { reply_to: replyTo } : {}),
    }),
  });
  if (!r.ok) return new Response(lang === 'en' ? 'Sorry, your message could not be sent. Please email info@unayabali.com.' : "Désolé, votre message n'a pas pu être envoyé. Écrivez-nous à info@unayabali.com.", { status: 502 });
  return Response.redirect(new URL(thanks, request.url), 303);
}
function esc(s) { return s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
