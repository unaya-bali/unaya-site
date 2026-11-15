import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/fb21bd82-28de-566e-9e55-058e68a3af45/scratchpad/gen')
from ui import ic, sec, head, cta, btn, faq
from urllib.parse import quote
R = '/home/claude/unaya-site/src/'
WA = '6285190211324'
GMAP = 'https://maps.app.goo.gl/otksPEBt1Gy6dxUA6'  # -8.8057373, 115.1356918

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
    pb1='Demander la brochure ou une visite', pb2='Écrire sur WhatsApp', pnote='Prix en dollars américains, bail d’environ 28 ans (jusqu’en mars 2055), prolongeable 30 ans au prix du marché.',
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
    cards=[dict(img='arawa-facade.jpg', title='Arawa Villas · Villa B', pts=['2 chambres', '≈ 106 m²', 'Parcelle 91,80 m²'], price='dès 170 000 USD'), dict(img='arawa-piscine.jpg', title='Arawa Villas · Villa D', pts=['2 chambres', '≈ 106 m²', 'Parcelle 105,41 m²'], price='dès 195 000 USD')], cz='Balangan · Uluwatu', cst='Disponible', cdeal='Livraison fin déc. 2026', cmore='Voir la villa',
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
    pb1='Ask for the brochure or a viewing', pb2='Chat on WhatsApp', pnote='Prices in US dollars, lease of about 28 years (until March 2055), extendable by 30 years at market price.',
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
    cards=[dict(img='arawa-facade.jpg', title='Arawa Villas · Villa B', pts=['2 bedrooms', '≈ 106 m²', '91.80 m² plot'], price='from USD 170,000'), dict(img='arawa-piscine.jpg', title='Arawa Villas · Villa D', pts=['2 bedrooms', '≈ 106 m²', '105.41 m² plot'], price='from USD 195,000')], cz='Balangan · Uluwatu', cst='Available', cdeal='Handover end Dec. 2026', cmore='View the villa',
    soon=('Coming soon', 'More villas are on the way. Tell us what you are looking for (area, budget, bedrooms) and we will let you know first.', 'Contact us', '/contact/'),
    ls=[('eye', 'Chosen', 'Location, build quality and progress checked on site.'), ('doc', 'Explained', 'Lease, price, what is included: all said clearly.'), ('key', 'Rented', 'After you buy, Unaya can manage the rental of your villa.')],
    lc=('Looking for something else?', 'A plot of land, a villa to build or a property to rent out: let’s talk.', ('See available land', '/land/'), ('Contact us', '/contact/')))}

L = "display:flex;flex-direction:column;gap:8px;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#5A3552;flex:1 1 240px;"
I = "font-family:'Jost',sans-serif;font-size:16px;padding:14px;border:1px solid #D9CCC2;background:#FFFFFF;color:#2E2429;"
import html as _h
def jattr(o): return _h.escape(json.dumps(o, ensure_ascii=False), quote=True)
PRICE = {'B': 170000, 'D': 195000}
PLOT = {'B': 91.80, 'D': 105.41}
def money(n, fr): return (f'{n:,}'.replace(',', ' ') + ' $') if fr else f'${n:,}'
def m2(v, fr): return (f'{v:.2f}'.replace('.', ',') if fr else f'{v:.2f}') + ' m²'
def sim_html(l, v):
    fr = l == 'fr'
    tx = (dict(h='Ce que la villa peut rapporter', lead='Bougez les curseurs : prix par nuit et taux d’occupation. Les chiffres et les graphiques se recalculent.',
               sc='Scénarios', pre=[(60, 'Prudent · 60 %'), (74, 'Promoteur, bas · 74 %'), (84, 'Promoteur, central · 84 %')],
               rate='Prix par nuit', occ='Taux d’occupation', nights='nuits louées par an',
               k=['Revenus par an', 'Revenu net par an', 'Rendement net', 'Prix couvert en'],
               d='Où vont les revenus', a='Revenu net cumulé sur les 28 ans du bail',
               note='Simulation indicative, sans garantie de revenus. Les scénarios « promoteur » reprennent les hypothèses d’Arawa : 175 $ la nuit et 50 % de charges (plateformes 15 %, gestion 15 %, taxe 10 %, frais d’exploitation 10 %). Le scénario prudent (60 %) est ajouté par Unaya. Ne tient compte ni de l’impôt sur le revenu, ni des gros travaux, ni de la prolongation du bail.')
          if fr else
          dict(h='What the villa could earn', lead='Move the sliders: nightly rate and occupancy. Figures and charts update as you go.',
               sc='Scenarios', pre=[(60, 'Cautious · 60%'), (74, 'Developer, low · 74%'), (84, 'Developer, mid · 84%')],
               rate='Nightly rate', occ='Occupancy', nights='nights booked per year',
               k=['Revenue per year', 'Net income per year', 'Net yield', 'Price covered in'],
               d='Where the revenue goes', a='Cumulative net income over the 28-year lease',
               note='Indicative simulation, no guaranteed income. The “developer” scenarios use Arawa’s assumptions: $175 a night and 50% costs (platforms 15%, management 15%, tax 10%, running costs 10%). The cautious scenario (60%) is added by Unaya. Excludes income tax, major works and the lease extension.'))
    pre = ''.join(f'<button type="button" class="cx-chip" data-preset="{o}" aria-pressed="false">{lab}</button>' for o, lab in tx['pre'])
    kp = ''.join(f'<div class="cx-kpi{" cx-kpi--net" if i == 1 else ""}"><span>{lab}</span><strong data-k="{key}">–</strong></div>' for i, (lab, key) in enumerate(zip(tx['k'], ['rev', 'net', 'yld', 'pay'])))
    return (head(tx['h'], tx['lead']) +
            f'<div class="cx-sim"><div class="cx-ctrl"><div class="cx-presets" role="group" aria-label="{tx["sc"]}"><span>{tx["sc"]}</span>{pre}</div>'
            f'<label class="cx-sl"><span>{tx["rate"]} <output data-out="rate"></output></span><input type="range" name="rate" min="100" max="300" step="5" value="175"></label>'
            f'<label class="cx-sl"><span>{tx["occ"]} <output data-out="occ"></output> <em>· <output data-out="nights"></output> {tx["nights"]}</em></span><input type="range" name="occ" min="40" max="95" step="1" value="74"></label></div>'
            f'<div class="cx-kpis">{kp}</div>'
            f'<div class="cx-grid"><figure class="cx-card"><figcaption>{tx["d"]}</figcaption><div class="cx-donut"></div><ul class="cx-dleg"></ul></figure>'
            f'<figure class="cx-card cx-card--w"><figcaption>{tx["a"]}</figcaption><div class="cx-area"></div></figure></div>'
            f'<p class="cx-note">{tx["note"]}</p></div>')
