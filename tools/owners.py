# Page « Propriétaires » (vue d'ensemble, FR/EN), version visuelle : grande photo, chiffres clés,
# 4 engagements, simulateur de revenus (repris de la page d'accueil), seul ou avec Unaya, 4 étapes,
# espace propriétaire, zones, formules, appel final.
# Icônes reprises de Prop_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
import home  # noqa: E402  (simulateur identique à la page d'accueil)

X = {
 'fr': dict(
  title='Propriétaires — Unaya Management', kick='Propriétaires · Gestion de villas à Bali',
  h1='Votre villa mérite mieux qu’une simple gestion.', sub='Nous la louons, nous en prenons soin et nous vous rendons des comptes clairs. Vous profitez de vos revenus, sans les soucis.',
  b1=('Confier ma villa', '/fr/proprietaires/confier-ma-villa/'), b2=('Voir les tarifs', '/fr/proprietaires/tarifs/'),
  badges=['Aucun frais fixe', 'Rapport chaque mois', 'Réponse sous 24 h'],
  keys=[('263', 'voyageurs accueillis depuis juillet 2026'), ('22', 'nationalités'), ('9,8/10', 'note moyenne sur Booking.com'), ('18 %', 'gestion complète, aucun frais fixe')],
  why_h='Unaya signifie « l’unique ». Chaque villa aussi.', why_p='Nous ne gérons pas des dizaines de villas à la chaîne : nous suivons chacune de près, avec une équipe sur place et une comptabilité rigoureuse.',
  vs_h='Gérer seul, ou avec Unaya ?', vs_p='Louer une villa à Bali, c’est un vrai métier. Voici ce qui change pour vous.',
  vs=(('Seul', ['Répondre aux voyageurs à toute heure, en plusieurs langues', 'Fixer les prix au jugé, nuit après nuit', 'Trouver, former et encadrer le personnel', 'Déclarer et payer la taxe PBJT, tenir les comptes', 'Gérer la panne de pompe de piscine un soir de week-end']),
      ('Avec Unaya', ['Assistance aux voyageurs 24h/24', 'Tarifs ajustés en continu sur toutes les plateformes', 'Une équipe sur place, formée et suivie 7j/7', 'Taxes payées et rapport financier chaque mois', 'Un interlocuteur unique, qui répond sous 24 h'])),
  st_h='4 étapes, et votre villa est entre de bonnes mains', st_p='Sans engagement jusqu’à la signature du contrat de gestion.',
  portal=('Espace propriétaire', 'Votre villa, en temps réel', 'Depuis votre téléphone, suivez tout ce qui se passe chez vous :', ['Réservations et calendrier', 'Revenus, mois par mois', 'Dépenses, avec les justificatifs', 'Relevés mensuels à télécharger'], 'Ouvrir mon espace propriétaire ↗'),
  zn_h='Nos zones', zn_p='Trois secteurs que nous connaissons rue par rue.',
  zones=[('zone-uluwatu-jimbaran.jpg', 'Uluwatu / Jimbaran', 'Falaises, surf, plages de sable blanc'), ('zone-tanah-lot-canggu.jpg', 'Tanah Lot / Canggu West', 'Rizières, plages de sable noir, temples'), ('zone-seminyak-kerobokan.jpg', 'Seminyak / Kerobokan', 'Beach clubs, restaurants, villas familiales')],
  pl_h='Deux formules, sans frais fixe', pl_p='Une commission sur les revenus, calculée après plateformes et taxe d’hébergement.',
  plans=[('Gestion complète', 'à partir de', '18 %', 'Nous nous occupons de tout : location, voyageurs, équipes, entretien et comptabilité.', True),
         ('Marketing seul', '', '11 %', 'Nous remplissons votre calendrier, vous gérez la villa sur place.', False)],
  pl_more='Comparer les formules', pop='Le plus choisi',
  cta_h='Prêt à confier votre villa ?', cta_p='Estimation de revenus gratuite et sans engagement, sous 24 h.',
 ),
 'en': dict(
  title='Owners — Unaya Management', kick='Owners · Villa management in Bali',
  h1='Your villa deserves more than basic management.', sub='We rent it, we look after it and we give you clear accounts. You enjoy the income, without the hassle.',
  b1=('List my villa', '/owners/list-your-villa/'), b2=('See pricing', '/owners/pricing/'),
  badges=['No fixed fees', 'A report every month', 'Reply within 24 hours'],
  keys=[('263', 'guests welcomed since July 2026'), ('22', 'nationalities'), ('9.8/10', 'average score on Booking.com'), ('18%', 'full management, no fixed fees')],
  why_h='Unaya means “the unique one”. So is every villa.', why_p='We don’t manage dozens of villas on a conveyor belt: we follow each one closely, with a team on the ground and rigorous accounting.',
  vs_h='Manage it yourself, or with Unaya?', vs_p='Renting out a villa in Bali is a real job. Here is what changes for you.',
  vs=(('On your own', ['Answering guests at any hour, in several languages', 'Setting prices by guesswork, night after night', 'Finding, training and supervising staff', 'Filing and paying PBJT tax, keeping the books', 'Handling a broken pool pump on a weekend evening']),
      ('With Unaya', ['24/7 guest support', 'Prices adjusted continuously on every platform', 'A trained team on site, supervised 7 days a week', 'Taxes paid and a financial report every month', 'One contact who replies within 24 hours'])),
  st_h='4 steps and your villa is in good hands', st_p='No commitment until the management contract is signed.',
  portal=('Owner portal', 'Your villa, in real time', 'From your phone, follow everything happening at your villa:', ['Bookings and calendar', 'Income, month by month', 'Expenses, with receipts', 'Monthly statements to download'], 'Open my owner portal ↗'),
  zn_h='Our areas', zn_p='Three areas we know street by street.',
  zones=[('zone-uluwatu-jimbaran.jpg', 'Uluwatu / Jimbaran', 'Cliffs, surf, white-sand beaches'), ('zone-tanah-lot-canggu.jpg', 'Tanah Lot / Canggu West', 'Rice fields, black-sand beaches, temples'), ('zone-seminyak-kerobokan.jpg', 'Seminyak / Kerobokan', 'Beach clubs, restaurants, family villas')],
  pl_h='Two plans, no fixed fees', pl_p='A commission on income, calculated after platform fees and accommodation tax.',
  plans=[('Full Management', 'from', '18%', 'We take care of everything: rentals, guests, staff, maintenance and accounting.', True),
         ('Marketing Only', '', '11%', 'We fill your calendar, you run the villa on site.', False)],
  pl_more='Compare plans', pop='Most popular',
  cta_h='Ready to hand over the keys?', cta_p='Free, no-commitment income estimate, within 24 hours.',
 ),
}

