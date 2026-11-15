// Signale à IndexNow (Bing, Yandex, Seznam, Naver) toutes les pages du sitemap.
// Appel : POST /api/indexnow. La clé est publique par conception (fichier /<clé>.txt à la racine du site).
const KEY = 'af1d1088d769f3c8db2e2ce5758b1914';
export async function onRequestPost({ request }) {
  const origin = new URL(request.url).origin;
  const xml = await fetch(origin + '/sitemap.xml').then(r => r.text());
  const urlList = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
  const res = await fetch('https://www.bing.com/indexnow', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify({ host: new URL(origin).host, key: KEY, keyLocation: origin + '/' + KEY + '.txt', urlList }),
  });
  return new Response(JSON.stringify({ status: res.status, sent: urlList.length }), { headers: { 'Content-Type': 'application/json' } });
}
