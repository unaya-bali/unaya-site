# Pages de zone (FR/EN) pour le référencement local : gestion + location + achat dans chaque secteur.
# Génère src/pages/{fr,en}/Zone*.html. Faits : ceux déjà publiés sur le site (villas, biens, guide).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

def R(page, lang):
    import json
    return json.load(open(os.path.join(SRC, '..', 'routes.json')))[page][lang]

Z = {
 'ZoneUluwatu': dict(img='zone-uluwatu-jimbaran.jpg', fr=dict(
    title='Gestion et location de villa à Uluwatu et Jimbaran | Unaya Bali',
    desc="Gestion de villa à Uluwatu et Jimbaran (Balangan, Bingin, Melasti), location de villas avec piscine et biens à vendre. Notre bureau est à Jimbaran.",
    h1='Gestion et location de villa à Uluwatu et Jimbaran', slogan='Le sud de Bali, c’est chez nous.',
    sub='Notre bureau est à Jimbaran et deux de nos villas sont à Balangan. On connaît les routes, les plages, les artisans et les saisons du coin.',
    keys=[('≈ 30 à 50 min', 'de l’aéroport selon le quartier'), ('2 villas', 'gérées par Unaya à Balangan'), ('4 biens', 'à vendre : 2 villas, 2 terrains'), ('Bureau', 'à Jimbaran, sur place 7j/7')],
    intro_h='Pourquoi Uluwatu et Jimbaran', intro=[
      "C’est la péninsule de Bukit, tout au sud de Bali : des falaises, des plages de sable blanc (Balangan, Bingin, Padang Padang, Melasti) et certaines des meilleures vagues de l’île. Les voyageurs y viennent pour le surf, les couchers de soleil et le calme, loin des embouteillages de Canggu.",
      "Pour un propriétaire, c’est un secteur qui se loue bien toute l’année, avec une clientèle de couples, de familles et de surfeurs. Jimbaran, plus proche de l’aéroport, attire aussi pour sa baie et ses restaurants de poisson grillé sur la plage."],
    hoods=[('Jimbaran', 'La baie, le marché aux poissons, les restaurants sur le sable. À 20-30 minutes de l’aéroport.'), ('Balangan', 'Une plage sauvage entre deux falaises. C’est là que se trouvent SUMA Bali, Rumah Jambu et Arawa Villas.'),
           ('Bingin et Padang Padang', 'Petites criques, surf, warungs perchés sur la falaise.'), ('Melasti et Ungasan', 'Grandes plages de sable blanc, nouveaux beach clubs. Nos deux terrains à vendre sont à Melasti.'),
           ('Uluwatu et Pecatu', 'Le temple sur la falaise, le surf, des villas avec vue sur l’océan.')],
    faq=[('Combien coûte la gestion d’une villa à Uluwatu ?', 'Chez Unaya, la gestion complète est à partir de 18 % des revenus, calculés après les commissions des plateformes et la taxe d’hébergement, et le marketing seul à 11 %. Aucun frais fixe.'),
         ('Est-ce que vous vous occupez aussi des villas à Jimbaran, Ungasan ou Pecatu ?', 'Oui, toute la péninsule de Bukit : Jimbaran, Balangan, Bingin, Padang Padang, Uluwatu, Pecatu, Ungasan et Melasti. Notre bureau est à Jimbaran, donc on est sur place rapidement.'),
         ('Peut-on louer une villa à la chambre à Uluwatu ?', 'Oui : SUMA Bali, à Balangan, se loue à la chambre ou en entier. Rumah Jambu se loue en entier.'),
         ('Peut-on acheter une villa à Uluwatu quand on est étranger ?', 'Oui, en leasehold (bail longue durée signé chez le notaire). Nos villas à vendre à Balangan sont dans ce cas. Notre guide pour investir explique ce qu’il faut vérifier.')]),
   en=dict(
    title='Villa Management & Rentals in Uluwatu and Jimbaran | Unaya Bali',
    desc="Villa management in Uluwatu and Jimbaran (Balangan, Bingin, Melasti), private pool villa rentals and property for sale. Our office is in Jimbaran.",
    h1='Villa management & rentals in Uluwatu and Jimbaran', slogan='South Bali is home for us.',
    sub='Our office is in Jimbaran and two of our villas are in Balangan. We know the roads, the beaches, the tradespeople and the seasons here.',
    keys=[('≈ 30–50 min', 'from the airport, depending on the area'), ('2 villas', 'managed by Unaya in Balangan'), ('4 properties', 'for sale: 2 villas, 2 plots'), ('Office', 'in Jimbaran, on site 7 days a week')],
    intro_h='Why Uluwatu and Jimbaran', intro=[
      "This is the Bukit peninsula, at the very south of Bali: cliffs, white-sand beaches (Balangan, Bingin, Padang Padang, Melasti) and some of the best waves on the island. Guests come for the surf, the sunsets and the calm, far from Canggu’s traffic.",
      "For an owner, it is an area that rents well all year round, with couples, families and surfers. Jimbaran, closer to the airport, also draws people with its bay and grilled-fish restaurants on the beach."],
    hoods=[('Jimbaran', 'The bay, the fish market, restaurants on the sand. 20–30 minutes from the airport.'), ('Balangan', 'A wild beach between two cliffs. Home to SUMA Bali, Rumah Jambu and Arawa Villas.'),
           ('Bingin & Padang Padang', 'Small coves, surf, warungs perched on the cliff.'), ('Melasti & Ungasan', 'Big white-sand beaches, new beach clubs. Our two plots for sale are in Melasti.'),
           ('Uluwatu & Pecatu', 'The cliff-top temple, surf, ocean-view villas.')],
    faq=[('How much does villa management cost in Uluwatu?', 'At Unaya, full management starts at 18% of income, calculated after platform commissions and accommodation tax, and marketing only is 11%. No fixed fees.'),
         ('Do you also manage villas in Jimbaran, Ungasan or Pecatu?', 'Yes, the whole Bukit peninsula: Jimbaran, Balangan, Bingin, Padang Padang, Uluwatu, Pecatu, Ungasan and Melasti. Our office is in Jimbaran, so we are on site quickly.'),
         ('Can I rent a villa by the room in Uluwatu?', 'Yes: SUMA Bali, in Balangan, can be rented by the room or as a whole. Rumah Jambu is rented as a whole.'),
         ('Can a foreigner buy a villa in Uluwatu?', 'Yes, on a leasehold (long lease signed before a notary). Our villas for sale in Balangan are leasehold. Our investment guide explains what to check.')]),
   villas=['VillaSuma', 'VillaRumahJambu'], sale=['ArawaVillaB', 'ArawaVillaD', 'TerrainMelasti795', 'TerrainMelasti']),
 'ZoneTanahLot': dict(img='zone-tanah-lot-canggu.jpg', fr=dict(
    title='Gestion et location de villa à Tanah Lot et Canggu | Unaya Bali',
    desc="Gestion de villa à Tanah Lot, Nyanyi, Pererenan et Canggu, et location de villa avec piscine face aux rizières. Estimation de revenus gratuite.",
    h1='Gestion et location de villa à Tanah Lot et Canggu', slogan='Les rizières, à vingt minutes de Canggu.',
    sub='La Villa Yuga, à Nyanyi, est gérée par Unaya depuis son ouverture. On connaît ce secteur, entre plages de sable noir, temples et cafés de Canggu.',
    keys=[('≈ 1 h à 1 h 30', 'de l’aéroport selon la circulation'), ('Villa Yuga', 'gérée par Unaya à Nyanyi'), ('Rizières', 'et plages de sable noir'), ('Canggu', 'à 15-25 minutes')],
    intro_h='Pourquoi Tanah Lot et Canggu', intro=[
      "À l’ouest de Canggu, la côte devient plus calme : Pererenan, Nyanyi, Kedungu, puis le temple de Tanah Lot sur son rocher. Des rizières, des plages de sable noir où l’on surfe, et des villas avec vue sur les champs.",
      "Les voyageurs y cherchent le calme et le Bali des rizières, tout en restant près des cafés et des restaurants de Canggu. Pour un propriétaire, ce sont souvent de plus grands terrains et une clientèle de familles et de groupes d’amis."],
    hoods=[('Canggu et Berawa', 'Cafés, surf, coworkings : le secteur le plus animé, et le plus demandé.'), ('Pererenan', 'Plus calme que Canggu, avec de bons restaurants et la plage.'),
           ('Nyanyi', 'Rizières et plage de sable noir. C’est là que se trouve la Villa Yuga.'), ('Kedungu et Tanah Lot', 'Le temple sur la mer, des vagues pour débuter, la campagne balinaise.')],
    faq=[('Gérez-vous des villas à Canggu ?', 'Oui, de Canggu et Berawa jusqu’à Tanah Lot, en passant par Pererenan, Nyanyi et Kedungu.'),
         ('Combien coûte la gestion d’une villa à Tanah Lot ?', 'La même chose partout : gestion complète à partir de 18 % des revenus (après plateformes et taxe), marketing seul à 11 %. Aucun frais fixe.'),
         ('Peut-on louer la Villa Yuga à la chambre ?', 'Oui, la Villa Yuga se loue à la chambre ou en entier, avec −15 % dès 7 nuits en réservant en direct.'),
         ('Est-ce loin de l’aéroport ?', 'Comptez en général 1 h à 1 h 30 selon l’heure. Nous organisons le transfert depuis l’aéroport.')]),
   en=dict(
    title='Villa Management & Rentals in Tanah Lot and Canggu | Unaya Bali',
    desc="Villa management in Tanah Lot, Nyanyi, Pererenan and Canggu, and private pool villa rental facing the rice fields. Free income estimate.",
    h1='Villa management & rentals in Tanah Lot and Canggu', slogan='Rice fields, twenty minutes from Canggu.',
    sub='Villa Yuga, in Nyanyi, has been managed by Unaya since it opened. We know this area, between black-sand beaches, temples and Canggu’s cafés.',
    keys=[('≈ 1–1.5 h', 'from the airport, depending on traffic'), ('Villa Yuga', 'managed by Unaya in Nyanyi'), ('Rice fields', 'and black-sand beaches'), ('Canggu', '15–25 minutes away')],
    intro_h='Why Tanah Lot and Canggu', intro=[
      "West of Canggu the coast gets quieter: Pererenan, Nyanyi, Kedungu, then Tanah Lot temple on its rock. Rice fields, black-sand surf beaches and villas looking over the fields.",
      "Guests come for the calm and rice-field Bali while staying close to Canggu’s cafés and restaurants. For owners, plots are often bigger and guests are families and groups of friends."],
    hoods=[('Canggu & Berawa', 'Cafés, surf, coworking: the busiest area, and the most in demand.'), ('Pererenan', 'Quieter than Canggu, with good restaurants and the beach.'),
           ('Nyanyi', 'Rice fields and a black-sand beach. Home to Villa Yuga.'), ('Kedungu & Tanah Lot', 'The sea temple, beginner waves, the Balinese countryside.')],
    faq=[('Do you manage villas in Canggu?', 'Yes, from Canggu and Berawa to Tanah Lot, including Pererenan, Nyanyi and Kedungu.'),
         ('How much does villa management cost in Tanah Lot?', 'The same everywhere: full management from 18% of income (after platforms and tax), marketing only 11%. No fixed fees.'),
         ('Can I rent Villa Yuga by the room?', 'Yes, Villa Yuga can be rented by the room or as a whole, with −15% from 7 nights when you book direct.'),
         ('Is it far from the airport?', 'Usually 1 to 1.5 hours depending on the time of day. We arrange the airport transfer.')]),
   villas=['VillaYuga'], sale=['VillaYugaVente']),
 'ZoneSeminyak': dict(img='zone-seminyak-kerobokan.jpg', fr=dict(
    title='Gestion de villa à Seminyak et Kerobokan | Unaya Bali',
    desc="Gestion de villa à Seminyak, Kerobokan, Petitenget et Umalas : location sur Airbnb et Booking, voyageurs, entretien, comptabilité. Estimation gratuite.",
    h1='Gestion de villa à Seminyak et Kerobokan', slogan='Le Bali des beach clubs et des familles.',
    sub='Vous avez une villa à Seminyak, Petitenget, Kerobokan ou Umalas ? Nous prenons de nouvelles villas dans ce secteur, avec la même équipe et les mêmes engagements.',
    keys=[('≈ 30 à 45 min', 'de l’aéroport selon la circulation'), ('Toute l’année', 'une demande régulière'), ('18 %', 'gestion complète, aucun frais fixe'), ('Rapport', 'chaque mois, avec justificatifs')],
    intro_h='Pourquoi Seminyak et Kerobokan', intro=[
      "Seminyak et Petitenget, c’est le Bali des restaurants, des boutiques et des beach clubs, à deux pas de la plage. Kerobokan et Umalas, juste derrière, sont plus résidentiels : de grandes villas familiales au calme, entre rizières et nouvelles rues.",
      "La demande y est régulière toute l’année. Mais la concurrence entre villas est forte : les photos, les prix ajustés chaque jour et la qualité de l’accueil font la différence. C’est exactement notre travail."],
    hoods=[('Seminyak', 'Restaurants, boutiques, coucher de soleil sur la plage.'), ('Petitenget', 'Beach clubs et grandes adresses, entre Seminyak et Canggu.'),
           ('Kerobokan', 'Plus calme, des villas familiales avec jardin.'), ('Umalas', 'Résidentiel, vert, apprécié des familles et des longs séjours.')],
    faq=[('Gérez-vous déjà des villas à Seminyak ?', 'Nos villas actuelles sont à Uluwatu et Tanah Lot. Nous prenons de nouvelles villas à Seminyak, Petitenget, Kerobokan et Umalas, avec la même organisation.'),
         ('Que comprend la gestion d’une villa à Seminyak ?', 'Les annonces et les prix sur Airbnb, Booking et notre site, l’accueil des voyageurs, le ménage et l’entretien, le suivi de l’équipe, les taxes et un rapport chaque mois.'),
         ('Combien coûte la gestion ?', 'Gestion complète à partir de 18 % des revenus (après plateformes et taxe), marketing seul à 11 %. Aucun frais fixe ni frais d’entrée.')]),
   en=dict(
    title='Villa Management in Seminyak and Kerobokan | Unaya Bali',
    desc="Villa management in Seminyak, Kerobokan, Petitenget and Umalas: Airbnb and Booking listings, guests, upkeep and accounting. Free income estimate.",
    h1='Villa management in Seminyak and Kerobokan', slogan='Beach-club Bali, and family Bali.',
    sub='Own a villa in Seminyak, Petitenget, Kerobokan or Umalas? We take on new villas in this area, with the same team and the same commitments.',
    keys=[('≈ 30–45 min', 'from the airport, depending on traffic'), ('All year', 'steady demand'), ('18%', 'full management, no fixed fees'), ('Report', 'every month, with receipts')],
    intro_h='Why Seminyak and Kerobokan', intro=[
      "Seminyak and Petitenget are Bali’s restaurants, boutiques and beach clubs, a short walk from the beach. Kerobokan and Umalas, just behind, are more residential: big family villas in quiet streets, between rice fields and new roads.",
      "Demand is steady all year. But competition between villas is tough: photos, prices adjusted every day and the quality of the welcome make the difference. That is exactly our job."],
    hoods=[('Seminyak', 'Restaurants, boutiques, sunsets on the beach.'), ('Petitenget', 'Beach clubs and big names, between Seminyak and Canggu.'),
           ('Kerobokan', 'Quieter, family villas with gardens.'), ('Umalas', 'Residential and green, popular with families and long stays.')],
    faq=[('Do you already manage villas in Seminyak?', 'Our current villas are in Uluwatu and Tanah Lot. We take on new villas in Seminyak, Petitenget, Kerobokan and Umalas, with the same set-up.'),
         ('What does villa management in Seminyak include?', 'Listings and pricing on Airbnb, Booking and our website, guest welcome, cleaning and upkeep, staff supervision, taxes and a monthly report.'),
         ('How much does it cost?', 'Full management from 18% of income (after platforms and tax), marketing only 11%. No fixed or set-up fees.')]),
   villas=[], sale=[]),
}
VIL = {'VillaSuma': ('suma-piscine-2.jpg', 'SUMA Bali', {'fr': 'Balangan · 5 chambres · à la chambre ou entière', 'en': 'Balangan · 5 bedrooms · by the room or whole'}),
       'VillaRumahJambu': ('rumah-jambu-jardin.jpg', 'Rumah Jambu', {'fr': 'Balangan · maison balinaise avec jardin', 'en': 'Balangan · Balinese house with garden'}),
       'VillaYuga': ('yuga-piscine.jpg', 'Villa Yuga', {'fr': 'Nyanyi · 4 chambres · rizières', 'en': 'Nyanyi · 4 bedrooms · rice fields'})}
