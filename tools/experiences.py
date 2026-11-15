# Page « Unaya Experiences » (FR/EN), version visuelle. On garde la page d'origine (calculateur de prix,
# formulaire, circuits, activités, avis, script) et on change : grande photo, chiffres clés, titres centrés,
# frise « comment ça se passe », photos Unsplash allégées (WebP à la bonne taille).
# Source : Exp_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

X = {
 'fr': dict(badges=['5,0/5 · 412 avis Tripadvisor', 'Guide francophone', 'Départ de votre villa'],
            keys=[('10', 'circuits à la journée, tous personnalisables'), ('5,0/5', '412 avis Tripadvisor de nos guides'), ('≈ 8 h', 'par jour, voiture privée climatisée'), ('dès 1,2 M', 'IDR par jour et par groupe')],
            how_k='Comment ça se passe', how_h='Une journée, sans rien organiser',
            how=[('Vous choisissez', 'Le circuit et la date, au plus tard 48 h avant.'), ('Nous confirmons', 'Avec le guide, puis sur WhatsApp, avec le prix final.'), ('Départ de la villa', 'Le guide vient vous chercher le matin.'), ('Retour le soir', 'Environ 8 h plus tard, à votre villa.')]),
 'en': dict(badges=['5.0/5 · 412 Tripadvisor reviews', 'French-speaking guide', 'Pick-up at your villa'],
            keys=[('10', 'day tours, all customisable'), ('5.0/5', '412 Tripadvisor reviews for our guides'), ('≈ 8 h', 'a day, private air-conditioned car'), ('from 1.2M', 'IDR per day and per group')],
            how_k='How it works', how_h='A full day, nothing to organise',
            how=[('You choose', 'The tour and the date, at least 48 hours ahead.'), ('We confirm', 'With the guide, then on WhatsApp, with the final price.'), ('Villa pick-up', 'Your guide picks you up in the morning.'), ('Back in the evening', 'About 8 hours later, at your villa.')]),
}

def unsplash(m):
    """Réécrit une image Unsplash en WebP léger avec plusieurs tailles."""
    tag = m.group(0)
    u = re.search(r'src="([^"]+)"', tag).group(1)
    base = u.split('?')[0]
    w0 = int((re.search(r'[?&]w=(\d+)', u) or [0, 1200])[1])
    h0 = re.search(r'[?&]h=(\d+)', u)
    ratio = int(h0.group(1)) / w0 if h0 else None
    def q(w):
        return f'{base}?w={w}' + (f'&h={round(w * ratio)}' if ratio else '') + '&q=55&fm=webp&fit=crop'
    widths = [800, 1200, 1600] if w0 >= 1600 else [w0 * 2 // 3, w0, round(w0 * 1.5)]
    src = q(1200 if w0 >= 1600 else w0)
    sizes = '100vw' if w0 >= 1600 else '(max-width: 900px) 100vw, 420px'
    tag = tag.replace(f'src="{u}"', f'src="{src}" srcset="{", ".join(f"{q(w)} {w}w" for w in widths)}" sizes="{sizes}"', 1)
    return tag

def page(lang):
    x, fr = X[lang], lang == 'fr'
    s = open(os.path.join(HERE, f'Exp_old_{lang}.html')).read()
    hero = re.search(r'<section class="u-hero u-hero--tall">.*?</section>', s, flags=re.S).group(0)
    img = re.search(r'<img src="([^"]+)"', hero).group(1)
    k = re.search(r'<p class="u-hero__k">(.*?)</p>', hero).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', hero).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', hero).group(1)
    btns = re.search(r'<div class="u-btns">(.*?)</div>', hero).group(1).replace('u-btn--white', 'hm-btn--glass')
    new = (f'<section class="hm-hero"><img src="{img}" alt="" fetchpriority="high" decoding="async"><div class="hm-hero__in"><p class="hm-hero__k">{k}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
           f'<div class="u-btns">{btns}</div><ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">★</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n'
           '<section class="iv-keys hm-keys"><div class="iv-keys__in">' + ''.join(f'<div class="iv-key"><strong>{a}</strong><span>{b}</span></div>' for a, b in x['keys']) + '</div></section>')
    s = s.replace(hero, new, 1)
    # titres centrés pour circuits et activités
    s = re.sub(r'<p class="xp-k">(.*?)</p><div class="u-head"><h2>', r'<div class="u-head u-head--c"><p class="hm-k">\1</p><h2>', s)
    # frise après les circuits
    tl = (f'<section class="u-sec u-sec--white xp-how"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["how_k"]}</p><h2>{x["how_h"]}</h2></div><ol class="iv-tl iv-tl--4">' +
          ''.join(f'<li style="--i:{i}"><b>{i}</b><strong>{a}</strong><span>{b}</span></li>' for i, (a, b) in enumerate(x['how'], 1)) + '</ol></div></section>\n')
    i = s.index('<section class="u-sec" id="activites">')
    s = s[:i] + tl + s[i:]
    # photos Unsplash allégées
    s = re.sub(r'<img src="https://images\.unsplash\.com[^>]*>', unsplash, s)
    s = s.replace('<!-- title:', '<!-- title:', 1)
    s = s.replace('\n<section class="hm-hero">', '\n<link rel="preconnect" href="https://images.unsplash.com">\n<div class="hm xp-page">\n<section class="hm-hero">', 1)
    j = s.index('<section class="u-cta">'); j = s.index('</section>', j) + len('</section>')
    s = s[:j] + '\n</div>' + s[j:]
    if '/assets/js/invest.js' not in s:
        s = s.rstrip() + '\n<script src="/assets/js/invest.js" defer></script>\n'
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'Experiences.html'), 'w').write(page(lang))
    print('ok')
