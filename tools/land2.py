# Terrains (v2, 15/11/2026) : même présentation que les villas à vendre (mosaïque, encadré prix, visite,
# partage, PDF, calculateur, cartes « alentours », carte Google, temps de trajet). Remplace la sortie de land.py.
import sys, json, html as _h
sys.path.insert(0, '/tmp/claude-0/-home-claude/fb21bd82-28de-566e-9e55-058e68a3af45/scratchpad/gen')
from urllib.parse import quote
from ui import ic, sec, head, cta, btn, faq
import land as L0  # textes du terrain de 500 m² (land.py écrit aussi ses pages : elles sont remplacées ci-dessous)
R = '/home/claude/unaya-site/src/'
WA = '6285190211324'
FX = 18158; FXD = {'fr': '11 nov. 2026', 'en': '11 Nov 2026'}
def jattr(o): return _h.escape(json.dumps(o, ensure_ascii=False), quote=True)
def idr(n, fr): return 'IDR ' + (f'{n:,.0f}'.replace(',', ' ') if fr else f'{n:,.0f}')
def usd(n, fr): n = round(n / 100) * 100; return ('≈ ' + f'{n:,.0f}'.replace(',', ' ') + ' USD') if fr else f'≈ USD {n:,.0f}'

def plan500(l): return L0.plan_svg(l)
def plan795(l):
    fr = l == 'fr'
    a, r = ('CHEMIN D’ACCÈS PRIVÉ', 'ROUTE PRIVÉE') if fr else ('PRIVATE ACCESS PATH', 'PRIVATE ROAD')
    return f'''<svg viewBox="0 0 380 300" role="img" aria-label="{'Plan de bornage indicatif' if fr else 'Indicative survey plan'}" class="ld-plan">
<path d="M40 70 L150 40 L350 18" stroke="#ddd3cb" stroke-width="12" fill="none" stroke-linecap="round"/>
<text x="230" y="22" font-size="10" letter-spacing="2" fill="#8B5A46" transform="rotate(-6 230 22)">{a}</text>
<line x1="28" y1="80" x2="60" y2="280" stroke="#ddd3cb" stroke-width="12" stroke-linecap="round"/>
<text x="22" y="230" transform="rotate(-80 22 230)" font-size="10" letter-spacing="2" fill="#8B5A46">{r}</text>
<polygon points="60,95 150,68 330,40 338,165 92,250" fill="#efe1d9" stroke="#3F2A3A" stroke-width="2"/>
<text x="100" y="72" font-size="12" fill="#2E2429" transform="rotate(-16 100 72)">13,36 m</text>
<text x="235" y="48" font-size="12" fill="#2E2429" transform="rotate(-9 235 48)">27,37 m</text>
<text x="350" y="108" font-size="12" fill="#2E2429" transform="rotate(87 350 108)">19,26 m</text>
<text x="215" y="226" font-size="12" fill="#2E2429" transform="rotate(-19 215 226)">46,21 m</text>
<text x="58" y="182" font-size="12" fill="#2E2429" transform="rotate(76 58 182)">19,82 m</text>
<text x="205" y="150" text-anchor="middle" font-family="Cormorant Garamond,serif" font-size="32" fill="#3F2A3A">795 m²</text>
<text x="362" y="290" text-anchor="middle" font-size="12" fill="#3F2A3A">N ↑</text></svg>'''

