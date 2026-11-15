# Page « Nos villas » (FR/EN), version visuelle : grande photo, chiffres, réserver en direct,
# une grande fiche par villa (3 photos, infos, prix mis par build.py, 2 boutons), avis, services, appel final.
# Textes des villas et icônes repris de Vil_old_{lang}.html ; avis repris de Main_old_{lang}.html.
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

MOS = {'suma': ['suma-piscine.jpg', 'suma-chambre-1.jpg', 'suma-terrasse.jpg'],
       'yuga': ['yuga-piscine-2.jpg', 'yuga-chambre.jpg', 'yuga-terrasse.jpg'],
       'rumah-jambu': ['rumah-jambu-jardin.jpg', 'rj-salon.jpg', 'rj-chambre.jpg']}
X = {
 'fr': dict(
  kick='Locations de vacances à Bali', b1=('Voir les villas', '#liste'),
  badges=['−15 % dès 7 nuits en direct', '−20 % dès 28 nuits', '9,8/10 sur Booking.com'],
  keys=[('3', 'villas privées avec piscine ou jardin'), ('9,8/10', 'note moyenne sur Booking.com'), ('4,93/5', 'note moyenne sur Airbnb'), ('263', 'voyageurs accueillis depuis juillet 2026')],
  dir_h='Réservez en direct, c’est mieux', dir_p='Sur notre site, vous parlez directement à l’équipe qui vous accueille.',
  dir=[('−15 %', 'dès 7 nuits', 'Une semaine ou plus ? La remise s’applique toute seule.'), ('−20 %', 'dès 28 nuits', 'Pour un mois à Bali, au calme.'), ('24h/24', 'sur WhatsApp', 'Une question avant ou pendant le séjour : on répond vite.')],
  list_h='Choisissez votre villa', book='Réserver', see='Découvrir la villa',
  rev_h='Ce qu’en disent nos voyageurs', rev_more='Tous les avis sur la page de chaque villa.',
  svc_k='Pendant votre séjour', svc_more=('Voir les services voyageurs', '/fr/services-voyageurs/'),
  soon_h='De nouvelles villas arrivent', soon_p='Notre collection s’agrandit : de nouvelles adresses rejoignent bientôt Unaya.', soon_b=('Être informé', '/fr/contact/'),
 ),
 'en': dict(
  kick='Holiday rentals in Bali', b1=('See the villas', '#liste'),
  badges=['−15% from 7 nights direct', '−20% from 28 nights', '9.8/10 on Booking.com'],
  keys=[('3', 'private villas with pool or garden'), ('9.8/10', 'average score on Booking.com'), ('4.93/5', 'average score on Airbnb'), ('263', 'guests welcomed since July 2026')],
  dir_h='Book direct, it’s better', dir_p='On our website you talk directly to the team that welcomes you.',
  dir=[('−15%', 'from 7 nights', 'A week or more? The discount applies automatically.'), ('−20%', 'from 28 nights', 'For a month in Bali, in peace.'), ('24/7', 'on WhatsApp', 'A question before or during your stay: we reply fast.')],
  list_h='Choose your villa', book='Book', see='Discover the villa',
  rev_h='What our guests say', rev_more='All reviews on each villa’s page.',
  svc_k='During your stay', svc_more=('See guest services', '/guest-services/'),
  soon_h='New villas are coming', soon_p='Our collection is growing: new addresses will join Unaya soon.', soon_b=('Keep me posted', '/contact/'),
 ),
}

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Vil_old_{lang}.html')).read()
    title = re.search(r'<!-- title: (.*?) -->', old).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', old).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', old).group(1)
    filters = re.search(r'<div class="vl-filters".*?</div>', old, flags=re.S).group(0)
    none = re.search(r'<p class="vl-none".*?</p>', old, flags=re.S).group(0)
    cards = re.findall(r'<a class="vl-card" data-zone="(\w+)" href="([^"]+)"><div class="vl-card__img"><img[^>]*><span class="vl-card__zone">(.*?)</span></div><div class="vl-card__b"><h3>(.*?)</h3><div class="vl-card__meta">(.*?)</div><p>(.*?)</p>', old, flags=re.S)
    svc_h = re.search(r'<section class="u-sec u-sec--white"><div class="u-wrap"><div class="u-head"><h2>(.*?)</h2>', old).group(1)
    svcs = re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', old, flags=re.S)
    soon_ic = re.search(r'<div class="vl-soon"[^>]*>(<svg.*?</svg>)', old, flags=re.S).group(1)
    cta = re.search(r'<section class="u-cta">.*?</section>', old, flags=re.S).group(0)
    quotes = re.findall(r'<div class="u-quote">.*?</span></div>', open(os.path.join(HERE, f'Main_old_{lang}.html')).read(), flags=re.S)[:3]
    s = f'<!-- title: {title} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero"><img src="/assets/images/suma-g1.jpg" alt="{"La Villa Suma à la tombée de la nuit" if fr else "Villa Suma at dusk"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="#reserver-direct">{x["dir_h"].split(",")[0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">★</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    s += '<section class="iv-keys hm-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) + '</div></section>\n'
    # Liste des villas
    rows = ''
    for i, (zone, href, zlabel, name, meta, desc) in enumerate(cards):
        slug = href.rstrip('/').split('/')[-1]
        imgs = MOS[slug]
        mos = (f'<div class="vr-mos"><img class="vr-mos__a" src="/assets/images/{imgs[0]}" alt="{name}" loading="lazy">'
               + ''.join(f'<img src="/assets/images/{im}" alt="" loading="lazy">' for im in imgs[1:]) + f'<span class="vl-card__zone">{zlabel}</span></div>')
        rows += (f'<article class="vl-card vr-row{" vr-row--rev" if i % 2 else ""}" data-zone="{zone}">{mos}<div class="vr-t"><span class="vr-n">0{i + 1}</span><h3>{name}</h3>'
                 f'<div class="vl-card__meta">{meta}</div><!--PRICE--><p class="vr-d">{desc}</p>'
                 f'<div class="u-btns"><a class="u-btn u-btn--solid" href="{href}#reserver">{x["book"]}</a><a class="u-btn u-btn--line" href="{href}">{x["see"]}</a></div></div></article>')
    s += (f'<section class="u-sec hm-sec" id="liste"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["list_h"]}</h2></div>{filters.replace("vl-filters", "vl-filters vr-filters", 1)}'
          f'<div class="vr-list">{rows}</div>{none}'
          f'<div class="vr-soon">{soon_ic}<div><strong>{x["soon_h"]}</strong><p>{x["soon_p"]}</p></div><a class="u-btn u-btn--line" href="{x["soon_b"][1]}">{x["soon_b"][0]}</a></div></div></section>\n')
    # Réserver en direct
    s += (f'<section class="u-sec u-sec--dark hm-sec hm-ges" id="reserver-direct"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["dir_h"]}</h2><p style="color:#E2D6CF">{x["dir_p"]}</p></div><div class="hm-ges__g">' +
          ''.join(f'<div class="hm-step"><strong class="vr-big">{a}</strong><h3>{b}</h3><p>{c}</p></div>' for a, b, c in x['dir']) + '</div></div></section>\n')
    # Avis
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["rev_h"]}</h2></div><div class="u-cards vr-quotes">{"".join(quotes)}</div>'
          f'<p class="hm-c" style="color:var(--prune);font-size:14.5px">{x["rev_more"]}</p></div></section>\n')
    # Services
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["svc_k"]}</p><h2>{svc_h}</h2></div><div class="ar-lv2 hm-gar">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{re.sub(r"width=.40. height=.40.", "width=\"26\" height=\"26\"", svg, count=1)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for svg, h, p in svcs) +
          f'</div><p class="hm-c"><a class="u-btn u-btn--line" href="{x["svc_more"][1]}">{x["svc_more"][0]}</a></p></div></section>\n')
    s += cta + '\n</div>\n<script src="/assets/js/invest.js" defer></script>\n'
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'Villas.html'), 'w').write(page(lang))
    print('ok')
