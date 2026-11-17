# Page de vente « Villa Yuga » (FR/EN) + carte dans « Villas à vendre ».
# Source : Yuga_Nyanyi_Suite_-_Fiche_de_vente.pdf (11/11/2026) + réponses de Sébastien (17/11/2026).
# Contact public = Unaya (pas le WhatsApp d'Elies). Pas de chiffres de revenus (demandé).
import os, re, sys, json
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ui import ic, faq
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
WA = '6285190211324'
LAT, LNG = -8.6173036, 115.1090637
GMAP = 'https://www.google.com/maps/place/YUGA+NYANYI+SUITE/@-8.6173036,115.1090637,896m/data=!3m2!1e3!4b1!4m9!3m8!1s0x2dd23900500f6823:0x5a17c2fcde3c8c31!5m2!4m1!1i2!8m2!3d-8.6173036!4d115.1090637!16s%2Fg%2F11z0wz9wvf!18m1!1e1'
URL = {'fr': '/fr/villas-a-vendre/yuga-nyanyi/', 'en': '/villas-for-sale/yuga-nyanyi/'}
GAL = [('yuga-piscine.jpg', 'Piscine et terrasses', 'Pool and terraces'), ('yuga-g1.jpg', 'Vue aérienne de la piscine', 'Aerial view of the pool'),
       ('yuga-g2.jpg', 'Transats face aux rizières', 'Sun loungers facing the rice fields'), ('yuga-chambre.jpg', 'Chambre avec lit king size', 'Bedroom with king-size bed'),
       ('yuga-terrasse.jpg', 'Terrasse d’une chambre sur le jardin', 'Bedroom terrace onto the garden'), ('yuga-g3.jpg', 'Cuisine extérieure', 'Outdoor kitchen'),
       ('yuga-sdb.jpg', 'Salle de bain tropicale', 'Tropical bathroom'), ('yuga-g5.jpg', 'Piscine et bungalows', 'Pool and bungalows'),
       ('yuga-nuit.jpg', 'La piscine le soir', 'The pool at night'), ('yuga-g7.jpg', 'Chambre, le soir', 'Bedroom at night'),
       ('yuga-entree.jpg', 'L’entrée à la tombée de la nuit', 'The entrance at dusk'), ('yuga-drone.jpg', 'La villa vue du ciel', 'The villa from above')]