# ---------- données des terrains ----------
def d500(l):
    t = L0.T[l]; fr = l == 'fr'
    total = 3150000000
    return dict(page='TerrainMelasti', ares=5, gps=('-8.84149', '115.14777'), maps='https://www.google.com/maps?q=-8.84149,115.14777',
        hero='terrain-melasti-plage.jpg', mosaic=None, rdtr='terrain-melasti-rdtr.jpg', plan=plan500(l),
        title=('Terrain de 500 m² à Melasti, Uluwatu (bail 30 ans) — Unaya Bali' if fr else '500 m² Land in Melasti, Uluwatu (30-Year Lease) — Unaya Bali'),
        kick=t['kick'], h1=t['h1'], sub=t['sub'], badges=[t['status'], ('Zone rose' if fr else 'Pink zone'), ('Bail 30 ans' if fr else '30-year lease')],
        facts=t['facts'], dh=t['dh'], dp=t['dp'], why=t['why'],
        prices=[(('Parcelle entière · 30 ans' if fr else 'Full plot · 30 years'), total)], pe=t['pe'],
        calc=None, around=t['around'], ah=t['ah'], al=t['al'],
        tbl=[x for x in t['tbl'] if x[0] not in ('Plage de Melasti', 'Melasti Beach', 'Savaya', 'Monster Padel', 'Aéroport', 'Airport')],
        dist=[('Monster Padel', '1 min'), (('Plage de Melasti' if fr else 'Melasti Beach'), '5 min'), ('Karma Kandara', '5 min'), ('Savaya', '10 min'), (('Aéroport' if fr else 'Airport'), '45 min')],
        qs=[q if not q[0].startswith(('Comment le prix', 'How is the price')) else (q[0], (f'IDR 21 000 000 par are et par an × 5 ares × 30 ans = IDR 3 150 000 000, soit {usd(total / FX, fr)} au taux du {FXD[l]}.' if fr else f'IDR 21,000,000 per are per year × 5 ares × 30 years = IDR 3,150,000,000, or {usd(total / FX, fr)} at the rate of {FXD[l]}.')) for q in t['qs']],
        name=('le terrain de 500 m² à Melasti' if fr else 'the 500 m² Melasti plot'), short='500 m²', zone='Melasti · Uluwatu', card_img='terrain-melasti-plage.jpg',
        card_pts=(['500 m²', 'Zone rose', 'Bail 30 ans'] if fr else ['500 m²', 'Pink zone', '30-year lease']), card_price=total, card_deal=('Bail 30 ans' if fr else '30-year lease'))