SALE = {'VillaYugaVente': ('yuga-piscine.jpg', {'fr': 'Villa Yuga', 'en': 'Villa Yuga'}, {'fr': 'Nyanyi · 4 suites · IDR 5,9 milliards (≈ 325 000 USD)', 'en': 'Nyanyi · 4 suites · IDR 5.9 billion (≈ USD 325,000)'}),
        'ArawaVillaB': ('arawa-facade.jpg', {'fr': 'Arawa · Villa B', 'en': 'Arawa · Villa B'}, {'fr': 'Balangan · 2 chambres · dès 170 000 USD', 'en': 'Balangan · 2 bedrooms · from USD 170,000'}),
        'ArawaVillaD': ('arawa-piscine.jpg', {'fr': 'Arawa · Villa D', 'en': 'Arawa · Villa D'}, {'fr': 'Balangan · 2 chambres · dès 195 000 USD', 'en': 'Balangan · 2 bedrooms · from USD 195,000'}),
        'TerrainMelasti795': ('terrain-melasti795-parcelle.jpg', {'fr': 'Terrain de 795 m²', 'en': '795 m² plot'}, {'fr': 'Melasti · zone rose · bail ou pleine propriété', 'en': 'Melasti · pink zone · leasehold or freehold'}),
        'TerrainMelasti': ('terrain-melasti-plage.jpg', {'fr': 'Terrain de 500 m²', 'en': '500 m² plot'}, {'fr': 'Melasti · zone rose · bail ou pleine propriété', 'en': 'Melasti · pink zone · leasehold or freehold'})}
