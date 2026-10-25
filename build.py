#!/usr/bin/env python3
"""Génère le site Unaya Management dans le dossier dist/.

Utilisation :  python3 build.py
Les textes des pages sont dans src/pages/fr/ et src/pages/en/ (HTML).
L'en-tête, le menu et le pied de page sont définis ci-dessous, une seule fois pour tout le site.
"""
import os, re, json, shutil, html, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST = os.path.join(ROOT, 'src'), os.path.join(ROOT, 'dist')
SITE = 'https://unayabali.com'
ROUTES = json.load(open(os.path.join(SRC, 'routes.json'), encoding='utf-8'))
PORTAL = 'https://owners.unayabali.com'
# Réservation en ligne : 'beds24' (paiement Midtrans actif) ou 'whatsapp' (demande de disponibilité, en attendant la validation Midtrans)
BOOKING_MODE = 'whatsapp'
WHATSAPP = {'VillaSuma': '6285190211324', 'VillaYuga': '6281330617077', 'VillaRumahJambu': '6285190211324'}
OWNER_PAGES = ['Proprietaires', 'ProprietairesServices', 'ProprietairesTarifs', 'ConfierMaVilla']
BEDS24 = {'VillaSuma': '359817', 'VillaYuga': '359816', 'VillaRumahJambu': '359818'}  # propriétés Unaya

T = {  # textes communs
 'fr': dict(nav=[('Proprietaires','Propriétaires'),('Main#villas','Nos villas'),('Main#zones','Nos zones'),('ServicesVoyageurs','Services voyageurs'),('APropos','À propos'),('Contact','Contact')],
            book='Réserver', owner='Confier ma villa', menu='Menu', skip='Aller au contenu', main_menu='Menu principal',
            sub=[('Proprietaires',"Vue d'ensemble"),('ProprietairesServices','Nos services'),('ProprietairesTarifs','Formules & tarifs'),('ConfierMaVilla','Confier ma villa')], sub_label='Propriétaires', portal='Espace propriétaire',
            f_nav='Navigation', f_contact='Contact', f_company='Société', f_links=[('Proprietaires','Propriétaires'),('Main#villas','Nos villas'),('ServicesVoyageurs','Services voyageurs'),('FAQ','FAQ'),('Contact','Contact')],
            legal=[('MentionsLegales','Mentions légales'),('Confidentialite','Confidentialité'),('Conditions','Conditions de réservation')],
            country='Indonésie', build='Unaya Build — Investir à Bali', ogloc='fr_FR'),
 'en': dict(nav=[('Proprietaires','Owners'),('Main#villas','Our villas'),('Main#zones','Our areas'),('ServicesVoyageurs','Guest services'),('APropos','About'),('Contact','Contact')],
            book='Book', owner='List my villa', menu='Menu', skip='Skip to content', main_menu='Main menu',
            sub=[('Proprietaires','Overview'),('ProprietairesServices','Our services'),('ProprietairesTarifs','Plans & pricing'),('ConfierMaVilla','List my villa')], sub_label='Owners', portal='Owner portal',
            f_nav='Navigation', f_contact='Contact', f_company='Company', f_links=[('Proprietaires','Owners'),('Main#villas','Our villas'),('ServicesVoyageurs','Guest services'),('FAQ','FAQ'),('Contact','Contact')],
            legal=[('MentionsLegales','Legal notice'),('Confidentialite','Privacy'),('Conditions','Booking terms')],
            country='Indonesia', build='Unaya Build — Invest in Bali', ogloc='en_US'),
}

