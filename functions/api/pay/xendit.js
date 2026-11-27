// Callback Xendit (facture payée). Réglage Xendit : Settings > Webhooks > « Invoices paid »
//   URL = https://unayabali.com/api/pay/xendit   ; le « Verification token » va dans la variable XENDIT_CALLBACK_TOKEN.
// On vérifie le jeton, on redemande la facture à Xendit (double contrôle), puis on informe Beds24.
// Une fois le jeton vérifié, on répond TOUJOURS 200 (sinon Xendit réessaie) ; les erreurs partent par e-mail.
import { xenAuth, beds24Paid, payFail, getBooking, paidSoFar } from '../../../lib/pay.js';

export async function onRequestPost({ request, env }) {
  if (!env.XENDIT_SECRET_KEY || !env.XENDIT_CALLBACK_TOKEN) return new Response('not configured', { status: 500 });
  if (request.headers.get('x-callback-token') !== env.XENDIT_CALLBACK_TOKEN) return new Response('bad token', { status: 403 });
  let n;
  try { n = await request.json(); } catch { return new Response('bad json', { status: 400 }); }
  const ext = String(n.external_id || '');
  try {
    if (/^SVC-/.test(ext)) return await svcPaid(env, n, ext); // lien de paiement d'un service voyageur
    const m = /^UNAYA-(\d+)-/.exec(ext);
    if (!m) return ok('ignored: not a site order');
    const s = await fetch(`https://api.xendit.co/v2/invoices/${encodeURIComponent(String(n.id || ''))}`, { headers: { Authorization: xenAuth(env) } });
    if (!s.ok) return await payFail(env, 'Xendit', ext, 'Xendit invoice check HTTP ' + s.status);
    const inv = await s.json();
    if (inv.external_id !== ext) return await payFail(env, 'Xendit', ext, 'external_id différent');
    if (!['PAID', 'SETTLED'].includes(String(inv.status))) return ok('no action: ' + inv.status);
    const amount = Number(inv.paid_amount || inv.amount || 0);
    let b = null; try { b = await getBooking(env, m[1]); } catch { b = null; } // lu AVANT d'enregistrer le paiement
    const err = await beds24Paid(env, m[1], amount, `Paiement Xendit (${inv.payment_method || inv.payment_channel || 'en ligne'}) ${ext}`, String(inv.id || ext));
    await paidEmails(env, inv, m[1], amount, b, err).catch(() => {}); // alerte Unaya + reçu client (ne bloque jamais)
    if (err) return await payFail(env, 'Xendit', ext, err);
    return ok('beds24 updated');
  } catch (e) {
    return await payFail(env, 'Xendit', ext, 'Exception: ' + (e && e.message));
  }
}
function ok(msg) { return new Response(msg, { status: 200 }); }

// Service voyageur payé (lien créé depuis l'e-mail de demande) : double contrôle chez Xendit puis e-mail à Unaya.
async function svcPaid(env, n, ext) {
  const s = await fetch(`https://api.xendit.co/v2/invoices/${encodeURIComponent(String(n.id || ''))}`, { headers: { Authorization: xenAuth(env) } });
  if (!s.ok) return ok('svc: check failed ' + s.status);
  const inv = await s.json();
  if (inv.external_id !== ext || !['PAID', 'SETTLED'].includes(String(inv.status))) return ok('svc: no action');
  if (env.RESEND_API_KEY) {
    const amt = Number(inv.paid_amount || inv.amount || 0).toLocaleString('fr-FR').replace(/\u202f/g, ' ');
    const e = x => String(x ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    await fetch('https://api.resend.com/emails', {
      method: 'POST', headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: env.FORM_FROM || 'Site Unaya <site@unayabali.com>', to: [env.FORM_TO || 'info@unayabali.com'],
        subject: `[Paiement reçu] ${String(inv.description || '').split(' · ')[0]} — IDR ${amt}`,
        html: `<div style="font-family:Arial,sans-serif;color:#2E2429"><h2 style="color:#3F2A3A">Paiement reçu ✅</h2><p><strong>${e(inv.description)}</strong></p><p>Montant : <strong>IDR ${amt}</strong> · ${e(inv.payment_method || inv.payment_channel || '')}</p><p>Client : ${e(inv.payer_email || '')}</p><p>Référence : ${e(ext)}</p></div>` }),
    }).catch(() => {});
  }
  return ok('svc: notified');
}