def cmp_html(l, v):
    fr = l == 'fr'
    o = 'D' if v == 'B' else 'B'
    def rows(f, unit_fmt):
        return [dict(l=f'Villa {x}', v=f(x), t=unit_fmt(f(x)), hl=(x == v)) for x in ('B', 'D')]
    ppm = lambda x: round(PRICE[x] / PLOT[x])
    blocks = [('Prix' if fr else 'Price', rows(lambda x: PRICE[x], lambda n: money(n, fr))),
              ('Parcelle' if fr else 'Plot', rows(lambda x: PLOT[x], lambda n: m2(n, fr))),
              ('Prix au m² de parcelle' if fr else 'Price per m² of plot', rows(ppm, lambda n: money(n, fr)))]
    h = 'Villa B ou villa D ?' if fr else 'Villa B or villa D?'
    lead = (f'Même villa, même finition. La villa {v} est en foncé. Au m² de parcelle, les deux prix sont presque identiques : la villa D coûte plus cher parce que son terrain est plus grand.'
            if fr else f'Same villa, same finish. Villa {v} is shown in dark. Per m² of plot the two prices are almost identical: villa D costs more because its plot is larger.')
    html_ = ''.join(f'<figure class="cx-card"><figcaption>{t}</figcaption><div class="cx-bars cx-bars--cmp" data-rows="{jattr(r)}"></div></figure>' for t, r in blocks)
    return head(h, lead) + f'<div class="cx-cmp">{html_}</div>'
def surf_html(l):
    fr = l == 'fr'
    data = [('Étage' if fr else 'Upstairs', 54.39), ('Rez-de-chaussée' if fr else 'Ground floor', 51.35), ('Deck de la piscine' if fr else 'Pool deck', 19.74), ('Jardin' if fr else 'Garden', 15.29), ('Piscine' if fr else 'Pool', 11.50)]
    rows = [dict(l=a, v=b, t=m2(b, fr), hl=i < 2, tip=f'<b>{a}</b><br>{m2(b, fr)} · {round(b / 152.27 * 100)} %' + (' du total' if fr else ' of total')) for i, (a, b) in enumerate(data)]
    cap = ('Surfaces du plan type · 152,27 m² au total, dont ≈ 106 m² habitables' if fr else 'Typical plan areas · 152.27 m² in total, of which ≈ 106 m² indoor')
    return f'<figure class="cx-card cx-card--surf"><figcaption>{cap}</figcaption><div class="cx-bars" data-rows="{jattr(rows)}"></div></figure>'
def dist_html(l, loc):
    import re as _re
    fr = l == 'fr'
    rows = []
    for a, b in loc:
        n = [int(x) for x in _re.findall(r'\d+', b)]
        rows.append(dict(l=a, v=sum(n) / len(n), t=b, tip=f'<b>{a}</b><br>{b}' + (' en voiture' if fr else ' by car')))
    return f'<figure class="cx-card cx-card--dist"><figcaption>{"Temps de trajet en voiture" if fr else "Driving time"}</figcaption><div class="cx-bars cx-bars--dist" data-rows="{jattr(rows)}"></div></figure>'
