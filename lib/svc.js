// Liens de paiement des services voyageurs (option B, 06/11/2026).
// L'e-mail de demande reçu par Unaya contient un bouton « Créer le lien de paiement ». Ce bouton porte les
// infos de la demande, signées (HMAC) pour que personne ne puisse les modifier. Clé de signature dérivée de
// XENDIT_SECRET_KEY (secret serveur, jamais visible côté client).
const enc = new TextEncoder();
const b64u = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const b64uStr = s => btoa(unescape(encodeURIComponent(s))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64uStr = s => decodeURIComponent(escape(atob(s.replace(/-/g, '+').replace(/_/g, '/'))));
async function hmac(env, msg) {
  const key = await crypto.subtle.importKey('raw', enc.encode('svc-link:' + (env.XENDIT_SECRET_KEY || '')), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return b64u(await crypto.subtle.sign('HMAC', key, enc.encode(msg)));
}
export async function signOrder(env, order) {
  const d = b64uStr(JSON.stringify(order));
  return { d, sig: await hmac(env, d) };
}
export async function readOrder(env, d, sig) {
  if (!d || !sig || !env.XENDIT_SECRET_KEY) return null;
  if ((await hmac(env, d)) !== sig) return null;
  try {
    const o = JSON.parse(unb64uStr(d));
    if (!o.t || Date.now() - o.t > 60 * 86400000) return null; // lien valable 60 jours
    return o;
  } catch { return null; }
}

// Montant proposé à partir de la demande (modifiable avant de créer le lien).
const num = s => { const m = String(s || '').replace(/[ ,.  ]/g, '').match(/(\d{4,})/); return m ? Number(m[1]) : 0; };
function describe0(service, data, lang) {
  const g = (...names) => { for (const n of names) { const v = data.get(n); if (v) return String(v); } return ''; };
  const fr = lang !== 'en';
  if (service === 'transfert') {
    const zone = g('villa_ou_zone', 'villa_or_area'), trip = g('trajet', 'trip');
    const one = num((zone.match(/\(([^)]*)\)/) || [])[1]);
    const amount = one ? one * (/retour|return/i.test(trip) && /aller|return trip/i.test(trip) ? 2 : 1) : 0;
    return { amount, desc: `${fr ? 'Transfert aéroport' : 'Airport transfer'} · ${trip} · ${zone.replace(/\s*\([^)]*\)/, '')} · ${g('date_du_vol', 'flight_date')} ${g('heure_du_vol', 'flight_time')}`.trim() };
  }
  if (service === 'scooter') {
    const model = g('modele', 'model'), from = g('du', 'from'), to = g('au', 'to'), n = Math.max(1, Number(g('nombre_de_scooters', 'number_of_scooters')) || 1);
    const perDay = num(model), days = Math.max(1, Math.round((new Date(to) - new Date(from)) / 86400000) || 1);
    return { amount: perDay ? perDay * days * n : 0, desc: `${fr ? 'Location scooter' : 'Scooter rental'} · ${model.replace(/\s*—.*$/, '')} × ${n} · ${from} → ${to} (${days} ${fr ? 'j' : 'd'}) · ${g('livraison_a', 'deliver_to')}` };
  }
  if (service === 'chauffeur') {
    return { amount: 0, desc: `${fr ? 'Chauffeur privé' : 'Private driver'} · ${g('duree', 'duration')} · ${g('date')} ${g('heure_de_prise_en_charge', 'pick_up_time')}`.trim() };
  }
  if (service === 'experiences') {
    const est = g('estimation');
    return { amount: num((est.match(/·\s*([\d\s ,.]+)\s*IDR\s*$/) || [])[1]), desc: `Unaya Experiences · ${g('circuit_souhaite', 'preferred_tour')} · ${est.replace(/\s*·\s*[\d\s ,.]+\s*IDR\s*$/, '')}`.slice(0, 250) };
  }
  return { amount: 0, desc: service };
}
export function describe(service, data, lang) {
  const r = describe0(service, data, lang);
  r.desc = String(r.desc).replace(/(\s*·\s*)+(?=·)/g, ' ').replace(/(\s*·\s*)+$/, '').replace(/\s{2,}/g, ' ').trim();
  return r;
}
