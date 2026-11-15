# Page « Nos services » (propriétaires, FR/EN), version visuelle : grande photo, menu des 5 pôles,
# un bloc photo + liste par pôle (numéroté, formules incluses), plateformes, 2 formules, appel final.
# Textes des 5 pôles repris de Svc_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

FULL, MKT = 'full', 'mkt'
X = {
 'fr': dict(
  title='Nos services — Unaya Management', kick='Propriétaires · Nos services',
  sub='Une seule équipe pour la louer, l’entretenir et en suivre les chiffres. Vous gardez la main, sans les soucis.',
  b1=('Confier ma villa', '/fr/proprietaires/confier-ma-villa/'), b2=('Voir les tarifs', '/fr/proprietaires/tarifs/'),
  badges=['5 pôles, une seule équipe', 'Assistance 24h/24', 'Rapport chaque mois'],
  nav='Aller à',
  inc='Inclus dans', full='Gestion complète', mkt='Marketing seul', part='en partie',
  # par pôle : photo, formules (complet / partiel), courte étiquette pour le menu
  svc=[('suma-g1.jpg', [(FULL, 0), (MKT, 0)], 'Marketing'), ('suma-entree.jpg', [(FULL, 0), (MKT, 1)], 'Voyageurs'),
       ('suma-chambre-1.jpg', [(FULL, 0)], 'Équipe'), ('yuga-piscine.jpg', [(FULL, 0)], 'Entretien'), (None, [(FULL, 0), (MKT, 1)], 'Comptabilité')],
  pl_lbl='Votre villa diffusée sur',
  pl_h='Deux formules, sans frais fixe', pl_p='Une commission sur les revenus, calculée après plateformes et taxe d’hébergement.',
  plans=[('Gestion complète', 'à partir de', '18 %', 'Les 5 pôles : nous nous occupons de tout.', True),
         ('Marketing seul', '', '11 %', 'Marketing, assistance en ligne et synthèse comptable. Vous gérez la villa sur place.', False)],
  pl_more='Comparer les formules en détail', pop='Le plus choisi',
  cta_h='Quelle formule pour votre villa ?', cta_p='On en parle, et on vous envoie une estimation de revenus gratuite sous 24 h.',
 ),
 'en': dict(
  title='Our services — Unaya Management', kick='Owners · Our services',
  sub='One team to rent it, maintain it and keep track of the numbers. You stay in control, without the hassle.',
  b1=('List my villa', '/owners/list-your-villa/'), b2=('See pricing', '/owners/pricing/'),
  badges=['5 areas, one team', '24/7 support', 'A report every month'],
  nav='Jump to',
  inc='Included in', full='Full Management', mkt='Marketing Only', part='partly',
  svc=[('suma-g1.jpg', [(FULL, 0), (MKT, 0)], 'Marketing'), ('suma-entree.jpg', [(FULL, 0), (MKT, 1)], 'Guests'),
       ('suma-chambre-1.jpg', [(FULL, 0)], 'Team'), ('yuga-piscine.jpg', [(FULL, 0)], 'Upkeep'), (None, [(FULL, 0), (MKT, 1)], 'Accounting')],
  pl_lbl='Your villa listed on',
  pl_h='Two plans, no fixed fees', pl_p='A commission on income, calculated after platform fees and accommodation tax.',
  plans=[('Full Management', 'from', '18%', 'All 5 areas: we take care of everything.', True),
         ('Marketing Only', '', '11%', 'Marketing, online support and a monthly accounting summary. You run the villa on site.', False)],
  pl_more='Compare plans in detail', pop='Most popular',
  cta_h='Which plan suits your villa?', cta_p='Let’s talk, and we’ll send you a free income estimate within 24 hours.',
 ),
}

