import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/fb21bd82-28de-566e-9e55-058e68a3af45/scratchpad/gen')
from ui import ic, sec, head, cta, btn, faq
from urllib.parse import quote
R = '/home/claude/unaya-site/src/'
WA = '6285190211324'
GMAP = 'https://maps.app.goo.gl/otksPEBt1Gy6dxUA6'

GAL = [('arawa-facade.jpg', 'Façade et piscine privée', 'Front of the villa and private pool'),
       ('arawa-salon.jpg', 'Salon ouvert sur la piscine', 'Living room opening onto the pool'),
       ('arawa-sejour.jpg', 'Séjour, salle à manger et cuisine', 'Living, dining and kitchen'),
       ('arawa-piscine.jpg', 'Piscine et deck', 'Pool and deck'),
       ('arawa-piscine-2.jpg', 'Piscine, cabana et baies vitrées', 'Pool, cabana and glass doors'),
       ('arawa-chambre-1.jpg', 'Chambre 1', 'Bedroom 1'),
       ('arawa-sdb-1.jpg', 'Salle de bain de la chambre 1', 'Bedroom 1 bathroom'),
       ('arawa-chambre-2.jpg', 'Chambre 2', 'Bedroom 2'),
       ('arawa-residence.jpg', 'La résidence de 6 villas vue du ciel', 'Aerial view of the 6-villa residence')]

