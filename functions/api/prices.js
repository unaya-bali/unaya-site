// Prix « à partir de » des villas, lus automatiquement sur la page de réservation Beds24 (API publique, sans clé).
// On interroge 12 séjours de 2 nuits (une fois par semaine sur les 12 prochaines semaines) et on garde le plus bas
// prix par nuit trouvé, pour la villa entière et pour une chambre. Résultat mis en cache 6 heures.
const VILLAS = {
  VillaYuga: { prop: '359816', villa: '741879', rooms: ['741880', '741881', '741882', '741883'] },
  VillaSuma: { prop: '359817', villa: '741884', rooms: ['741885', '741886', '741887', '741888', '741889'] },
  VillaRumahJambu: { prop: '359818', villa: '741890', rooms: [] },
};
const TTL = 6 * 3600;
const ymd = d => d.toISOString().slice(0, 10).replace(/-/g, '');

async function compute() {
  const jobs = [];
  for (const [name, v] of Object.entries(VILLAS)) {
    for (let k = 1; k <= 12; k++) {
      const a = new Date(Date.now() + k * 7 * 86400000), b = new Date(a.getTime() + 86400000);
      jobs.push(fetch('https://api.beds24.com/json/getAvailabilities', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ checkIn: ymd(a), lastNight: ymd(b), propId: v.prop, numAdult: '2' }),
      }).then(r => (r.ok ? r.json() : null)).catch(() => null).then(j => ({ name, j })));
    }
  }
  const out = {};
  for (const { name, j } of await Promise.all(jobs)) {
    if (!j) continue;
    const v = VILLAS[name], o = (out[name] ||= { villa: null, room: null });
    const nightly = id => { const p = Number(j[id] && j[id].price); return p > 0 ? Math.round(p / 2) : null; };
    const pv = nightly(v.villa);
    if (pv && (o.villa === null || pv < o.villa)) o.villa = pv;
    for (const r of v.rooms) { const pr = nightly(r); if (pr && (o.room === null || pr < o.room)) o.room = pr; }
  }
  return out;
}

export async function onRequestGet({ request, waitUntil }) {
  const cache = caches.default;
  const key = new Request(new URL('/api/prices?v=1', request.url).toString());
  const hit = await cache.match(key);
  if (hit) return hit;
  let data = {};
  try { data = await compute(); } catch (e) { data = {}; }
  const res = new Response(JSON.stringify({ updated: new Date().toISOString(), ...data }), {
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': `public, max-age=${TTL}` },
  });
  if (Object.keys(data).length) waitUntil(cache.put(key, res.clone()));
  return res;
}
