# Page « À propos » (FR/EN), version visuelle : grande photo, chiffres clés, histoire avec photo en arche,
# le symbole expliqué autour du logo, valeurs, la famille Unaya, appel final.
# Textes et icônes repris de Abt_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

X = {
 'fr': dict(kick='À propos', b1=('Nous contacter', '/fr/contact/'), b2=('Nos villas', '/fr/villas/'),
            badges=['Société indonésienne enregistrée', 'Équipe sur place 7j/7', 'Uluwatu · Tanah Lot · Seminyak'],
            keys=[('263', 'voyageurs accueillis depuis juillet 2026'), ('22', 'nationalités'), ('9,8/10', 'note moyenne sur Booking.com'), ('3', 'zones, connues rue par rue')],
            story_k='Notre histoire', facts=[('Née à Bali', 'à Jimbaran'), ('Peu de villas', 'suivies de près')],
            sym_k='Notre symbole', val_k='Nos valeurs', grp_k='Unaya Bali Group'),
 'en': dict(kick='About', b1=('Contact us', '/contact/'), b2=('Our villas', '/villas/'),
            badges=['Registered Indonesian company', 'Team on site 7 days a week', 'Uluwatu · Tanah Lot · Seminyak'],
            keys=[('263', 'guests welcomed since July 2026'), ('22', 'nationalities'), ('9.8/10', 'average score on Booking.com'), ('3', 'areas, known street by street')],
            story_k='Our story', facts=[('Born in Bali', 'in Jimbaran'), ('Few villas', 'followed closely')],
            sym_k='Our symbol', val_k='Our values', grp_k='Unaya Bali Group'),
}

def sz(svg, n):
    return re.sub(r'width="\d+" height="\d+"', f'width="{n}" height="{n}"', svg, count=1)

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Abt_old_{lang}.html')).read()
    title = re.search(r'<!-- title: (.*?) -->', old).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', old).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', old).group(1)
    st = re.search(r'<div class="u-split__txt"><h2>(.*?)</h2>(.*?)</div></div></div></section>', old, flags=re.S)
    logo = re.search(r'<div class="a-sym__logo">(<svg.*?</svg>)', old, flags=re.S).group(1)
    sym_h = re.search(r'<div class="a-sym">.*?<h2>(.*?)</h2>', old, flags=re.S).group(1)
    sym = re.findall(r'<div class="u-row">(<svg.*?</svg>)<div><h3>(.*?)</h3><p>(.*?)</p></div>', old, flags=re.S)
    val_h = re.search(r'<h2>([^<]*)</h2></div><div class="u-feats u-feats--3">', old).group(1)
    vals = re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', old, flags=re.S)
    grp = re.search(r'<div class="u-head"><h2>([^<]*)</h2><p>([^<]*)</p></div><div class="a-group">(.*?)</div><div class="a-co">(.*?)</div></div></section>', old, flags=re.S)
    items = re.findall(r'<(div class=a-cur|a href="[^"]+"|div)>(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p>(?:<span[^>]*>(.*?)</span>)?</(?:div|a)>', grp.group(3), flags=re.S)
    cta = re.search(r'<section class="u-cta">.*?</section>', old, flags=re.S).group(0)
    s = f'<!-- title: {title} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/suma-jardin.jpg" alt="{"Le jardin de SUMA Bali" if fr else "SUMA Bali garden"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="{x["b2"][1]}">{x["b2"][0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    s += '<section class="iv-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) + '</div></section>\n'
    # Histoire
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="hm-bld"><div class="hm-bld__img"><img src="/assets/images/yuga-drone.jpg" alt="{"La Villa Yuga vue du ciel" if fr else "Villa Yuga from above"}" loading="lazy">'
          '<div class="hm-bld__facts">' + ''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in x['facts']) + '</div></div>'
          f'<div class="hm-bld__t ab-story"><p class="hm-k">{x["story_k"]}</p><h2>{st.group(1)}</h2>{st.group(2)}</div></div></div></section>\n')
    # Symbole
    cl = [f'<div class="ab-sym__c"><span class="ab-sym__n">0{i}</span>{sz(svg, 30)}<h3>{h}</h3><p>{p}</p></div>' for i, (svg, h, p) in enumerate(sym, 1)]
    s += (f'<section class="u-sec u-sec--dark hm-sec ab-sym"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k" style="color:#D2A48C">{x["sym_k"]}</p><h2>{sym_h}</h2></div>'
          f'<div class="ab-sym__g"><div class="ab-sym__col">{"".join(cl[:2])}</div><div class="ab-sym__logo">{logo}</div><div class="ab-sym__col">{"".join(cl[2:])}</div></div></div></section>\n')
    # Valeurs
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["val_k"]}</p><h2>{val_h}</h2></div><div class="ar-lv2 hm-gar">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{sz(svg, 26)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for svg, h, p in vals) + '</div></div></section>\n')
    # Famille Unaya
    fam = ''
    for tag, svg, h, p, link in items:
        cur = tag.startswith('div class=a-cur')
        if tag.startswith('a '):
            fam += f'<{tag} class="ab-fam__c ab-fam__c--link">{sz(svg, 34)}<h3>{h}</h3><p>{p}</p><span class="u-link">{link}</span></a>'
        else:
            if cur:
                href, lbl = ('/fr/proprietaires/', 'Nos services de gestion') if fr else ('/owners/', 'Our management services')
                fam += f'<a href="{href}" class="ab-fam__c ab-fam__c--cur ab-fam__c--link">{sz(svg, 34)}<h3>{h}</h3><p>{p}</p><span class="u-link">{lbl}</span></a>'
            else:
                fam += f'<div class="ab-fam__c">{sz(svg, 34)}<h3>{h}</h3><p>{p}</p></div>'
    co = ''.join(f'<span>{c}</span>' for c in re.findall(r'<span>(.*?)</span>', grp.group(4), flags=re.S))
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["grp_k"]}</p><h2>{grp.group(1)}</h2><p>{grp.group(2)}</p></div>'
          f'<div class="ab-fam">{fam}</div><div class="ab-co">{co}</div></div></section>\n')
    s += cta + '\n</div>\n<script src="/assets/js/invest.js" defer></script>\n'
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'APropos.html'), 'w').write(page(lang))
    print('ok')
