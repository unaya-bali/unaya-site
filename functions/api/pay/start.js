// Étape 1 : Beds24 (Passerelle personnalisée) envoie ici le client après sa réservation.
// Réglage Beds24 : URL = https://<site>/api/pay/start   Post data = bookid=[BOOKID]&amount=[PAYMENTAMOUNT]
// On vérifie la réservation, on crée la transaction Midtrans (Snap) et on redirige le client vers la page de paiement.
import { snapUrl, midAuth, getBooking, isProd, UNAYA_PROPS, page } from '../../../lib/pay.js';

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
  if (!bookId || !env.MIDTRANS_SERVER_KEY) return page(lang, T.err, T.msg, 400);

  let guest = {};
  try {
    const b = await getBooking(env, bookId);
    if (b) {
      if (!UNAYA_PROPS.has(String(b.propertyId)) || String(b.status) === 'cancelled') return page(lang, T.err, T.msg, 400);
      const total = Math.round(Number(b.price) || 0);
      const min = Math.ceil(total * (Number(env.DEPOSIT_PERCENT || 30) / 100));
      // Le montant envoyé par le navigateur peut être modifié : on le borne entre l'acompte minimum et le total.
      if (total > 0) amount = Math.min(Math.max(amount, min), total);
      guest = { first_name: b.firstName || '', last_name: b.lastName || '', email: b.email || '', phone: b.phone || b.mobile || '' };
    } else if (isProd(env)) {
      return page(lang, T.err, T.msg, 400); // en production, la vérification Beds24 est obligatoire
    }
  } catch (e) {
    return page(lang, T.err, T.msg, 502);
  }
  if (amount < 1000) return page(lang, T.err, T.msg, 400);

  const orderId = `UNAYA-${bookId}-${Date.now().toString(36)}`;
  const finish = `${url.origin}${lang === 'en' ? '/payment/' : '/fr/paiement/'}?bookid=${bookId}`;
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