DESC = {
 ('fr','Investir'):"Investir à Bali : bail ou PT PMA, acheter ou faire construire, taxes et location en règle. Unaya Build vous accompagne du terrain à la mise en location.",
 ('en','Investir'):"Investing in Bali: leasehold or PT PMA, buying or building, taxes and legal renting. Unaya Build supports you from the land to renting out your villa.",
 ('fr','Main'):"Gestion locative de villas à Bali : marketing, réservations, entretien et rapport financier chaque mois. Commission dès 18 %, sans frais fixes. Uluwatu / Jimbaran, Tanah Lot / Canggu West, Seminyak / Kerobokan.",
 ('en','Main'):"Bali villa management: marketing, bookings, maintenance and a monthly financial report. Commission from 18%, no fixed fees. Uluwatu / Jimbaran, Tanah Lot / Canggu West, Seminyak / Kerobokan.",
 ('fr','VillaSuma'):"Villa Suma à Balangan, Uluwatu : 5 suites, piscine privée, jusqu'à 10 voyageurs, à 5 minutes de la plage. Réservation directe.",
 ('en','VillaSuma'):"Villa Suma in Balangan, Uluwatu: 5 suites, private pool, up to 10 guests, 5 minutes from the beach. Book direct.",
 ('fr','VillaYuga'):"Villa Yuga à Nyanyi : 4 chambres, piscine privée, vue sur les rizières, à 5 minutes de Nuanu. Jusqu'à 8 voyageurs. Réservation directe.",
 ('en','VillaYuga'):"Villa Yuga in Nyanyi: 4 bedrooms, private pool, rice-field views, 5 minutes from Nuanu. Up to 8 guests. Book direct.",
 ('fr','VillaRumahJambu'):"Rumah Jambu : maison balinaise authentique avec jardin tropical, au cœur du village de Balangan, Uluwatu. 2 chambres, 4 voyageurs.",
 ('en','VillaRumahJambu'):"Rumah Jambu: an authentic Balinese house with a tropical garden in the heart of Balangan village, Uluwatu. 2 bedrooms, 4 guests.",
 ('fr','Proprietaires'):"Confiez votre villa à Unaya Management : location, entretien et rapport financier chaque mois, sans frais fixes. Uluwatu / Jimbaran, Tanah Lot / Canggu West, Seminyak / Kerobokan.",
 ('en','Proprietaires'):"Entrust your villa to Unaya Management: rentals, maintenance and a monthly financial report, with no fixed fees. Uluwatu / Jimbaran, Tanah Lot / Canggu West, Seminyak / Kerobokan.",
 ('fr','ProprietairesServices'):"Marketing, réservations, accueil des voyageurs, entretien et comptabilité : tous les services Unaya Management pour votre villa à Bali.",
 ('en','ProprietairesServices'):"Marketing, bookings, guest welcome, maintenance and accounting: every Unaya Management service for your Bali villa.",
 ('fr','ProprietairesTarifs'):"Gestion complète à partir de 18 % ou Marketing seul à 11 %. Sans frais fixes, commission calculée après plateformes et taxe d'hébergement.",
 ('en','ProprietairesTarifs'):"Full Management from 18% or Marketing Only at 11%. No fixed fees, commission calculated after platform fees and accommodation tax.",
 ('fr','ConfierMaVilla'):"Présentez-nous votre villa à Bali et recevez une estimation de revenus gratuite et sans engagement sous 24 h.",
 ('en','ConfierMaVilla'):"Tell us about your Bali villa and receive a free, no-obligation income estimate within 24 hours.",
}

# Version des fichiers CSS/JS (change à chaque modification → le navigateur recharge la nouvelle version)
ASSET_V = hashlib.md5(b''.join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), 'rb').read() for f in ('assets/css/site.css', 'assets/js/site.js'))).hexdigest()[:8]

def url(name, lang):
    base, _, anchor = name.partition('#')
    return ROUTES[base][lang] + (('#' + anchor) if anchor else '')

