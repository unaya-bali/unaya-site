// Étape 1 : Beds24 (Passerelle personnalisée) envoie ici le client après sa réservation.
// Réglage Beds24 : URL = https://<site>/api/pay/start   Post data = bookid=[BOOKID]&amount=[PAYMENTAMOUNT]
// On vérifie la réservation, on crée la transaction Midtrans (Snap) et on redirige le client vers la page de paiement.
import { snapUrl, midAuth, getBooking, isProd, UNAYA_PROPS, page, provider, xenAuth } from '../../../lib/pay.js';

export async function onRequest({ request, env }) {
  const url = new URL(request.url);
  const form = request.method === 'POST' ? await request.formData() : url.searchParams;
  const l = String(form.get('lang') || request.headers.get('Accept-Language') || '').toLowerCase();
  const lang = l.startsWith('fr') ? 'fr' : 'en';
  const T = lang === 'en'
    ? { err: 'Payment unavailable', msg: 'We could not start the payment. Please contact us at info@unayabali.com — your booking is kept.' }
    : { err: 'Paiement indisponible', msg: "Nous n'avons pas pu lancer le paiement. Écrivez-nous à info@unayabali.com — votre réservation est conservée." };

  const bookId = String(form.get('bookid') || '').replace(/\D/g, '');
  let amount = Math.round(parseFloat(String(form.get('amount') || '0').replace(/[^\d.]/g, '')) || 0);
  const prov = provider(env);
  if (!bookId || (prov === 'midtrans' ? !env.MIDTRANS_SERVER_KEY : !env.XENDIT_SECRET_KEY)) return page(lang, T.err, T.msg, 400);

  let guest = {};
  try {
    const b = await getBooking(env, bookId);
    if (b) {
      if (!UNAYA_PROPS.has(String(b.propertyId)) || String(b.status) === 'cancelled') return page(lang, T.err, T.msg, 400);
      const total = Math.round(Number(b.price) || 0);
      // Le montant est calculé ici (acompte = DEPOSIT_PERCENT % du total), jamais pris tel quel depuis le navigateur.
      if (total > 0) amount = Math.ceil(total * (Number(env.DEPOSIT_PERCENT || 30) / 100));
      guest = { first_name: b.firstName || '', last_name: b.lastName || '', email: b.email || '', phone: b.phone || b.mobile || '' };
    } else if (isProd(env)) {
      return page(lang, T.err, T.msg, 400); // en production, la vérification Beds24 est obligatoire
    } else if (amount < 1000) {
      amount = Number(env.TEST_AMOUNT || 100000); // mode test sans API Beds24 : montant fictif
    }
  } catch (e) {
    return page(lang, T.err, T.msg, 502);
  }
  if (amount < 1000) return page(lang, T.err, T.msg, 400);

  const orderId = `UNAYA-${bookId}-${Date.now().toString(36)}`;
  const finish = `${url.origin}${lang === 'en' ? '/payment/' : '/fr/paiement/'}?bookid=${bookId}`;
  if (prov === 'xendit') {
    // Facture Xendit (cartes, QRIS, virements, e-wallets selon les moyens activés sur le compte)
    const x = await fetch('https://api.xendit.co/v2/invoices', {
      method: 'POST',
      headers: { Authorization: xenAuth(env), 'Content-Type': 'application/json' },
      body: JSON.stringify({
        external_id: orderId,
        amount,
        currency: 'IDR',
        description: (lang === 'en' ? 'Unaya booking #' : 'Réservation Unaya n°') + bookId,
        ...(guest.email ? { payer_email: guest.email } : {}),
        customer: { given_names: guest.first_name || undefined, surname: guest.last_name || undefined, email: guest.email || undefined, mobile_number: guest.phone || undefined },
        success_redirect_url: finish,
        failure_redirect_url: finish,
        locale: 'en',
        invoice_duration: 86400,
      }),
    });
    if (!x.ok) return page(lang, T.err, T.msg, 502);
    const xj = await x.json();
    return Response.redirect(xj.invoice_url, 303);
  }

  const r = await fetch(snapUrl(env), {
    method: 'POST',
    headers: { Authorization: midAuth(env), 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify({
      transaction_details: { order_id: orderId, gross_amount: amount },
      item_details: [{ id: 'B' + bookId, price: amount, quantity: 1, name: (lang === 'en' ? 'Booking #' : 'Réservation n°') + bookId }],
      customer_details: guest,
      callbacks: { finish },
    }),
  });
  if (!r.ok) return page(lang, T.err, T.msg, 502);
  const j = await r.json();
  return Response.redirect(j.redirect_url, 303);
}