T = {'fr': dict(
    bc=[('Accueil', '/fr/'), ('Investir à Bali', '/fr/investir-a-bali/'), ('Villas à vendre', '/fr/villas-a-vendre/'), ('Arawa Villas', None)],
    kick='Balangan · Uluwatu · Bali', h1='Arawa Villas, 2 villas à vendre à Balangan',
    sub='Villas de 2 chambres avec piscine privée, livrées meublées fin décembre 2026. Presque terminées : vous visitez le vrai bien avant d’acheter.',
    badges=['2 villas disponibles', 'Livraison fin décembre 2026'],
    facts=[('bed', 'Chambres', '2 en suite', '+ WC invités'), ('home', 'Surface', '≈ 106 m²', 'sur 2 niveaux'), ('pool', 'Piscine', 'Privée', '4,5 × 2,5 m'), ('doc', 'Bail', '≈ 28 ans', '+ option 30 ans')],
    dh='Le projet',
    dp=['Arawa est une petite résidence de 6 villas à Balangan, côté Uluwatu. Il en reste deux à vendre, la B et la D. Le chantier est avancé à 85–90 % : la structure, les façades et les piscines sont là, les finitions sont en cours.',
        'Chaque villa a deux chambres avec salle de bain et dressing à l’étage, un grand séjour ouvert sur la piscine au rez-de-chaussée, et elle est livrée entièrement meublée et équipée. Vous pouvez y vivre, la louer, ou faire les deux.'],
    why=['Bien visitable dès maintenant, sans l’incertitude d’un achat sur plan', 'Livrée meublée et équipée, prête à louer', 'Garantie d’un an après la remise des clés', 'Gestion locative possible avec Unaya'],
    pk='Prix', villas=[('Villa B', '170 000', '91,80 m²'), ('Villa D', '195 000', '105,41 m²')], pfrom='à partir de', plot='parcelle',
    pb1='Demander la brochure ou une visite', pb2='Écrire sur WhatsApp', pnote='Prix en dollars américains, bail d’environ 28 ans avec option de prolongation de 30 ans.',
    ph='La philosophie Arawa', pl='Arawa ne se contente pas de vendre une villa. Le projet tient sur quatre idées simples.',
    phil=[('arch', 'Une construction soignée', 'Béton armé, bois d’ulin et de teck choisis à Java, mobilier et menuiseries fabriqués sur mesure par Arawa.'),
          ('sun', 'La lumière naturelle', 'Hauts plafonds, grandes baies vitrées : la maison s’ouvre sur la piscine et le jardin.'),
          ('leaf', 'La vie tropicale, en pratique', 'Des espaces pensés pour le quotidien : cuisine ouverte, douche extérieure, cabana, dressing dans chaque chambre.'),
          ('shield', 'Un achat transparent', 'Des points réguliers sur l’avancement et des réponses claires, de la première question à la remise des clés.')],
    gh='En images', gl='Images de synthèse (3D) du projet. Le rendu final peut varier légèrement.',
    vh='La villa', vl='Architecture tropicale contemporaine, pensée pour la lumière et un usage simple au quotidien.',
    lv=[('Rez-de-chaussée', ['Salon et salle à manger', 'Cuisine avec îlot', 'WC invités', 'Piscine privée de 4,5 × 2,5 m avec deck en pierre', 'Petite cabana et douche extérieure', 'Jardin']),
        ('Étage', ['2 chambres, chacune avec salle de bain et dressing', 'Une terrasse partagée', 'Climatisation dans les chambres']),
        ('Matériaux et équipements', ['Bois d’ulin et de teck de Java', 'Mobilier, cadres et menuiseries sur mesure', 'Piscine en pierre verte de Sukabumi, équipement Hayward', 'Puits privé en eau profonde pour la résidence'])],
    ch='Où en est le chantier', cl='Photos prises sur place en octobre et novembre 2026.', chc=['Villa B, 9 novembre 2026', 'Villa B, 26 octobre 2026', 'Villa D, 9 novembre 2026'],
    plh='Les plans', pll='Plan de masse de la résidence et plan type d’une villa de 2 chambres (indicatif).', plc=['Plan de masse : 6 villas autour d’une allée centrale', 'Rez-de-chaussée', 'Étage'],
    lh='L’emplacement', ll='Balangan, près du golf, des plages, des restaurants et des cafés d’Uluwatu, dans un coin resté calme.',
    loc=[('Supermarché, spa, salle de sport', '2 à 3 min'), ('Plage de Balangan', '4 à 5 min'), ('Plage de Dreamland', '9 min'), ('Plage de Bingin', '13 min'), ('Beach clubs, yoga, restaurants', '15 min'), ('Plage de Padang Padang', '17 min'), ('Aéroport international', '40 min')],
    maps='Voir sur Google Maps',
    ah='Comment se passe l’achat', al='Nous vous accompagnons à chaque étape, avec Arawa.',
    steps=[('chat', 'Premier contact', 'Brochure, réponses à vos questions et visite sur place, ou en vidéo si vous êtes loin.'),
           ('doc', 'Achat', 'Réservation de la villa puis signature du bail chez un notaire. Faites vérifier les documents par votre avocat.'),
           ('eye', 'Suivi du chantier', 'Photos et points réguliers jusqu’à la fin des travaux.'),
           ('key', 'Clés et location', 'Remise des clés fin décembre 2026. Si vous voulez louer la villa, Unaya peut s’en occuper.')],
    qh='Questions fréquentes',
    qs=[('Un étranger peut-il acheter ces villas ?', 'Oui. La villa est vendue en leasehold (bail) : vous avez le droit d’en profiter pendant environ 28 ans, avec une option de prolongation de 30 ans. C’est la formule la plus courante à Bali pour les acheteurs étrangers. Plus d’explications sur notre page <a href="/fr/investir-a-bali/">Investir à Bali</a>.'),
        ('Peut-on visiter ?', 'Oui. Les villas sont presque terminées, vous voyez le bien réel. Écrivez-nous pour fixer un rendez-vous, ou demandez une visite en vidéo.'),
        ('La villa peut-elle être louée ?', 'Oui, elle peut servir de résidence personnelle ou être louée. Unaya Management peut s’occuper de la location : annonces, voyageurs, ménage, entretien et rapport chaque mois. Voir nos <a href="/fr/proprietaires/tarifs/">formules</a>.'),
        ('Qu’est-ce qui est compris dans le prix ?', 'La villa terminée, entièrement meublée et équipée, avec une garantie d’un an après la remise des clés. Demandez-nous la liste du mobilier et le descriptif des matériaux.'),
        ('Pourquoi deux prix différents ?', 'La villa D est sur une parcelle plus grande (105,41 m² contre 91,80 m² pour la B).')],
    fh='Recevoir la brochure', fp='Brochure, plans, liste du mobilier ou visite : laissez vos coordonnées, nous vous répondons vite.',
    fl=('Nom', 'E-mail', 'WhatsApp (facultatif)', 'Villa', 'Message'), fo=['Villa B ou D, je ne sais pas encore', 'Villa B', 'Villa D'],
    fmsg='Bonjour, je suis intéressé(e) par les Arawa Villas à Balangan. Pouvez-vous m’envoyer la brochure ?',
    fc='J’accepte que mes données soient utilisées pour répondre à ma demande (politique de confidentialité).', fs='Envoyer la demande',
    legal='Informations données à titre indicatif, sans valeur contractuelle, sous réserve de disponibilité. Images de synthèse non contractuelles. Faites vérifier les documents par votre notaire ou votre avocat avant tout engagement.',
    wa_txt='Bonjour Unaya, je suis intéressé(e) par les Arawa Villas à Balangan.',
    t='Arawa Villas, Balangan — 2 villas 2 chambres à vendre dès 170 000 USD | Unaya Bali',
    # liste
    lt='Villas à vendre à Bali — Unaya Bali', lkick='Investir à Bali', lh1='Villas à vendre', lsub='Des villas choisies par notre équipe, à acheter pour y vivre, pour les louer, ou les deux.',
    lih='Villas disponibles', lil='Pour chaque projet, nous vérifions l’emplacement, l’avancement et les documents avant de le proposer.',
    card=dict(zone='Balangan · Uluwatu', title='Arawa Villas', pts=['2 chambres', '≈ 106 m²', 'Piscine privée'], status='2 villas disponibles', price='dès 170 000 USD', deal='Livraison fin déc. 2026', more='Voir les villas'),
    soon=('Bientôt', 'D’autres villas arrivent. Dites-nous ce que vous cherchez (zone, budget, nombre de chambres), nous vous prévenons en premier.', 'Nous contacter', '/fr/contact/'),
    ls=[('eye', 'Choisies', 'Emplacement, qualité de construction et avancement vérifiés sur place.'), ('doc', 'Expliquées', 'Bail, prix, ce qui est compris : tout est dit clairement.'), ('key', 'Louées', 'Après l’achat, Unaya peut gérer la location de votre villa.')],
    lc=('Vous cherchez autre chose ?', 'Un terrain, une villa à faire construire ou un bien à mettre en location : parlons-en.', ('Voir les terrains', '/fr/terrains/'), ('Nous contacter', '/fr/contact/'))),
  'en': dict(
    bc=[('Home', '/'), ('Invest in Bali', '/invest-in-bali/'), ('Villas for sale', '/villas-for-sale/'), ('Arawa Villas', None)],
    kick='Balangan · Uluwatu · Bali', h1='Arawa Villas, 2 villas for sale in Balangan',
    sub='Two-bedroom villas with a private pool, handed over fully furnished at the end of December 2026. Nearly finished: you see the real property before you buy.',
    badges=['2 villas available', 'Handover end of December 2026'],
    facts=[('bed', 'Bedrooms', '2 en suite', '+ guest WC'), ('home', 'Size', '≈ 106 m²', 'over 2 floors'), ('pool', 'Pool', 'Private', '4.5 × 2.5 m'), ('doc', 'Lease', '≈ 28 years', '+ 30-year option')],
    dh='The project',
    dp=['Arawa is a small residence of 6 villas in Balangan, on the Uluwatu side. Two are still for sale, B and D. Construction is 85–90% done: structure, façades and pools are in place, finishing works are under way.',
        'Each villa has two bedrooms upstairs, each with its own bathroom and walk-in wardrobe, and a large living space opening onto the pool downstairs. It comes fully furnished and equipped. Live in it, rent it out, or both.'],
    why=['You can visit the real property now, no off-plan uncertainty', 'Handed over furnished and equipped, ready to rent', 'One-year warranty after handover', 'Rental management available with Unaya'],
    pk='Price', villas=[('Villa B', '170,000', '91.80 m²'), ('Villa D', '195,000', '105.41 m²')], pfrom='from', plot='plot',
    pb1='Ask for the brochure or a viewing', pb2='Chat on WhatsApp', pnote='Prices in US dollars, lease of about 28 years with a 30-year extension option.',
    ph='The Arawa philosophy', pl='Arawa is about more than selling a villa. The project rests on four simple ideas.',
    phil=[('arch', 'Careful construction', 'Reinforced concrete, ironwood and teak selected in Java, furniture and joinery made to measure by Arawa.'),
          ('sun', 'Natural light', 'High ceilings and large glass doors: the house opens onto the pool and garden.'),
          ('leaf', 'Tropical living that works', 'Spaces designed for everyday life: open kitchen, outdoor shower, cabana, walk-in wardrobe in each bedroom.'),
          ('shield', 'A transparent purchase', 'Regular progress updates and clear answers, from your first question to handover.')],
    gh='Gallery', gl='3D renderings of the project. The finished villa may differ slightly.',
    vh='The villa', vl='Contemporary tropical architecture, designed around natural light and easy everyday living.',
    lv=[('Ground floor', ['Living and dining room', 'Kitchen with island', 'Guest WC', 'Private 4.5 × 2.5 m pool with stone deck', 'Small cabana and outdoor shower', 'Garden']),
        ('Upstairs', ['2 bedrooms, each with bathroom and walk-in wardrobe', 'A shared terrace', 'Air conditioning in the bedrooms']),
        ('Materials and equipment', ['Ironwood (ulin) and teak from Java', 'Made-to-measure furniture, frames and joinery', 'Green Sukabumi stone pool, Hayward equipment', 'Private deep-water well for the residence'])],
    ch='Construction progress', cl='Photos taken on site in October and November 2026.', chc=['Villa B, 9 November 2026', 'Villa B, 26 October 2026', 'Villa D, 9 November 2026'],
    plh='Plans', pll='Site plan of the residence and a typical two-bedroom villa layout (indicative).', plc=['Site plan: 6 villas along a central walkway', 'Ground floor', 'Upstairs'],
    lh='Location', ll='Balangan, close to the golf course, beaches, restaurants and cafés of Uluwatu, in a quiet corner.',
    loc=[('Supermarket, spa, gym', '2–3 min'), ('Balangan Beach', '4–5 min'), ('Dreamland Beach', '9 min'), ('Bingin Beach', '13 min'), ('Beach clubs, yoga, restaurants', '15 min'), ('Padang Padang Beach', '17 min'), ('International airport', '40 min')],
    maps='View on Google Maps',
    ah='How buying works', al='We support you at every step, together with Arawa.',
    steps=[('chat', 'First contact', 'Brochure, answers to your questions and a viewing on site, or by video if you are far away.'),
           ('doc', 'Purchase', 'Reserve the villa, then sign the lease with a notary. Have the documents checked by your lawyer.'),
           ('eye', 'Construction updates', 'Photos and regular updates until the works are finished.'),
           ('key', 'Keys and renting', 'Handover at the end of December 2026. If you want to rent the villa out, Unaya can take care of it.')],
    qh='Frequently asked questions',
    qs=[('Can a foreigner buy these villas?', 'Yes. The villa is sold leasehold: you have the right to use it for about 28 years, with a 30-year extension option. It is the most common route for foreign buyers in Bali. More on our <a href="/invest-in-bali/">Invest in Bali</a> page.'),
        ('Can I visit?', 'Yes. The villas are nearly finished, so you see the real property. Message us to book a time, or ask for a video tour.'),
        ('Can the villa be rented out?', 'Yes, it can be a personal home or a rental. Unaya Management can run the rental for you: listings, guests, cleaning, maintenance and a monthly report. See our <a href="/owners/pricing/">packages</a>.'),
        ('What is included in the price?', 'The finished villa, fully furnished and equipped, with a one-year warranty after handover. Ask us for the furniture list and the materials schedule.'),
        ('Why two different prices?', 'Villa D sits on a larger plot (105.41 m² versus 91.80 m² for villa B).')],
    fh='Get the brochure', fp='Brochure, plans, furniture list or a viewing: leave your details and we will get back to you quickly.',
    fl=('Name', 'Email', 'WhatsApp (optional)', 'Villa', 'Message'), fo=['Villa B or D, not sure yet', 'Villa B', 'Villa D'],
    fmsg='Hello, I am interested in Arawa Villas in Balangan. Could you send me the brochure?',
    fc='I agree that my data may be used to reply to my request (privacy policy).', fs='Send request',
    legal='Information given for guidance only, not contractual, subject to availability. 3D renderings are not contractual. Have the documents checked by your notary or lawyer before committing.',
    wa_txt="Hello Unaya, I'm interested in Arawa Villas in Balangan.",
    t='Arawa Villas, Balangan — 2-Bedroom Pool Villas for Sale from USD 170,000 | Unaya Bali',
    lt='Villas for Sale in Bali — Unaya Bali', lkick='Invest in Bali', lh1='Villas for sale', lsub='Villas chosen by our team, to buy as a home, a rental, or both.',
    lih='Available villas', lil='For every project we check the location, progress and documents before we list it.',
    card=dict(zone='Balangan · Uluwatu', title='Arawa Villas', pts=['2 bedrooms', '≈ 106 m²', 'Private pool'], status='2 villas available', price='from USD 170,000', deal='Handover end Dec. 2026', more='View the villas'),
    soon=('Coming soon', 'More villas are on the way. Tell us what you are looking for (area, budget, bedrooms) and we will let you know first.', 'Contact us', '/contact/'),
    ls=[('eye', 'Chosen', 'Location, build quality and progress checked on site.'), ('doc', 'Explained', 'Lease, price, what is included: all said clearly.'), ('key', 'Rented', 'After you buy, Unaya can manage the rental of your villa.')],
    lc=('Looking for something else?', 'A plot of land, a villa to build or a property to rent out: let’s talk.', ('See available land', '/land/'), ('Contact us', '/contact/')))}