def d795(l):
    fr = l == 'fr'
    lease = 7.95 * 21000000 * 30; free = 7.95 * 1100000000
    if fr:
        txt = dict(
            title='Terrain de 795 m² à Melasti, Uluwatu — bail ou pleine propriété | Unaya Bali',
            h1='Terrain d’angle de 795 m² en zone rose', sub='Sur un chemin privé, pavé et sans passage, à 5 minutes de la plage de Melasti. En bail dès 4 ares, ou en pleine propriété pour la parcelle entière.',
            badges=['Disponible', 'Zone rose', 'Bail ou pleine propriété'],
            facts=[('map', 'Surface', '795 m²', '7,95 ares · terrain d’angle'), ('temple', 'Zonage', 'Zone rose · W', 'Zona Pariwisata'), ('doc', 'Titre foncier', 'SHM · Hak Milik', 'certificat de pleine propriété'), ('home', 'Constructible', '50 % au sol', 'surface de plancher × 2')],
            dh='Le terrain',
            dp=['Un beau terrain d’angle de 795 m² sur un chemin privé, pavé et sans circulation : rien que du calme. Une belle façade et de la place pour une grande villa avec piscine et jardin tropical, plusieurs villas ou un petit projet hôtelier.',
                'Juste en contrebas, un projet de villas haut de gamme se construit en terrasses : placé plus haut, le terrain garde sa vue dégagée.',
                'À 5 minutes de la plage de Melasti, sable blanc et eau turquoise au pied des falaises calcaires. Les beach clubs, les meilleures tables et le spa Karma Kandara sont à 5 minutes, Savaya à 10 minutes. On y arrive par une route neuve et élargie, puis par un chemin privé qui ne dessert que les parcelles.',
                '<strong>Un quartier en plein essor, un coin à l’écart.</strong> De grands projets haut de gamme voient le jour dans le secteur, avec boutiques, cafés et espaces bien-être, mais à distance du terrain.'],
            why=['Terrain d’angle avec une large façade', 'Vue dégagée, au-dessus du projet voisin', 'Zone rose : villas, hôtels, restaurants et location à la journée autorisés', 'Chemin privé pavé, sans passage'],
            pe='Bail : IDR 21 000 000 / are / an, minimum 4 ares · Pleine propriété : IDR 1 100 000 000 / are, parcelle entière',
            prices=[('Parcelle entière · bail 30 ans', lease), ('4 ares · bail 30 ans', 4 * 21000000 * 30), ('Pleine propriété · parcelle entière', free)],
            name='le terrain de 795 m² à Melasti', card_pts=['795 m²', 'Terrain d’angle', 'Zone rose'], card_deal='Bail dès 4 ares ou pleine propriété',
            qs=[('Un étranger peut-il prendre ce terrain ?', 'Oui. En bail (hak sewa) enregistré chez un notaire : vous avez le droit d’usage pendant 30 ans, avec une option de prolongation de 30 ans. La pleine propriété (SHM) est réservée aux Indonésiens ou se fait au nom d’une société PT PMA. Voir notre page <a href="/fr/investir-a-bali/">Investir à Bali</a>.'),
                ('Peut-on prendre seulement une partie ?', 'Oui, en bail, à partir de 4 ares (400 m²). La pleine propriété ne se vend que pour la parcelle entière de 7,95 ares.'),
                ('Que peut-on construire ?', 'En zone rose (Zona Pariwisata) : villas, hôtels, resorts, boutique-hôtels, restaurants, cafés, avec location à la journée autorisée. Emprise au sol maximale 50 %, coefficient de plancher 2,0 : sur 795 m², jusqu’à environ 397 m² au sol et 1 590 m² de plancher.'),
                ('Comment le prix est-il calculé ?', f'Bail : IDR 21 000 000 par are et par an × nombre d’ares × 30 ans. Parcelle entière : IDR 5 008 500 000 ({usd(lease / FX, True)}). Pleine propriété : IDR 1 100 000 000 par are, soit IDR 8 745 000 000 ({usd(free / FX, True)}). Dollars au taux du {FXD[l]}.'),
                ('Pouvez-vous construire la villa ?', 'Oui : Unaya s’occupe des plans, du permis (PBG) et de la construction, puis de la mise en location.')])
    else:
        txt = dict(
            title='795 m² Land in Melasti, Uluwatu — Leasehold or Freehold | Unaya Bali',
            h1='795 m² corner plot in the pink zone', sub='On a paved private lane with no through traffic, 5 minutes from Melasti Beach. Leasehold from 4 ares, or freehold for the full plot.',
            badges=['Available', 'Pink zone', 'Leasehold or freehold'],
            facts=[('map', 'Land area', '795 m²', '7.95 ares · corner plot'), ('temple', 'Zoning', 'Pink zone · W', 'Zona Pariwisata'), ('doc', 'Land title', 'SHM · Hak Milik', 'freehold certificate'), ('home', 'Buildable', '50% coverage', 'floor-area ratio 2.0')],
            dh='The land',
            dp=['A fine 795 m² corner plot on a paved private lane with no through traffic: nothing but calm. Generous frontage and room for a large villa with pool and tropical garden, several villas or a small boutique project.',
                'Just below, a high-end villa project is being built in terraces: set higher up, the plot keeps its open view.',
                'Five minutes from Melasti Beach, white sand and turquoise water at the foot of limestone cliffs. Beach clubs, the best restaurants and the Karma Kandara spa are 5 minutes away, Savaya 10 minutes. Reached by a brand-new, widened road, then a private lane serving only the plots.',
                '<strong>A fast-rising area, a quiet corner.</strong> Major high-end projects are coming to life nearby, with boutiques, cafés and wellness spaces, yet at a distance from the land.'],
            why=['Corner plot with wide frontage', 'Open view, above the neighbouring project', 'Pink zone: villas, hotels, restaurants and daily rentals allowed', 'Paved private lane, no through traffic'],
            pe='Leasehold: IDR 21,000,000 / are / year, minimum 4 ares · Freehold: IDR 1,100,000,000 / are, full plot only',
            prices=[('Full plot · 30-year lease', lease), ('4 ares · 30-year lease', 4 * 21000000 * 30), ('Freehold · full plot', free)],
            name='the 795 m² Melasti plot', card_pts=['795 m²', 'Corner plot', 'Pink zone'], card_deal='Leasehold from 4 ares or freehold',
            qs=[('Can a foreigner take this land?', 'Yes. Through a lease (hak sewa) registered with a notary: you hold the right of use for 30 years, with a 30-year extension option. Freehold (SHM) is reserved for Indonesians or held through a PT PMA company. See our <a href="/invest-in-bali/">Invest in Bali</a> page.'),
                ('Can I take only part of it?', 'Yes, on lease, from 4 ares (400 m²). Freehold is only sold for the full 7.95-are plot.'),
                ('What can be built?', 'In the pink zone (Zona Pariwisata): villas, hotels, resorts, boutique hotels, restaurants and cafés, with daily rentals allowed. Maximum site coverage 50%, floor-area ratio 2.0: on 795 m², up to about 397 m² of footprint and 1,590 m² of floor area.'),
                ('How is the price calculated?', f'Lease: IDR 21,000,000 per are per year × number of ares × 30 years. Full plot: IDR 5,008,500,000 ({usd(lease / FX, False)}). Freehold: IDR 1,100,000,000 per are, i.e. IDR 8,745,000,000 ({usd(free / FX, False)}). Dollars at the rate of {FXD[l]}.'),
                ('Can you build the villa?', 'Yes: Unaya handles design, the building permit (PBG) and construction, then renting it out.')])
    t5 = L0.T[l]
    return dict(page='TerrainMelasti795', ares=7.95, gps=('-8.83984', '115.14755'), maps='https://maps.app.goo.gl/9vwM9hmSg7mE4Sik6',
        hero='terrain-melasti-plage.jpg', mosaic=['terrain-melasti795-parcelle.jpg', 'terrain-melasti795-chemin.jpg', 'terrain-melasti-plage.jpg'], rdtr='terrain-melasti795-rdtr.jpg', plan=plan795(l),
        kick='Melasti · Uluwatu · Bali', calc=dict(min=4, max=7.95, rate=21000000, years=30, free=1100000000, fx=FX),
        around=t5['around'], ah=t5['ah'], al=t5['al'],
        tbl=[(('Titre foncier' if fr else 'Land title'), 'SHM · Hak Milik'), (('Surface' if fr else 'Land area'), ('795 m² (7,95 ares), terrain d’angle' if fr else '795 m² (7.95 ares), corner plot')),
             (('Zonage' if fr else 'Zoning'), ('Zone rose · W — Zona Pariwisata' if fr else 'Pink zone · W — Zona Pariwisata')), (('Emprise au sol' if fr else 'Site coverage'), ('50 % maximum' if fr else '50% maximum')),
             (('Coefficient de plancher' if fr else 'Floor-area ratio'), '2,0' if fr else '2.0'), ('GPS', '-8.83984, 115.14755')],
        dist=[('Monster Padel', '1 min'), (('Plage de Melasti' if fr else 'Melasti Beach'), '5 min'), ('Karma Kandara', '5 min'), ('Savaya', '10 min'), (('Aéroport' if fr else 'Airport'), '45 min')],
        short='795 m²', zone='Melasti · Uluwatu', card_img='terrain-melasti795-parcelle.jpg', card_price=lease, **txt)