def prog_html(l):
    fr = l == 'fr'
    steps = ([('Juin 2026', 'Premières photos du chantier'), ('Oct.–nov. 2026', 'Façades, menuiseries, piscines'), ('Fin déc. 2026', 'Remise des clés, villa meublée')] if fr else
             [('June 2026', 'First site photos'), ('Oct–Nov 2026', 'Façades, joinery, pools'), ('End Dec 2026', 'Handover, villa furnished')])
    tl = ''.join(f'<li class="{"is-done" if i < 2 else "is-next"}"><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(steps))
    return (f'<div class="cx-prog"><div class="cx-ring" data-pct="87.5" data-text="85–90 %" data-label="{"Avancement des travaux : 85 à 90 %" if fr else "Construction progress: 85 to 90%"}"></div>'
            f'<div><p class="cx-prog__k">{"Avancement des travaux" if fr else "Construction progress"}</p><ol class="cx-tl">{tl}</ol></div></div>')

SOLD = 4  # villas déjà vendues sur 6 (A, C, E, F) — à mettre à jour
def sold_html(l):
    fr = l == 'fr'
    dots = ''.join(f'<i class="{"is-sold" if x in "ACEF" else "is-free"}" title="Villa {x} : {("vendue" if fr else "sold") if x in "ACEF" else ("disponible" if fr else "available")}">{x}</i>' for x in 'ABCDEF')
    return f'<div class="ar-sold"><span class="ar-sold__dots">{dots}</span><span>{f"{SOLD} villas sur 6 déjà vendues" if fr else f"{SOLD} of 6 villas already sold"}</span></div>'
def pdf_url(l, vv):
    return f'/assets/docs/arawa-{("villa-" + vv.lower()) if vv else "residence"}-{l}.pdf'
def share_html(l, page_url, title):
    fr = l == 'fr'
    u = quote('https://unayabali.com' + page_url, safe='')
    tt = quote(title)
    return (f'<div class="ar-share" data-share-url="https://unayabali.com{page_url}" data-share-title="{title}"><span>{"Partager" if fr else "Share"}</span>'
            f'<a href="https://wa.me/?text={tt}%20{u}" target="_blank" rel="noopener" aria-label="WhatsApp">WhatsApp</a>'
            f'<a href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>'
            f'<a href="mailto:?subject={tt}&amp;body={u}" aria-label="E-mail">E-mail</a>'
            f'<button type="button" class="ar-copy" data-ok="{"Lien copié" if fr else "Link copied"}">{"Copier le lien" if fr else "Copy link"}</button></div>')
def lease_html(l):
    fr = l == 'fr'
    rows = ([('Remise des clés', 'fin décembre 2026'), ('Fin du bail du terrain', '21 mars 2055, soit environ 28 ans après la remise des clés'),
             ('Prolongation', 'option de 30 ans de plus, au prix du marché à ce moment-là (prévue dans le bail du terrain)'), ('Garantie', '1 an après la remise des clés')] if fr else
            [('Handover', 'end of December 2026'), ('Land lease ends', '21 March 2055, about 28 years after handover'),
             ('Extension', '30-year option, at the market price at that time (set out in the land lease)'), ('Warranty', '1 year after handover')])
    return (f'<div class="ar-lease"><h3>{"Bail et garanties" if fr else "Lease and warranty"}</h3><dl>' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows) + '</dl>'
            f'<p>{"Dates tirées du bail du terrain. Faites vérifier le contrat d’achat par votre notaire ou votre avocat." if fr else "Dates taken from the land lease. Have the purchase contract checked by your notary or lawyer."}</p></div>')