def header(lang, page):
    t = T[lang]; other = 'en' if lang == 'fr' else 'fr'
    nav = ''.join(f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if (n == page or (n == "Proprietaires" and page in OWNER_PAGES)) else ""}>{lbl}</a>' for n, lbl in t['nav'])
    langsw = (f'<a class="lang" href="{url(page, other)}" hreflang="{other}"><strong>FR</strong> · EN</a>' if lang == 'fr'
              else f'<a class="lang" href="{url(page, other)}" hreflang="{other}">FR · <strong>EN</strong></a>')
    sub = ''
    if page in OWNER_PAGES:
        sub = f'<nav class="subnav" aria-label="{t["sub_label"]}">' + ''.join(
            f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if n == page else ""}>{lbl}</a>' for n, lbl in t['sub']) + f'<a class="subnav-portal" href="{PORTAL}">{t["portal"]} ↗</a></nav>'
    book_target = '#reserver' if page in BEDS24 else url('Main#villas', lang)
    return f'''<a class="skip" href="#contenu">{t['skip']}</a>
<header class="site-header">
<div class="site-header__in">
<a class="site-header__logo" href="{url('Main', lang)}"><img src="/assets/logos/unaya-management-horizontal.svg" alt="Unaya Management" width="176" height="40"></a>
<nav class="site-nav" id="site-nav" aria-label="{t['main_menu']}">{nav}<a class="nav-lang" href="{url(page, other)}" hreflang="{other}">{'English' if lang == 'fr' else 'Français'}</a></nav>
<div class="site-header__actions">{langsw}<a class="btn" href="{url('ConfierMaVilla', lang)}">{t['owner']}</a><a class="btn btn--plein" href="{book_target}">{t['book']}</a>
<button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{t['menu']}"><svg width="22" height="16" viewBox="0 0 22 16" aria-hidden="true"><path d="M0 1h22M0 8h22M0 15h22" stroke="currentColor" stroke-width="1.6"/></svg></button></div>
</div>
</header>
{sub}'''

def footer(lang, page):
    t = T[lang]; other = 'en' if lang == 'fr' else 'fr'
    L = 'color: #E9DED6; text-decoration: none;'
    H = 'font-size: 12px; letter-spacing: 0.28em; text-transform: uppercase; color: #D2A48C; margin-bottom: 6px;'
    links = ''.join(f'<a href="{url(n, lang)}" style="{L}">{lbl}</a>\n' for n, lbl in t['f_links'])
    legal = ''.join(f'<a href="{url(n, lang)}" style="color: #CDBFB6; text-decoration: none;">{lbl}</a>\n' for n, lbl in t['legal'])
    sw = ('<strong style="font-weight: 500;">FR</strong> · EN' if lang == 'fr' else 'FR · <strong style="font-weight: 500;">EN</strong>')
    return f'''<footer style="background: #3F2A3A; color: #E9DED6; font-size: 15px;">
<div style="max-width: 1280px; margin: 0 auto; padding: 80px 32px 40px; display: flex; flex-wrap: wrap; gap: 56px;">
<div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
<img src="/assets/logos/unaya-management-vertical-fonce.svg" alt="Unaya Management" style="width: 170px; height: auto; display: block;" loading="lazy">
<span style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 22px; color: #D2A48C;">Uniquely cared for.</span>
</div>
<div style="flex: 1 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
<div style="{H}">{t['f_nav']}</div>
{links}<a href="{PORTAL}" style="{L} margin-top: 6px; color: #D2A48C;">{t['portal']} ↗</a>
</div>
<div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
<div style="{H}">{t['f_contact']}</div>
<span>Jalan Balangan Hijau VI No. 15<br>Jimbaran, Kuta Selatan<br>Badung, Bali — {t['country']}</span>
<a href="mailto:info@unayabali.com" style="color: #E9DED6;">info@unayabali.com</a>
</div>
<div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
<div style="{H}">{t['f_company']}</div>
<span>PT Unaya Bali Grup</span>
<span>NIB 3009260021018</span>
<a href="{url('Investir', lang)}" style="color: #D2A48C; text-decoration: none;">{t['build']} →</a>
</div>
</div>
<div style="max-width: 1280px; margin: 0 auto; padding: 24px 32px 40px; border-top: 1px solid #5A3552; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 16px; font-size: 13px; color: #CDBFB6;">
<span>© 2026 PT Unaya Bali Grup</span>
<div style="display: flex; flex-wrap: wrap; gap: 24px;">
{legal}<a href="{url(page, other)}" hreflang="{other}" style="color: #CDBFB6; text-decoration: none;">{sw}</a>
</div>
</div>
</footer>'''

def slug(s):
    s = re.sub(r'[*()]', '', s).strip().lower()
    for a, b in [('é','e'),('è','e'),('ê','e'),('à','a'),('ç','c'),('ô','o'),('°','')]:
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '_', s).strip('_')[:40] or 'champ'