L = {'fr': dict(doors_h='Que cherchez-vous ici ?', own=('Propriétaire', 'Faire gérer ma villa', 'Location, voyageurs, entretien et comptabilité. Estimation gratuite.', 'Confier ma villa', 'ConfierMaVilla'),
                guest=('Voyageur', 'Louer une villa', 'Des villas privées avec piscine, au calme. −15 % dès 7 nuits en direct.', 'Voir nos villas', 'Villas'),
                inv=('Investisseur', 'Acheter un bien', 'Villas et terrains à vendre, vérifiés par Unaya, et le guide pour acheter.', 'Investir à Bali', 'Investir'),
                vil_h='Nos villas dans le secteur', sale_h='À vendre dans le secteur', hood_h='Les quartiers', faq_h='Questions fréquentes', see='Voir', other_h='Nos autres zones',
                cta=('Une villa dans le secteur ?', 'Recevez une estimation de revenus gratuite sous 24 h.', 'Demander une estimation')),
     'en': dict(doors_h='What are you looking for here?', own=('Owner', 'Get my villa managed', 'Rentals, guests, upkeep and accounting. Free income estimate.', 'List my villa', 'ConfierMaVilla'),
                guest=('Guest', 'Rent a villa', 'Private pool villas in quiet spots. −15% from 7 nights direct.', 'See our villas', 'Villas'),
                inv=('Investor', 'Buy property', 'Villas and land for sale, checked by Unaya, and the buying guide.', 'Invest in Bali', 'Investir'),
                vil_h='Our villas in the area', sale_h='For sale in the area', hood_h='The neighbourhoods', faq_h='Frequently asked questions', see='View', other_h='Our other areas',
                cta=('A villa in the area?', 'Get a free income estimate within 24 hours.', 'Get an estimate'))}
