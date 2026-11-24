# Page « Formules & tarifs » (propriétaires, FR/EN), version visuelle : grande photo, 2 formules
# (✓ / ✕ groupés), calcul de la commission en barre, simulateur (repris de l'accueil), rendement,
# bon à savoir, appel final. Textes et icônes repris de Tar_old_{lang}.html (sauvegarde du 15/11/2026).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', 'src', 'pages'))
import home  # noqa: E402

def f(n, fr):
    s = f'{n:,.0f}'
    return s.replace(',', ' ') if fr else s

X = {
 'fr': dict(
  title='Formules & tarifs — Unaya Management', kick='Propriétaires · Formules & tarifs',
  b1=('Choisir ma formule', '#formules'), b2=('Demander une estimation', '/fr/proprietaires/confier-ma-villa/'),
  badges=['Aucun frais fixe', 'Sans abonnement', 'Commission après plateformes et taxe'],
  pl_h='Deux formules, une seule logique', pl_p='Nous sommes payés quand votre villa est louée. Rien d’autre.',
  groups=('Marketing et suivi', 'Sur place'), pop='Le plus choisi',
  calc_h='Comment se calcule la commission ?', calc_p='Sur l’argent qui arrive vraiment chez vous : après les plateformes et la taxe d’hébergement. Exemple pour IDR 10 000 000 de réservations.',
  calc=dict(gross='Réservations', plat='Plateformes ≈ 15 %', pbjt='Taxe PBJT 10 % (incluse)', base='Base de calcul', com='Notre commission', you='Pour la villa et vous', s_plat='Plateformes', s_pbjt='PBJT', s_com='Unaya', s_you='Pour la villa et vous'),
  calc_note='Exemple illustratif : la commission des plateformes varie selon le canal (0 % en réservation directe sur unayabali.com). Les charges de la villa (personnel, énergie, entretien) sont payées sur la part « pour la villa et vous ».',
  why_k='Pour votre rendement', ok_h='Bon à savoir',
  cta_h='Combien peut rapporter votre villa ?', cta_p='Demandez votre estimation de revenus gratuite. Réponse sous 24 h.', cta_b=('Demander une estimation', '/fr/proprietaires/confier-ma-villa/'),
 ),
 'en': dict(
  title='Plans & pricing — Unaya Management', kick='Owners · Plans & pricing',
  b1=('Choose my plan', '#formules'), b2=('Get an estimate', '/owners/list-your-villa/'),
  badges=['No fixed fees', 'No subscription', 'Commission after platforms and tax'],
  pl_h='Two plans, one logic', pl_p='We get paid when your villa is booked. Nothing else.',
  groups=('Marketing and tracking', 'On site'), pop='Most popular',
  calc_h='How is the commission calculated?', calc_p='On the money that actually reaches you: after platform fees and accommodation tax. Example for IDR 10,000,000 of bookings.',
  calc=dict(gross='Bookings', plat='Platforms ≈ 15%', pbjt='PBJT tax 10% (included)', base='Commission base', com='Our commission', you='For the villa and you', s_plat='Platforms', s_pbjt='PBJT', s_com='Unaya', s_you='For the villa and you'),
  calc_note='Illustrative example: platform commission varies by channel (0% for direct bookings on unayabali.com). Villa running costs (staff, energy, maintenance) are paid from the “villa and you” share.',
  why_k='For your returns', ok_h='Good to know',
  cta_h='How much could your villa earn?', cta_p='Request your free income estimate. Reply within 24 hours.', cta_b=('Get an estimate', '/owners/list-your-villa/'),
 ),
}

def m1(v, fr):
    t = f'{v / 1e6:.1f}'
    return (t.replace('.', ',') + ' M') if fr else (t + 'M')

def size(svg, n):
    return re.sub(r'width="\d+" height="\d+"', f'width="{n}" height="{n}"', svg, count=1)