def fix_forms(body, lang, page):
    """Formulaires : noms de champs, envoi vers la fonction Cloudflare /api/form (Resend), anti-spam."""
    n = [0]
    def one(m):
        if 'data-beds24' in m.group(1) or 'data-wa' in m.group(1):  # bloc réservation : géré par site.js
            return m.group(0)
        n[0] += 1
        inner = m.group(2)
        inner = re.sub(r'(<label[^>]*>)([^<]+?)(<(?:input|select|textarea))', lambda k: f'{k.group(1)}{k.group(2)}{k.group(3)} name="{slug(k.group(2))}"', inner)
        inner = re.sub(r'<label style="display: flex; gap: 10px;[^"]*"><input type="checkbox"', lambda k: k.group(0) + ' name="consentement" required', inner)
        inner = inner.replace('<button type="button"', '<button type="submit"')
        inner = re.sub(r'(<(?:input|select)[^>]*?)(name="(?:nom|nom_complet|name|full_name|e_mail|email)")', r'\1\2 required', inner)
        fname = f'{page.lower()}-{lang}' + (f'-{n[0]}' if n[0] > 1 else '')
        return (f'<form name="{fname}" method="POST" action="/api/form"{m.group(1)}>'
                f'<input type="hidden" name="form-name" value="{fname}"><input type="hidden" name="lang" value="{lang}"><p class="hp"><label>Site web <input name="site_web" tabindex="-1" autocomplete="off"></label></p>' + inner + '</form>')
    return re.sub(r'<form([^>]*)>(.*?)</form>', one, body, flags=re.S)

def fix_booking(body, lang, page):
    propid = BEDS24[page]
    a = body.index('<aside id="reserver"'); b = body.index('</aside>', a) + len('</aside>')
    aside = body[a:b]
    I = "font-family: 'Jost', sans-serif; font-size: 16px; padding: 12px; border: 1px solid #A8705A; background: #F7F2EE; color: #2E2429; width: 100%;"
    L = "flex: 1 1 130px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: #D2A48C;"
    lab = dict(fr=('Arrivée','Départ','Voyageurs','Vérifier les disponibilités','voyageur','voyageurs'), en=('Check-in','Check-out','Guests','Check availability','guest','guests'))[lang]
    maxg = {'VillaSuma': 10, 'VillaYuga': 8, 'VillaRumahJambu': 4}[page]
    opts = ''.join(f'<option value="{g}"{" selected" if g == 2 else ""}>{g} {lab[4] if g == 1 else lab[5]}</option>' for g in range(1, maxg + 1))
    wa = BOOKING_MODE == 'whatsapp'
    if wa:
        lab = lab[:3] + (('Demander la disponibilité sur WhatsApp',) if lang == 'fr' else ('Ask for availability on WhatsApp',)) + lab[4:]
    vname = {'VillaSuma': 'Villa Suma', 'VillaYuga': 'Villa Yuga', 'VillaRumahJambu': 'Rumah Jambu'}[page]
    attr = f'data-wa="{WHATSAPP[page]}" data-villa="{vname}"' if wa else f'data-beds24="{propid}"'
    note = ''
    if wa:
        note = ('<p style="margin: 0; font-size: 14px; color: #E9DED6;">La réservation en ligne ouvre très bientôt. En attendant, envoyez-nous vos dates : nous vous répondons rapidement sur WhatsApp avec la disponibilité et le prix.</p>' if lang == 'fr'
                else '<p style="margin: 0; font-size: 14px; color: #E9DED6;">Online booking opens very soon. In the meantime, send us your dates: we reply quickly on WhatsApp with availability and price.</p>')
    form = (f'<form {attr} style="display: flex; flex-direction: column; gap: 16px;">' + note +
            f'<div style="display: flex; flex-wrap: wrap; gap: 12px;"><label style="{L}">{lab[0]}<input type="date" name="checkin" required style="{I}"></label>'
            f'<label style="{L}">{lab[1]}<input type="date" name="checkout" required style="{I}"></label></div>'
            f'<label style="{L}">{lab[2]}<select name="numadult" style="{I}">{opts}</select></label>'
            f'<button type="submit" style="font-family: \'Jost\', sans-serif; padding: 16px; background: #D2A48C; color: #3F2A3A; border: none; font-size: 14px; letter-spacing: 0.14em; text-transform: uppercase; font-weight: 500; cursor: pointer;">{lab[3]}</button></form>')
    i = aside.index('<div style="display: flex; flex-wrap: wrap; gap: 12px;">')
    j = aside.index('</button>', i) + len('</button>')
    aside = aside[:i] + form + aside[j:]
    if wa:
        aside = aside.replace('Calendrier synchronisé en temps réel (Beds24) · Paiement sécurisé', 'Réponse rapide sur WhatsApp · Sans engagement').replace('Real-time synchronised calendar (Beds24) · Secure payment', 'Quick reply on WhatsApp · No commitment')
    return body[:a] + aside + body[b:]