# ---------- blocs ----------
def share(l, url, title):
    fr = l == 'fr'; u = quote('https://unayabali.com' + url, safe=''); tt = quote(title)
    return (f'<div class="ar-share" data-share-url="https://unayabali.com{url}" data-share-title="{_h.escape(title)}"><span>{"Partager" if fr else "Share"}</span>'
            f'<a href="https://wa.me/?text={tt}%20{u}" target="_blank" rel="noopener">WhatsApp</a><a href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener">Facebook</a>'
            f'<a href="mailto:?subject={tt}&amp;body={u}">E-mail</a><button type="button" class="ar-copy" data-ok="{"Lien copié" if fr else "Link copied"}">{"Copier le lien" if fr else "Copy link"}</button></div>')
L = "display:flex;flex-direction:column;gap:8px;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#5A3552;flex:1 1 220px;"
I = "font-family:'Jost',sans-serif;font-size:16px;padding:14px;border:1px solid #D9CCC2;background:#FFFFFF;color:#2E2429;"
def visit(l, name):
    fr = l == 'fr'
    lab = (('Nom', 'WhatsApp', 'E-mail', 'Type de visite', 'Date souhaitée', 'Moment de la journée', 'Message (facultatif)') if fr else ('Name', 'WhatsApp', 'Email', 'Viewing type', 'Preferred date', 'Time of day', 'Message (optional)'))
    vt = ['Sur place à Melasti', 'En vidéo (WhatsApp ou Zoom)'] if fr else ['On site in Melasti', 'By video (WhatsApp or Zoom)']
    mo = ['Matin', 'Après-midi', 'Peu importe'] if fr else ['Morning', 'Afternoon', 'Any time']
    form = (f'<form style="width:100%;background:#FFFFFF;border:1px solid #E6DCD4;padding:32px;display:flex;flex-direction:column;gap:18px;">'
            f'<div style="display:flex;flex-wrap:wrap;gap:18px;"><label style="{L}">{lab[0]}<input type="text" style="{I}"></label><label style="{L}">{lab[1]}<input type="tel" required placeholder="+61 412 345 678" style="{I}"></label><label style="{L}">{lab[2]}<input type="email" style="{I}"></label></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:18px;"><label style="{L}">{lab[3]}<select style="{I}">' + ''.join(f'<option>{o}</option>' for o in vt) + f'</select></label><label style="{L}">{lab[4]}<input type="date" data-mindate style="{I}"></label><label style="{L}">{lab[5]}<select style="{I}">' + ''.join(f'<option>{o}</option>' for o in mo) + '</select></label></div>'
            f'<label style="{L}">{lab[6]}<textarea rows="3" style="{I}">{("Visite de " if fr else "Viewing of ") + name + "."}</textarea></label>'
            f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><input type="checkbox" style="margin-top: 5px;">{"J’accepte que mes données soient utilisées pour organiser la visite (politique de confidentialité)." if fr else "I agree that my data may be used to arrange the viewing (privacy policy)."}</label>'
            f'<button type="button" style="display:inline-block;padding:16px 30px;background:#3F2A3A;color:#F7F2EE;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;border:none;font-family:\'Jost\',sans-serif;cursor:pointer;align-self:flex-start;">{"Demander la visite" if fr else "Request the viewing"}</button></form>')
    return f'<div class="ld-form">{head("Planifier une visite" if fr else "Book a viewing", "Sur place, ou en vidéo si vous êtes loin. Choisissez un jour, nous vous confirmons l’heure sur WhatsApp." if fr else "On site, or by video if you are far away. Pick a day and we confirm the time on WhatsApp.")}{form}</div>'
