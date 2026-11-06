// Page interne (lien reçu dans l'e-mail de demande) : crée le lien de paiement Xendit d'un service voyageur
// et l'envoie au client par e-mail. GET = formulaire (montant modifiable) ; POST = création + envoi.
import { readOrder } from '../../../lib/svc.js';
import { xenAuth } from '../../../lib/pay.js';

const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const shell = (title, body) => new Response(`<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>${title}</title><link rel="stylesheet" href="/assets/css/site.css"></head><body><main><section style="max-width:680px;margin:0 auto;padding:56px 24px"><img src="/assets/logos/unaya-management-horizontal.svg" alt="Unaya Management" style="height:36px;margin-bottom:32px"><h1 style="font-family:'Cormorant Garamond',serif;font-weight:400;font-size:38px;color:#3F2A3A;margin:0 0 16px">${title}</h1>${body}</section></main></body></html>`, { headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' } });
const field = 'width:100%;box-sizing:border-box;font-family:Jost,sans-serif;font-size:16px;padding:12px;border:1px solid #D9CCC2;background:#fff;color:#2E2429';
const label = 'display:flex;flex-direction:column;gap:6px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#5A3552';

export async function onRequestGet({ request, env }) {
  const u = new URL(request.url);
  const o = await readOrder(env, u.searchParams.get('d'), u.searchParams.get('sig'));
  if (!o) return shell('Lien invalide ou expiré', '<p>Ce lien de création de paiement n\'est pas valide (ou a plus de 60 jours). Créez le lien directement dans Xendit → Payment Links.</p>');
  return shell('Vérifier le montant', `
<p style="margin:0 0 12px;padding:12px 16px;background:#F3E9E2;border-left:4px solid #D2A48C">Étape 2 sur 2 — vérifiez ou <strong>modifiez le montant</strong> et la description, puis confirmez. Rien n'est envoyé au client tant que vous n'avez pas confirmé.</p>
<p style="margin:0 0 20px">Client : <strong>${esc(o.n)}</strong> · ${esc(o.e)}${o.w ? ' · WhatsApp ' + esc(o.w) : ''}</p>
<form method="POST" style="display:flex;flex-direction:column;gap:16px;background:#fff;border:1px solid #E6DCD4;padding:24px">
<input type="hidden" name="d" value="${esc(u.searchParams.get('d'))}"><input type="hidden" name="sig" value="${esc(u.searchParams.get('sig'))}">
<label style="${label}">Description (vue par le client)<textarea name="desc" rows="3" style="${field}">${esc(o.d)}</textarea></label>
<label style="${label}">Montant en IDR (modifiable)${o.a ? ' — proposé : ' + esc(Number(o.a).toLocaleString('fr-FR').replace(/\u202f/g, ' ')) : ' — à compléter'}<input name="amount" inputmode="numeric" required value="${o.a ? esc(o.a) : ''}" placeholder="ex. 450000" autofocus style="${field};font-size:26px;font-weight:500;border:2px solid #D2A48C"></label>
<label style="${label}">E-mail du client<input name="email" type="email" value="${esc(o.e)}" style="${field}"></label>
<label style="display:flex;gap:10px;align-items:center;font-size:15px"><input type="checkbox" name="send" value="1" checked> Envoyer le lien au client par e-mail (copie à info@)</label>
<button type="submit" style="height:52px;border:none;background:#3F2A3A;color:#F7F2EE;font-size:13px;letter-spacing:.2em;text-transform:uppercase;cursor:pointer">Confirmer ce montant et envoyer le lien</button>
<p style="margin:0;font-size:13px;color:#5A4E54">À faire seulement après avoir vérifié la disponibilité. Le lien est valable 3 jours ; le client paie par carte, virement, QRIS ou e-wallet.</p>
</form>`);
}

export async function onRequestPost({ request, env }) {
  const f = await request.formData();
  const o = await readOrder(env, String(f.get('d') || ''), String(f.get('sig') || ''));
  if (!o) return shell('Lien invalide ou expiré', '<p>Recommencez depuis l\'e-mail de la demande, ou créez le lien dans Xendit → Payment Links.</p>');
  const amount = Math.round(Number(String(f.get('amount') || '').replace(/[^\d]/g, '')));
  const desc = String(f.get('desc') || o.d).slice(0, 250);
  const email = String(f.get('email') || o.e).trim();
  if (!(amount >= 10000)) return shell('Montant manquant', '<p>Indiquez un montant d\'au moins 10 000 IDR. <a href="javascript:history.back()">← Retour</a></p>');
  const en = o.l === 'en';
  const ret = `https://unayabali.com${en ? '' : '/fr'}/${en ? 'payment' : 'paiement'}/`;
  const x = await fetch('https://api.xendit.co/v2/invoices', {
    method: 'POST',
    headers: { Authorization: xenAuth(env), 'Content-Type': 'application/json' },
    body: JSON.stringify({
      external_id: `SVC-${o.s}-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      amount, currency: 'IDR', description: desc, invoice_duration: 3 * 86400,
      ...(email.includes('@') ? { payer_email: email } : {}),
      customer: { given_names: o.n || undefined, email: email.includes('@') ? email : undefined },
      success_redirect_url: ret + '?transaction_status=settlement',
      failure_redirect_url: ret + '?transaction_status=failed',
    }),
  });
  if (!x.ok) { let c = ''; try { c = (await x.json()).error_code || ''; } catch {} return shell('Erreur Xendit', `<p>Le lien n'a pas pu être créé (code ${esc(x.status)} ${esc(c)}). Créez-le dans Xendit → Payment Links.</p>`); }
  const inv = await x.json();
  const link = inv.invoice_url;
  const amt = amount.toLocaleString(en ? 'en-US' : 'fr-FR').replace(/ /g, ' ');
  let mailInfo = '';
  if (f.get('send') && email.includes('@') && env.RESEND_API_KEY) {
    const subject = en ? `Your payment link — ${desc.split(' · ')[0]}` : `Votre lien de paiement — ${desc.split(' · ')[0]}`;
    const body = en
      ? `<p>Hello ${esc(o.n)},</p><p>Your request is confirmed. Here is your secure payment link:</p><p><strong>${esc(desc)}</strong><br>Amount: <strong>IDR ${amt}</strong></p><p><a href="${link}" style="background:#3F2A3A;color:#F7F2EE;padding:14px 22px;text-decoration:none;border-radius:4px">Pay now</a></p><p>Card, bank transfer, QRIS or e-wallet. The link is valid for 3 days.</p><p>See you soon,<br>The Unaya team</p>`
      : `<p>Bonjour ${esc(o.n)},</p><p>Votre demande est confirmée. Voici votre lien de paiement sécurisé :</p><p><strong>${esc(desc)}</strong><br>Montant : <strong>IDR ${amt}</strong></p><p><a href="${link}" style="background:#3F2A3A;color:#F7F2EE;padding:14px 22px;text-decoration:none;border-radius:4px">Payer maintenant</a></p><p>Carte bancaire, virement, QRIS ou e-wallet. Le lien est valable 3 jours.</p><p>À très bientôt,<br>L'équipe Unaya</p>`;
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST', headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: env.FORM_FROM || 'Site Unaya <site@unayabali.com>', to: [email], cc: [env.FORM_TO || 'info@unayabali.com'], reply_to: env.FORM_TO || 'info@unayabali.com', subject, html: `<div style="font-family:Arial,sans-serif;color:#2E2429">${body}</div>` }),
    });
    mailInfo = r.ok ? `<p>✅ Lien envoyé par e-mail à <strong>${esc(email)}</strong> (copie à info@).</p>` : '<p>⚠️ L\'e-mail au client n\'a pas pu partir : envoyez le lien ci-dessous sur WhatsApp.</p>';
  }
  const waNum = String(o.w || '').replace(/[^\d]/g, '');
  const waText = encodeURIComponent((en ? `Hello ${o.n}, here is your secure payment link for ${desc} (IDR ${amt}): ` : `Bonjour ${o.n}, voici votre lien de paiement sécurisé pour ${desc} (IDR ${amt}) : `) + link);
  return shell('Lien de paiement créé', `${mailInfo}
<p style="margin:16px 0 8px"><strong>${esc(desc)}</strong> — IDR ${amt}</p>
<p style="word-break:break-all;background:#fff;border:1px solid #E6DCD4;padding:12px">${esc(link)}</p>
<p style="display:flex;gap:12px;flex-wrap:wrap"><a href="${esc(link)}" target="_blank" rel="noopener" style="padding:12px 18px;border:1px solid #3F2A3A;color:#3F2A3A;text-decoration:none">Voir la page de paiement</a>${waNum ? `<a href="https://wa.me/${waNum}?text=${waText}" target="_blank" rel="noopener" style="padding:12px 18px;background:#25D366;color:#fff;text-decoration:none">Envoyer sur WhatsApp</a>` : ''}</p>
<p style="font-size:13px;color:#5A4E54">Quand le client a payé, vous recevez un e-mail « Paiement reçu » et le paiement apparaît dans Xendit → Transactions.</p>`);
}