def visit_html(l, vv):
    fr = l == 'fr'
    L2 = L; I2 = I
    villa = f'Villa {vv}' if vv else ('Villa B ou D' if fr else 'Villa B or D')
    h = 'Planifier une visite' if fr else 'Book a viewing'
    lead = ('Sur place à Balangan, ou en vidéo si vous êtes loin. Choisissez un jour, nous vous confirmons l’heure sur WhatsApp.' if fr else
            'On site in Balangan, or by video if you are far away. Pick a day and we confirm the time on WhatsApp.')
    lab = (('Nom', 'WhatsApp', 'E-mail', 'Type de visite', 'Date souhaitée', 'Moment de la journée', 'Message (facultatif)') if fr else
           ('Name', 'WhatsApp', 'Email', 'Viewing type', 'Preferred date', 'Time of day', 'Message (optional)'))
    vt = ['Sur place à Balangan', 'En vidéo (WhatsApp ou Zoom)'] if fr else ['On site in Balangan', 'By video (WhatsApp or Zoom)']
    mo = ['Matin', 'Après-midi', 'Peu importe'] if fr else ['Morning', 'Afternoon', 'Any time']
    form = (f'<form class="ar-visit" style="width:100%;background:#FFFFFF;border:1px solid #E6DCD4;padding:32px;display:flex;flex-direction:column;gap:18px;">'
            f'<div style="display:flex;flex-wrap:wrap;gap:18px;"><label style="{L2}">{lab[0]}<input type="text" style="{I2}"></label><label style="{L2}">{lab[1]}<input type="tel" required placeholder="+61 412 345 678" style="{I2}"></label><label style="{L2}">{lab[2]}<input type="email" style="{I2}"></label></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:18px;"><label style="{L2}">{lab[3]}<select style="{I2}">' + ''.join(f'<option>{o}</option>' for o in vt) + f'</select></label>'
            f'<label style="{L2}">{lab[4]}<input type="date" data-mindate style="{I2}"></label><label style="{L2}">{lab[5]}<select style="{I2}">' + ''.join(f'<option>{o}</option>' for o in mo) + '</select></label></div>'
            f'<label style="{L2}">{lab[6]}<textarea rows="3" style="{I2}">{("Visite de la " if fr else "Viewing of ") + villa + " — Arawa Villas, Balangan."}</textarea></label>'
            f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><input type="checkbox" style="margin-top: 5px;">{"J’accepte que mes données soient utilisées pour organiser la visite (politique de confidentialité)." if fr else "I agree that my data may be used to arrange the viewing (privacy policy)."}</label>'
            f'<button type="button" style="display:inline-block;padding:16px 30px;background:#3F2A3A;color:#F7F2EE;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;border:none;font-family:\'Jost\',sans-serif;cursor:pointer;align-self:flex-start;">{"Demander la visite" if fr else "Request the viewing"}</button></form>')
    return f'<div class="ld-form">{head(h, lead)}{form}</div>'