// ---- E-mails après un paiement de réservation (27/11/2026) ----
// 1) Alerte à Unaya (FORM_TO, copie PAY_ALERT_TO) : qui a payé, combien, ce qui reste dû.
// 2) Reçu au client (adresse de la réservation / de la facture), en anglais ou en français.
const fmt = n => Math.round(Number(n) || 0).toLocaleString('en-US');
const esc = x => String(x ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const VILLA = { 359816: 'Yuga Bali', 359817: 'SUMA Bali', 359818: 'Rumah Jambu' };
function dFR(iso) { const d = new Date(String(iso || '') + 'T00:00:00Z'); return isNaN(d) ? '' : d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }); }
function dEN(iso) { const d = new Date(String(iso || '') + 'T00:00:00Z'); return isNaN(d) ? '' : d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }); }
async function send(env, msg) {
  if (!env.RESEND_API_KEY) return;
  await fetch('https://api.resend.com/emails', { method: 'POST', headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ from: env.FORM_FROM || 'Unaya <site@unayabali.com>', ...msg }) });
}
async function paidEmails(env, inv, bookId, amount, b, err) {
  const en = /booking #/i.test(String(inv.description || '')) || String(b?.lang || '').toLowerCase().startsWith('en');
  const total = b ? Number(b.price) || 0 : 0;
  const before = b ? paidSoFar(b) : 0;
  const left = b ? Math.max(0, total - before - amount) : null;
  const villa = VILLA[b?.propertyId] || 'Unaya';
  const guest = [b?.firstName, b?.lastName].filter(Boolean).join(' ') || inv.payer_email || '';
  const email = b?.email || inv.payer_email || '';
  const how = inv.payment_method === 'CREDIT_CARD' ? 'card' : (inv.payment_channel || inv.payment_method || '');
  const rooms = b?.groupIds?.length > 1 ? ` (${b.groupIds.length} chambres)` : '';
  // 1) Alerte Unaya
  const to = [env.FORM_TO || 'info@unayabali.com', ...(env.PAY_ALERT_TO ? String(env.PAY_ALERT_TO).split(',') : [])].map(x => x.trim()).filter(Boolean);
  await send(env, { to: [...new Set(to)], ...(email ? { reply_to: email } : {}),
    subject: `💰 Paiement reçu — ${villa} — IDR ${fmt(amount)} — ${guest} (#${bookId})`,
    html: `<div style="font-family:Arial,sans-serif;color:#2E2429;font-size:15px;line-height:1.5"><h2 style="color:#3F2A3A;margin:0 0 12px">Paiement reçu ✅</h2>
<p><b>${esc(guest)}</b> vient de payer <b>IDR ${fmt(amount)}</b> (${esc(how)}) sur le site.</p>
<p>Villa : <b>${esc(villa)}</b>${esc(rooms)}<br>Réservation : <b>#${esc(bookId)}</b>${b ? `<br>Séjour : ${esc(dFR(b.arrival))} → ${esc(dFR(b.departure))}` : ''}</p>
${b ? `<p>Total du séjour : IDR ${fmt(total)}<br>Déjà payé avec ce paiement : IDR ${fmt(before + amount)}<br><b>${left > 0 ? `Reste à payer : IDR ${fmt(left)}` : 'Séjour entièrement payé'}</b></p>` : ''}
<p>Client : ${esc(email)}${b?.phone || b?.mobile ? ' · ' + esc(b.phone || b.mobile) : ''}</p>
${err ? `<p style="color:#B3261E"><b>⚠️ Le paiement n'a pas pu être enregistré automatiquement dans Beds24 : à ajouter à la main.</b><br>${esc(err)}</p>` : '<p style="color:#5A4E54">Le paiement est déjà enregistré dans Beds24. Un reçu a été envoyé au client.</p>'}</div>` });
  // 2) Reçu client
  if (!email) return;
  const first = b?.firstName || '';
  const T = en ? {
    s: `Payment received — your booking at ${villa} (#${bookId})`,
    h: `Payment received`, hi: `Hello ${first},`.replace(' ,', ','),
    p: `We have received your payment of <b>IDR ${fmt(amount)}</b> for your booking at <b>${villa}</b>. Thank you!`,
    st: 'Stay', bk: 'Booking number', tt: 'Total of your stay', pd: 'Paid so far', lf: 'Remaining balance',
    full: 'Your stay is now fully paid.',
    bal: 'The remaining balance is due 14 days before arrival (30 days in high season). We will send you a reminder with a payment link.',
    q: 'Any question? Just reply to this email or message us on WhatsApp: +62 851 9021 1324', sig: 'See you soon,<br>The Unaya team', d: dEN,
  } : {
    s: `Paiement reçu — votre réservation à ${villa} (n°${bookId})`,
    h: `Paiement reçu`, hi: `Bonjour ${first},`.replace(' ,', ','),
    p: `Nous avons bien reçu votre paiement de <b>IDR ${fmt(amount)}</b> pour votre réservation à <b>${villa}</b>. Merci !`,
    st: 'Séjour', bk: 'Numéro de réservation', tt: 'Total du séjour', pd: 'Déjà payé', lf: 'Reste à payer',
    full: 'Votre séjour est maintenant entièrement payé.',
    bal: "Le solde est à régler 14 jours avant l'arrivée (30 jours en haute saison). Nous vous enverrons un rappel avec un lien de paiement.",
    q: 'Une question ? Répondez simplement à cet e-mail ou écrivez-nous sur WhatsApp : +62 851 9021 1324', sig: "À très bientôt,<br>L'équipe Unaya", d: dFR,
  };
  const row = (k, v) => `<tr><td style="padding:6px 0;color:#7A6E74">${k}</td><td style="padding:6px 0;text-align:right"><b>${v}</b></td></tr>`;
  await send(env, { to: [email], reply_to: env.FORM_TO || 'info@unayabali.com', subject: T.s,
    html: `<div style="font-family:Arial,sans-serif;color:#2E2429;font-size:15px;line-height:1.55;max-width:560px">
<h2 style="color:#3F2A3A;margin:0 0 14px">${T.h} ✓</h2><p>${esc(T.hi)}</p><p>${T.p}</p>
<table style="width:100%;border-collapse:collapse;border-top:1px solid #EEE4DD;border-bottom:1px solid #EEE4DD;margin:14px 0">
${row(T.bk, '#' + esc(bookId))}${b ? row(T.st, esc(T.d(b.arrival)) + ' → ' + esc(T.d(b.departure))) : ''}
${row(en ? 'Amount paid now' : 'Montant payé', 'IDR ' + fmt(amount))}
${b ? row(T.tt, 'IDR ' + fmt(total)) + row(T.pd, 'IDR ' + fmt(before + amount)) + (left > 0 ? row(T.lf, 'IDR ' + fmt(left)) : '') : ''}</table>
${b ? `<p>${left > 0 ? T.bal : T.full}</p>` : ''}<p>${T.q}</p><p>${T.sig}</p></div>` });
}
