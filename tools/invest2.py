# Page « Le guide pour investir » (FR/EN), version visuelle : chiffres clés, 3 façons de détenir,
# simulateur de revenus, acheter ou construire + budget, zonage, étapes, biens à vendre, FAQ par thème.
# Reprend les textes et sources de invest.py (exécuté jusqu'à sa boucle d'écriture).
import os, json, html
G = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(G, 'invest.py')).read()
ns = {}
exec(src[:src.index('for lang,t in T.items():')].replace("old=open(R+'fr/Investir.html').read()", "old=open('%s/Investir_old_fr.html').read()" % G), ns)
T, S, SEN, form, ic, STYLE, R = ns['T'], ns['S'], ns['SEN'], ns['form'], ns['ic'], ns['STYLE'], ns['R']
FX = 18158

X = {}
X['fr'] = dict(
 kick='Unaya Build · Le guide',
 b1='Simuler mes revenus', b2='Voir les biens à vendre',
 keys=[('6 – 10 %', 'rendement net par an d’une villa bien gérée, une fois lancée'), ('20 – 30 ans', 'durée habituelle d’un bail (leasehold), prolongeable'),
       ('10 %', 'taxe sur les nuitées (PBJT) dans la régence de Badung'), ('Mai 2026', 'Bali ferme l’hébergement touristique aux nouvelles PT PMA')],
 own_h='Les 3 façons de détenir un bien', own_p='Un étranger ne peut pas être pleinement propriétaire d’un terrain à Bali. Voici ce qui est possible, et ce que chaque formule permet.',
 own=[('home', 'Leasehold', 'Le plus courant', 'Un bail notarié avec le propriétaire indonésien.', [('Pour qui', 'Tout étranger'), ('Usage', 'Habitation'), ('Durée', 'Selon le bail, souvent 20 à 30 ans'), ('Louer aux touristes', 'Fermé aux nouvelles PT PMA*')], 'ok'),
      ('key', 'Hak Pakai', 'Pour y vivre', 'Un droit d’usage d’une maison, pour les résidents.', [('Pour qui', 'Étranger avec titre de séjour'), ('Usage', 'Habitation uniquement'), ('Durée', 'Limitée, prolongeable'), ('Louer aux touristes', 'Non')], 'no'),
      ('doc', 'PT PMA + HGB', 'Pour détenir un titre', 'Une société indonésienne à capitaux étrangers.', [('Pour qui', 'Société à capitaux étrangers'), ('Usage', 'Détenir le terrain et les murs'), ('Durée', 'Limitée, prolongeable'), ('Louer aux touristes', 'Fermé aux nouvelles PT PMA*')], 'ok')],
 pma=('Depuis mai 2026 : plus de nouvelles licences de location touristique pour les PT PMA', 'La province de Bali a fermé dans OSS 18 activités aux nouvelles sociétés à capitaux étrangers, dont l’hébergement touristique et la location de biens immobiliers. Une PT PMA créée aujourd’hui ne peut plus obtenir de licence pour louer une villa à la nuit. Les PT PMA déjà licenciées gardent la leur. Vous avez un projet ? Écrivez-nous, on vous dit ce qui est faisable aujourd’hui.', '* Sauf PT PMA déjà licenciée avant mai 2026.'),
 nominee=('Le prête-nom : à éviter absolument', 'Acheter au nom d’un ami indonésien ne vous protège en rien : le bien lui appartient légalement. Bali a interdit ces montages fin 2025, avec des sanctions jusqu’aux notaires.'),
 sim_h='Simulez les revenus d’une villa', sim_p='Bougez les curseurs : le revenu net, le rendement et la répartition de chaque roupie se recalculent.',
 sim=dict(rate='Prix moyen par nuit', occ='Taux d’occupation', val='Valeur du bien', nights='nuits louées par an', pre='Scénario', presets=[(55, 'Prudent 55 %'), (65, 'Marché 65 %'), (75, 'Très bien géré 75 %')],
          k=['Revenu brut / an', 'Revenu net / an', 'Net par mois', 'Rendement net'], wf='Où va l’argent, sur une année', yl='Votre rendement face au marché',
          note='Hypothèses : commissions des plateformes 15 %, PBJT 10 % incluse dans le prix, honoraires Unaya 18 % (gestion complète), personnel, énergie, entretien et réserve ≈ 20 % du brut. Avant impôt sur le revenu. Taux : 1 USD = IDR 18 158. Exemple illustratif, pas une promesse.'),
 bb_h='Acheter une villa ou faire construire ?', bb_p='Deux chemins, deux rythmes. Le bon choix dépend de votre budget, de vos délais et du temps que vous pouvez y consacrer.',
 buy=('suma-piscine.jpg', 'Acheter une villa existante', 'Louable presque tout de suite', ['Revenus dès les premiers mois', 'Vous voyez ce que vous achetez', 'Titres, permis et état du bâtiment à vérifier de près', 'Moins de marge pour l’adapter à la location']),
 build=('arawa-b-chantier-2.jpg', 'Faire construire', 'Souvent le meilleur rendement', ['Une villa pensée pour la location', 'Matériaux et finitions à votre goût', 'Plus long : terrain, plans, permis, chantier', 'Suivi sur place indispensable']),
 bud=dict(h='Estimez le budget de construction', area='Surface construite', tiers=[('std', 'Standard', 850, 1100), ('hdg', 'Haut de gamme', 1200, 1600), ('lux', 'Luxe', 1800, 2400)], out='Budget construction', chart='Coût au m² selon la gamme (USD, hors terrain et meubles)',
          note='Fourchettes de marché 2026 données par les agences, pas des chiffres officiels : seul un devis détaillé fait foi. Le terrain en bail se paie à part (souvent 25 à 60 M IDR par are et par an dans le sud).'),
 zn_h='Lire le zonage d’un terrain', zn_p='Chaque parcelle a une couleur sur le plan officiel (RDTR). Une villa louée aux touristes doit être sur une zone qui l’autorise.',
 zones=[('#7FA36B', 'Vert', 'Agricole, espace vert', 'Pas de villa commerciale', 'no'), ('#E8C66A', 'Jaune', 'Habitation', 'Maison, selon les règles locales', 'mid'),
        ('#E9A6C8', 'Rose', 'Tourisme', 'Hébergement touristique possible', 'ok'), ('#D9534F', 'Rouge', 'Commerce et services', 'Selon le règlement de la zone', 'mid')],
 zn_cap='Exemple réel : notre terrain de Melasti sur le plan officiel, en zone W (Pariwisata = tourisme).', zn_note='Les couleurs exactes varient selon les plans : seul le plan officiel (RDTR) fait foi.',
 st_h='Les étapes d’un achat', st_p='De l’idée à la première réservation, six étapes. Le notaire intervient au milieu, pas au début : les vérifications passent avant.',
 op_h='Les biens à vendre en ce moment', op_p='Sélectionnés et vérifiés par Unaya. Cliquez pour voir la fiche complète, les plans et les prix.',
 opps=[('/fr/villas-a-vendre/arawa-villa-b/', 'arawa-facade.jpg', 'Balangan · Uluwatu', 'Villa', 'Arawa Villas · Villa B', ['2 chambres', '≈ 106 m²'], 'dès 170 000 USD', 'Livraison fin déc. 2026'),
       ('/fr/villas-a-vendre/arawa-villa-d/', 'arawa-piscine.jpg', 'Balangan · Uluwatu', 'Villa', 'Arawa Villas · Villa D', ['2 chambres', '≈ 106 m²'], 'dès 195 000 USD', 'Livraison fin déc. 2026'),
       ('/fr/terrains/melasti-795-m2/', 'terrain-melasti795-parcelle.jpg', 'Melasti · Uluwatu', 'Terrain', 'Terrain d’angle de 795 m²', ['Zone rose', 'Bail ou pleine propriété'], 'IDR 5 008 500 000', '≈ 275 800 USD'),
       ('/fr/terrains/melasti-uluwatu/', 'terrain-melasti-plage.jpg', 'Melasti · Uluwatu', 'Terrain', 'Terrain de 500 m²', ['Zone rose', 'Bail ou pleine propriété'], 'IDR 3 150 000 000', '≈ 173 500 USD')],
 op_more=[('Toutes les villas à vendre', '/fr/villas-a-vendre/'), ('Tous les terrains', '/fr/terrains/')], see='Voir la fiche',
 fq_h='Vos questions, thème par thème', fq_p='Les réponses courtes, avec les textes officiels en source.',
 acc_h='Notre accompagnement Unaya Build', acc_p='Une seule équipe, du terrain à la première réservation.',
)
X['en'] = dict(
 kick='Unaya Build · The guide',
 b1='Simulate my income', b2='See properties for sale',
 keys=[('6 – 10%', 'net yield per year for a well-managed villa, once up and running'), ('20 – 30 yrs', 'usual length of a lease (leasehold), extendable'),
       ('10%', 'tax on nightly stays (PBJT) in Badung regency'), ('May 2026', 'Bali closes tourist accommodation to new PT PMA')],
 own_h='Three ways to hold property', own_p='A foreigner cannot fully own land in Bali. Here is what is possible, and what each option lets you do.',
 own=[('home', 'Leasehold', 'Most common', 'A notarised lease with the Indonesian landowner.', [('For whom', 'Any foreigner'), ('Use', 'Living'), ('Term', 'Per the lease, often 20 to 30 yrs'), ('Rent to tourists', 'Closed to new PT PMA*')], 'ok'),
      ('key', 'Hak Pakai', 'To live in', 'A right to use a house, for residents.', [('For whom', 'Foreigner with a residence permit'), ('Use', 'Living only'), ('Term', 'Limited, extendable'), ('Rent to tourists', 'No')], 'no'),
      ('doc', 'PT PMA + HGB', 'To hold a title', 'An Indonesian foreign-owned company.', [('For whom', 'Foreign-owned company'), ('Use', 'Holding the land and buildings'), ('Term', 'Limited, extendable'), ('Rent to tourists', 'Closed to new PT PMA*')], 'ok')],
 pma=('Since May 2026: no new tourist-rental licences for PT PMA', 'Bali province has closed 18 business lines in OSS to new foreign-owned companies, including tourist accommodation and renting out real estate. A PT PMA set up today can no longer get a licence to rent out a villa by the night. PT PMA already licensed keep theirs. Got a project? Write to us and we’ll tell you what is doable today.', '* Except PT PMA already licensed before May 2026.'),
 nominee=('Nominees: avoid them', 'Buying in an Indonesian friend’s name gives you no protection: the property legally belongs to them. Bali banned these arrangements in late 2025, with sanctions reaching notaries.'),
 sim_h='Simulate a villa’s income', sim_p='Move the sliders: net income, yield and where every rupiah goes update instantly.',
 sim=dict(rate='Average nightly rate', occ='Occupancy', val='Property value', nights='nights booked per year', pre='Scenario', presets=[(55, 'Cautious 55%'), (65, 'Market 65%'), (75, 'Very well run 75%')],
          k=['Gross income / yr', 'Net income / yr', 'Net per month', 'Net yield'], wf='Where the money goes, over a year', yl='Your yield vs the market',
          note='Assumptions: platform commissions 15%, PBJT 10% included in the rate, Unaya fees 18% (full management), staff, energy, maintenance and reserve ≈ 20% of gross. Before income tax. Rate: 1 USD = IDR 18,158. Illustrative example, not a promise.'),
 bb_h='Buy a villa or build one?', bb_p='Two paths, two paces. The right choice depends on your budget, your timing and how much time you can give it.',
 buy=('suma-piscine.jpg', 'Buy an existing villa', 'Rentable almost straight away', ['Income from the first months', 'You see what you buy', 'Titles, permits and condition need close checks', 'Less room to adapt it for rental']),
 build=('arawa-b-chantier-2.jpg', 'Build', 'Often the best return', ['A villa designed for rental', 'Materials and finishes to your taste', 'Longer: land, plans, permits, works', 'On-site supervision essential']),
 bud=dict(h='Estimate the construction budget', area='Built area', tiers=[('std', 'Standard', 850, 1100), ('hdg', 'Upscale', 1200, 1600), ('lux', 'Luxury', 1800, 2400)], out='Construction budget', chart='Cost per m² by finish level (USD, excl. land and furniture)',
          note='2026 market ranges from agencies, not official figures: only a detailed quote counts. Leasehold land is paid separately (often IDR 25–60 M per are per year in the south).'),
 zn_h='Reading a plot’s zoning', zn_p='Every plot has a colour on the official plan (RDTR). A villa rented to tourists must sit in a zone that allows it.',
 zones=[('#7FA36B', 'Green', 'Agricultural, green space', 'No commercial villa', 'no'), ('#E8C66A', 'Yellow', 'Residential', 'Home, per local rules', 'mid'),
        ('#E9A6C8', 'Pink', 'Tourism', 'Tourist accommodation possible', 'ok'), ('#D9534F', 'Red', 'Trade and services', 'Per the zone’s rules', 'mid')],
 zn_cap='Real example: our Melasti plot on the official plan, in zone W (Pariwisata = tourism).', zn_note='Exact colours vary between plans: only the official plan (RDTR) counts.',
 st_h='Buying step by step', st_p='From idea to first booking, six steps. The notary comes in the middle, not at the start: checks come first.',
 op_h='Properties for sale right now', op_p='Selected and checked by Unaya. Click for the full listing, plans and prices.',
 opps=[('/villas-for-sale/arawa-villa-b/', 'arawa-facade.jpg', 'Balangan · Uluwatu', 'Villa', 'Arawa Villas · Villa B', ['2 bedrooms', '≈ 106 m²'], 'from USD 170,000', 'Handover end Dec 2026'),
       ('/villas-for-sale/arawa-villa-d/', 'arawa-piscine.jpg', 'Balangan · Uluwatu', 'Villa', 'Arawa Villas · Villa D', ['2 bedrooms', '≈ 106 m²'], 'from USD 195,000', 'Handover end Dec 2026'),
       ('/land/melasti-795-m2/', 'terrain-melasti795-parcelle.jpg', 'Melasti · Uluwatu', 'Land', '795 m² corner plot', ['Pink zone', 'Leasehold or freehold'], 'IDR 5,008,500,000', '≈ USD 275,800'),
       ('/land/melasti-uluwatu/', 'terrain-melasti-plage.jpg', 'Melasti · Uluwatu', 'Land', '500 m² plot', ['Pink zone', 'Leasehold or freehold'], 'IDR 3,150,000,000', '≈ USD 173,500')],
 op_more=[('All villas for sale', '/villas-for-sale/'), ('All land', '/land/')], see='View listing',
 fq_h='Your questions, topic by topic', fq_p='Short answers, with the official texts as sources.',
 acc_h='How Unaya Build supports you', acc_p='One team, from the land to the first booking.',
)

