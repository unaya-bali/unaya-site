// Page d'accueil "/" : les visiteurs dont le navigateur est en français sont envoyés vers /fr/
export async function onRequestGet({ request, env }) {
  const al = (request.headers.get('Accept-Language') || '').toLowerCase();
  const ref = request.headers.get('Referer') || '';
  const fromSite = ref.includes(new URL(request.url).host);
  if (!fromSite && al.startsWith('fr')) return Response.redirect(new URL('/fr/', request.url), 302);
  return env.ASSETS.fetch(request);
}
