# Page « Services voyageurs » (FR/EN), version visuelle : grande photo, menu des 4 services,
# grandes cartes (photo + prix + bouton qui ouvre le formulaire), étapes, bandeau villas, appel final.
# Cartes, textes, prix et formulaires (dialogues) repris tels quels de Gst_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))

EXP_IC = '<svg aria-hidden="true" class="u-ic" width="24" height="24" viewBox="0 0 48 48" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M4 40 18 18l8 12 6-8 12 18Z"/><circle cx="34" cy="11" r="4"/></svg>'
X = {
 'fr': dict(kick='Services voyageurs', badges=['Réponse sous 24 h sur WhatsApp', 'Paiement sécurisé : carte, virement, QRIS', 'Scooter livré à la villa'],
            nav=['Transfert', 'Chauffeur', 'Scooter', 'Excursions'], from_='dès', ask='sur demande',
            how_h='Comment ça marche', how_p='Trois étapes, sans appel ni attente.',
            vil=('Vous réservez une villa Unaya ?', 'Ajoutez le transfert et le scooter directement lors de votre réservation.', 'Voir nos villas', '/fr/villas/'),
            cta=('Pas encore de villa pour votre séjour ?', 'Des villas privées avec piscine, au calme. −15 % dès 7 nuits en réservant en direct.', 'Voir nos villas', '/fr/villas/')),
 'en': dict(kick='Guest services', badges=['Reply within 24 hours on WhatsApp', 'Secure payment: card, transfer, QRIS', 'Scooter delivered to the villa'],
            nav=['Transfer', 'Driver', 'Scooter', 'Day trips'], from_='from', ask='on request',
            how_h='How it works', how_p='Three steps, no calls, no waiting.',
            vil=('Booking an Unaya villa?', 'Add the transfer and the scooter directly when you book.', 'See our villas', '/villas/'),
            cta=('No villa for your stay yet?', 'Private pool villas in quiet spots. −15% from 7 nights when you book direct.', 'See our villas', '/villas/')),
}

def hero_img(u):
    b = u.split('?')[0]
    q = lambda w: f'{b}?w={w}&q=60&fm=webp&fit=crop'
    return (f'<img src="{q(1600)}" srcset="{q(800)} 800w, {q(1200)} 1200w, {q(1600)} 1600w, {q(2000)} 2000w" sizes="100vw" alt="" fetchpriority="high">')

def card_img(u):
    b = u.split('?')[0]
    q = lambda w: f'{b}?w={w}&h={round(w * .5625)}&q=60&fm=webp&fit=crop'
    return q(900), f'{q(600)} 600w, {q(900)} 900w, {q(1200)} 1200w'

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Gst_old_{lang}.html')).read()
    title = re.search(r'<!-- title: (.*?) -->', old).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', old).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', old).group(1)
    dialogs = '\n'.join(re.findall(r'<dialog .*?</dialog>', old, flags=re.S))
    icons = re.findall(r'<div class="u-feat">(<svg.*?</svg>)', open(os.path.join(HERE, f'Vil_old_{lang}.html')).read(), flags=re.S)[:3] + [EXP_IC]
    icons = [re.sub(r'width="\d+" height="\d+"', 'width="24" height="24"', i, count=1) for i in icons]
    cards = re.findall(r'<div id="(\w+)" style="[^"]*"><img class="sv-ph" src="([^"]+)" alt="([^"]*)" loading="lazy"><h2[^>]*>(.*?)</h2><p[^>]*>(.*?)</p><div style="margin-top: auto[^"]*">(.*?)</div>((?:<button|<a ).*?(?:</button>|</a>))</div>', old, flags=re.S)
    steps = re.findall(r'<span style="font-family: \'Cormorant Garamond\'[^"]*color: #A8705A;">\d</span><div><p[^>]*>(.*?)</p><p[^>]*>(.*?)</p></div>', old, flags=re.S)
    s = f'<!-- title: {title} -->\n<link rel="preconnect" href="https://images.unsplash.com">\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm">{hero_img(re.search(r'<section class="u-hero"><img src="([^"]+)"', old).group(1))}'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    s += ('<nav class="sv-nav gs-nav" aria-label="Services"><div class="sv-nav__in">' +
          ''.join(f'<a href="#{c[0]}">{ic}<span>{n}</span></a>' for c, ic, n in zip(cards, icons, x['nav'])) + '</div></nav>\n')
    out = ''
    for cid, img, alt, h, p, rows, btn in cards:
        prices = re.findall(r'<span>(.*?)</span><span style="[^"]*">(.*?)</span>', rows)
        note = re.search(r'<span style="font-size: 13px[^"]*">(.*?)</span>', rows)
        nums = [re.search(r'IDR [\d  ,]+', v) for _, v in prices]
        nums = [m.group(0).strip() for m in nums if m]
        badge = f'{x["from_"]} {min(nums, key=lambda t: int(re.sub(r"\D", "", t)))}' if nums else x['ask']
        btn = re.sub(r' style="[^"]*"', '', btn, count=1)
        btn = btn.replace('<button type="button" data-open-dialog', '<button type="button" class="u-btn u-btn--solid gs-btn" data-open-dialog').replace('<a href=', '<a class="u-btn gs-btn gs-btn--exp" href=')
        out += (f'<article class="gs-card{" gs-card--exp" if cid == "experiences" else ""}" id="{cid}"><div class="gs-card__img"><img src="{card_img(img)[0]}" srcset="{card_img(img)[1]}" sizes="(max-width: 900px) 100vw, 600px" alt="{alt}" loading="lazy"><span class="gs-card__badge">{badge}</span></div>'
                f'<div class="gs-card__b"><h2>{h}</h2><p class="gs-card__p">{p}</p><dl class="gs-rows">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in prices) + '</dl>'
                + (f'<p class="gs-note">{note.group(1)}</p>' if note else '') + f'{btn}</div></article>')
    s += f'<section class="u-sec hm-sec gs-sec"><div class="u-wrap"><div class="gs-grid">{out}</div></div></section>\n'
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["how_h"]}</h2><p>{x["how_p"]}</p></div><ol class="iv-tl iv-tl--3">' +
          ''.join(f'<li style="--i:{i}"><b>{i}</b><strong>{a}</strong><span>{b}</span></li>' for i, (a, b) in enumerate(steps, 1)) + '</ol>'
          f'<div class="gs-vil"><div><strong>{x["vil"][0]}</strong><p>{x["vil"][1]}</p></div><a class="u-btn u-btn--rose" href="{x["vil"][3]}">{x["vil"][2]}</a></div></div></section>\n')
    s += (f'<section class="u-cta"><img src="/assets/images/suma-g1.jpg" alt="" loading="lazy"><div class="u-cta__in"><h2>{x["cta"][0]}</h2><p>{x["cta"][1]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["cta"][3]}">{x["cta"][2]}</a></div></div></section>\n</div>\n{dialogs}\n<script src="/assets/js/invest.js" defer></script>\n')
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'ServicesVoyageurs.html'), 'w').write(page(lang))
    print('ok')
