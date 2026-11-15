# Page d'accueil (FR/EN), version visuelle : grande photo, chiffres clés, 3 portes, villas,
# simulateur de revenus propriétaire, garanties, gestion complète, zones, Unaya Build, avis, tarifs, FAQ.
# Les avis, tarifs, zones et FAQ sont repris tels quels de Main_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re, json, html
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
FX = 18158

X = {
 'fr': dict(
  kick='Gestion de villas à Bali', h1='Votre villa à Bali, gérée comme si c’était la nôtre.',
  sub='Location, voyageurs, entretien et comptabilité, à Uluwatu, Jimbaran, Tanah Lot, Canggu et Seminyak. Un rapport chaque mois, aucun frais fixe.',
  b1=('Confier ma villa', '/fr/proprietaires/confier-ma-villa/'), b2=('Réserver un séjour', '/fr/villas/'),
  badges=['9,8/10 sur Booking.com', '4,93/5 sur Airbnb', 'Assistance 24h/24'],
  keys=[('263', 'voyageurs accueillis depuis juillet 2026'), ('22', 'nationalités'), ('9,8/10', 'note moyenne sur Booking.com'), ('18 %', 'gestion complète, aucun frais fixe')],
  doors_h='Par où commencer ?', doors_p='Que vous ayez une villa, que vous cherchiez un séjour ou un projet d’investissement, on s’en occupe.',
  doors=[('yuga-drone.jpg', 'Propriétaire', 'Je confie ma villa', 'Nous la louons, l’entretenons et vous rendons des comptes clairs, chaque mois.', 'Découvrir nos services', '/fr/proprietaires/'),
         ('suma-piscine-2.jpg', 'Voyageur', 'Je cherche une villa', 'Des villas privées avec piscine, au calme. −15 % dès 7 nuits en réservant en direct.', 'Voir nos villas', '/fr/villas/'),
         ('arawa-facade.jpg', 'Investisseur', 'J’investis à Bali', 'Villas et terrains à vendre, vérifiés par Unaya, et un guide pour acheter sans mauvaise surprise.', 'Le guide pour investir', '/fr/investir-a-bali/')],
  sim_h='Combien peut rapporter votre villa ?', sim_p='Une première idée en 10 secondes. Pour un chiffre précis, on étudie votre villa gratuitement.',
  sim=dict(rate='Prix moyen par nuit', occ='Taux d’occupation', nights='nuits louées par an', fml='Formule', fmls=[('18', 'Gestion complète 18 %'), ('11', 'Marketing seul 11 %')], pre='Scénario',
           presets=[(55, 'Prudent 55 %'), (65, 'Marché 65 %'), (75, 'Très bien géré 75 %')],
           k=['Revenu brut / an', 'Pour vous / an', 'Pour vous / mois', 'Notre commission / an'], wf='Où va l’argent, sur une année',
           cta_h='Une estimation précise pour votre villa', cta_p='Nous regardons votre villa, votre quartier et vos dates, et vous envoyons une projection de revenus sous 24 h. Gratuit et sans engagement.', cta_b='Demander mon estimation',
           note='Hypothèses : commissions des plateformes 15 %, taxe PBJT 10 % incluse dans le prix, notre commission calculée après plateformes et taxe, personnel, énergie, entretien et réserve ≈ 20 % du brut. Avant impôt. 1 USD = IDR 18 158. Exemple illustratif, pas une promesse.'),
  gar_h='Ce que nous vous garantissons', gar_p='Six engagements simples, tenus tous les mois.',
  ges_k='Gestion complète', ges_more='Voir tous nos services',
  zn_p='Trois secteurs que nous connaissons rue par rue.',
  bld=('Unaya Build', 'Investir à Bali', 'Des villas et des terrains à vendre, que nous avons visités et vérifiés. Et une fois le bien acheté, nous le louons pour vous.',
       [('Villas à vendre', '/fr/villas-a-vendre/'), ('Terrains', '/fr/terrains/')], ('Le guide pour investir', '/fr/investir-a-bali/'),
       [('dès 170 000 USD', 'Arawa Villas, Balangan'), ('795 m²', 'terrain d’angle à Melasti')]),
  rev_p='Les mots de nos voyageurs, tirés de leurs avis Airbnb et Booking.com.',
  tar_p='Une commission sur les revenus, rien d’autre. Pas de frais d’entrée, pas d’abonnement.',
  cta_img='suma-piscine.jpg',
 ),
 'en': dict(
  kick='Villa management in Bali', h1='Your villa in Bali, managed as if it were our own.',
  sub='Rentals, guests, upkeep and accounting in Uluwatu, Jimbaran, Tanah Lot, Canggu and Seminyak. A report every month, no fixed fees.',
  b1=('List my villa', '/owners/list-your-villa/'), b2=('Book a stay', '/villas/'),
  badges=['9.8/10 on Booking.com', '4.93/5 on Airbnb', '24/7 support'],
  keys=[('263', 'guests welcomed since July 2026'), ('22', 'nationalities'), ('9.8/10', 'average score on Booking.com'), ('18%', 'full management, no fixed fees')],
  doors_h='Where to start?', doors_p='Whether you own a villa, are looking for a stay or an investment, we take care of it.',
  doors=[('yuga-drone.jpg', 'Owner', 'I list my villa', 'We rent it, look after it and give you clear accounts, every month.', 'Our services', '/owners/'),
         ('suma-piscine-2.jpg', 'Guest', 'I’m looking for a villa', 'Private pool villas, in quiet spots. −15% from 7 nights when you book direct.', 'See our villas', '/villas/'),
         ('arawa-facade.jpg', 'Investor', 'I invest in Bali', 'Villas and land for sale, checked by Unaya, and a guide to buying without bad surprises.', 'The investment guide', '/invest-in-bali/')],
  sim_h='How much could your villa earn?', sim_p='A first idea in 10 seconds. For an accurate figure, we study your villa for free.',
  sim=dict(rate='Average nightly rate', occ='Occupancy', nights='nights booked per year', fml='Plan', fmls=[('18', 'Full Management 18%'), ('11', 'Marketing Only 11%')], pre='Scenario',
           presets=[(55, 'Cautious 55%'), (65, 'Market 65%'), (75, 'Very well run 75%')],
           k=['Gross income / yr', 'For you / yr', 'For you / month', 'Our commission / yr'], wf='Where the money goes, over a year',
           cta_h='An accurate estimate for your villa', cta_p='We look at your villa, your area and your dates, and send you an income projection within 24 hours. Free, no commitment.', cta_b='Get my estimate',
           note='Assumptions: platform commissions 15%, PBJT tax 10% included in the rate, our commission calculated after platforms and tax, staff, energy, maintenance and reserve ≈ 20% of gross. Before tax. 1 USD = IDR 18,158. Illustrative example, not a promise.'),
  gar_h='What we guarantee', gar_p='Six simple commitments, kept every month.',
  ges_k='Full management', ges_more='See all our services',
  zn_p='Three areas we know street by street.',
  bld=('Unaya Build', 'Invest in Bali', 'Villas and land for sale that we have visited and checked. And once you have bought, we rent it out for you.',
       [('Villas for sale', '/villas-for-sale/'), ('Land', '/land/')], ('The investment guide', '/invest-in-bali/'),
       [('from USD 170,000', 'Arawa Villas, Balangan'), ('795 m²', 'corner plot in Melasti')]),
  rev_p='Our guests’ own words, from their Airbnb and Booking.com reviews.',
  tar_p='A commission on income, nothing else. No set-up fee, no subscription.',
  cta_img='suma-piscine.jpg',
 ),
}