def calc_html(l, c):
    fr = l == 'fr'
    tx = (dict(h='Calculer votre prix', lead='Choisissez la surface et la formule : le prix, la surface constructible et l’équivalent en dollars se mettent à jour.', s='Surface', o1='Bail 30 ans', o2='Pleine propriété',
               k=['Prix total', 'En dollars', 'Constructible au sol', 'Surface de plancher max.'], note=f'Bail : IDR 21 000 000 par are et par an, minimum 4 ares, + option de prolongation de 30 ans. Pleine propriété : parcelle entière uniquement. Taux : 1 USD = IDR {FX:,} ({FXD["fr"]}).'.replace(',', ' '), free='La pleine propriété porte sur la parcelle entière (7,95 ares).')
          if fr else
          dict(h='Work out your price', lead='Pick the size and the option: price, buildable area and the dollar equivalent update as you go.', s='Land size', o1='30-year lease', o2='Freehold',
               k=['Total price', 'In dollars', 'Buildable footprint', 'Max. floor area'], note=f'Lease: IDR 21,000,000 per are per year, minimum 4 ares, + 30-year extension option. Freehold: full plot only. Rate: 1 USD = IDR {FX:,} ({FXD["en"]}).', free='Freehold covers the full plot (7.95 ares).'))
    kp = ''.join(f'<div class="cx-kpi{" cx-kpi--net" if i == 0 else ""}"><span>{lab}</span><strong data-k="{key}">–</strong></div>' for i, (lab, key) in enumerate(zip(tx['k'], ['tot', 'usd', 'foot', 'floor'])))
    return (head(tx['h'], tx['lead']) + f'<div class="cx-sim ld-calc" data-calc="{jattr(c)}"><div class="cx-ctrl">'
            f'<div class="cx-presets" role="group"><button type="button" class="cx-chip" data-mode="lease" aria-pressed="true">{tx["o1"]}</button><button type="button" class="cx-chip" data-mode="free" aria-pressed="false">{tx["o2"]}</button></div>'
            f'<label class="cx-sl" style="grid-column:1/-1"><span>{tx["s"]} <output data-out="ares"></output> <em>· <output data-out="m2"></output> m²</em></span><input type="range" name="ares" min="{c["min"]}" max="{c["max"]}" step="0.05" value="{c["max"]}"></label>'
            f'<p class="ld-calc__free" hidden>{tx["free"]}</p></div><div class="cx-kpis">{kp}</div>'
            f'<div class="ld-calc__viz"><svg viewBox="0 0 400 40" preserveAspectRatio="none" aria-hidden="true"><rect x="0" y="0" width="400" height="40" rx="6" fill="#F3ECE6"/><rect class="ld-calc__bar" x="0" y="0" width="400" height="40" rx="6" fill="#0E9180"/><rect class="ld-calc__built" x="0" y="0" width="200" height="40" rx="6" fill="#0B6F62" opacity=".55"/></svg>'
            f'<div class="ld-calc__leg"><span><i style="background:#0E9180"></i>{"Surface choisie" if fr else "Selected area"}</span><span><i style="background:#0B6F62;opacity:.55"></i>{"Constructible au sol (50 %)" if fr else "Buildable footprint (50%)"}</span><span><i style="background:#F3ECE6"></i>{"Reste de la parcelle" if fr else "Rest of the plot"}</span></div></div>'
            f'<p class="cx-note">{tx["note"]}</p></div>')
