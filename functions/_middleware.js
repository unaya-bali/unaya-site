// Redirige l'ancienne adresse (unaya-site.pages.dev) et www vers le domaine principal unayabali.com.
// Les fonctions de paiement (/api/pay/...) ne sont pas redirigées, pour ne pas casser Beds24 / Midtrans pendant la transition.
export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  const h = url.hostname;
  if ((h === 'unaya-site.pages.dev' || h === 'www.unayabali.com') && !url.pathname.startsWith('/api/')) {
    url.hostname = 'unayabali.com';
    return Response.redirect(url.toString(), 301);
  }
  return next();
}