def detail(l, t, page):
    fr = l == 'fr'
    bc = ' <span>›</span> '.join(f'<a href="{u}">{n}</a>' if u else n for n, u in t['bc'])
    wa = f'https://wa.me/{WA}?text={quote(t["wa_txt"])}'
    s = f'<!-- title: {t["t"]} -->\n'
    s += (f'<section class="ld-hero"><img src="/assets/images/{t.get("hero", "arawa-facade.jpg")}" alt="" fetchpriority="high"><div class="ld-hero__in">'
          f'<nav class="art-bc" aria-label="breadcrumb">{bc}</nav><p class="ld-kick">{t["kick"]}</p><h1>{t["h1"]}</h1><p>{t["sub"]}</p>'
          f'<div class="ld-badges"><span class="ld-badge ld-badge--ok">{t["badges"][0]}</span><span class="ld-badge">{t["badges"][1]}</span><span class="ld-badge">{("4 villas sur 6 vendues" if fr else "4 of 6 villas sold")}</span></div></div></section>\n')
    s += '<section class="ld-facts"><div class="ld-facts__in">' + ''.join(f'<div class="ld-fact">{ic(k,30)}<span>{a}</span><strong>{b}</strong><em>{c}</em></div>' for k, a, b, c in t['facts']) + '</div></section>\n'
    desc = ''.join(f'<p>{p}</p>' for p in t['dp']) + '<ul class="u-checks">' + ''.join(f'<li>{w}</li>' for w in t['why']) + '</ul>'
    rows = ''.join(f'<div class="ar-pr"><span>{(f"<a href={chr(34)}{VHREF[n[-1]][l]}{chr(34)}>{n} →</a>" if page == "ArawaVillas" else n)}</span><strong><small>{t["pfrom"]}</small> USD {p}</strong><em>{t["plot"]} {pl}</em></div>' for n, p, pl in t['villas'])
    vv = page[-1] if page != 'ArawaVillas' else None
    purl = VHREF[vv][l] if vv else RES[l]
    dl = (f'<div class="ar-dl"><a href="{pdf_url(l, vv)}" download>{"Télécharger la fiche (PDF)" if fr else "Download the brochure (PDF)"}</a>'
          f'<a href="/assets/docs/arawa-plans.pdf" download>{"Télécharger les plans (PDF)" if fr else "Download the floor plans (PDF)"}</a></div>')
    price = (f'<aside class="ld-price"><span class="ld-price__k">{t["pk"]}</span>{rows}{sold_html(l)}'
             f'<a class="u-btn u-btn--rose" href="#visite">{"Planifier une visite" if fr else "Book a viewing"}</a><a class="ld-wa" href="{wa}" target="_blank" rel="noopener">{t["pb2"]}</a>'
             f'{dl}<p>{t["pnote"]}</p>' + (f'<p class="ar-other">{t["other"]}</p>' if t.get('other') else '') + share_html(l, purl, t['h1'] + ' — Balangan, Bali') + '</aside>')
    mz = t.get('mosaic', ['arawa-piscine.jpg', 'arawa-salon.jpg', 'arawa-sejour.jpg'])
    alt = {f: (a if fr else b) for f, a, b in GAL}
    s += ('<section class="u-sec ar-mz-sec"><div class="u-wrap"><div class="ar-mz">'
          f'<a class="ar-mz__big" href="#galerie" data-open-gallery><img src="/assets/images/{mz[0]}" alt="{alt.get(mz[0], "")}"></a>'
          f'<a class="ar-mz__s" href="#galerie" data-open-gallery><img src="/assets/images/{mz[1]}" alt="{alt.get(mz[1], "")}" loading="lazy"></a>'
          f'<a class="ar-mz__s ar-mz__more" href="#galerie" data-open-gallery><img src="/assets/images/{mz[2]}" alt="{alt.get(mz[2], "")}" loading="lazy"><span>{"Voir les" if fr else "View all"} {len(GAL)} {"photos" if fr else "photos"}</span></a>'
          f'<a class="ar-mz__plan" href="#plans">{"Voir les plans" if fr else "View floor plans"}</a>'
          '</div></div></section>\n')
    s += sec(f'<div class="ld-main"><div class="ld-desc">{head(t["dh"])}{desc}{lease_html(l)}</div>{price}</div>')
    if vv:
        s += f'<div hidden data-arawa="{jattr(dict(price=PRICE[vv], lease=28))}"></div>\n'
        s += sec(sim_html(l, vv), 'white', id='rendement')
        s += sec(cmp_html(l, vv))
    PHIMG = ['arawa-residence.jpg', 'arawa-salon.jpg', 'arawa-piscine-2.jpg', 'arawa-chantier-1.jpg']
    phc = ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__img"><img src="/assets/images/{PHIMG[i]}" alt="{h}" loading="lazy"><span class="ar-lv2__n">0{i + 1}</span></div>'
                  f'<div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(k, 26)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for i, (k, h, p) in enumerate(t['phil']))
    s += sec(head(t['ph'], t['pl'], True) + f'<div class="ar-lv2 ar-lv2--4">{phc}</div>', 'white')
    gal = ''.join(f'<figure><img src="/assets/images/{f}" alt="{a if fr else b}" loading="lazy"></figure>' for f, a, b in GAL)
    s += sec(head(t['gh'], t['gl']) + f'<div class="ar-gal" data-gallery>{gal}</div>', id='galerie')
    LVIMG = [('arawa-cuisine.jpg', 'home', '01'), ('arawa-chambre-2.jpg', 'bed', '02'), ('arawa-sdb-1.jpg', 'leaf', '03')]
    lv = ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__img"><img src="/assets/images/{LVIMG[i][0]}" alt="{h}" loading="lazy"><span class="ar-lv2__n">{LVIMG[i][2]}</span></div>'
                 f'<div class="ar-lv2__b"><span class="ar-lv2__ic">{ic(LVIMG[i][1], 26)}</span><h3>{h}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in li) + '</ul></div></article>' for i, (h, li) in enumerate(t['lv']))
    s += sec(head(t['vh'], t['vl'], True) + f'<div class="ar-lv2">{lv}</div>' + (surf_html(l) if vv else ''), 'white')
    ph = ''.join(f'<figure><img src="/assets/images/{f}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c in zip(t.get('chf', ['arawa-chantier-1.jpg', 'arawa-chantier-2.jpg', 'arawa-chantier-3.jpg']), t['chc']))
    s += sec(head(t['ch'], t['cl']) + (prog_html(l) if vv else '') + f'<div class="ar-site">{ph}</div>')
    pl = ''.join(f'<figure><a href="/assets/images/{f}" target="_blank" rel="noopener"><img src="/assets/images/{f}" alt="{c}" loading="lazy"></a><figcaption>{c}</figcaption></figure>' for f, c in zip(['arawa-plan-masse.jpg', 'arawa-plan-rdc.jpg', 'arawa-plan-etage.jpg'], t['plc']))
    s += sec(head(t['plh'], t['pll']) + f'<div class="ar-plans">{pl}</div>', 'white', id='plans')
    tbl = '<dl class="ld-tbl">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in t['loc']) + '</dl>'
    if vv: tbl = dist_html(l, t['loc'])
    mapt = 'Emplacement des Arawa Villas, Balangan' if fr else 'Arawa Villas location, Balangan'
    s += sec(head(t['lh'], t['ll']) + f'<div class="ld-zone ar-zone"><div class="ld-map"><iframe title="{mapt}" src="https://maps.google.com/maps?q=-8.8057373,115.1356918&amp;t=k&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="u-btn u-btn--line" href="{GMAP}" target="_blank" rel="noopener">{t["maps"]} ↗</a></div>{tbl}</div>')
    st = '<div class="u-path u-path--4">' + ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k,34)}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k, h, p in t['steps']) + '</div>'
    s += sec(head(t['ah'], t['al']) + st, 'white')
    s += sec(head(t['qh']) + faq(t['qs']))
    form = (f'<form style="width:100%;background:#FFFFFF;border:1px solid #E6DCD4;padding:40px;display:flex;flex-direction:column;gap:20px;">'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{t["fl"][0]}<input type="text" style="{I}"></label><label style="{L}">{t["fl"][1]}<input type="email" style="{I}"></label></div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:20px;"><label style="{L}">{t["fl"][2]}<input type="tel" style="{I}"></label><label style="{L}">{t["fl"][3]}<select style="{I}">' + ''.join(f'<option>{o}</option>' for o in t['fo']) + '</select></label></div>'
            f'<label style="{L}">{t["fl"][4]}<textarea rows="5" style="{I}">{t["fmsg"]}</textarea></label>'
            f'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><input type="checkbox" style="margin-top: 5px;">{t["fc"]}</label>'
            f'<button type="button" style="display:inline-block;padding:16px 30px;background:#3F2A3A;color:#F7F2EE;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;border:none;font-family:\'Jost\',sans-serif;cursor:pointer;align-self:flex-start;">{t["fs"]}</button></form>')
    s += sec(visit_html(l, vv), id='visite')
    s += sec(f'<div class="ld-form">{head(t["fh"],t["fp"])}{form}<p class="ld-legal">{t["legal"]}</p></div>', 'white', id='dossier')
    if vv: s += '<script src="/assets/js/arawa-charts.js" defer></script>\n'
    open(R + f'pages/{l}/{page}.html', 'w').write(s)

