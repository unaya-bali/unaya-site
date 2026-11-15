#!/usr/bin/env python3
"""Génère le site Unaya Management dans le dossier dist/.

Utilisation :  python3 build.py
Les textes des pages sont dans src/pages/fr/ et src/pages/en/ (HTML).
L'en-tête, le menu et le pied de page sont définis ci-dessous, une seule fois pour tout le site.
"""
import json, os, re, json, shutil, html, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST = os.path.join(ROOT, 'src'), os.path.join(ROOT, 'dist')
SITE = 'https://unayabali.com'
ROUTES = json.load(open(os.path.join(SRC, 'routes.json'), encoding='utf-8'))
PORTAL = 'https://owners.unayabali.com'
# Réservation en ligne : 'beds24' (paiement Xendit actif via la passerelle Beds24) ou 'whatsapp' (demande de disponibilité)
BOOKING_MODE = 'beds24'
WHATSAPP = {'VillaSuma': '6285190211324', 'VillaYuga': '6281330617077', 'VillaRumahJambu': '6285190211324'}
# Cloudflare Turnstile (case anti-robot) : clé PUBLIQUE du widget (la clé secrète va dans Cloudflare, variable TURNSTILE_SECRET)
TURNSTILE_SITEKEY = '0x4AAAAAAFl92qPSywb2bEJt'
SOCIAL = {'instagram': 'https://www.instagram.com/unayabali/', 'linktree': 'https://linktr.ee/Unaya_Management'}
OWNER_PAGES = ['Proprietaires', 'ProprietairesServices', 'ProprietairesTarifs', 'ConfierMaVilla']
INVEST_PAGES = ['Investir', 'Terrains', 'TerrainMelasti', 'VillasAVendre', 'ArawaVillas']
INVEST_SUB = {'fr': [('Investir', 'Le guide pour investir'), ('VillasAVendre', 'Villas à vendre'), ('Terrains', 'Terrains disponibles')], 'en': [('Investir', 'Investment guide'), ('VillasAVendre', 'Villas for sale'), ('Terrains', 'Available land')]}
BEDS24 = {'VillaSuma': '359817', 'VillaYuga': '359816', 'VillaRumahJambu': '359818'}  # propriétés Unaya

T = {  # textes communs
 'fr': dict(nav=[('Proprietaires','Propriétaires'),('Villas','Nos villas'),('Investir','Investir à Bali'),('ServicesVoyageurs','Services voyageurs'),('APropos','À propos'),('Contact','Contact')],
            book='Réserver', owner='Confier ma villa', menu='Menu', skip='Aller au contenu', main_menu='Menu principal',
            sub=[('Proprietaires',"Vue d'ensemble"),('ProprietairesServices','Nos services'),('ProprietairesTarifs','Formules & tarifs'),('ConfierMaVilla','Confier ma villa')], sub_label='Propriétaires', portal='Espace propriétaire',
            f_nav='Navigation', f_contact='Contact', f_company='Société', f_links=[('Proprietaires','Propriétaires'),('Villas','Nos villas'),('Investir','Investir à Bali'),('VillasAVendre','Villas à vendre'),('Terrains','Terrains'),('ServicesVoyageurs','Services voyageurs'),('FAQ','FAQ'),('Contact','Contact')],
            legal=[('MentionsLegales','Mentions légales'),('Confidentialite','Confidentialité'),('Conditions','Conditions de réservation')],
            country='Indonésie', build='Unaya Build — Investir à Bali', ogloc='fr_FR'),
 'en': dict(nav=[('Proprietaires','Owners'),('Villas','Our villas'),('Investir','Invest in Bali'),('ServicesVoyageurs','Guest services'),('APropos','About'),('Contact','Contact')],
            book='Book', owner='List my villa', menu='Menu', skip='Skip to content', main_menu='Main menu',
            sub=[('Proprietaires','Overview'),('ProprietairesServices','Our services'),('ProprietairesTarifs','Plans & pricing'),('ConfierMaVilla','List my villa')], sub_label='Owners', portal='Owner portal',
            f_nav='Navigation', f_contact='Contact', f_company='Company', f_links=[('Proprietaires','Owners'),('Villas','Our villas'),('Investir','Invest in Bali'),('VillasAVendre','Villas for sale'),('Terrains','Land'),('ServicesVoyageurs','Guest services'),('FAQ','FAQ'),('Contact','Contact')],
            legal=[('MentionsLegales','Legal notice'),('Confidentialite','Privacy'),('Conditions','Booking terms')],
            country='Indonesia', build='Unaya Build — Invest in Bali', ogloc='en_US'),
}