def sections(s):
    parts = re.split(r'\n(?=<section)', s)
    return parts[0], parts[1:]

def center(sec, p=None):
    sec = sec.replace('<div class="u-head">', '<div class="u-head u-head--c">', 1)
    if p:
        sec = re.sub(r'(<div class="u-head u-head--c"><h2>.*?</h2>)', lambda m: m.group(1) + f'<p>{p}</p>', sec, count=1)
    return sec

def feats(sec):
    return re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', sec, flags=re.S)

def small(svg):
    return svg.replace('width="40" height="40"', 'width="26" height="26"')

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Main_old_{lang}.html')).read()
    head, secs = sections(old)
    hero, doors, gar, ges, zones, rev, tar, faq, cta = secs
    s = head.split('\n')[0] + '\n<div class="hm">\n'
    # 1. Grande photo
    s += (f'<section class="hm-hero"><img src="/assets/images/suma-g1.jpg" alt="{"La Villa Suma et sa piscine éclairée à la tombée de la nuit, Balangan Uluwatu" if fr else "Villa Suma and its lit pool at dusk, Balangan Uluwatu"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{x["h1"]}</h1><p class="hm-hero__sub">{x["sub"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="{x["b2"][1]}">{x["b2"][0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">★</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    # 2. Chiffres clés
    s += '<section class="iv-keys hm-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) + '</div></section>\n'
    # 3. Trois portes
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["doors_h"]}</h2><p>{x["doors_p"]}</p></div><div class="ar-lv2 hm-doors">' +
          ''.join(f'<a class="ar-lv2__c hm-door" href="{u}"><div class="ar-lv2__img"><img src="/assets/images/{img}" alt="{h}" loading="lazy"><span class="ar-lv2__n">{k}</span></div><div class="ar-lv2__b"><h3>{h}</h3><p class="ar-lv2__p">{p}</p><span class="u-link">{l}</span></div></a>'
                  for img, k, h, p, l, u in x['doors']) + '</div></div></section>\n')
    # 4. Nos villas (rempli par build.py)
    s += '<!-- VILLAS -->\n'
    # 5. Simulateur propriétaire
    m = x['sim']
    cfg = json.dumps({'fx': FX, 'comm': .15, 'fee': .18, 'cost': .20, 'lang': lang, 'owner': 1,
                      'lbl': ({'gross': 'Revenu brut', 'comm': 'Plateformes', 'pbjt': 'PBJT 10 %', 'fee': 'Commission Unaya', 'cost': 'Charges', 'net': 'Pour vous', 'ofg': 'du brut', 'yr': '/ an'} if fr else
                              {'gross': 'Gross income', 'comm': 'Platforms', 'pbjt': 'PBJT 10%', 'fee': 'Unaya commission', 'cost': 'Running costs', 'net': 'For you', 'ofg': 'of gross', 'yr': '/ yr'})})
    s += (f'<section class="u-sec u-sec--white hm-sec" id="estimer"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["sim_h"]}</h2><p>{x["sim_p"]}</p></div>'
          f'<div class="cx-sim iv-sim" data-iv="{html.escape(cfg)}"><div class="cx-ctrl iv-ctrl"><div class="hm-chips"><div class="cx-presets" role="group" aria-label="{m["fml"]}"><span>{m["fml"]}</span>' +
          ''.join(f'<button type="button" class="cx-chip" data-fee="{v}" aria-pressed="{"true" if v == "18" else "false"}">{l}</button>' for v, l in m['fmls']) + '</div>'
          f'<div class="cx-presets" role="group" aria-label="{m["pre"]}"><span>{m["pre"]}</span>' +
          ''.join(f'<button type="button" class="cx-chip" data-occ="{o}" aria-pressed="{"true" if o == 65 else "false"}">{l}</button>' for o, l in m['presets']) + '</div></div>'
          f'<label class="cx-sl"><span>{m["rate"]} <output data-out="rate"></output></span><input type="range" name="rate" min="1000000" max="15000000" step="100000" value="3000000"></label>'
          f'<label class="cx-sl"><span>{m["occ"]} <output data-out="occ"></output> <em>· <output data-out="nights"></output> {m["nights"]}</em></span><input type="range" name="occ" min="35" max="90" step="1" value="65"></label></div>'
          '<div class="cx-kpis">' + ''.join(f'<div class="cx-kpi{" cx-kpi--net" if i == 1 else ""}"><span>{l}</span><strong data-k="{k}">–</strong>{"<em data-k=netusd></em>" if i == 1 else ""}</div>' for i, (k, l) in enumerate(zip(['gross', 'net', 'month', 'feey'], m['k']))) + '</div>'
          f'<div class="iv-sgrid"><figure class="cx-card"><figcaption>{m["wf"]}</figcaption><div class="iv-wf" role="img" aria-label="{m["wf"]}"></div></figure>'
          f'<div class="cx-card hm-est"><h3>{m["cta_h"]}</h3><p>{m["cta_p"]}</p><a class="u-btn u-btn--solid" href="{x["b1"][1]}">{m["cta_b"]}</a></div></div>'
          f'<p class="cx-note">{m["note"]}</p></div></div></section>\n')
    # 6. Garanties
    g = feats(gar)
    h2 = re.search(r'<h2>(.*?)</h2>', gar).group(1)
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{h2}</h2><p>{x["gar_p"]}</p></div><div class="ar-lv2 hm-gar">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{small(svg)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for svg, h, p in g) +
          '</div></div></section>\n')
    # 7. Gestion complète (fond sombre, numérotée)
    g = feats(ges)
    h2 = re.search(r'<h2>(.*?)</h2>', ges).group(1)
    more = re.search(r'href="([^"]+)">[^<]*</a></p></div></section>', ges).group(1)
    s += (f'<section class="u-sec u-sec--dark hm-sec hm-ges"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["ges_k"]}</p><h2>{h2}</h2></div><div class="hm-ges__g">' +
          ''.join(f'<div class="hm-step"><span class="hm-step__n">0{i}</span>{svg}<h3>{h}</h3><p>{p}</p></div>' for i, (svg, h, p) in enumerate(g, 1)) +
          f'</div><p class="hm-c"><a class="u-btn hm-btn--glass" href="{more}">{x["ges_more"]}</a></p></div></section>\n')
    # 8. Zones
    s += center(zones, x['zn_p']).replace('class="u-sec u-sec--white" id="zones"', 'class="u-sec u-sec--white hm-sec" id="zones"') + '\n'
    # 9. Unaya Build
    k, h, p, btns, guide, facts = x['bld']
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="hm-bld"><div class="hm-bld__img"><img src="/assets/images/arawa-piscine.jpg" alt="Arawa Villas, Balangan" loading="lazy">'
          '<div class="hm-bld__facts">' + ''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in facts) + '</div></div>'
          f'<div class="hm-bld__t"><p class="hm-k">{k}</p><h2>{h}</h2><p>{p}</p><div class="u-btns">' +
          ''.join(f'<a class="u-btn {"u-btn--solid" if i == 0 else "u-btn--line"}" href="{u}">{l}</a>' for i, (l, u) in enumerate(btns)) +
          f'</div><a class="u-link" href="{guide[1]}">{guide[0]}</a></div></div></div></section>\n')
    # 10. Avis, 11. Tarifs, 12. FAQ, 13. Appel final
    rev = rev.replace('class="u-sec u-sec--white"', 'class="u-sec u-sec--white hm-sec"', 1)
    rev = rev.replace('<div class="u-head"><h2>', '<div class="u-head"><h2>', 1)
    s += rev + '\n'
    s += center(tar, x['tar_p']).replace('class="u-sec"', 'class="u-sec hm-sec"', 1) + '\n'
    s += faq + '\n'
    s += re.sub(r'<img src="https://images\.unsplash\.com[^"]*"', f'<img src="/assets/images/{x["cta_img"]}"', cta)
    s = s.rstrip() + '\n</div>\n<script src="/assets/js/invest.js" defer></script>\n'
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'Main.html'), 'w').write(page(lang))
    print('ok')