def around_cards(l, d):
    return '<div class="ar-lv2 ar-lv2--4 ld-ar2">' + ''.join(
        f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(k, 26)}</span><span class="ld-ar2__n">0{i + 1}</span><h3>{h}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in li) + '</ul></div></article>'
        for i, (k, h, li) in enumerate(d['around'])) + '</div>'
def dist_bars(l, d):
    import re
    rows = [dict(l=a, v=int(re.findall(r'\d+', b)[0]), t=b) for a, b in d['dist']]
    return f'<figure class="cx-card cx-card--dist"><figcaption>{"Temps de trajet en voiture" if l == "fr" else "Driving time"}</figcaption><div class="cx-bars cx-bars--dist" data-rows="{jattr(rows)}"></div></figure>'

def page(l, d):
    fr = l == 'fr'
    route = json.load(open(R + 'routes.json'))
    url = route[d['page']][l] if d['page'] in route else ('/fr/terrains/melasti-795-m2/' if fr else '/land/melasti-795-m2/')
    bcl = [('Accueil' if fr else 'Home', '/fr/' if fr else '/'), ('Investir à Bali' if fr else 'Invest in Bali', '/fr/investir-a-bali/' if fr else '/invest-in-bali/'), ('Terrains' if fr else 'Land', '/fr/terrains/' if fr else '/land/'), (d['short'], None)]
    bc = ' <span>›</span> '.join(f'<a href="{u}">{n}</a>' if u else n for n, u in bcl)
    wa = f'https://wa.me/{WA}?text={quote(("Bonjour Unaya, je suis intéressé(e) par " if fr else "Hello Unaya, I am interested in ") + d["name"] + ".")}'
    s = f'<!-- title: {d["title"]} -->\n'
    s += (f'<section class="ld-hero"><img src="/assets/images/{d["hero"]}" alt="" fetchpriority="high"><div class="ld-hero__in"><nav class="art-bc" aria-label="breadcrumb">{bc}</nav>'
          f'<p class="ld-kick">{d["kick"]}</p><h1>{d["h1"]}</h1><p>{d["sub"]}</p><div class="ld-badges">' + ''.join(f'<span class="ld-badge{" ld-badge--ok" if i == 0 else ""}">{b}</span>' for i, b in enumerate(d['badges'])) + '</div></div></section>\n')
    s += '<section class="ld-facts"><div class="ld-facts__in">' + ''.join(f'<div class="ld-fact">{ic(k,30)}<span>{a}</span><strong>{b}</strong><em>{c}</em></div>' for k, a, b, c in d['facts']) + '</div></section>\n'
    if d['mosaic']:
        mz = d['mosaic']; cap = (['La parcelle', 'Le chemin privé', 'La plage de Melasti, à 5 min'] if fr else ['The plot', 'The private lane', 'Melasti Beach, 5 min away'])
        s += ('<section class="u-sec ar-mz-sec"><div class="u-wrap"><div class="ar-mz" data-gallery>'
              f'<a class="ar-mz__big"><img src="/assets/images/{mz[0]}" alt="{cap[0]}"><span class="ld-mz__cap">{cap[0]}</span></a>'
              f'<a class="ar-mz__s"><img src="/assets/images/{mz[1]}" alt="{cap[1]}" loading="lazy"><span class="ld-mz__cap">{cap[1]}</span></a>'
              f'<a class="ar-mz__s"><img src="/assets/images/{mz[2]}" alt="{cap[2]}" loading="lazy"><span class="ld-mz__cap">{cap[2]}</span></a>'
              f'<a class="ar-mz__plan" href="#plan">{"Voir le plan et le zonage" if fr else "View plan and zoning"}</a></div></div></section>\n')
    desc = ''.join(f'<p>{p}</p>' for p in d['dp']) + '<ul class="u-checks">' + ''.join(f'<li>{w}</li>' for w in d['why']) + '</ul>'
    rows = ''.join(f'<div class="ar-pr"><span>{n}</span><strong>{idr(v, fr)}</strong><em>{usd(v / FX, fr)}</em></div>' for n, v in d['prices'])
    pdf = f'/assets/docs/terrain-{"melasti-795" if d["page"].endswith("795") else "melasti-500"}-{l}.pdf'
    price = (f'<aside class="ld-price"><span class="ld-price__k">{"Prix" if fr else "Price"}</span>{rows}<p class="ld-price__s">{d["pe"]}</p>'
             f'<a class="u-btn u-btn--rose" href="#visite">{"Planifier une visite" if fr else "Book a viewing"}</a><a class="ld-wa" href="{wa}" target="_blank" rel="noopener">{"Écrire sur WhatsApp" if fr else "Chat on WhatsApp"}</a>'
             f'<div class="ar-dl"><a href="{pdf}" download>{"Télécharger la fiche (PDF)" if fr else "Download the brochure (PDF)"}</a></div>'
             f'<p>{("Dollars au taux du " if fr else "Dollars at the rate of ") + FXD[l]}. {"Unaya vous accompagne : vérifications, notaire, plans et construction." if fr else "Unaya supports you: due diligence, notary, design and construction."}</p>'
             + share(l, url, d['h1'] + ' — Melasti, Bali') + '</aside>')
    s += sec(f'<div class="ld-main"><div class="ld-desc">{head(d["dh"])}{desc}</div>{price}</div>')
    if d['calc']:
        s += sec(calc_html(l, d['calc']), 'white', id='prix')
    s += sec(head(d['ah'], d['al'], True) + around_cards(l, d))
    tbl = '<dl class="ld-tbl">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in d['tbl']) + '</dl>'
    lat, lng = d['gps']
    s += sec(head('Parcelle et zonage' if fr else 'Plot & zoning', 'Données du plan de bornage officiel (Peta Bidang Tanah) et du plan d’urbanisme (RDTR) enregistrés au cadastre indonésien (BPN).' if fr else 'Data from the official land survey (Peta Bidang Tanah) and the spatial plan (RDTR) recorded with the Indonesian land registry (BPN).', True) +
             f'<div class="ld-zone ar-zone"><div class="ld-map"><iframe title="{"Emplacement du terrain" if fr else "Plot location"}" src="https://maps.google.com/maps?q={lat},{lng}&amp;t=k&amp;z=17&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="u-btn u-btn--line" href="{d["maps"]}" target="_blank" rel="noopener">{"Ouvrir dans Google Maps" if fr else "Open in Google Maps"} ↗</a></div><div>{tbl}{dist_bars(l, d)}</div></div>'
             f'<div class="ld-docs"><figure><figcaption>{"Plan de bornage (schéma)" if fr else "Survey plan (diagram)"}</figcaption>{d["plan"]}</figure><figure><figcaption>{"Zonage officiel (RDTR)" if fr else "Official zoning (RDTR)"}</figcaption><img src="/assets/images/{d["rdtr"]}" alt="RDTR — W Zona Pariwisata" loading="lazy"></figure></div>', 'white', id='plan')
    st = '<div class="u-path u-path--4">' + ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k,34)}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k, h, p in L0.T[l]['steps']).replace('Unaya Build', 'Unaya') + '</div>'
    s += sec(head('Du terrain à la villa' if fr else 'From land to villa', '', True) + st)
    s += sec(head('Questions fréquentes' if fr else 'Frequently asked questions') + faq(d['qs']), 'white')
    s += sec(visit(l, d['name']), id='visite')
    t5 = L0.T[l]
    form = (f'<form style="width:100%;background:#FFFFFF;border:1px solid #E6DCD4;padding:40px;display:flex;flex-direction:column;gap:20px;">'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{t5["fl"][0]}<input type="text" style="{I}"></label><label style="{L}">{t5["fl"][1]}<input type="email" style="{I}"></label></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{"WhatsApp (facultatif)" if fr else "WhatsApp (optional)"}<input type="tel" style="{I}"></label><label style="{L}">{t5["fl"][3]}<select style="{I}">' + ''.join(f'<option>{o}</option>' for o in t5['fo']) + '</select></label></div>'
            f'<label style="{L}">{t5["fl"][4]}<textarea rows="5" style="{I}">{("Bonjour, je suis intéressé(e) par " if fr else "Hello, I am interested in ") + d["name"] + (". Merci de m’envoyer le dossier complet." if fr else ". Please send me the full file.")}</textarea></label>'
            f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><input type="checkbox" style="margin-top: 5px;">{t5["fc"]}</label>'
            f'<button type="button" style="display:inline-block;padding:16px 30px;background:#3F2A3A;color:#F7F2EE;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;border:none;font-family:\'Jost\',sans-serif;cursor:pointer;align-self:flex-start;">{t5["fs"]}</button></form>')
    s += sec(f'<div class="ld-form">{head(t5["fh"], t5["fp"])}{form}<p class="ld-legal">{t5["legal"]}</p></div>', 'white', id='dossier')
    s += '<script src="/assets/js/arawa-charts.js" defer></script><div hidden data-arawa="{}"></div>\n'
    open(R + f'pages/{l}/{d["page"]}.html', 'w').write(s)
    return url