def small(svg, n=26):
    return re.sub(r'width="\d+" height="\d+"', f'width="{n}" height="{n}"', svg, count=1)

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Prop_old_{lang}.html')).read()
    feats = re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', old, flags=re.S)
    steps = re.findall(r'<div class="u-path__s"><span class="u-path__dot">(<svg.*?</svg>)</span><div><h3>(.*?)</h3><p>(.*?)</p></div></div>', old, flags=re.S)
    portal_ic = re.search(r'<div class="u-band">(<svg.*?</svg>)', old, flags=re.S).group(1)
    s = f'<!-- title: {x["title"]} -->\n<div class="hm">\n'
    # 1. Grande photo
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/suma-piscine-2.jpg" alt="{"La piscine de SUMA Bali, Balangan Uluwatu" if fr else "SUMA Bali pool, Balangan Uluwatu"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{x["h1"]}</h1><p class="hm-hero__sub">{x["sub"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="{x["b2"][1]}">{x["b2"][0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    # 2. Chiffres clés
    s += '<section class="iv-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) + '</div></section>\n'
    # 3. Quatre engagements
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["why_h"]}</h2><p>{x["why_p"]}</p></div><div class="ar-lv2 hm-gar hm-gar--4">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{small(svg)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for svg, h, p in feats) +
          '</div></div></section>\n')
    # 4. Simulateur (même bloc que l'accueil)
    s += re.search(r'<section class="u-sec u-sec--white hm-sec" id="estimer">.*?</section>\n', home.page(lang), flags=re.S).group(0)
    # 5. Seul ou avec Unaya
    (h1, l1), (h2, l2) = x['vs']
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["vs_h"]}</h2><p>{x["vs_p"]}</p></div><div class="ow-vs">'
          f'<div class="ow-vs__c ow-vs__c--no"><h3>{h1}</h3><ul>' + ''.join(f'<li>{v}</li>' for v in l1) + '</ul></div>'
          f'<div class="ow-vs__c ow-vs__c--ok"><h3>{h2}</h3><ul>' + ''.join(f'<li>{v}</li>' for v in l2) + '</ul>'
          f'<a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a></div></div></div></section>\n')
    # 6. Étapes
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["st_h"]}</h2><p>{x["st_p"]}</p></div><ol class="iv-tl iv-tl--4">' +
          ''.join(f'<li style="--i:{i}"><b>{i}</b><strong>{h}</strong><span>{p}</span></li>' for i, (svg, h, p) in enumerate(steps, 1)) + '</ol></div></section>\n')
    # 7. Espace propriétaire
    k, h, p, li, btn = x['portal']
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="ow-portal"><div class="ow-portal__t"><p class="hm-k">{k}</p><h2>{h}</h2><p>{p}</p><ul class="ow-portal__l">' +
          ''.join(f'<li>{v}</li>' for v in li) + f'</ul><a class="u-btn u-btn--rose" href="https://owners.unayabali.com">{btn}</a></div>'
          f'<div class="ow-portal__v" aria-hidden="true"><div class="ow-phone"><div class="ow-phone__ic">{small(portal_ic, 34)}</div>'
          + ''.join(f'<div class="ow-phone__r"><span></span><i style="width:{w}%"></i></div>' for w in (78, 56, 88, 42)) +
          '<div class="ow-phone__bars">' + ''.join(f'<i style="height:{hh}%"></i>' for hh in (38, 55, 47, 70, 62, 84, 76)) + '</div></div></div></div></div></section>\n')
    # 8. Zones
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["zn_h"]}</h2><p>{x["zn_p"]}</p></div><div class="ow-zones">' +
          ''.join(f'<div class="ow-zone"><img src="/assets/images/{img}" alt="{n}" loading="lazy"><div><strong>{n}</strong><span>{d}</span></div></div>' for img, n, d in x['zones']) + '</div></div></section>\n')
    # 9. Formules
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["pl_h"]}</h2><p>{x["pl_p"]}</p></div><div class="ow-plans">' +
          ''.join(f'<a class="ow-plan{" ow-plan--pop" if pop else ""}" href="{x["b2"][1]}">{"<span class=ow-plan__pop>" + x["pop"] + "</span>" if pop else ""}<h3>{n}</h3><p class="ow-plan__pct"><small>{f}</small> {pct}</p><p>{d}</p></a>' for n, f, pct, d, pop in x['plans']) +
          f'</div><p class="hm-c"><a class="u-link" href="{x["b2"][1]}">{x["pl_more"]}</a></p></div></section>\n')
    # 10. Appel final
    s += (f'<section class="u-cta"><img src="/assets/images/yuga-nuit.jpg" alt="" loading="lazy"><div class="u-cta__in"><h2>{x["cta_h"]}</h2><p>{x["cta_p"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn u-btn--white" href="{x["b2"][1]}">{x["b2"][0]}</a></div></div></section>\n')
    s += '</div>\n<script src="/assets/js/invest.js" defer></script>\n'
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'Proprietaires.html'), 'w').write(page(lang))
    print('ok')