def mark(m):
    return {'ok': '<i class="iv-m iv-m--ok" aria-hidden="true">✓</i>', 'no': '<i class="iv-m iv-m--no" aria-hidden="true">✕</i>', 'mid': '<i class="iv-m iv-m--mid" aria-hidden="true">~</i>'}[m]

def page(lang):
    t, x = T[lang], X[lang]
    fr = lang == 'fr'
    s = f'<!-- title: {t["title"]} -->\n' + STYLE + '\n<div class="inv iv">\n'
    # 1. Hero
    s += (f'<section class="inv-hero"><img src="/assets/images/yuga-drone.jpg" alt="" fetchpriority="high"><div class="inv-hero__in"><p style="font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#E2C3B2;margin:0 0 14px">{x["kick"]}</p>'
          f'<h1 style="max-width:16ch">{t["h1"]}</h1><p>{t["sub"]}</p><div style="display:flex;flex-wrap:wrap;gap:14px"><a class="inv-btn inv-btn--rose" href="#simulateur">{x["b1"]}</a><a class="inv-btn inv-btn--line" href="#opportunites">{x["b2"]}</a></div></div></section>\n')
    # 2. Chiffres clés
    s += ('<section class="iv-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) +
          f'</div><p class="iq-verified iv-ver">{ic("shield", 22)}<span>{t["verified"]}</span></p></section>\n')
    # 3. Détenir
    cards = ''
    for k, h, tag, p, rows, m in x['own']:
        cards += (f'<article class="ar-lv2__c iv-own{" iv-own--no" if m == "no" else ""}"><div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(k, 26)}</span><span class="iv-tag">{tag}</span><h3>{h}</h3><p class="iv-own__p">{p}</p><dl class="iv-dl">' +
                  ''.join(f'<div><dt>{a}</dt><dd>{(mark("ok" if not b.startswith(("Non", "No", "Fermé", "Closed")) else "no") + " ") if i == 3 else ""}{b}</dd></div>' for i, (a, b) in enumerate(rows)) + '</dl></div></article>')
    s += (f'<section class="u-sec" id="detenir"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["own_h"]}</h2><p>{x["own_p"]}</p></div><div class="ar-lv2 iv-owns">{cards}</div>'
          f'<p class="cx-note iv-c">{x["pma"][2]}</p><div class="iv-warn iv-warn--pma">{ic("doc", 40)}<div><strong>{x["pma"][0]}</strong><p>{x["pma"][1]} <a href="#estimation">→</a></p></div></div>'
          f'<div class="iv-warn">{ic("shield", 40)}<div><strong>{x["nominee"][0]}</strong><p>{x["nominee"][1]}</p></div></div></div></section>\n')
    # 4. Simulateur
    m = x['sim']
    cfg = json.dumps({'fx': FX, 'comm': .15, 'fee': .18, 'cost': .20, 'lang': lang, 'lbl': ({'gross': 'Revenu brut', 'comm': 'Commissions', 'pbjt': 'PBJT 10 %', 'fee': 'Honoraires Unaya', 'cost': 'Charges', 'net': 'Net', 'band': 'Fourchette du marché', 'you': 'Vous', 'ofg': 'du brut', 'yr': '/ an'} if fr else
                                                                                    {'gross': 'Gross income', 'comm': 'Commissions', 'pbjt': 'PBJT 10%', 'fee': 'Unaya fees', 'cost': 'Running costs', 'net': 'Net', 'band': 'Market range', 'you': 'You', 'ofg': 'of gross', 'yr': '/ yr'})})
    s += (f'<section class="u-sec u-sec--white" id="simulateur"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["sim_h"]}</h2><p>{x["sim_p"]}</p></div>'
          f'<div class="cx-sim iv-sim" data-iv="{html.escape(cfg)}"><div class="cx-ctrl iv-ctrl"><div class="cx-presets" role="group" aria-label="{m["pre"]}"><span>{m["pre"]}</span>' +
          ''.join(f'<button type="button" class="cx-chip" data-occ="{o}" aria-pressed="{"true" if o == 65 else "false"}">{l}</button>' for o, l in m['presets']) + '</div>'
          f'<label class="cx-sl"><span>{m["rate"]} <output data-out="rate"></output></span><input type="range" name="rate" min="1000000" max="10000000" step="100000" value="3000000"></label>'
          f'<label class="cx-sl"><span>{m["occ"]} <output data-out="occ"></output> <em>· <output data-out="nights"></output> {m["nights"]}</em></span><input type="range" name="occ" min="35" max="90" step="1" value="65"></label>'
          f'<label class="cx-sl"><span>{m["val"]} <output data-out="val"></output></span><input type="range" name="val" min="100000" max="1500000" step="5000" value="250000"></label></div>'
          '<div class="cx-kpis">' + ''.join(f'<div class="cx-kpi{" cx-kpi--net" if i == 1 else ""}"><span>{l}</span><strong data-k="{k}">–</strong>{"<em data-k=netusd></em>" if i == 1 else ""}</div>' for i, (k, l) in enumerate(zip(['gross', 'net', 'month', 'yld'], m['k']))) + '</div>'
          f'<div class="iv-sgrid"><figure class="cx-card"><figcaption>{m["wf"]}</figcaption><div class="iv-wf" role="img" aria-label="{m["wf"]}"></div></figure>'
          f'<figure class="cx-card iv-ycard"><figcaption>{m["yl"]}</figcaption><div class="iv-yg"></div><div class="iv-ybig"><strong data-k="yld2">–</strong><span data-k="ymsg"></span></div></figure></div>'
          f'<p class="cx-note">{m["note"]}</p></div></div></section>\n')
    # 5. Acheter ou construire + budget
    def bcard(c, n):
        img, h, tag, li = c
        return (f'<article class="ar-lv2__c iv-bb"><div class="ar-lv2__img"><img src="/assets/images/{img}" alt="{h}" loading="lazy"><span class="ar-lv2__n">{n}</span></div><div class="ar-lv2__b"><span class="iv-tag">{tag}</span><h3>{h}</h3><ul class="iv-pc">' +
                ''.join(f'<li class="{"is-p" if i < 2 else "is-m"}">{v}</li>' for i, v in enumerate(li)) + '</ul></div></article>')
    b = x['bud']
    tiers = json.dumps([{'id': i, 'l': l, 'a': a, 'z': z} for i, l, a, z in b['tiers']])
    s += (f'<section class="u-sec" id="construire"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["bb_h"]}</h2><p>{x["bb_p"]}</p></div><div class="ar-lv2 iv-bbs">{bcard(x["buy"], "01")}{bcard(x["build"], "02")}</div>'
          f'<div class="iv-bud" data-tiers="{html.escape(tiers)}" data-lang="{lang}"><div class="iv-bud__c"><h3>{b["h"]}</h3><div class="cx-presets" role="group">' +
          ''.join(f'<button type="button" class="cx-chip" data-tier="{i}" aria-pressed="{"true" if i == "hdg" else "false"}">{l}</button>' for i, l, a, z in b['tiers']) + '</div>'
          f'<label class="cx-sl"><span>{b["area"]} <output data-out="area"></output></span><input type="range" name="area" min="80" max="500" step="10" value="200"></label>'
          f'<div class="iv-bud__out"><span>{b["out"]}</span><strong data-k="bud">–</strong><em data-k="budidr"></em></div></div>'
          f'<figure class="cx-card iv-bud__f"><figcaption>{b["chart"]}</figcaption><div class="iv-rng"></div></figure></div><p class="cx-note iv-c">{b["note"]}</p></div></section>\n')
    # 6. Zonage
    s += (f'<section class="u-sec u-sec--white" id="zonage"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["zn_h"]}</h2><p>{x["zn_p"]}</p></div><div class="iv-zn"><div class="iv-zones">' +
          ''.join(f'<div class="iv-zone" style="--z:{c}"><span class="iv-zone__sw"></span><div><small>{n}</small><strong>{a}</strong><span>{mark(mm)} {bb}</span></div></div>' for c, n, a, bb, mm in x['zones']) +
          f'</div><figure class="iv-zfig"><img src="/assets/images/terrain-melasti-rdtr.jpg" alt="RDTR — W Zona Pariwisata" loading="lazy"><figcaption>{x["zn_cap"]}</figcaption></figure></div><p class="cx-note iv-c">{x["zn_note"]}</p></div></section>\n')
    # 7. Étapes
    s += (f'<section class="u-sec" id="etapes"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["st_h"]}</h2><p>{x["st_p"]}</p></div><ol class="iv-tl">' +
          ''.join(f'<li style="--i:{i}"><b>{i}</b><strong>{a}</strong><span>{bb}</span></li>' for i, (a, bb) in enumerate(t['steps'], 1)) + '</ol></div></section>\n')
    # 8. Biens à vendre
    oc = ''
    for href, img, zone, kind, h, meta, price, sub in x['opps']:
        oc += (f'<a class="vl-card ld-card iv-op" href="{href}"><div class="vl-card__img"><img src="/assets/images/{img}" alt="{h}" loading="lazy"><span class="vl-card__zone">{zone}</span></div>'
               f'<div class="vl-card__b"><span class="ld-card__st">{kind}</span><h3>{h}</h3><div class="vl-card__meta">' + ''.join(f'<span>{v}</span>' for v in meta) + f'</div><div class="ld-card__p"><span>{sub}</span><strong>{price}</strong></div><span class="u-link">{x["see"]}</span></div></a>')
    s += (f'<section class="u-sec u-sec--white" id="opportunites"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["op_h"]}</h2><p>{x["op_p"]}</p></div><div class="iv-ops">{oc}</div>'
          '<div class="iv-more">' + ''.join(f'<a class="u-btn u-btn--line" href="{u}">{l}</a>' for l, u in x['op_more']) + '</div></div></section>\n')
    # 9. FAQ par thème (onglets)
    tabs = ''.join(f'<button type="button" role="tab" id="ivt-{k}" aria-controls="ivp-{k}" aria-selected="{"true" if i == 0 else "false"}" class="iv-tab">{ic(icn, 26)}<span>{h}</span></button>' for i, (k, icn, h, _, qa) in enumerate(t['themes']))
    panels = ''.join(f'<div class="iv-panel" role="tabpanel" id="ivp-{k}" aria-labelledby="ivt-{k}"><h3 class="iv-panel__h">{h}</h3><div class="u-faq iq-faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qa) + '</div></div>' for k, icn, h, _, qa in t['themes'])
    s += (f'<section class="u-sec" id="questions"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["fq_h"]}</h2><p>{x["fq_p"]}</p></div><div class="iv-faq"><div class="iv-tabs" role="tablist">{tabs}</div><div class="iv-panels">{panels}</div></div></div></section>\n')
    # 10. Accompagnement
    s += (f'<section class="u-sec u-sec--white" id="accompagnement"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["acc_h"]}</h2><p>{x["acc_p"]}</p></div><div class="ar-lv2 ar-lv2--4 ld-ar2">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(k, 26)}</span><span class="ld-ar2__n">0{i}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for i, (k, h, p) in enumerate(t['acc'], 1)) + '</div></div></section>\n')
    # 11. Formulaire + sources
    s += (f'<section class="iq-formsec" id="estimation"><div class="iq-formsec__in"><div>{ic("report", 48)}<h2>{t["form_h"]}</h2><p>{t["form_p"]}</p></div><div class="iq-formbox">{form(t, lang)}</div></div></section>\n')
    srcs = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{(n if fr else SEN[k])}</a></li>' for k, (n, u) in S.items())
    s += f'<section class="iq-sources" id="sources"><h2>{t["src_h"]}</h2><ol>{srcs}</ol><p class="inv-disc" style="margin:24px 0 0">{t["disc"]}</p></section>\n</div>\n'
    s += '<script src="/assets/js/invest.js" defer></script>\n'
    return s

for lang in ('fr', 'en'):
    open(R + f'{lang}/Investir.html', 'w').write(page(lang))
print('ok')