VHREF = {'B': {'fr': '/fr/villas-a-vendre/arawa-villa-b/', 'en': '/villas-for-sale/arawa-villa-b/'}, 'D': {'fr': '/fr/villas-a-vendre/arawa-villa-d/', 'en': '/villas-for-sale/arawa-villa-d/'}}
RES = {'fr': '/fr/villas-a-vendre/arawa-balangan/', 'en': '/villas-for-sale/arawa-balangan/'}
V = {'B': {'fr': dict(
        h1='Arawa Villas · Villa B', sub='Villa de 2 chambres avec piscine privée sur une parcelle de 91,80 m², à Balangan. Livrée meublée fin décembre 2026, à partir de 170 000 USD.',
        badges=['Disponible', 'Livraison fin décembre 2026'],
        facts=[('bed', 'Chambres', '2 en suite', '+ WC invités'), ('home', 'Surface', '≈ 106 m²', 'sur 2 niveaux'), ('map', 'Parcelle', '91,80 m²', '13,50 × 6,80 m'), ('doc', 'Bail', '≈ 28 ans', '+ option 30 ans')],
        dh='La villa B',
        dp=['La villa B se trouve au milieu de la rangée est de la résidence, entre les villas A et C. Sa parcelle fait 91,80 m² (13,50 × 6,80 m). C’est la villa la plus accessible du projet.',
            'Elle suit le plan des autres villas Arawa : au rez-de-chaussée, un grand séjour avec cuisine ouvert sur la piscine privée, un WC invités, une petite cabana et une douche extérieure ; à l’étage, deux chambres avec chacune sa salle de bain et son dressing, et une terrasse. Elle est livrée entièrement meublée et équipée.',
            'Le chantier est bien avancé : façades, menuiseries en bois, piscine et escalier sont en place, les finitions intérieures sont en cours (photos du 9 novembre 2026).'],
        villas=[('Villa B', '170 000', '91,80 m²')], pnote='Prix en dollars américains, bail d’environ 28 ans (jusqu’en mars 2055), prolongeable 30 ans au prix du marché.',
        other=f'Voir aussi la <a href="/fr/villas-a-vendre/arawa-villa-d/">villa D</a> (105,41 m², dès 195 000 USD) ou <a href="/fr/villas-a-vendre/arawa-balangan/">la résidence Arawa</a>.',
        ch='Où en est la villa B', cl='Photos prises sur place en octobre et novembre 2026.', chc=['Villa B, 9 novembre 2026', 'Villa B, 2 novembre 2026', 'Villa B, 26 octobre 2026'],
        chf=['arawa-chantier-1.jpg', 'arawa-b-chantier-3.jpg', 'arawa-chantier-2.jpg'],
        plc=['Plan de masse : la villa B est au centre de la rangée est', 'Rez-de-chaussée (plan type)', 'Étage (plan type)'],
        fo=['Villa B', 'Villa D', 'Les deux villas'], fmsg='Bonjour, je suis intéressé(e) par la villa B des Arawa Villas à Balangan. Pouvez-vous m’envoyer la brochure ?',
        wa_txt='Bonjour Unaya, je suis intéressé(e) par la villa B des Arawa Villas à Balangan.',
        bc=[('Accueil', '/fr/'), ('Villas à vendre', '/fr/villas-a-vendre/'), ('Arawa Villas', '/fr/villas-a-vendre/arawa-balangan/'), ('Villa B', None)],
        t='Arawa Villas · Villa B, Balangan — 2 chambres, piscine, dès 170 000 USD | Unaya Bali'),
      'en': dict(
        h1='Arawa Villas · Villa B', sub='Two-bedroom villa with a private pool on a 91.80 m² plot in Balangan. Handed over furnished at the end of December 2026, from USD 170,000.',
        badges=['Available', 'Handover end of December 2026'],
        facts=[('bed', 'Bedrooms', '2 en suite', '+ guest WC'), ('home', 'Size', '≈ 106 m²', 'over 2 floors'), ('map', 'Plot', '91.80 m²', '13.50 × 6.80 m'), ('doc', 'Lease', '≈ 28 years', '+ 30-year option')],
        dh='Villa B',
        dp=['Villa B sits in the middle of the east row of the residence, between villas A and C. Its plot is 91.80 m² (13.50 × 6.80 m). It is the most affordable villa in the project.',
            'It follows the same layout as the other Arawa villas: downstairs, a large living space with an open kitchen facing the private pool, a guest WC, a small cabana and an outdoor shower; upstairs, two bedrooms each with its own bathroom and walk-in wardrobe, plus a terrace. It comes fully furnished and equipped.',
            'Construction is well advanced: façades, wooden joinery, pool and staircase are in place, interior finishing is under way (photos from 9 November 2026).'],
        villas=[('Villa B', '170,000', '91.80 m²')], pnote='Price in US dollars, lease of about 28 years (until March 2055), extendable by 30 years at market price.',
        other=f'See also <a href="/villas-for-sale/arawa-villa-d/">villa D</a> (105.41 m², from USD 195,000) or <a href="/villas-for-sale/arawa-balangan/">the Arawa residence</a>.',
        ch='Villa B progress', cl='Photos taken on site in October and November 2026.', chc=['Villa B, 9 November 2026', 'Villa B, 2 November 2026', 'Villa B, 26 October 2026'],
        chf=['arawa-chantier-1.jpg', 'arawa-b-chantier-3.jpg', 'arawa-chantier-2.jpg'],
        plc=['Site plan: villa B is in the middle of the east row', 'Ground floor (typical layout)', 'Upstairs (typical layout)'],
        fo=['Villa B', 'Villa D', 'Both villas'], fmsg='Hello, I am interested in villa B at Arawa Villas in Balangan. Could you send me the brochure?',
        wa_txt="Hello Unaya, I'm interested in villa B at Arawa Villas in Balangan.",
        bc=[('Home', '/'), ('Villas for sale', '/villas-for-sale/'), ('Arawa Villas', '/villas-for-sale/arawa-balangan/'), ('Villa B', None)],
        t='Arawa Villas · Villa B, Balangan — 2-Bedroom Pool Villa from USD 170,000 | Unaya Bali')},
  'D': {'fr': dict(
        hero='arawa-piscine.jpg', mosaic=['arawa-piscine-2.jpg', 'arawa-sejour.jpg', 'arawa-chambre-1.jpg'],
        h1='Arawa Villas · Villa D', sub='Villa de 2 chambres avec piscine privée sur la plus grande parcelle restante, 105,41 m², à Balangan. Livrée meublée fin décembre 2026, à partir de 195 000 USD.',
        badges=['Disponible', 'Livraison fin décembre 2026'],
        facts=[('bed', 'Chambres', '2 en suite', '+ WC invités'), ('home', 'Surface', '≈ 106 m²', 'sur 2 niveaux'), ('map', 'Parcelle', '105,41 m²', 'la plus grande restante'), ('doc', 'Bail', '≈ 28 ans', '+ option 30 ans')],
        dh='La villa D',
        dp=['La villa D est en tête de la rangée ouest, du côté de la route d’accès. Sa parcelle de 105,41 m² est la plus grande des deux villas encore à vendre : la villa est la même, mais le terrain autour est plus large.',
            'Comme les villas E et F, elle a accès à un espace de rangement, ce que n’ont pas les villas de l’autre rangée.',
            'À l’intérieur, le plan Arawa : au rez-de-chaussée, un grand séjour avec cuisine ouvert sur la piscine privée, un WC invités, une petite cabana et une douche extérieure ; à l’étage, deux chambres avec chacune sa salle de bain et son dressing, et une terrasse. Livrée entièrement meublée et équipée.',
            'Le gros œuvre et les façades sont terminés, les finitions sont en cours (photos du 9 novembre 2026).'],
        villas=[('Villa D', '195 000', '105,41 m²')], pnote='Prix en dollars américains, bail d’environ 28 ans (jusqu’en mars 2055), prolongeable 30 ans au prix du marché.',
        other=f'Voir aussi la <a href="/fr/villas-a-vendre/arawa-villa-b/">villa B</a> (91,80 m², dès 170 000 USD) ou <a href="/fr/villas-a-vendre/arawa-balangan/">la résidence Arawa</a>.',
        ch='Où en est la villa D', cl='Photos prises sur place le 9 novembre 2026.', chc=['Villa D, façade', 'Villa D, terrasse et piscine', 'Villa D, côté jardin'],
        chf=['arawa-chantier-3.jpg', 'arawa-d-chantier-3.jpg', 'arawa-d-chantier-2.jpg'],
        plc=['Plan de masse : la villa D est en tête de la rangée ouest', 'Rez-de-chaussée (plan type)', 'Étage (plan type)'],
        fo=['Villa D', 'Villa B', 'Les deux villas'], fmsg='Bonjour, je suis intéressé(e) par la villa D des Arawa Villas à Balangan. Pouvez-vous m’envoyer la brochure ?',
        wa_txt='Bonjour Unaya, je suis intéressé(e) par la villa D des Arawa Villas à Balangan.',
        bc=[('Accueil', '/fr/'), ('Villas à vendre', '/fr/villas-a-vendre/'), ('Arawa Villas', '/fr/villas-a-vendre/arawa-balangan/'), ('Villa D', None)],
        t='Arawa Villas · Villa D, Balangan — 2 chambres, piscine, dès 195 000 USD | Unaya Bali'),
      'en': dict(
        hero='arawa-piscine.jpg', mosaic=['arawa-piscine-2.jpg', 'arawa-sejour.jpg', 'arawa-chambre-1.jpg'],
        h1='Arawa Villas · Villa D', sub='Two-bedroom villa with a private pool on the largest remaining plot, 105.41 m², in Balangan. Handed over furnished at the end of December 2026, from USD 195,000.',
        badges=['Available', 'Handover end of December 2026'],
        facts=[('bed', 'Bedrooms', '2 en suite', '+ guest WC'), ('home', 'Size', '≈ 106 m²', 'over 2 floors'), ('map', 'Plot', '105.41 m²', 'largest remaining'), ('doc', 'Lease', '≈ 28 years', '+ 30-year option')],
        dh='Villa D',
        dp=['Villa D sits at the head of the west row, on the access-road side. Its 105.41 m² plot is the larger of the two villas still for sale: same villa, more land around it.',
            'Like villas E and F, it has access to a storage space, which the villas in the other row do not.',
            'Inside, the Arawa layout: downstairs, a large living space with an open kitchen facing the private pool, a guest WC, a small cabana and an outdoor shower; upstairs, two bedrooms each with its own bathroom and walk-in wardrobe, plus a terrace. Fully furnished and equipped.',
            'Structure and façades are finished, finishing works are under way (photos from 9 November 2026).'],
        villas=[('Villa D', '195,000', '105.41 m²')], pnote='Price in US dollars, lease of about 28 years (until March 2055), extendable by 30 years at market price.',
        other=f'See also <a href="/villas-for-sale/arawa-villa-b/">villa B</a> (91.80 m², from USD 170,000) or <a href="/villas-for-sale/arawa-balangan/">the Arawa residence</a>.',
        ch='Villa D progress', cl='Photos taken on site on 9 November 2026.', chc=['Villa D, front', 'Villa D, terrace and pool', 'Villa D, garden side'],
        chf=['arawa-chantier-3.jpg', 'arawa-d-chantier-3.jpg', 'arawa-d-chantier-2.jpg'],
        plc=['Site plan: villa D is at the head of the west row', 'Ground floor (typical layout)', 'Upstairs (typical layout)'],
        fo=['Villa D', 'Villa B', 'Both villas'], fmsg='Hello, I am interested in villa D at Arawa Villas in Balangan. Could you send me the brochure?',
        wa_txt="Hello Unaya, I'm interested in villa D at Arawa Villas in Balangan.",
        bc=[('Home', '/'), ('Villas for sale', '/villas-for-sale/'), ('Arawa Villas', '/villas-for-sale/arawa-balangan/'), ('Villa D', None)],
        t='Arawa Villas · Villa D, Balangan — 2-Bedroom Pool Villa from USD 195,000 | Unaya Bali')}}