L = "display:flex;flex-direction:column;gap:8px;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#5A3552;flex:1 1 240px;"
I = "font-family:'Jost',sans-serif;font-size:16px;padding:14px;border:1px solid #D9CCC2;background:#FFFFFF;color:#2E2429;"
for l, t in T.items():
    fr = l == 'fr'
    bc = ' <span>›</span> '.join(f'<a href="{u}">{n}</a>' if u else n for n, u in t['bc'])
    wa = f'https://wa.me/{WA}?text={quote(t["wa_txt"])}'
    s = f'<!-- title: {t["t"]} -->\n'
    s += (f'<section class="ld-hero"><img src="/assets/images/arawa-facade.jpg" alt="" fetchpriority="high"><div class="ld-hero__in">'
          f'<nav class="art-bc" aria-label="breadcrumb">{bc}</nav><p class="ld-kick">{t["kick"]}</p><h1>{t["h1"]}</h1><p>{t["sub"]}</p>'
          f'<div class="ld-badges"><span class="ld-badge ld-badge--ok">{t["badges"][0]}</span><span class="ld-badge">{t["badges"][1]}</span></div></div></section>\n')
    s += '<section class="ld-facts"><div class="ld-facts__in">' + ''.join(f'<div class="ld-fact">{ic(k,30)}<span>{a}</span><strong>{b}</strong><em>{c}</em></div>' for k, a, b, c in t['facts']) + '</div></section>\n'
    desc = ''.join(f'<p>{p}</p>' for p in t['dp']) + '<ul class="u-checks">' + ''.join(f'<li>{w}</li>' for w in t['why']) + '</ul>'
    rows = ''.join(f'<div class="ar-pr"><span>{n}</span><strong><small>{t["pfrom"]}</small> USD {p}</strong><em>{t["plot"]} {pl}</em></div>' for n, p, pl in t['villas'])
    price = (f'<aside class="ld-price"><span class="ld-price__k">{t["pk"]}</span>{rows}'
             f'<a class="u-btn u-btn--rose" href="#dossier">{t["pb1"]}</a><a class="ld-wa" href="{wa}" target="_blank" rel="noopener">{t["pb2"]}</a>'
             f'<p>{t["pnote"]}</p></aside>')
    s += sec(f'<div class="ld-main"><div class="ld-desc">{head(t["dh"])}{desc}</div>{price}</div>')
    s += sec(head(t['ph'], t['pl']) + '<div class="u-feats u-feats--4">' + ''.join(f'<div class="u-feat">{ic(k)}<h3>{h}</h3><p>{p}</p></div>' for k, h, p in t['phil']) + '</div>', 'white')
    gal = ''.join(f'<figure><img src="/assets/images/{f}" alt="{a if fr else b}" loading="lazy"></figure>' for f, a, b in GAL)
    s += sec(head(t['gh'], t['gl']) + f'<div class="ar-gal" data-gallery>{gal}</div>')
    lv = ''.join(f'<div class="ld-ar"><h3>{h}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in li) + '</ul></div>' for h, li in t['lv'])
    s += sec(head(t['vh'], t['vl']) + f'<div class="ld-around ar-lv">{lv}</div>', 'white')
    ph = ''.join(f'<figure><img src="/assets/images/arawa-chantier-{i+1}.jpg" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for i, c in enumerate(t['chc']))
    s += sec(head(t['ch'], t['cl']) + f'<div class="ar-site">{ph}</div>')
    pl = ''.join(f'<figure><a href="/assets/images/{f}" target="_blank" rel="noopener"><img src="/assets/images/{f}" alt="{c}" loading="lazy"></a><figcaption>{c}</figcaption></figure>' for f, c in zip(['arawa-plan-masse.jpg', 'arawa-plan-rdc.jpg', 'arawa-plan-etage.jpg'], t['plc']))
    s += sec(head(t['plh'], t['pll']) + f'<div class="ar-plans">{pl}</div>', 'white')
    tbl = '<dl class="ld-tbl">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in t['loc']) + '</dl>'
    s += sec(head(t['lh'], t['ll']) + f'<div class="ar-loc">{tbl}<a class="u-btn u-btn--line" href="{GMAP}" target="_blank" rel="noopener">{t["maps"]} ↗</a></div>')
    st = '<div class="u-path u-path--4">' + ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k,34)}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k, h, p in t['steps']) + '</div>'
    s += sec(head(t['ah'], t['al']) + st, 'white')
    s += sec(head(t['qh']) + faq(t['qs']))
    form = (f'<form style="width:100%;background:#FFFFFF;border:1px solid #E6DCD4;padding:40px;display:flex;flex-direction:column;gap:20px;">'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{t["fl"][0]}<input type="text" style="{I}"></label><label style="{L}">{t["fl"][1]}<input type="email" style="{I}"></label></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{t["fl"][2]}<input type="tel" style="{I}"></label><label style="{L}">{t["fl"][3]}<select style="{I}">' + ''.join(f'<option>{o}</option>' for o in t['fo']) + '</select></label></div>'
            f'<label style="{L}">{t["fl"][4]}<textarea rows="5" style="{I}">{t["fmsg"]}</textarea></label>'
            f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><input type="checkbox" style="margin-top: 5px;">{t["fc"]}</label>'
            f'<button type="button" style="display:inline-block;padding:16px 30px;background:#3F2A3A;color:#F7F2EE;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;border:none;font-family:\'Jost\',sans-serif;cursor:pointer;align-self:flex-start;">{t["fs"]}</button></form>')
    s += sec(f'<div class="ld-form">{head(t["fh"],t["fp"])}{form}<p class="ld-legal">{t["legal"]}</p></div>', 'white', id='dossier')
    open(R + f'pages/{l}/ArawaVillas.html', 'w').write(s)

    # ---- page liste ----
    c = t['card']
    href = '/fr/villas-a-vendre/arawa-balangan/' if fr else '/villas-for-sale/arawa-balangan/'
    s = f'<!-- title: {t["lt"]} -->\n'
    s += (f'<section class="u-hero"><img src="/assets/images/arawa-piscine-2.jpg" alt="" fetchpriority="high"><div class="u-hero__in"><p class="u-hero__k">{t["lkick"]}</p><h1>{t["lh1"]}</h1><p class="u-hero__sub">{t["lsub"]}</p></div></section>\n')
    card = (f'<a class="vl-card ld-card" href="{href}"><div class="vl-card__img"><img src="/assets/images/arawa-facade.jpg" alt="Arawa Villas, Balangan" loading="lazy"><span class="vl-card__zone">{c["zone"]}</span></div>'
            f'<div class="vl-card__b"><span class="ld-card__st">{c["status"]}</span><h3>{c["title"]}</h3><div class="vl-card__meta">' + ''.join(f'<span>{p}</span>' for p in c['pts']) + '</div>'
            f'<div class="ld-card__p"><span>{c["deal"]}</span><strong>{c["price"]}</strong></div><span class="u-link">{c["more"]}</span></div></a>')
    so = t['soon']
    soon = f'<div class="ld-soon">{ic("home",40)}<h3>{so[0]}</h3><p>{so[1]}</p><a class="u-btn u-btn--line" href="{so[3]}">{so[2]}</a></div>'
    s += sec(head(t['lih'], t['lil']) + f'<div class="ld-grid">{card}{soon}</div>')
    s += sec('<div class="u-feats u-feats--3">' + ''.join(f'<div class="u-feat">{ic(k)}<h3>{h}</h3><p>{p}</p></div>' for k, h, p in t['ls']) + '</div>', 'white')
    lc = t['lc']
    s += cta('arawa-salon.jpg', lc[0], lc[1], btn(lc[2][0], lc[2][1], 'rose') + btn(lc[3][0], lc[3][1], 'white'))
    open(R + f'pages/{l}/VillasAVendre.html', 'w').write(s)

r = json.load(open(R + 'routes.json'))
r['VillasAVendre'] = {'en': '/villas-for-sale/', 'fr': '/fr/villas-a-vendre/'}
r['ArawaVillas'] = {'en': '/villas-for-sale/arawa-balangan/', 'fr': '/fr/villas-a-vendre/arawa-balangan/'}
json.dump(r, open(R + 'routes.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