def page(lang):
    x, fr = X[lang], lang == 'fr'
    old = open(os.path.join(HERE, f'Tar_old_{lang}.html')).read()
    h1 = re.search(r'<h1>(.*?)</h1>', old).group(1)
    sub = re.search(r'<p class="u-hero__sub">(.*?)</p>', old).group(1)
    cards = re.findall(r'<div class="p-card[^"]*"><div class="p-card__h"><h3>(.*?)</h3><p>(.*?)</p></div><div class="p-card__pct"><small>(.*?)</small><strong>(\d+)<sup>%</sup></strong><span>(.*?)</span></div><ul>(.*?)</ul><p class="p-card__note">(.*?)</p><div class="p-card__btn"><a class="[^"]*" href="([^"]+)">(.*?)</a>', old, flags=re.S)
    why_h = re.search(r'<div class="p-why"><div class="u-head u-head--c"><h2>(.*?)</h2>', old).group(1)
    why = re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', old.split('<div class="p-why">')[1].split('</section>')[0], flags=re.S)
    ok = re.findall(r'<div class="u-feat">(<svg.*?</svg>)<h3>(.*?)</h3><p>(.*?)</p></div>', old.split('u-feats--4')[1], flags=re.S)
    s = f'<!-- title: {x["title"]} -->\n<div class="hm">\n'
    s += (f'<section class="hm-hero hm-hero--sm"><img src="/assets/images/suma-terrasse.jpg" alt="{"La terrasse de SUMA Bali, Balangan Uluwatu" if fr else "SUMA Bali terrace, Balangan Uluwatu"}" fetchpriority="high">'
          f'<div class="hm-hero__in"><p class="hm-hero__k">{x["kick"]}</p><h1>{h1}</h1><p class="hm-hero__sub">{sub}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["b1"][1]}">{x["b1"][0]}</a><a class="u-btn hm-btn--glass" href="{x["b2"][1]}">{x["b2"][0]}</a></div>'
          '<ul class="hm-badges">' + ''.join(f'<li><span aria-hidden="true">✓</span>{b}</li>' for b in x['badges']) + '</ul></div></section>\n')
    # Formules
    s += f'<section class="u-sec hm-sec" id="formules"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["pl_h"]}</h2><p>{x["pl_p"]}</p></div><div class="pr-cards">'
    for i, (name, tag, frm, pct, of, ul, note, href, btn) in enumerate(cards):
        items = re.findall(r'<li( class=no)?><svg.*?</svg><span>(.*?)</span></li>', ul, flags=re.S)
        def grp(lst):
            return '<ul>' + ''.join(f'<li class="{"is-no" if no else "is-ok"}">{t}</li>' for no, t in lst) + '</ul>'
        pop = i == 0
        s += (f'<article class="pr-card{" pr-card--pop" if pop else ""}">{"<span class=ow-plan__pop>" + x["pop"] + "</span>" if pop else ""}'
              f'<h3>{name}</h3><p class="pr-card__tag">{tag}</p><p class="pr-card__pct"><small>{frm if frm != "&nbsp;" else ""}</small><strong>{pct}<sup>%</sup></strong><span>{of}</span></p>'
              f'<p class="pr-card__g">{x["groups"][0]}</p>{grp(items[:7])}<p class="pr-card__g">{x["groups"][1]}</p>{grp(items[7:])}'
              f'<p class="pr-card__note">{note}</p><a class="u-btn {"u-btn--rose" if pop else "u-btn--line"}" href="{href}">{btn}</a></article>')
    s += '</div></div></section>\n'
    # Calcul de la commission
    G = 10_000_000; plat = G * .15; pb = G / 11; base = G - plat - pb
    c = x['calc']
    rows = ''
    for name, pct in ((cards[0][0], 18), (cards[1][0], 11)):
        com = base * pct / 100; you = base - com
        segs = [('plat', plat, c['plat']), ('pbjt', pb, c['pbjt']), ('com', com, f'{c["com"]} {pct}{" %" if fr else "%"}'), ('you', you, c['you'])]
        rows += (f'<div class="pr-bar"><p class="pr-bar__h"><strong>{name}</strong><span>{c["com"]}{" :" if fr else ":"} <b>IDR {f(com, fr)}</b></span></p><div class="pr-bar__t">' +
                 ''.join(f'<span class="pr-seg pr-seg--{k}" style="--w:{v / G * 100:.2f}%" title="{l} : IDR {f(v, fr)}"><em>{c["s_" + k]}</em><b>{m1(v, fr)}</b></span>' for k, v, l in segs) + '</div></div>')
    s += (f'<section class="u-sec u-sec--white hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["calc_h"]}</h2><p>{x["calc_p"]}</p></div>'
          f'<div class="pr-calc"><div class="pr-calc__base"><span>{c["gross"]} <b>IDR {f(G, fr)}</b></span><span>→</span><span>{c["base"]} <b>IDR {f(base, fr)}</b></span></div>{rows}'
          f'<div class="pr-leg">' + ''.join(f'<span><i class="pr-seg--{k}"></i>{l}</span>' for k, l in (('plat', c['plat']), ('pbjt', c['pbjt']), ('com', c['com']), ('you', c['you']))) + '</div>'
          f'<p class="cx-note iv-c">{x["calc_note"]}</p></div></div></section>\n')
    # Rendement
    s += (f'<section class="u-sec u-sec--dark hm-sec hm-ges"><div class="u-wrap"><div class="u-head u-head--c"><p class="hm-k">{x["why_k"]}</p><h2>{why_h}</h2></div><div class="hm-ges__g">' +
          ''.join(f'<div class="hm-step"><span class="hm-step__n">0{i}</span>{svg}<h3>{h}</h3><p>{p}</p></div>' for i, (svg, h, p) in enumerate(why, 1)) + '</div></div></section>\n')
    # Bon à savoir
    s += (f'<section class="u-sec hm-sec"><div class="u-wrap"><div class="u-head u-head--c"><h2>{x["ok_h"]}</h2></div><div class="ar-lv2 hm-gar hm-gar--4">' +
          ''.join(f'<article class="ar-lv2__c"><div class="ar-lv2__b"><span class="ar-lv2__ic">{size(svg, 26)}</span><h3>{h}</h3><p class="ar-lv2__p">{p}</p></div></article>' for svg, h, p in ok) + '</div></div></section>\n')
    s += (f'<section class="u-cta"><img src="/assets/images/suma-jardin.jpg" alt="" loading="lazy"><div class="u-cta__in"><h2>{x["cta_h"]}</h2><p>{x["cta_p"]}</p>'
          f'<div class="u-btns"><a class="u-btn u-btn--rose" href="{x["cta_b"][1]}">{x["cta_b"][0]}</a></div></div></section>\n</div>\n')
    return s

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        open(os.path.join(SRC, lang, 'ProprietairesTarifs.html'), 'w').write(page(lang))
    print('ok')