T = {'fr': dict(
  title='Villa à vendre à Nyanyi, Tanah Lot : Yuga, 4 chambres, piscine | Unaya',
  desc='Villa Yuga à vendre à Nyanyi, près de Tanah Lot et Canggu : 4 suites, piscine privée, vendue meublée et déjà louée. Bail jusqu’en 2054. IDR 5,9 milliards (≈ 325 000 USD).',
  bc=[('Accueil', '/fr/'), ('Villas à vendre', '/fr/villas-a-vendre/'), ('Villa Yuga', None)],
  kick='Nyanyi · Tabanan · Bali', h1='Villa Yuga, 4 chambres à vendre à Nyanyi',
  sub='Quatre suites autour d’une piscine, face aux rizières de Beraban. Vendue meublée et déjà louée aux voyageurs : vous continuez à louer dès le premier jour.',
  badges=['Disponible', 'Déjà louée · 9,6/10', 'Bail jusqu’en 2054'],
  facts=[('bed', 'Chambres', '4 suites', 'chacune sa salle de bain'), ('map', 'Terrain', '310 m²', '3,1 ares'), ('pool', 'Piscine', 'Privée', 'avec deck'), ('doc', 'Bail', '≈ 27,5 ans', 'jusqu’en juin 2054')],
  more='Voir les {n} photos',
  dh='La villa',
  dp=['Yuga, ce sont quatre suites autour d’une piscine, sur un terrain de 310 m² face aux rizières de Beraban. La villa est sur Jalan Pantai Nyanyi, la route qui descend à la plage de Nyanyi, dans l’un des coins de la côte de Tanah Lot qui bougent le plus vite. Nuanu et ses restaurants sont à 5 minutes, Pererenan et Canggu à 10-15 minutes, sans leurs embouteillages.',
      'Terminée en 2026, elle est vendue entièrement meublée et équipée, et elle accueille déjà des voyageurs, qui lui donnent 9,6/10. Elle se loue en entier ou à la chambre, et l’équipe de ménage et de piscine est en place.',
      'Depuis octobre 2026, c’est Unaya Villa Management qui la gère. Vous pouvez garder cette gestion après l’achat : les locations à la nuit continuent sous la licence d’Unaya, même si vous vivez à l’étranger.'],
  why=['Déjà louée, avec de très bons avis voyageurs', 'Vendue meublée : linge, équipement et produits voyageurs compris', 'Location à la nuit possible tout de suite, sous la licence d’Unaya', 'Wi-Fi fibre, interrupteurs connectés, personnel en place'],
  lh='Le bail et les documents',
  lease=[('Type', 'leasehold (bail notarié), cédé avec la villa'), ('Fin du bail', '20 juin 2054, soit environ 27,5 ans'), ('Prolongation', 'priorité pour prolonger, au prix du marché à ce moment-là'),
         ('Permis (PBG / SLF)', 'en cours, dossier déposé en septembre 2026'), ('Mobilier', 'vendu entièrement meublé et équipé')],
  lnote='Faites vérifier le bail et les documents par votre notaire ou votre avocat avant de vous engager.',
  pk='Prix', usd='≈ USD 325 000', rate='1 USD = IDR 18 158 (11 nov. 2026). Le prix de référence est en roupies.',
  b1='Planifier une visite', b2='Écrire sur WhatsApp', dl='Télécharger la brochure (PDF)',
  wa='Bonjour Unaya, je suis intéressé(e) par la Villa Yuga à vendre à Nyanyi.',
  other='Voir aussi les <a href="/fr/villas-a-vendre/arawa-balangan/">Arawa Villas</a> à Balangan, dès 170 000 USD.',
  share='Partager', copy='Copier le lien', copied='Lien copié',
  vh='Ce que vous achetez', vl='Une villa terminée, meublée et qui tourne déjà.',
  lv=[('yuga-chambre.jpg', 'bed', 'Les quatre suites', ['4 chambres climatisées, chacune avec sa salle de bain', '3 lits king size et 1 chambre à deux lits simples', 'Une terrasse privée par chambre, sur le jardin et la piscine', 'Un bureau dans les chambres']),
      ('yuga-g2.jpg', 'pool', 'Dehors', ['Piscine privée avec deck', 'Transats et parasols', 'Cuisine extérieure', 'Jardin tropical et vue sur les rizières', 'Parking privé']),
      ('yuga-terrasse.jpg', 'key', 'Prête à louer', ['Entièrement meublée et équipée', 'Linge et produits voyageurs', 'Wi-Fi fibre, interrupteurs connectés, coffre-fort', 'Équipe de ménage et de piscine en place'])],
  rh='Acheter depuis l’étranger ?',
  rp=['Depuis mai 2026, une nouvelle PT PMA (société à capitaux étrangers) ne peut plus obtenir à Bali la licence pour louer une villa à la nuit. C’est le principal problème des acheteurs étrangers en ce moment.',
      'Avec Yuga, la question est réglée : Unaya Villa Management peut continuer à gérer la villa et à la louer à la nuit sous sa propre licence. Vous recevez les revenus et un rapport chaque mois, où que vous soyez.'],
  rl=('Comment marche la gestion', '/fr/proprietaires/services/'), rl2=('Le leasehold expliqué', '/fr/guides/leasehold-bali/'),
  zh='L’emplacement', zl='Nyanyi, entre Tanah Lot et Canggu : les rizières d’un côté, la plage et Nuanu de l’autre.',
  near=[('Plage de Nyanyi', 'sur la même route'), ('Nuanu Creative City', '5 min'), ('Luna Beach Club', 'tout près, à Nuanu'), ('Pererenan et Canggu', '10 à 15 min'), ('Temple de Tanah Lot', 'dans le secteur')],
  maps='Voir sur Google Maps', mtitle='Emplacement de la Villa Yuga, Nyanyi',
  ah='Comment se passe l’achat', al='Unaya vous accompagne à chaque étape.',
  steps=[('chat', 'Premier contact', 'Questions, photos, visite sur place à Nyanyi, ou en vidéo si vous êtes loin.'),
         ('doc', 'Vérifications', 'Votre avocat vérifie le bail, les permis et les documents de la villa.'),
         ('key', 'Chez le notaire', 'Signature de la cession du bail chez le notaire et paiement.'),
         ('report', 'La villa continue', 'Si vous le souhaitez, Unaya continue la location. Vous recevez un rapport chaque mois.')],
  qh='Questions fréquentes',
  qs=[('Un étranger peut-il acheter la villa ?', 'Oui. Elle est vendue en leasehold : on vous cède le bail du terrain, avec la villa, jusqu’au 20 juin 2054. C’est la formule la plus courante à Bali pour les acheteurs étrangers. Plus de détails dans notre guide <a href="/fr/guides/leasehold-bali/">le leasehold à Bali</a>.'),
      ('Pourra-t-on continuer à louer à la nuit ?', 'Oui. Unaya Villa Management gère déjà la villa et peut continuer après la vente, sous sa licence. C’est important parce que, depuis mai 2026, une nouvelle PT PMA ne peut plus obtenir cette licence à Bali. Voir nos <a href="/fr/proprietaires/tarifs/">formules de gestion</a>.'),
      ('À quel prix se loue-t-elle ?', 'Aujourd’hui, à partir de IDR 2 900 000 la nuit pour la villa entière et de IDR 650 000 pour une chambre (voir la <a href="/fr/villas/yuga/">page de location</a>). Pour estimer ce qu’une villa rapporte, lisez <a href="/fr/guides/combien-rapporte-une-villa-a-bali/">notre calcul pas à pas</a>.'),
      ('Qu’est-ce qui est compris dans le prix ?', 'La villa, son mobilier et son équipement (linge et produits voyageurs compris), et les années de bail qui restent, jusqu’en juin 2054, avec la priorité pour prolonger.'),
      ('Où en sont les permis ?', 'Les permis (PBG et SLF) sont en cours : le dossier a été déposé en septembre 2026. Nous vous montrons où il en est, et votre avocat peut le vérifier.'),
      ('Le prix est en roupies ou en dollars ?', 'Le prix de référence est IDR 5 900 000 000. Le montant en dollars (≈ 325 000 USD) est indicatif, au taux du 11 novembre 2026.')],
  vf=dict(h='Planifier une visite', p='Sur place à Nyanyi, ou en vidéo si vous êtes loin. Choisissez un jour, nous vous confirmons l’heure sur WhatsApp.',
          rep=[('Sur place à Balangan', 'Sur place à Nyanyi'), ('Visite de la Villa B — Arawa Villas, Balangan.', 'Visite de la Villa Yuga — Nyanyi.')]),
  legal='Informations données à titre indicatif, sans valeur contractuelle, sous réserve de disponibilité. Faites vérifier les documents par votre notaire ou votre avocat avant tout engagement.',
  card=dict(zone='Nyanyi · Tanah Lot', st='Disponible', title='Villa Yuga', pts=['4 suites', 'Terrain 310 m²', 'Déjà louée'], left='≈ 325 000 USD · bail jusqu’en 2054', price='IDR 5,9 milliards', more='Voir la villa', alt='Villa Yuga à vendre, Nyanyi'),
  ),
 'en': dict(
  title='Villa for Sale in Nyanyi, Tanah Lot: Yuga, 4 Bedrooms, Pool | Unaya',
  desc='Villa Yuga for sale in Nyanyi, near Tanah Lot and Canggu: 4 suites, private pool, sold furnished and already renting. Lease to 2054. IDR 5.9 billion (≈ USD 325,000).',
  bc=[('Home', '/'), ('Villas for sale', '/villas-for-sale/'), ('Villa Yuga', None)],
  kick='Nyanyi · Tabanan · Bali', h1='Villa Yuga, a 4-bedroom villa for sale in Nyanyi',
  sub='Four suites around one pool, looking out over the rice fields of Beraban. Sold furnished and already taking guests: you keep renting from day one.',
  badges=['Available', 'Already renting · 9.6/10', 'Lease to 2054'],
  facts=[('bed', 'Bedrooms', '4 suites', 'each with a bathroom'), ('map', 'Land', '310 m²', '3.1 are'), ('pool', 'Pool', 'Private', 'with sun deck'), ('doc', 'Lease', '≈ 27.5 years', 'to June 2054')],
  more='See all {n} photos',
  dh='The villa',
  dp=['Yuga is four suites around one pool, on 310 m² of land facing the rice fields of Beraban. It sits on Jalan Pantai Nyanyi, the road down to Nyanyi Beach, in one of the fastest-moving corners of the Tanah Lot coast. Nuanu and its restaurants are 5 minutes away, Pererenan and Canggu 10–15 minutes, without their traffic.',
      'Finished in 2026, it is sold fully furnished and equipped, and it already takes guests, who rate it 9.6/10. It rents as a whole or by the room, and the cleaning and pool staff are in place.',
      'Since October 2026 it has been run by Unaya Villa Management. You can keep that management after you buy: nightly rentals carry on under Unaya’s licence, even if you live abroad.'],
  why=['Already renting, with very good guest reviews', 'Sold furnished: linen, equipment and guest supplies included', 'Nightly rentals possible straight away, under Unaya’s licence', 'Fibre Wi-Fi, smart switches, staff in place'],
  lh='Lease and documents',
  lease=[('Type', 'leasehold (notarial lease), transferred with the villa'), ('Lease ends', '20 June 2054, about 27.5 years left'), ('Extension', 'priority to extend, at the market price at that time'),
         ('Permits (PBG / SLF)', 'in progress, application filed in September 2026'), ('Furniture', 'sold fully furnished and equipped')],
  lnote='Have the lease and documents checked by your notary or lawyer before you commit.',
  pk='Price', usd='≈ USD 325,000', rate='1 USD = IDR 18,158 (11 Nov 2026). The reference price is in rupiah.',
  b1='Book a viewing', b2='Chat on WhatsApp', dl='Download the brochure (PDF)',
  wa='Hello Unaya, I’m interested in Villa Yuga for sale in Nyanyi.',
  other='See also <a href="/villas-for-sale/arawa-balangan/">Arawa Villas</a> in Balangan, from USD 170,000.',
  share='Share', copy='Copy link', copied='Link copied',
  vh='What you are buying', vl='A finished, furnished villa that is already up and running.',
  lv=[('yuga-chambre.jpg', 'bed', 'The four suites', ['4 air-conditioned bedrooms, each with its own bathroom', '3 king-size beds and 1 twin room', 'A private terrace for each room, onto the garden and pool', 'A desk in the rooms']),
      ('yuga-g2.jpg', 'pool', 'Outside', ['Private pool with sun deck', 'Sun loungers and parasols', 'Outdoor kitchen', 'Tropical garden and rice-field view', 'Private parking']),
      ('yuga-terrasse.jpg', 'key', 'Ready to rent', ['Fully furnished and equipped', 'Linen and guest supplies', 'Fibre Wi-Fi, smart switches, safe', 'Cleaning and pool staff in place'])],
  rh='Buying from abroad?',
  rp=['Since May 2026, a new PT PMA (foreign-owned company) can no longer get a licence in Bali to rent out a villa by the night. It is the main problem foreign buyers face right now.',
      'With Yuga, that is solved: Unaya Villa Management can keep running the villa and renting it by the night under its own licence. You receive the income and a report every month, wherever you are.'],
  rl=('How our management works', '/owners/services/'), rl2=('Leasehold explained', '/guides/leasehold-bali/'),
  zh='Location', zl='Nyanyi, between Tanah Lot and Canggu: rice fields on one side, the beach and Nuanu on the other.',
  near=[('Nyanyi Beach', 'on the same road'), ('Nuanu Creative City', '5 min'), ('Luna Beach Club', 'close by, at Nuanu'), ('Pererenan and Canggu', '10 to 15 min'), ('Tanah Lot temple', 'in the area')],
  maps='View on Google Maps', mtitle='Location of Villa Yuga, Nyanyi',
  ah='How buying works', al='Unaya guides you through each step.',
  steps=[('chat', 'First contact', 'Questions, photos, a viewing on site in Nyanyi, or by video if you are far away.'),
         ('doc', 'Checks', 'Your lawyer checks the lease, the permits and the villa’s documents.'),
         ('key', 'At the notary', 'The lease transfer is signed before a notary and paid.'),
         ('report', 'The villa carries on', 'If you wish, Unaya keeps renting it out. You get a report every month.')],
  qh='Frequently asked questions',
  qs=[('Can a foreigner buy the villa?', 'Yes. It is sold as a leasehold: the land lease is transferred to you, with the villa, until 20 June 2054. It is the most common route in Bali for foreign buyers. More in our guide <a href="/guides/leasehold-bali/">leasehold in Bali</a>.'),
      ('Can it keep renting by the night?', 'Yes. Unaya Villa Management already runs the villa and can carry on after the sale, under its licence. That matters because, since May 2026, a new PT PMA can no longer get that licence in Bali. See our <a href="/owners/pricing/">management plans</a>.'),
      ('What does it rent for?', 'Today, from IDR 2,900,000 a night for the whole villa and from IDR 650,000 for one room (see the <a href="/villas/yuga/">rental page</a>). To estimate what a villa earns, read <a href="/guides/bali-villa-rental-income/">our step-by-step calculation</a>.'),
      ('What is included in the price?', 'The villa, its furniture and equipment (linen and guest supplies included), and the remaining lease years, until June 2054, with priority to extend.'),
      ('Where are the permits?', 'The permits (PBG and SLF) are in progress: the application was filed in September 2026. We show you where it stands, and your lawyer can check it.'),
      ('Is the price in rupiah or dollars?', 'The reference price is IDR 5,900,000,000. The dollar amount (≈ USD 325,000) is indicative, at the 11 November 2026 rate.')],
  vf=dict(h='Book a viewing', p='On site in Nyanyi, or by video if you are far away. Pick a day and we confirm the time on WhatsApp.',
          rep=[('On site in Balangan', 'On site in Nyanyi'), ('Viewing of Villa B — Arawa Villas, Balangan.', 'Viewing of Villa Yuga — Nyanyi.')]),
  legal='Information given for guidance only, not contractual, subject to availability. Have the documents checked by your notary or lawyer before any commitment.',
  card=dict(zone='Nyanyi · Tanah Lot', st='Available', title='Villa Yuga', pts=['4 suites', '310 m² land', 'Already renting'], left='≈ USD 325,000 · lease to 2054', price='IDR 5.9 billion', more='View the villa', alt='Villa Yuga for sale, Nyanyi'),
  )}
