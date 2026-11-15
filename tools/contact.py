# Page « Contact » (FR/EN), version visuelle : grande photo (même photo, allégée), 4 façons de nous joindre,
# formulaire + coordonnées + carte (repris tels quels), « vous êtes… » en 3 cartes.
# Source : Ctc_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
WA = 'https://wa.me/6285190211324'

X = {
 'fr': dict(kick='Contact', badges=['Réponse sous 24 h', 'En français ou en anglais', 'Bureau à Jimbaran'],
            ways=[('WhatsApp', '+62 851 9021 1324', 'Le plus rapide, de 8 h à 20 h', WA), ('E-mail', 'info@unayabali.com', 'Réponse sous 24 h', 'mailto:info@unayabali.com'),
                  ('Instagram', '@unayabali', 'Nos villas en photos', 'https://www.instagram.com/unayabali/'), ('Bureau', 'Jimbaran, Bali', 'Sur rendez-vous', '#carte')],
            form_k='Écrivez-nous', form_h='Votre message',
            who_h='Vous êtes…', who=[('yuga-drone.jpg', 'Propriétaire', 'Confiez-nous votre villa : estimation de revenus gratuite.', 'Confier ma villa', '/fr/proprietaires/confier-ma-villa/'),
                                     ('suma-piscine-2.jpg', 'Voyageur', 'Réservez en direct : −15 % dès 7 nuits.', 'Voir nos villas', '/fr/villas/'),
                                     ('arawa-facade.jpg', 'Investisseur', 'Villas et terrains à vendre, vérifiés par Unaya.', 'Investir à Bali', '/fr/investir-a-bali/')]),
 'en': dict(kick='Contact', badges=['Reply within 24 hours', 'In English or French', 'Office in Jimbaran'],
            ways=[('WhatsApp', '+62 851 9021 1324', 'The fastest, 8 am to 8 pm', WA), ('E-mail', 'info@unayabali.com', 'Reply within 24 hours', 'mailto:info@unayabali.com'),
                  ('Instagram', '@unayabali', 'Our villas in pictures', 'https://www.instagram.com/unayabali/'), ('Office', 'Jimbaran, Bali', 'By appointment', '#carte')],
            form_k='Write to us', form_h='Your message',
            who_h='You are…', who=[('yuga-drone.jpg', 'An owner', 'Hand over your villa: free income estimate.', 'List my villa', '/owners/list-your-villa/'),
                                   ('suma-piscine-2.jpg', 'A guest', 'Book direct: −15% from 7 nights.', 'See our villas', '/villas/'),
                                   ('arawa-facade.jpg', 'An investor', 'Villas and land for sale, checked by Unaya.', 'Invest in Bali', '/invest-in-bali/')]),
}

def hero_img(u):
    b = u.split('?')[0]
    q = lambda w: f'{b}?w={w}&q=50&fm=webp&fit=crop'
    return f'<img src="{q(1200)}" srcset="{q(800)} 800w, {q(1200)} 1200w, {q(1600)} 1600w" sizes="100vw" alt="" fetchpriority="high" decoding="async">'

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Ctc_old_{lang}.html')).read()
    title = re.search(r'<!-- title: (.*?) -->', old).group(1)
    hero = re.search(r'<section class="u-hero">.*?</section>', old, flags=re.S).group(0)
    img = re.search(r'<img src="([^"]+)"', hero).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', hero).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', hero).group(1)
    main = old[old.index(hero) + len(hero):].strip()
    main = main.replace('<div class="c-form">', f'<div class="c-form"><p class="hm-k">{x["form_k"]}</p><h2 class="ct-h">{x["form_h"]}</h2>', 1)
    main = main.replace('<div class="c-map">', '<div class="c-map" id="carte">', 1)
    main = main.replace('<section class="u-sec">', '<section class="u-sec hm-sec ct-main">', 1)
    s = f'<!-- title: {title} -->\n<link rel="preconnect" href="https://images.unsplash.com">\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm">{hero_img(img)}<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    s += main + '\n'
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["who_h"]}</h2></div><div class="ar-lv2 hm-doors">' +
          ''.join(f'<a class="ar-lv2__c hm-door" href="{u}"><div class="ar-lv2__img"><img src="/assets/images/{im}" alt="" loading="lazy"></div><div class="ar-lv2__b"><h3>{h}</h3><p class="ar-lv2__p">{p}</p><span class="u-link">{l}</span></div></a>' for im, h, p, l, u in x['who']) +
          '</div></div></section>\n</div>\n<script src="/assets/js/invest.js" defer></script>\n')
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'Contact.html'), 'w').write(page(lang))
    print('ok')