def listing(l, ds, urls):
    fr = l == 'fr'; t5 = L0.T[l]
    s = f'<!-- title: {"Terrains à vendre à Bali — Unaya Bali" if fr else "Land for Sale in Bali — Unaya Bali"} -->\n'
    s += (f'<section class="u-hero"><img src="/assets/images/terrain-melasti-plage.jpg" alt="" fetchpriority="high"><div class="u-hero__in"><p class="u-hero__k">{"Investir à Bali" if fr else "Invest in Bali"}</p><h1>{t5["lh1"]}</h1><p class="u-hero__sub">{t5["lsub"]}</p></div></section>\n')
    cards = ''.join(f'<a class="vl-card ld-card" href="{u}"><div class="vl-card__img"><img src="/assets/images/{d["card_img"]}" alt="{d["h1"]}" loading="lazy"><span class="vl-card__zone">{d["zone"]}</span></div>'
                    f'<div class="vl-card__b"><span class="ld-card__st">{"Disponible" if fr else "Available"}</span><h3>{d["h1"]}</h3><div class="vl-card__meta">' + ''.join(f'<span>{p}</span>' for p in d['card_pts']) + '</div>'
                    f'<div class="ld-card__p"><span>{d["card_deal"]}</span><strong>{idr(d["card_price"], fr)}</strong><em>{usd(d["card_price"] / FX, fr)}</em></div><span class="u-link">{t5["more"]}</span></div></a>' for d, u in zip(ds, urls))
    soon = ('<div class="ld-soon">' + ic('leaf', 40) + ('<h3>Bientôt</h3><p>De nouveaux terrains arrivent. Dites-nous ce que vous cherchez, nous vous prévenons en premier.</p>' if fr else '<h3>Coming soon</h3><p>New plots are on the way. Tell us what you are looking for and we will let you know first.</p>') + f'<a class="u-btn u-btn--line" href="{t5["cb"][1]}">{t5["cb"][0]}</a></div>')
    s += sec(head(t5['lih'], t5['lil'], True) + f'<div class="ld-grid">{cards}{soon}</div>')
    st = '<div class="u-path u-path--4">' + ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k,34)}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k, h, p in t5['steps']).replace('Unaya Build', 'Unaya') + '</div>'
    s += sec(head('Du terrain à la villa' if fr else 'From land to villa', '', True) + st, 'white')
    s += cta('yuga-nuit.jpg', t5['ch'], t5['cp'], btn(t5['cb'][0], t5['cb'][1], 'rose') + btn(t5['cb2'][0], t5['cb2'][1], 'white'))
    open(R + f'pages/{l}/Terrains.html', 'w').write(s)

r = json.load(open(R + 'routes.json'))
r['TerrainMelasti795'] = {'en': '/land/melasti-795-m2/', 'fr': '/fr/terrains/melasti-795-m2/'}
json.dump(r, open(R + 'routes.json', 'w'), ensure_ascii=False, indent=2)
DATA = {}
for l in ('fr', 'en'):
    ds = [d795(l), d500(l)]
    urls = [page(l, d) for d in ds]
    listing(l, ds, urls)
    DATA[l] = ds
print('ok')