PRICE = {'fr': 'IDR 5 900 000 000', 'en': 'IDR 5,900,000,000'}

def visit_form(lang):
    s = open(os.path.join(SRC, lang, 'ArawaVillaB.html')).read()
    sec = [x for x in re.split(r'(?=<section)', s) if 'id="visite"' in x][0].strip()
    v = T[lang]['vf']
    sec = re.sub(r'<h2>[^<]*</h2><p>[^<]*</p>', f'<h2>{v["h"]}</h2><p>{v["p"]}</p>', sec, count=1)
    for a, b in v['rep']:
        sec = sec.replace(a, b)
    return sec.replace('class="ar-visit"', 'class="ar-visit" data-subject="Villa Yuga"')

def page(lang):
    x = T[lang]; fr = lang == 'fr'
    full = 'https://unayabali.com' + URL[lang]
    bc = ' <span>›</span> '.join(f'<a href="{u}">{n}</a>' if u else n for n, u in x['bc'])
    s = f'<!-- title: {x["title"]} -->\n'
    s += (f'<section class="ld-hero"><img src="/assets/images/yuga-piscine.jpg" alt="" fetchpriority="high"><div class="ld-hero__in"><nav class="art-bc" aria-label="breadcrumb">{bc}</nav>'
          f'<p class="ld-kick">{x["kick"]}</p><h1>{x["h1"]}</h1><p>{x["sub"]}</p><div class="ld-badges">' +
          ''.join(f'<span class="ld-badge{" ld-badge--ok" if i == 0 else ""}">{b}</span>' for i, b in enumerate(x['badges'])) + '</div></div></section>\n')
    s += '<section class="ld-facts"><div class="ld-facts__in">' + ''.join(f'<div class="ld-fact">{ic(k, 30)}<span>{a}</span><strong>{b}</strong><em>{c}</em></div>' for k, a, b, c in x['facts']) + '</div></section>\n'
    g = lambda i: (GAL[i][0], GAL[i][1 if fr else 2])
    s += (f'<section class="u-sec ar-mz-sec"><div class="u-wrap"><div class="ar-mz"><a class="ar-mz__big" href="#galerie" data-open-gallery><img src="/assets/images/{g(1)[0]}" alt="{g(1)[1]}"></a>'
          f'<a class="ar-mz__s" href="#galerie" data-open-gallery><img src="/assets/images/{g(2)[0]}" alt="{g(2)[1]}" loading="lazy"></a>'
          f'<a class="ar-mz__s ar-mz__more" href="#galerie" data-open-gallery><img src="/assets/images/{g(3)[0]}" alt="{g(3)[1]}" loading="lazy"><span>{x["more"].format(n=len(GAL))}</span></a></div>'
          '<div hidden data-gallery id="galerie">' + ''.join(f'<figure><img src="/assets/images/{f}" alt="{a if fr else e}" loading="lazy"></figure>' for f, a, e in GAL) + '</div></div></section>\n')
    wa = f'https://wa.me/{WA}?text={quote(x["wa"])}'
    sh = quote(f'Villa Yuga — Nyanyi, Bali {full}')
    s += (f'<section class="u-sec"><div class="u-wrap"><div class="ld-main"><div class="ld-desc"><div class="u-head"><h2>{x["dh"]}</h2></div>' + ''.join(f'<p>{p}</p>' for p in x['dp']) +
          '<ul class="u-checks">' + ''.join(f'<li>{w}</li>' for w in x['why']) + '</ul>'
          f'<div class="ar-lease"><h3>{x["lh"]}</h3><dl>' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in x['lease']) + f'</dl><p>{x["lnote"]}</p></div></div>'
          f'<aside class="ld-price"><span class="ld-price__k">{x["pk"]}</span><div class="ar-pr"><span>Villa Yuga</span><strong>{PRICE[lang]}</strong><em>{x["usd"]}</em></div>'
          f'<a class="u-btn u-btn--rose" href="#visite">{x["b1"]}</a><a class="ld-wa" href="{wa}" target="_blank" rel="noopener">{x["b2"]}</a>'
          f'<div class="ar-dl"><a href="/assets/docs/villa-yuga-{lang}.pdf" download>{x["dl"]}</a></div><p>{x["rate"]}</p><p class="ar-other">{x["other"]}</p>'
          f'<div class="ar-share" data-share-url="{full}" data-share-title="Villa Yuga — Nyanyi, Bali"><span>{x["share"]}</span>'
          f'<a href="https://wa.me/?text={sh}" target="_blank" rel="noopener" aria-label="WhatsApp">WhatsApp</a>'
          f'<a href="https://www.facebook.com/sharer/sharer.php?u={quote(full, safe="")}" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>'
          f'<a href="mailto:?subject={quote("Villa Yuga — Nyanyi, Bali")}&amp;body={quote(full, safe="")}" aria-label="E-mail">E-mail</a>'
          f'<button type="button" class="ar-copy" data-ok="{x["copied"]}">{x["copy"]}</button></div></aside></div></div></section>\n')
    s += (f'<section class="u-sec u-sec--white"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["vh"]}</h2><p>{x["vl"]}</p></div><div class="ar-lv2">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__img"><img src="/assets/images/{im}" alt="{h}" loading="lazy"><span class="ar-lv2__n">0{i}</span></div>'
                  f'<div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(k, 26)}</span><h3>{h}</h3><ul>' + ''.join(f'<li>{li}</li>' for li in lst) + '</ul></div></article>'
                  for i, (im, k, h, lst) in enumerate(x['lv'], 1)) + '</div></div></section>\n')
    s += (f'<section class="u-sec"><div class="u-wrap"><div class="u-split"><div class="u-split__img u-arch"><img src="/assets/images/yuga-nuit.jpg" alt="" loading="lazy"></div>'
          f'<div class="u-split__txt"><h2>{x["rh"]}</h2>' + ''.join(f'<p>{p}</p>' for p in x['rp']) +
          f'<div class="u-btns"><a class="u-link" href="{x["rl"][1]}">{x["rl"][0]}</a><a class="u-link" href="{x["rl2"][1]}">{x["rl2"][0]}</a></div></div></div></div></section>\n')
    s += (f'<section class="u-sec u-sec--white"><div class="u-wrap"><div class="u-head"><h2>{x["zh"]}</h2><p>{x["zl"]}</p></div><div class="ld-zone yg-zone"><div class="ld-map">'
          f'<iframe title="{x["mtitle"]}" src="https://maps.google.com/maps?q={LAT},{LNG}&amp;t=k&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
          f'<a class="u-btn u-btn--line" href="{GMAP}" target="_blank" rel="noopener">{x["maps"]} ↗</a></div>'
          '<ul class="yg-near">' + ''.join(f'<li><span>{a}</span><strong>{b}</strong></li>' for a, b in x['near']) + '</ul></div></div></section>\n')
    s += (f'<section class="u-sec"><div class="u-wrap"><div class="u-head"><h2>{x["ah"]}</h2><p>{x["al"]}</p></div><div class="u-path u-path--4">' +
          ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k, 34)}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k, h, p in x['steps']) + '</div></div></section>\n')
    s += f'<section class="u-sec u-sec--white"><div class="u-wrap"><div class="u-head"><h2>{x["qh"]}</h2></div>{faq(x["qs"])}</div></section>\n'
    vf = visit_form(lang)
    s += vf.replace('</form></div></div></section>', f'</form><p class="ld-legal">{x["legal"]}</p></div></div></section>', 1) + '\n'
    return s