ZNAME = {'ZoneUluwatu': {'fr': 'Uluwatu et Jimbaran', 'en': 'Uluwatu & Jimbaran'}, 'ZoneTanahLot': {'fr': 'Tanah Lot et Canggu', 'en': 'Tanah Lot & Canggu'}, 'ZoneSeminyak': {'fr': 'Seminyak et Kerobokan', 'en': 'Seminyak & Kerobokan'}}

def card(href, img, h, p, more):
    return (f'<a class="ar-lv2__c hm-door" href="{href}"><div class="ar-lv2__img"><img src="/assets/images/{img}" alt="{h}" loading="lazy"></div>'
            f'<div class="ar-lv2__b"><h3>{h}</h3><p class="ar-lv2__p">{p}</p><span class="u-link">{more}</span></div></a>')

def page(key, lang):
    z = Z[key]; t = z[lang]; l = L[lang]
    s = f'<!-- title: {t["title"]} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/{z["img"]}" alt="{ZNAME[key][lang]}" fetchpriority="high"><div class="hm-hero__in">'
          f'<h1 class="hm-hero__k">{t["h1"]}</h1><p class="hm-h1">{t["slogan"]}</p><p class="hm-hero__sub">{t["sub"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{R("ConfierMaVilla", lang)}">{l["own"][3]}</a><a class="u-btn hm-btn--glass" href="{R("Villas", lang)}">{l["guest"][3]}</a></div></div></section>\n')
    s += '<section class="iv-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in t['keys']) + '</div></section>\n'
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap zn-intro"><div class="u-head u-head--c"><h2>{t["intro_h"]}</h2></div>' + ''.join(f'<p>{p}</p>' for p in t['intro']) + '</div></section>\n')
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["doors_h"]}</h2></div><div class="ar-lv2 hm-doors">' +
          ''.join(card(R(d[4], lang), img, d[1], d[2], d[3]) for d, img in ((l['own'], 'yuga-drone.jpg'), (l['guest'], 'suma-piscine.jpg'), (l['inv'], 'arawa-facade.jpg'))) + '</div></div></section>\n')
    if z['villas']:
        s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["vil_h"]}</h2></div><div class="ar-lv2 hm-doors zn-{len(z["villas"])}">' +
              ''.join(card(R(v, lang), VIL[v][0], VIL[v][1], VIL[v][2][lang], l['see'] + ' →') for v in z['villas']) + '</div></div></section>\n')
    if z['sale']:
        s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["sale_h"]}</h2></div><div class="iv-ops">' +
              ''.join(f'<a class="vl-card ld-card iv-op" href="{R(v, lang)}"><div class="vl-card__img"><img src="/assets/images/{SALE[v][0]}" alt="{SALE[v][1][lang]}" loading="lazy"></div><div class="vl-card__b"><h3>{SALE[v][1][lang]}</h3><p>{SALE[v][2][lang]}</p><span class="u-link">{l["see"]}</span></div></a>' for v in z['sale']) +
              '</div></div></section>\n')
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["hood_h"]}</h2></div><div class="zn-hoods">' +
          ''.join(f'<div class="zn-hood"><strong>{a}</strong><span>{b}</span></div>' for a, b in t['hoods']) + '</div></div></section>\n')
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap zn-faq"><div class="u-head u-head--c"><h2>{l["faq_h"]}</h2></div><div class="u-faq">' +
          ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq']) + '</div></div></section>\n')
    others = [k for k in Z if k != key]
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{l["other_h"]}</h2></div><div class="ar-lv2 hm-doors zn-2">' +
          ''.join(card(R(k, lang), Z[k]['img'], ZNAME[k][lang], Z[k][lang]['slogan'], l['see'] + ' →') for k in others) + '</div></div></section>\n')
    s += (f'<section class="u-cta"><img src="/assets/images/{z["img"]}" alt="" loading="lazy"><div class="u-cta__in"><h2>{l["cta"][0]}</h2><p>{l["cta"][1]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{R("ConfierMaVilla", lang)}">{l["cta"][2]}</a></div></div></section>\n</div>\n<script src="/assets/js/invest.js" defer></script>\n')
    return s

META = {(lang, k): (Z[k][lang]['title'], Z[k][lang]['desc']) for k in Z for lang in ('fr', 'en')}

if __name__ == '__main__':
    for k in Z:
        for lang in ('fr', 'en'):
            open(os.path.join(SRC, lang, f'{k}.html'), 'w').write(page(k, lang))
    print('ok')