for l, t in T.items():
    fr = l == 'fr'
    detail(l, t, 'ArawaVillas')
    for k in V:
        detail(l, {**t, **V[k][l]}, 'ArawaVilla' + k)

    # ---- page liste ----
    href = '/fr/villas-a-vendre/arawa-balangan/' if fr else '/villas-for-sale/arawa-balangan/'
    s = f'<!-- title: {t["lt"]} -->\n'
    s += (f'<section class="u-hero"><img src="/assets/images/arawa-piscine-2.jpg" alt="" fetchpriority="high"><div class="u-hero__in"><p class="u-hero__k">{t["lkick"]}</p><h1>{t["lh1"]}</h1><p class="u-hero__sub">{t["lsub"]}</p></div></section>\n')
    card = ''.join(f'<a class="vl-card ld-card" href="{VHREF[c["title"][-1]][l]}"><div class="vl-card__img"><img src="/assets/images/{c["img"]}" alt="{c["title"]}, Balangan" loading="lazy"><span class="vl-card__zone">{t["cz"]}</span></div>'
            f'<div class="vl-card__b"><span class="ld-card__st">{t["cst"]}</span><h3>{c["title"]}</h3><div class="vl-card__meta">' + ''.join(f'<span>{p}</span>' for p in c['pts']) + '</div>'
            f'<div class="ld-card__p"><span>{t["cdeal"]}</span><strong>{c["price"]}</strong></div><span class="u-link">{t["cmore"]}</span></div></a>' for c in t['cards'])
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
r['ArawaVillaB'] = VHREF['B']
r['ArawaVillaD'] = VHREF['D']
json.dump(r, open(R + 'routes.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