def card(lang):
    c = T[lang]['card']
    return (f'<a class="vl-card ld-card" href="{URL[lang]}"><div class="vl-card__img"><img src="/assets/images/yuga-piscine.jpg" alt="{c["alt"]}" loading="lazy"><span class="vl-card__zone">{c["zone"]}</span></div>'
            f'<div class="vl-card__b"><span class="ld-card__st">{c["st"]}</span><h3>{c["title"]}</h3><div class="vl-card__meta">' + ''.join(f'<span>{p}</span>' for p in c['pts']) +
            f'</div><div class="ld-card__p"><span>{c["left"]}</span><strong>{c["price"]}</strong></div><span class="u-link">{c["more"]}</span></div></a>')

META = {(l, 'VillaYugaVente'): (T[l]['title'], T[l]['desc']) for l in ('fr', 'en')}

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'VillaYugaVente.html'), 'w').write(page(lang))
        p = os.path.join(SRC, lang, 'VillasAVendre.html'); s = open(p).read()
        s = re.sub(r'<a class="vl-card ld-card" href="/(?:fr/villas-a-vendre|villas-for-sale)/yuga-nyanyi/">.*?</a>(?=<a class="vl-card|<div class="ld-soon")', '', s, flags=re.S)
        s = s.replace('<div class="ld-soon">', card(lang) + '<div class="ld-soon">', 1)
        open(p, 'w').write(s)
    r = os.path.join(SRC, '..', 'routes.json'); R = json.load(open(r))
    R['VillaYugaVente'] = URL
    json.dump(R, open(r, "w"), ensure_ascii=False, indent=2)
    print('ok')