def transform(body, lang, page):
    body = body.replace('<a href="#">info@unayabali.com</a>', '<a href="mailto:info@unayabali.com">info@unayabali.com</a>')
    body = body.replace('<a href="#" style="font-size: 20px;">info@unayabali.com</a>', '<a href="mailto:info@unayabali.com" style="font-size: 20px;">info@unayabali.com</a>')
    if page == 'Main':
        body = body.replace('<!-- 5. ZONES -->\n<section ', '<!-- 5. ZONES -->\n<section id="zones" ', 1)
    if page in BEDS24:
        body = body.replace('<!-- GALERIE -->\n<section ', '<!-- GALERIE -->\n<section data-gallery ', 1)
        body = re.sub(r'<a href="#"( style="position: absolute;[^"]*")>', r'<a href="#" data-open-gallery\1>', body)
        body = fix_booking(body, lang, page)
    if '<form' in body:
        body = fix_forms(body, lang, page)
    # images : chargement différé sauf la première
    first = [True]
    def lazy(m):
        if first[0]: first[0] = False; return m.group(0)
        return m.group(0).replace('<img ', '<img loading="lazy" ', 1)
    body = re.sub(r'<img [^>]+>', lazy, body)
    return body

def layout(lang, page, title, desc, body):
    other = 'en' if lang == 'fr' else 'fr'
    canon = SITE + url(page, lang)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="{lang}" href="{canon}">
<link rel="alternate" hreflang="{other}" href="{SITE + url(page, other)}">
<link rel="alternate" hreflang="x-default" href="{SITE + url(page, 'en')}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/images/suma-piscine.jpg"><meta property="og:locale" content="{T[lang]['ogloc']}">
<link rel="icon" href="/assets/logos/symbole.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
</head>
<body>
{header(lang, page)}
<main id="contenu">
{body}
</main>
{footer(lang, page)}
<script src="/assets/js/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''

def build():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(DIST, 'assets'))
    urls = []
    for lang in ('fr', 'en'):
        d = os.path.join(SRC, 'pages', lang)
        for fn in sorted(os.listdir(d)):
            page = fn[:-5]
            raw = open(os.path.join(d, fn), encoding='utf-8').read()
            m = re.match(r'<!-- title: (.*?) -->\n', raw)
            title = m.group(1) if m else 'Unaya Management'
            body = raw[m.end():] if m else raw
            desc = DESC.get((lang, page)) or DESC[(lang, 'Main')]
            out = layout(lang, page, title, desc, transform(body, lang, page))
            path = os.path.join(DIST, url(page, lang).strip('/'), 'index.html')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w', encoding='utf-8').write(out)
            if page not in ('Merci','Paiement'): urls.append(SITE + url(page, lang))
    open(os.path.join(DIST, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(DIST, '_headers'), 'w').write('/assets/*\n  Cache-Control: public, max-age=604800\n')
    open(os.path.join(DIST, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    shutil.copy(os.path.join(SRC, '404.html'), os.path.join(DIST, '404.html')) if os.path.exists(os.path.join(SRC, '404.html')) else None
    print(f'{len(urls)} pages générées dans dist/')

if __name__ == '__main__':
    build()