def size(svg, n):
    return re.sub(r'width="\d+" height="\d+"', f'width="{n}" height="{n}"', svg, count=1)

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Svc_old_{lang}.html')).read()
    h1 = re.search(r'<h1>(.*?)</h1>', old).group(1)
    blocks = re.findall(r'<div class="u-svc__b"><div class="u-svc__h">(<svg.*?</svg>)<h3>(.*?)</h3></div><p>(.*?)</p><ul class="u-checks">(.*?)</ul></div>', old, flags=re.S)
    plat = re.search(r'<div class="pl-row">.*?</div>', open(os.path.join(HERE, f'Main_old_{lang}.html')).read(), flags=re.S).group(0)
    s = f'<!-- title: {x["title"]} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/yuga-terrasse.jpg" alt="{"La terrasse de la Villa Yuga, Nyanyi" if fr else "Villa Yuga terrace, Nyanyi"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{x["sub"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="{x["b2"][1]}">{x["b2"][0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    # Menu des 5 pôles
    s += (f'<nav class="sv-nav" aria-label="{x["nav"]}"><div class="sv-nav__in">' +
          ''.join(f'<a href="#pole-{i}">{size(svg, 22)}<span>{lbl}</span></a>' for i, ((svg, h, p, li), (_, _, lbl)) in enumerate(zip(blocks, x['svc']), 1)) + '</div></nav>\n')
    # Les 5 pôles
    s += '<section class="u-sec hm-sec sv-list"><div class="u-wrap">'
    for i, ((svg, h, p, li), (img, inc, _)) in enumerate(zip(blocks, x['svc']), 1):
        items = re.findall(r'<li>(.*?)</li>', li, flags=re.S)
        tags = ''.join(f'<span class="sv-tag sv-tag--{k}">{x[k]}{" (" + x["part"] + ")" if part else ""}</span>' for k, part in inc)
        if img:
            vis = f'<div class="sv-vis"><img src="/assets/images/{img}" alt="{h}" loading="lazy"><span class="sv-vis__ic">{size(svg, 30)}</span></div>'
        else:
            vis = ('<div class="sv-vis sv-vis--phone" aria-hidden="true"><div class="ow-phone"><div class="ow-phone__ic">' + size(svg, 34) + '</div>' +
                   ''.join(f'<div class="ow-phone__r"><span></span><i style="width:{w}%"></i></div>' for w in (78, 56, 88, 42)) +
                   '<div class="ow-phone__bars">' + ''.join(f'<i style="height:{hh}%"></i>' for hh in (38, 55, 47, 70, 62, 84, 76)) + '</div></div></div>')
        s += (f'<article class="sv-row{" sv-row--rev" if i % 2 == 0 else ""}" id="pole-{i}">{vis}<div class="sv-t"><span class="sv-n">0{i}</span><h2>{h}</h2><p class="sv-lead">{p}</p>'
              f'<ul class="sv-checks">' + ''.join(f'<li>{v}</li>' for v in items) + f'</ul><div class="sv-inc"><small>{x["inc"]}</small>{tags}</div></div></article>')
        if i == 1:
            s += f'<div class="sv-plat"><p>{x["pl_lbl"]}</p>{plat}</div>'
    s += '</div></section>\n'
    # Formules
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["pl_h"]}</h2><p>{x["pl_p"]}</p></div><div class="ow-plans">' +
          ''.join(f'<a class="ow-plan{" ow-plan--pop" if pop else ""}" href="{x["b2"][1]}">{"<span class=ow-plan__pop>" + x["pop"] + "</span>" if pop else ""}<h3>{n}</h3><p class="ow-plan__pct"><small>{f}</small> {pct}</p><p>{d}</p></a>' for n, f, pct, d, pop in x['plans']) +
          f'</div><p class="hm-c"><a class="u-link" href="{x["b2"][1]}">{x["pl_more"]}</a></p></div></section>\n')
    s += (f'<section class="u-cta"><img src="/assets/images/yuga-nuit.jpg" alt="" loading="lazy"><div class="u-cta__in"><h2>{x["cta_h"]}</h2><p>{x["cta_p"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn u-btn--white" href="{x["b2"][1]}">{x["b2"][0]}</a></div></div></section>\n</div>\n')
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'ProprietairesServices.html'), 'w').write(page(lang))
    print('ok')