DESC = {
 ('fr','Villas'):"Nos villas privées avec piscine à Bali : Villa Suma et Rumah Jambu à Uluwatu, Villa Yuga à Tanah Lot. Gérées par Unaya, réservation en direct.",
 ('en','Villas'):"Our private pool villas in Bali: Villa Suma and Rumah Jambu in Uluwatu, Villa Yuga in Tanah Lot. Managed by Unaya, book direct.",
 ('fr','SiteWeb'):"Un site web pour votre villa à Bali : plus de visibilité, une meilleure expérience voyageurs, un marketing rentable et plus de réservations directes. Inclus dans nos formules.",
 ('en','SiteWeb'):"A website for your Bali villa: more visibility, a better guest experience, cost-effective marketing and more direct bookings. Included in our plans.",
 ('fr','Terrains'):"Terrains à Bali sélectionnés et vérifiés par Unaya Build : titre foncier, zonage, accès. Bail ou PT PMA, construction et mise en location.",
('en','Terrains'):"Land in Bali selected and checked by Unaya Build: land title, zoning, access. Leasehold or PT PMA, construction and renting out.",
('fr','VillasAVendre'):"Villas à vendre à Bali choisies par Unaya : villas avec piscine à Uluwatu, en bail (leasehold), à habiter ou à louer, gestion locative possible.",
('en','VillasAVendre'):"Villas for sale in Bali chosen by Unaya: pool villas in Uluwatu, leasehold, to live in or rent out, with rental management available.",
('fr','ArawaVillas'):"Arawa Villas à Balangan, Uluwatu : 2 villas de 2 chambres avec piscine privée, livrées meublées fin décembre 2026, dès 170 000 USD en bail.",
('en','ArawaVillas'):"Arawa Villas in Balangan, Uluwatu: two 2-bedroom villas with private pool, handed over furnished end of December 2026, from USD 170,000 leasehold.",
('fr','TerrainMelasti'):"Terrain de 500 m² en zone rose à Melasti, Uluwatu : bail 30 ans + option 30 ans, titre SHM, à 5 min de la plage. IDR 3,15 milliards.",
('en','TerrainMelasti'):"500 m² pink-zone plot in Melasti, Uluwatu: 30-year lease + 30-year option, SHM title, 5 min from the beach. IDR 3.15 billion.",
 ('fr','Experiences'):"Unaya Experiences : excursions privées à Bali avec guide francophone ou chauffeur, départ de votre villa. 10 circuits à la journée, activités et calcul du prix en ligne.",
('en','Experiences'):"Unaya Experiences: private day trips in Bali with a French-speaking guide or a driver, from your villa. 10 day tours, activities and an online price calculator.",
 ('fr','Investir'):"Investir à Bali : bail ou PT PMA, acheter ou faire construire, taxes et location en règle. Unaya Build vous accompagne du terrain à la mise en location.",
 ('en','Investir'):"Investing in Bali: leasehold or PT PMA, buying or building, taxes and legal renting. Unaya Build supports you from the land to renting out your villa.",
 ('fr','Main'):"Unaya Bali gère votre villa : annonces, voyageurs, entretien, rapport mensuel, dès 18 % sans frais fixes. Et 3 villas avec piscine à louer à Uluwatu et Tanah Lot.",
 ('en','Main'):"Unaya Bali manages your villa: listings, guests, upkeep and a monthly report, from 18% with no fixed fees. Plus 3 pool villas for rent in Uluwatu and Tanah Lot.",
 ('fr','Contact'):"Contactez Unaya Bali sur WhatsApp (+62 851 9021 1324) ou par e-mail : gestion de villa, réservation ou service voyageur. Réponse sous 24 h, bureau à Jimbaran.",
 ('en','Contact'):"Contact Unaya Bali on WhatsApp (+62 851 9021 1324) or by email: villa management, bookings or guest services. Reply within 24 hours, office in Jimbaran.",
 ('fr','APropos'):"Unaya Bali, agence de gestion de villas à Jimbaran : peu de villas, suivies de près, une équipe sur place 7 j/7 et des comptes clairs chaque mois.",
 ('en','APropos'):"Unaya Bali, a boutique villa management agency in Jimbaran: fewer villas, closely managed, a team on the ground 7 days a week and clear monthly accounts.",
 ('fr','FAQ'):"Questions fréquentes sur la gestion de villa à Bali avec Unaya (commission, rapport, revenus) et sur la réservation de nos villas (acompte, annulation, arrivée).",
 ('en','FAQ'):"Frequently asked questions about villa management in Bali with Unaya (commission, reports, payouts) and booking our villas (deposit, cancellation, check-in).",
 ('fr','ServicesVoyageurs'):"Transfert aéroport, chauffeur privé, location de scooter livré à la villa et excursions à Bali : demande en une minute, confirmation sur WhatsApp.",
 ('en','ServicesVoyageurs'):"Airport transfer, private driver, scooter rental delivered to your villa and day trips in Bali: request in a minute, confirmed on WhatsApp.",
 ('fr','Conditions'):"Conditions de réservation des villas Unaya en direct : acompte de 30 %, solde 14 jours avant l'arrivée (30 en haute saison), annulation et règles de la maison.",
 ('en','Conditions'):"Booking terms for Unaya villas booked direct: 30% deposit, balance 14 days before arrival (30 in high season), cancellation and house rules.",
 ('fr','Confidentialite'):"Politique de confidentialité du site Unaya Bali : données collectées par les formulaires et les réservations, utilisation, conservation et vos droits.",
 ('en','Confidentialite'):"Unaya Bali privacy policy: data collected through forms and bookings, how it is used and stored, and your rights.",
 ('fr','MentionsLegales'):"Mentions légales du site unayabali.com, édité par PT Unaya Bali Grup (NIB 3009260021018), Jimbaran, Bali, Indonésie.",
 ('en','MentionsLegales'):"Legal notice for unayabali.com, published by PT Unaya Bali Grup (NIB 3009260021018), Jimbaran, Bali, Indonesia.",
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

def subnav(lang, page):
    t = T[lang]
    if page in INVEST_PAGES:
        cur = {'TerrainMelasti': 'Terrains', 'ArawaVillas': 'VillasAVendre'}.get(page, page)
        return f'<nav class="subnav" aria-label="{"Investir à Bali" if lang == "fr" else "Invest in Bali"}">' + ''.join(
            f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if n == cur else ""}>{lbl}</a>' for n, lbl in INVEST_SUB[lang]) + '</nav>'
    if page not in OWNER_PAGES: return ''
    return f'<nav class="subnav" aria-label="{t["sub_label"]}">' + ''.join(
        f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if n == page else ""}>{lbl}</a>' for n, lbl in t['sub']) + f'<a class="subnav-portal" href="{PORTAL}">{t["portal"]} ↗</a></nav>'

def with_subnav(body, lang, page):
    sn = subnav(lang, page)
    if not sn: return body
    b = body.lstrip()
    if b.startswith('<section class="u-hero'):
        i = b.index('</section>') + len('</section>')
        return b[:i] + '\n' + sn + b[i:]
    if page in INVEST_PAGES and '<section' in body:
        i = body.index('</section>', body.index('<section')) + len('</section>')
        return body[:i] + '\n' + sn + body[i:]
    return sn + '\n' + body

def header(lang, page):
    t = T[lang]; other = 'en' if lang == 'fr' else 'fr'
    nav = ''.join(f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if (n == page or (n == "Proprietaires" and page in OWNER_PAGES) or (n == "Investir" and page in INVEST_PAGES)) else ""}>{lbl}</a>' for n, lbl in t['nav'])
    langsw = (f'<a class="lang" href="{url(page, other)}" hreflang="{other}"><strong>FR</strong> · EN</a>' if lang == 'fr'
              else f'<a class="lang" href="{url(page, other)}" hreflang="{other}">FR · <strong>EN</strong></a>')
    return_sub = None
    sub = ''
    if page in OWNER_PAGES:
        sub = f'<nav class="subnav" aria-label="{t["sub_label"]}">' + ''.join(
            f'<a href="{url(n, lang)}"{" aria-current=\"page\"" if n == page else ""}>{lbl}</a>' for n, lbl in t['sub']) + f'<a class="subnav-portal" href="{PORTAL}">{t["portal"]} ↗</a></nav>'
    book_target = '#reserver' if page in BEDS24 else url('Villas', lang)
    return f'''<a class="skip" href="#contenu">{t['skip']}</a>
<header class="site-header">
<div class="site-header__in">
<a class="site-header__logo" href="{url('Main', lang)}"><img src="/assets/logos/unaya-management-horizontal.svg" alt="Unaya Management" width="176" height="40"></a>
<nav class="site-nav" id="site-nav" aria-label="{t['main_menu']}">{nav}<a class="nav-lang" href="{url(page, other)}" hreflang="{other}">{'English' if lang == 'fr' else 'Français'}</a></nav>
<div class="site-header__actions">{langsw}<a class="btn" href="{url('ConfierMaVilla', lang)}">{t['owner']}</a><a class="btn btn--plein" href="{book_target}">{t['book']}</a>
<button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{t['menu']}"><svg width="22" height="16" viewBox="0 0 22 16" aria-hidden="true"><path d="M0 1h22M0 8h22M0 15h22" stroke="currentColor" stroke-width="1.6"/></svg></button></div>
</div>
</header>
'''

def footer(lang, page):
    t = T[lang]; other = 'en' if lang == 'fr' else 'fr'
    L = 'color: #E9DED6; text-decoration: none;'
    H = 'font-size: 13px; letter-spacing: 0.28em; text-transform: uppercase; color: #D2A48C; margin-bottom: 6px;'
    links = ''.join(f'<a href="{url(n, lang)}" style="{L}">{lbl}</a>\n' for n, lbl in t['f_links'])
    legal = ''.join(f'<a href="{url(n, lang)}" style="color: #CDBFB6; text-decoration: none;">{lbl}</a>\n' for n, lbl in t['legal'])
    sw = ('<strong style="font-weight: 500;">FR</strong> · EN' if lang == 'fr' else 'FR · <strong style="font-weight: 500;">EN</strong>')
    return f'''<footer style="background: #3F2A3A; color: #E9DED6; font-size: 15px;">
<div style="max-width: 1280px; margin: 0 auto; padding: 80px 32px 40px; display: flex; flex-wrap: wrap; gap: 56px;">
<div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
<img src="/assets/logos/unaya-management-vertical-fonce.svg" alt="Unaya Management" style="width: 170px; height: auto; display: block;" loading="lazy">
<span style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 22px; color: #D2A48C;">Uniquely cared for.</span>
<div class="f-social"><a href="{SOCIAL['instagram']}" target="_blank" rel="noopener" aria-label="Instagram Unaya"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg><span>@unayabali</span></a><a href="{SOCIAL['linktree']}" target="_blank" rel="noopener" aria-label="Linktree Unaya"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 3v18M5 8l7-5 7 5M5 14h14M7 19h10"/></svg><span>Linktree</span></a></div>
</div>
<div style="flex: 1 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
<div style="{H}">{t['f_nav']}</div>
{links}<a href="{PORTAL}" style="{L} margin-top: 6px; color: #D2A48C;">{t['portal']} ↗</a>
</div>
<div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
<div style="{H}">{t['f_contact']}</div>
<span>Jalan Balangan Hijau VI No. 15<br>Jimbaran, Kuta Selatan<br>Badung, Bali — {t['country']}</span>
<a href="{wa_url(lang, page)}" target="_blank" rel="noopener" style="color: #E9DED6;">WhatsApp {WA_SHOW}</a>
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
        if TURNSTILE_SITEKEY:
            ts = f'<div class="cf-turnstile" data-sitekey="{TURNSTILE_SITEKEY}" data-language="{lang}" data-theme="light" style="margin:4px 0"></div>'
            k = inner.rfind('<button type="submit"')
            inner = inner[:k] + ts + inner[k:] if k >= 0 else inner + ts
        fname = f'{page.lower()}-{lang}' + (f'-{n[0]}' if n[0] > 1 else '')
        return (f'<form name="{fname}" method="POST" action="/api/form"{m.group(1)}>'
                f'<input type="hidden" name="form-name" value="{fname}"><input type="hidden" name="lang" value="{lang}"><p class="hp"><label>Site web <input name="site_web" tabindex="-1" autocomplete="off"></label></p>' + inner + '</form>')
    return re.sub(r'<form([^>]*)>(.*?)</form>', one, body, flags=re.S)

def fix_booking(body, lang, page):
    propid = BEDS24[page]
    a = body.index('<aside id="reserver"'); b = body.index('</aside>', a) + len('</aside>')
    aside = body[a:b]
    # Prix « à partir de » mis à jour automatiquement depuis Beds24 (/api/prices, voir assets/js/site.js)
    aside = aside.replace('<aside id="reserver"', f'<aside id="reserver" data-prices="{page}"', 1)
    aside = aside.replace("<span style=\"font-family: 'Cormorant Garamond', serif; font-size: 40px;", "<span data-price=\"villa\" style=\"font-family: 'Cormorant Garamond', serif; font-size: 40px;", 1)
    aside = aside.replace("<span style=\"font-family: 'Cormorant Garamond', serif; font-size: 30px;", "<span data-price=\"room\" style=\"font-family: 'Cormorant Garamond', serif; font-size: 30px;", 1)
    I = "font-family: 'Jost', sans-serif; font-size: 16px; padding: 12px; border: 1px solid #A8705A; background: #F7F2EE; color: #2E2429; width: 100%;"
    L = "flex: 1 1 130px; display: flex; flex-direction: column; gap: 6px; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: #D2A48C;"
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
    if not wa:
        aside = aside.replace('Calendrier synchronisé en temps réel (Beds24) · Paiement sécurisé', 'Paiement sécurisé · Acompte 30 % à la réservation, solde 14 jours avant l\'arrivée (<a href="/fr/conditions-reservation/" style="color: inherit;">conditions</a>)').replace('Real-time synchronised calendar (Beds24) · Secure payment', 'Secure payment · 30% deposit at booking, balance 14 days before arrival (<a href="/booking-terms/" style="color: inherit;">terms</a>)')
    if wa:
        aside = aside.replace('Calendrier synchronisé en temps réel (Beds24) · Paiement sécurisé', 'Réponse rapide sur WhatsApp · Sans engagement').replace('Real-time synchronised calendar (Beds24) · Secure payment', 'Quick reply on WhatsApp · No commitment')
    return body[:a] + aside + body[b:]


# ---- Conversion (15/11/2026) : WhatsApp partout, barre de réservation mobile, villas sur l'accueil ----
WA_MAIN = '6285190211324'
WA_SHOW = '+62 851 9021 1324'
VNAME = {'VillaSuma': 'Villa Suma', 'VillaYuga': 'Villa Yuga', 'VillaRumahJambu': 'Rumah Jambu'}
PRICE0 = {'VillaSuma': 5800000, 'VillaYuga': 2900000, 'VillaRumahJambu': 1200000}  # repli si /api/prices ne répond pas
def wa_text(lang, page):
    fr = lang == 'fr'
    if page in VNAME:
        return (f"Bonjour Unaya, je suis intéressé(e) par {'la ' if page != 'VillaRumahJambu' else ''}{VNAME[page]}. Mes dates : " if fr else f"Hello Unaya, I'm interested in {VNAME[page]}. My dates: ")
    if page in ('VillasAVendre', 'ArawaVillas'):
        return ("Bonjour Unaya, je suis intéressé(e) par les Arawa Villas à Balangan." if fr else "Hello Unaya, I'm interested in Arawa Villas in Balangan.")
    if page in ('Terrains', 'TerrainMelasti'):
        return ("Bonjour Unaya, je souhaite des informations sur le terrain de Melasti." if fr else "Hello Unaya, I'd like information about the Melasti land.")
    if page in OWNER_PAGES or page == 'Investir':
        return ("Bonjour Unaya, je souhaite des informations sur la gestion de ma villa." if fr else "Hello Unaya, I'd like information about managing my villa.")
    if page in ('ServicesVoyageurs', 'Experiences'):
        return ("Bonjour Unaya, je voudrais réserver un service pendant mon séjour : " if fr else "Hello Unaya, I'd like to book a service during my stay: ")
    if page == 'Villas':
        return ("Bonjour Unaya, je cherche une villa. Mes dates : " if fr else "Hello Unaya, I'm looking for a villa. My dates: ")
    return ("Bonjour Unaya, " if fr else "Hello Unaya, ")
def wa_url(lang, page):
    from urllib.parse import quote
    return f'https://wa.me/{WA_MAIN}?text={quote(wa_text(lang, page))}'
WA_SVG = '<svg width="26" height="26" viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3Zm0 23.6c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6Zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.5 6.5 0 0 0 1.3 3.4 14.6 14.6 0 0 0 5.6 5c2.1.9 2.9 1 4 .8.6-.1 1.9-.8 2.2-1.5s.3-1.4.2-1.5-.3-.2-.6-.4Z"/></svg>'
def wa_float(lang, page):
    if page in ('Merci', 'Paiement'):
        return ''
    lbl = 'Écrire sur WhatsApp' if lang == 'fr' else 'Chat on WhatsApp'
    return f'<a class="wa-float{" wa-float--bar" if page in BEDS24 else ""}" href="{wa_url(lang, page)}" target="_blank" rel="noopener" aria-label="{lbl}">{WA_SVG}<span>WhatsApp</span></a>'
def fmt_idr(n, lang):
    return 'IDR ' + (f'{n:,}'.replace(',', ' ') if lang == 'fr' else f'{n:,}')
def bk_bar(lang, page):
    if page not in BEDS24:
        return ''
    fr = lang == 'fr'
    return (f'<div class="bk-bar" data-prices="{page}" aria-hidden="false"><div class="bk-bar__p"><small>{"À partir de" if fr else "From"}</small>'
            f'<strong data-price="villa">{fmt_idr(PRICE0[page], lang)}</strong><small>{"/ nuit · villa entière" if fr else "/ night · entire villa"}</small></div>'
            f'<a class="bk-bar__b" href="#reserver">{"Disponibilités" if fr else "Availability"}</a></div>')
def villa_cards(lang):
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'pages', lang, 'Villas.html'), encoding='utf-8').read()
    cards = re.findall(r'<a class="vl-card".*?</a>', src, flags=re.S)
    return [add_price(c, lang) for c in cards]
def add_price(card, lang):
    m = re.search(r'href="[^"]*/(suma|yuga|rumah-jambu)/"', card)
    if not m:
        return card
    page = {'suma': 'VillaSuma', 'yuga': 'VillaYuga', 'rumah-jambu': 'VillaRumahJambu'}[m.group(1)]
    fr = lang == 'fr'
    price = (f'<span class="vl-card__price" data-prices="{page}">{"À partir de" if fr else "From"} <strong data-price="villa">{fmt_idr(PRICE0[page], lang)}</strong> {"/ nuit" if fr else "/ night"}</span>')
    return card.replace('<p>', price + '<p>', 1)
def home_villas(lang):
    fr = lang == 'fr'
    cards = ''.join(villa_cards(lang))
    h = 'Nos villas' if fr else 'Our villas'
    sub = ('Réservez en direct sur notre site : −15 % dès 7 nuits, −20 % dès 28 nuits.' if fr else 'Book direct on our website: −15% from 7 nights, −20% from 28 nights.')
    more = ('Voir toutes les villas' if fr else 'See all villas')
    return (f'<section class="u-sec h-villas" id="villas"><div class="u-wrap"><div class="u-head"><h2>{h}</h2><p>{sub}</p></div>'
            f'<div class="vl-grid">{cards}</div><p style="margin:28px 0 0"><a class="u-link" href="{url("Villas", lang)}">{more}</a></p></div></section>\n')
def contact_wa(lang):
    fr = lang == 'fr'
    return (f'<div class="c-item c-item--wa"><span class="c-wa-ic">{WA_SVG}</span><div><strong>WhatsApp</strong><span><a href="{wa_url(lang, "Contact")}" target="_blank" rel="noopener">{WA_SHOW}</a><br>'
            f'{"Le plus rapide : réponse en général dans l’heure, de 8 h à 20 h." if fr else "The fastest way: we usually reply within the hour, 8 am to 8 pm."}</span></div></div>')

# ---- Photos allégées (15/11/2026) : WebP en 800 / 1200 / 1600 px (générées par tools/webp.py) ----
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'images')
def _variants(name):
    return [w for w in (800, 1200, 1600) if os.path.exists(os.path.join(IMG_DIR, f'{name}-{w}.webp'))]
def webpify(page_html):
    def srcset(name, ws):
        return ', '.join(f'/assets/images/{name}-{w}.webp {w}w' for w in ws)
    def img(m):
        tag = m.group(0); name = m.group(1); ws = _variants(name)
        if not ws or 'srcset=' in tag:
            return tag
        full = 'fetchpriority="high"' in tag
        sizes = '100vw' if full else '(max-width: 640px) 100vw, (max-width: 1100px) 50vw, 720px'
        mid = 1200 if 1200 in ws else ws[-1]
        tag = tag.replace(f'src="/assets/images/{name}.jpg"', f'src="/assets/images/{name}-{mid}.webp" srcset="{srcset(name, ws)}" sizes="{sizes}" data-full="/assets/images/{name}-{ws[-1]}.webp"', 1)
        return tag
    page_html = re.sub(r'<img [^>]*src="/assets/images/([a-z0-9-]+)\.jpg"[^>]*>', img, page_html)
    def source(m):
        media, name = m.group(1), m.group(2); ws = _variants(name)
        return f'<source media="{media}" srcset="{srcset(name, ws)}" sizes="100vw">' if ws else m.group(0)
    page_html = re.sub(r'<source media="([^"]*)" srcset="/assets/images/([a-z0-9-]+)\.jpg">', source, page_html)
    return page_html

def fill_alts(body, lang):
    """Images sans description : on reprend le titre le plus proche qui suit (carte, circuit, section)."""
    def one(m):
        tag = m.group(0)
        after = body[m.end():m.end() + 2500]
        h = re.search(r'<(h1|h2|h3|strong)[^>]*>(.*?)</\1>', after, flags=re.S)
        if h and h.group(1) in ('h1', 'h2'):  # image de fond d'une section : décorative, on la laisse vide
            return tag
        if not h:
            return tag
        txt = html.unescape(re.sub(r'<[^>]+>', ' ', h.group(2)))
        txt = re.sub(r'\s+', ' ', txt).strip()[:110]
        if not txt:
            return tag
        return tag.replace('alt=""', f'alt="{html.escape(txt)}"', 1)
    return re.sub(r'<img [^>]*alt=""[^>]*>', one, body)

# Chiffres réels (Beds24, réservations confirmées, calculés le 15/11/2026) — à mettre à jour de temps en temps
STATS = dict(guests='263', countries='22', booking='9,8', since=('juillet 2026', 'July 2026'))
def stats_band(lang):
    fr = lang == 'fr'
    items = [(STATS['guests'], f"voyageurs accueillis depuis {STATS['since'][0]}" if fr else f"guests welcomed since {STATS['since'][1]}"),
             (STATS['countries'], 'nationalités' if fr else 'nationalities'),
             ((STATS['booking'] if fr else STATS['booking'].replace(',', '.')) + '/10', 'sur Booking.com' if fr else 'on Booking.com')]
    li = ''.join(f'<div class="st-i"><strong>{n}</strong><span>{t}</span></div>' for n, t in items)
    return f'<section class="st-band" aria-label="{"Unaya en chiffres" if fr else "Unaya in numbers"}"><div class="st-in">{li}</div></section>\n'

def transform(body, lang, page):
    body = body.replace('<a href="#">info@unayabali.com</a>', '<a href="mailto:info@unayabali.com">info@unayabali.com</a>')
    body = body.replace('<a href="#" style="font-size: 20px;">info@unayabali.com</a>', '<a href="mailto:info@unayabali.com" style="font-size: 20px;">info@unayabali.com</a>')
    if page == 'Main':
        body = body.replace('<!-- 5. ZONES -->\n<section ', '<!-- 5. ZONES -->\n<section id="zones" ', 1)
        alt = 'La Villa Suma et sa piscine éclairée à la tombée de la nuit, Balangan Uluwatu' if lang == 'fr' else 'Villa Suma and its lit pool at dusk, Balangan Uluwatu'
        body = body.replace('<div class="h-home__arch"><img src="/assets/logos/unaya-management-vertical-fonce.svg" alt="Unaya Management"></div>',
                            f'<div class="h-home__arch h-home__arch--photo"><img src="/assets/images/suma-g1.jpg" alt="{alt}" fetchpriority="high"></div>', 1)
        imgs = re.findall(r'<span class="h-door__img"><img src="https://images\.unsplash\.com[^"]*"', body)
        for old, new in zip(imgs, ['/assets/images/yuga-drone.jpg', '/assets/images/suma-piscine-2.jpg']):
            body = body.replace(old, '<span class="h-door__img"><img src="' + new + '"', 1)
        i = body.index('class="h-doors"'); j = body.index('</section>', i) + len('</section>')
        body = body[:j] + '\n' + home_villas(lang) + body[j:]
    if page in ('Main', 'Proprietaires'):
        j = body.index('</section>') + len('</section>')
        body = body[:j] + '\n' + stats_band(lang) + body[j:]
    if page == 'Villas':
        body = re.sub(r'<a class="vl-card".*?</a>', lambda m: add_price(m.group(0), lang), body, flags=re.S)
    if page == 'Contact':
        body = body.replace('<div class="c-side"><div class="c-item">', '<div class="c-side">' + contact_wa(lang) + '<div class="c-item">', 1)
    if page in BEDS24:
        body = body.replace('<!-- GALERIE -->\n<section ', '<!-- GALERIE -->\n<section data-gallery ', 1)
        body = re.sub(r'<a href="#"( style="position: absolute;[^"]*")>', r'<a href="#" data-open-gallery\1>', body)
        body = fix_booking(body, lang, page)
    if '<form' in body:
        body = fix_forms(body, lang, page)
    body = fill_alts(body, lang)
    # images : chargement différé sauf la première
    first = [True]
    def lazy(m):
        if first[0]: first[0] = False; return m.group(0)
        return m.group(0).replace('<img ', '<img loading="lazy" ', 1)
    body = re.sub(r'<img [^>]+>', lazy, body)
    return body

# ---- SEO (14/11/2026) ----
GOOGLE_VERIFY = ''  # code « google-site-verification » de la Search Console (méthode « balise HTML »), si utilisé
SEO_TITLES = {
 ('fr','Main'): 'Unaya Bali — Gestion de villas et locations de vacances à Bali',
 ('en','Main'): 'Unaya Bali — Villa Management & Holiday Villas in Bali',
 ('fr','Villas'): 'Villas à louer à Bali avec piscine (Uluwatu, Tanah Lot) — Unaya Bali',
 ('en','Villas'): 'Private Pool Villas for Rent in Bali (Uluwatu, Tanah Lot) — Unaya Bali',
 ('fr','VillaSuma'): 'Villa Suma, Balangan Uluwatu — villa 5 chambres avec piscine | Unaya Bali',
 ('en','VillaSuma'): 'Villa Suma, Balangan Uluwatu — 5-Bedroom Pool Villa | Unaya Bali',
 ('fr','VillaYuga'): 'Villa Yuga, Nyanyi Tanah Lot — villa 4 chambres avec piscine | Unaya Bali',
 ('en','VillaYuga'): 'Villa Yuga, Nyanyi Tanah Lot — 4-Bedroom Pool Villa | Unaya Bali',
 ('fr','VillaRumahJambu'): 'Rumah Jambu, Uluwatu — maison balinaise avec jardin | Unaya Bali',
 ('en','VillaRumahJambu'): 'Rumah Jambu, Uluwatu — Authentic Balinese House | Unaya Bali',
 ('fr','Proprietaires'): 'Gestion locative de villa à Bali — Unaya Bali',
 ('en','Proprietaires'): 'Bali Villa Management for Owners — Unaya Bali',
 ('fr','ProprietairesTarifs'): 'Tarifs gestion de villa à Bali, commission dès 18 % — Unaya Bali',
 ('en','ProprietairesTarifs'): 'Bali Villa Management Fees, Commission from 18% — Unaya Bali',
 ('fr','ProprietairesServices'): 'Services de gestion de villa à Bali — Unaya Bali',
 ('en','ProprietairesServices'): 'Bali Villa Management Services — Unaya Bali',
 ('fr','ConfierMaVilla'): 'Confier ma villa en gestion à Bali — Unaya Bali',
 ('en','ConfierMaVilla'): 'List Your Villa for Management in Bali — Unaya Bali',
 ('fr','Investir'): 'Investir dans une villa à Bali : le guide — Unaya Bali',
 ('en','Investir'): 'Investing in a Villa in Bali: the Guide — Unaya Bali',
 ('fr','Terrains'): 'Terrains à Bali (bail, zone rose) — Unaya Bali',
 ('en','Terrains'): 'Land for Lease in Bali (Pink Zone) — Unaya Bali',
 ('fr','ServicesVoyageurs'): 'Transfert aéroport, chauffeur et scooter à Bali — Unaya Bali',
 ('en','ServicesVoyageurs'): 'Bali Airport Transfer, Private Driver & Scooter Rental — Unaya Bali',
 ('fr','Experiences'): 'Excursions privées à Bali avec guide francophone — Unaya Experiences',
 ('en','Experiences'): 'Private Day Trips in Bali with a Guide or Driver — Unaya Experiences',
 ('fr','APropos'): 'À propos — Unaya Bali, gestion de villas à Uluwatu',
 ('en','APropos'): 'About Us — Unaya Bali, Villa Management in Uluwatu',
 ('fr','Contact'): 'Contact — Unaya Bali, gestion de villas à Jimbaran, Bali',
 ('en','Contact'): 'Contact Unaya Bali — Villa Management in Jimbaran, Bali',
 ('fr','FAQ'): 'Questions fréquentes — gestion et location de villas | Unaya Bali',
 ('en','FAQ'): 'FAQ — Villa Management & Villa Rentals in Bali | Unaya Bali',
 ('fr','TerrainMelasti'): 'Terrain de 500 m² à Melasti, Uluwatu (bail de 30 ans) — Unaya Bali',
 ('en','TerrainMelasti'): '500 m² Land in Melasti, Uluwatu (30-Year Lease) — Unaya Bali',
}
ORG_ID = SITE + '/#organisation'
LODGING = {
 'VillaSuma': dict(name='Villa Suma', loc='Balangan, Uluwatu', img='suma-g1.jpg', rooms=5, guests=10),
 'VillaYuga': dict(name='Villa Yuga', loc='Nyanyi, Tanah Lot', img='yuga-g1.jpg', rooms=4, guests=8),
 'VillaRumahJambu': dict(name='Rumah Jambu', loc='Balangan, Uluwatu', img='rj-g1.jpg', rooms=2, guests=4),
}
PARENT = {'VillaSuma':'Villas','VillaYuga':'Villas','VillaRumahJambu':'Villas','TerrainMelasti':'Terrains','ArawaVillas':'VillasAVendre',
          'ProprietairesServices':'Proprietaires','ProprietairesTarifs':'Proprietaires','ConfierMaVilla':'Proprietaires','SiteWeb':'Proprietaires'}

def jsonld(lang, page, title, body):
    canon = SITE + url(page, lang)
    org = {'@type': 'Organization', '@id': ORG_ID, 'name': 'Unaya Management', 'alternateName': ['Unaya Bali', 'Unaya', 'PT Unaya Bali Grup'],
           'url': SITE + '/', 'logo': SITE + '/assets/images/og-unaya.jpg', 'email': 'info@unayabali.com', 'telephone': '+62 851 9021 1324',
           'address': {'@type': 'PostalAddress', 'streetAddress': 'Jalan Balangan Hijau VI No. 15', 'addressLocality': 'Jimbaran, Kuta Selatan', 'addressRegion': 'Bali', 'addressCountry': 'ID'},
           'areaServed': 'Bali, Indonesia', 'sameAs': [SOCIAL['instagram'], SOCIAL['linktree'], 'https://www.instagram.com/yuga_nyanyi_bali/', 'https://www.instagram.com/suma_bali_/']}
    graph = [org, {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Unaya Bali', 'alternateName': 'Unaya Management', 'publisher': {'@id': ORG_ID}, 'inLanguage': ['fr', 'en']}]
    if page in LODGING:
        v = LODGING[page]
        graph.append({'@type': 'LodgingBusiness', '@id': canon + '#villa', 'name': v['name'], 'url': canon, 'image': SITE + '/assets/images/' + v['img'],
                      'description': DESC.get((lang, page), ''), 'address': {'@type': 'PostalAddress', 'addressLocality': v['loc'], 'addressRegion': 'Bali', 'addressCountry': 'ID'},
                      'numberOfRooms': v['rooms'], 'petsAllowed': page == 'VillaRumahJambu', 'checkinTime': '14:00', 'checkoutTime': '11:00',
                      'amenityFeature': [{'@type': 'LocationFeatureSpecification', 'name': n, 'value': True} for n in ('Private pool', 'Wi-Fi', 'Air conditioning', 'Kitchen', 'Free parking')],
                      'telephone': '+62 851 9021 1324', 'priceRange': 'IDR', 'parentOrganization': {'@id': ORG_ID}})
    if page == 'FAQ':
        qa = re.findall(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>', body, re.S)
        clean = lambda x: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(x))).strip()
        if qa: graph.append({'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': clean(q), 'acceptedAnswer': {'@type': 'Answer', 'text': clean(a)}} for q, a in qa]})
    if page != 'Main':
        home = T[lang]['nav'] and ('Accueil' if lang == 'fr' else 'Home')
        items = [(home, SITE + url('Main', lang))]
        if page in PARENT: items.append((dict(T[lang]['nav']).get(PARENT[page]) or PARENT[page], SITE + url(PARENT[page], lang)))
        items.append((title.split(' — ')[0].split(' | ')[0], canon))
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]})
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def layout(lang, page, title, desc, body):
    other = 'en' if lang == 'fr' else 'fr'
    canon = SITE + url(page, lang)
    return webpify(_layout(lang, page, title, desc, body))

def _layout(lang, page, title, desc, body):
    other = 'en' if lang == 'fr' else 'fr'
    canon = SITE + url(page, lang)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">{'<meta name="robots" content="noindex">' if page in ('Merci','Paiement') else ''}{f'<meta name="google-site-verification" content="{GOOGLE_VERIFY}">' if GOOGLE_VERIFY else ''}
<link rel="alternate" hreflang="{lang}" href="{canon}">
<link rel="alternate" hreflang="{other}" href="{SITE + url(page, other)}">
<link rel="alternate" hreflang="x-default" href="{SITE + url(page, 'en')}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/images/og-unaya.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Unaya Management"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}/assets/images/og-unaya.jpg"><meta property="og:locale" content="{T[lang]['ogloc']}">
<meta name="color-scheme" content="only light">
<link rel="icon" href="/assets/logos/symbole.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/jost-v20-latin-regular.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/cormorant-garamond-v21-latin-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
{jsonld(lang, page, title, body)}
</head>
<body>
{header(lang, page)}
<main id="contenu">
{with_subnav(body, lang, page)}
</main>
{footer(lang, page)}
{bk_bar(lang, page)}{wa_float(lang, page)}
<script src="/assets/js/site.js?v={ASSET_V}" defer></script>{'<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>' if TURNSTILE_SITEKEY and 'cf-turnstile' in body else ''}
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
            title = SEO_TITLES.get((lang, page)) or title.replace('— Unaya Management', '— Unaya Bali')
            body = raw[m.end():] if m else raw
            desc = DESC.get((lang, page)) or DESC[(lang, 'Main')]
            out = layout(lang, page, title, desc, transform(body, lang, page))
            path = os.path.join(DIST, url(page, lang).strip('/'), 'index.html')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w', encoding='utf-8').write(out)
            if page not in ('Merci','Paiement'): urls.append((SITE + url(page, lang), SITE + url(page, 'fr'), SITE + url(page, 'en')))
    today = __import__('datetime').date.today().isoformat()
    open(os.path.join(DIST, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{today}</lastmod><xhtml:link rel="alternate" hreflang="fr" href="{fr}"/><xhtml:link rel="alternate" hreflang="en" href="{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{en}"/></url>\n' for u, fr, en in urls) + '</urlset>\n')
    open(os.path.join(DIST, '_headers'), 'w').write('/assets/*\n  Cache-Control: public, max-age=604800\n')
    open(os.path.join(DIST, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    shutil.copy(os.path.join(SRC, '404.html'), os.path.join(DIST, '404.html')) if os.path.exists(os.path.join(SRC, '404.html')) else None
    print(f'{len(urls)} pages générées dans dist/')

if __name__ == '__main__':
    build()
