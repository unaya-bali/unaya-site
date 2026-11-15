# Génère les fiches PDF des Arawa Villas (FR/EN, villa B, villa D, résidence) et le PDF des plans.
# Utilise les textes de tools/arawa.py (importé, il régénère aussi les pages) et Chromium (Playwright).
import os, sys, json, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import arawa as A  # noqa: E402
IMG = 'file://' + os.path.join(SITE, 'assets', 'images') + '/'
FONTS = 'file://' + os.path.join(SITE, 'assets', 'fonts') + '/'
OUT = os.path.join(SITE, 'assets', 'docs')
TMP = os.path.join(SITE, '..', 'arawa-pdf-tmp')
os.makedirs(OUT, exist_ok=True); os.makedirs(TMP, exist_ok=True)

def im(name, w=1200):
    base = name[:-4]
    p = os.path.join(SITE, 'assets', 'images', f'{base}-{w}.webp')
    return IMG + (f'{base}-{w}.webp' if os.path.exists(p) else name)

CSS = f'''
@font-face{{font-family:'Cormorant Garamond';font-weight:400;src:url({FONTS}cormorant-garamond-v21-latin-regular.woff2)}}
@font-face{{font-family:'Cormorant Garamond';font-weight:500;src:url({FONTS}cormorant-garamond-v21-latin-500.woff2)}}
@font-face{{font-family:'Jost';font-weight:300;src:url({FONTS}jost-v20-latin-300.woff2)}}
@font-face{{font-family:'Jost';font-weight:400;src:url({FONTS}jost-v20-latin-regular.woff2)}}
@font-face{{font-family:'Jost';font-weight:500;src:url({FONTS}jost-v20-latin-500.woff2)}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Jost,sans-serif;color:#2E2429;font-size:10.5pt;line-height:1.5}}
.pg{{width:210mm;height:297mm;padding:16mm 16mm 14mm;position:relative;page-break-after:always;overflow:hidden;background:#F7F2EE}}
.pg:last-child{{page-break-after:auto}}
h1,h2{{font-family:'Cormorant Garamond',serif;font-weight:500;color:#3F2A3A;margin:0}}
h1{{font-size:34pt;line-height:1.05}}h2{{font-size:20pt;margin:0 0 4mm}}
.k{{font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:#8B5A46}}
.logo{{height:10mm}}
.cover{{width:100%;height:120mm;object-fit:cover;border-radius:6mm;display:block;margin:7mm 0 7mm}}
.facts{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:6mm 0}}
.facts div{{background:#fff;border:1px solid #E6DCD4;padding:3.5mm}}
.facts b{{display:block;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:16pt;color:#3F2A3A}}
.price{{display:flex;gap:4mm;margin-top:5mm}}
.price div{{flex:1;background:#3F2A3A;color:#F7F2EE;padding:5mm}}
.price b{{display:block;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:22pt}}
.badge{{display:inline-block;background:#0E9180;color:#fff;border-radius:99px;padding:1.5mm 4mm;font-size:8.5pt;margin-right:2mm}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin:5mm 0}}
.grid img{{width:100%;height:52mm;object-fit:cover;border-radius:3mm;display:block}}
dl{{margin:0}}dl div{{display:grid;grid-template-columns:45mm 1fr;gap:4mm;padding:2mm 0;border-bottom:1px solid #E6DCD4}}
dt{{font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:#8B5A46}}dd{{margin:0}}
.plans img{{width:100%;max-height:60mm;object-fit:contain;background:#fff;border:1px solid #E6DCD4;display:block;margin-bottom:3mm}}
.foot{{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font-size:8pt;color:#5A4E54;border-top:1px solid #E6DCD4;padding-top:3mm}}
.small{{font-size:8pt;color:#5A4E54}}
ul{{margin:2mm 0;padding-left:5mm}}li{{margin:1mm 0}}
'''

def doc(l, t, vv):
    fr = l == 'fr'
    url = 'https://unayabali.com' + (A.VHREF[vv][l] if vv else A.RES[l])
    foot = f'<div class="foot"><span>Unaya Bali · PT Unaya Bali Grup · WhatsApp +62 851 9021 1324 · info@unayabali.com</span><span>{html.escape(url)}</span></div>'
    hero = t.get('hero', 'arawa-facade.jpg')
    villas = t['villas']
    pr = ''.join(f'<div><span class="k" style="color:#D2A48C">{n}</span><b>{"à partir de " if fr else "from "}USD {p}</b><span>{"parcelle" if fr else "plot"} {pl}</span></div>' for n, p, pl in villas)
    facts = ''.join(f'<div><span class="k">{a}</span><b>{b}</b><span class="small">{c}</span></div>' for k, a, b, c in t['facts'])
    sold = '4 villas sur 6 déjà vendues' if fr else '4 of 6 villas already sold'
    p1 = (f'<section class="pg"><img class="logo" src="file://{SITE}/assets/logos/unaya-management-horizontal.svg"><img class="cover" src="{im(hero)}">'
          f'<p class="k">{t["kick"]}</p><h1>{t["h1"]}</h1><p style="font-size:12pt;margin:3mm 0">{t["sub"]}</p>'
          f'<p><span class="badge">{t["badges"][0]}</span><span class="badge" style="background:#D2A48C;color:#3F2A3A">{sold}</span></p>'
          f'<div class="facts">{facts}</div><div class="price">{pr}</div>{foot}</section>')
    mz = t.get('mosaic', ['arawa-piscine.jpg', 'arawa-salon.jpg', 'arawa-sejour.jpg']) + ['arawa-chambre-1.jpg' if 'arawa-chambre-1.jpg' not in t.get('mosaic', []) else 'arawa-chambre-2.jpg']
    desc = ''.join(f'<p>{x}</p>' for x in t['dp'])
    lease = ([('Remise des clés', 'fin décembre 2026'), ('Fin du bail du terrain', '21 mars 2055 (≈ 28 ans)'), ('Prolongation', 'option de 30 ans, au prix du marché du moment'), ('Garantie', '1 an après la remise des clés'), ('Meublée', 'oui, entièrement meublée et équipée')] if fr else
             [('Handover', 'end of December 2026'), ('Land lease ends', '21 March 2055 (≈ 28 years)'), ('Extension', '30-year option, at the market price at that time'), ('Warranty', '1 year after handover'), ('Furnished', 'yes, fully furnished and equipped')])
    p2 = (f'<section class="pg"><h2>{t["dh"]}</h2>{desc}<div class="grid">' + ''.join(f'<img src="{im(x, 800)}">' for x in mz) + '</div>'
          f'<h2 style="font-size:16pt">{"Bail et garanties" if fr else "Lease and warranty"}</h2><dl>' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in lease) + '</dl>'
          f'<p class="small" style="margin-top:3mm">{"Images de synthèse (3D) non contractuelles. Dates tirées du bail du terrain : faites vérifier le contrat d’achat par votre notaire ou votre avocat." if fr else "3D renderings are not contractual. Dates taken from the land lease: have the purchase contract checked by your notary or lawyer."}</p>{foot}</section>')
    lv = ''.join(f'<div><b style="font-weight:500">{h}</b><ul>' + ''.join(f'<li>{x}</li>' for x in li) + '</ul></div>' for h, li in t['lv'])
    loc = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in t['loc'])
    p3 = (f'<section class="pg"><h2>{"Plans et emplacement" if fr else "Plans and location"}</h2><div class="plans"><img src="{IMG}arawa-plan-rdc.jpg"><img src="{IMG}arawa-plan-etage.jpg"></div>'
          f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm"><div style="font-size:8.8pt;line-height:1.35">{lv}</div><div><p class="k">{"Temps de trajet" if fr else "Driving time"}</p><dl>{loc}</dl></div></div>'
          f'<p style="margin-top:5mm"><b style="font-weight:500">{"Visite, questions, réservation :" if fr else "Viewing, questions, reservation:"}</b> WhatsApp +62 851 9021 1324 · info@unayabali.com · {html.escape(url)}</p>{foot}</section>')
    return f'<!doctype html><html lang="{l}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{p1}{p2}{p3}</body></html>'

jobs = []
for l, t in A.T.items():
    for vv in (None, 'B', 'D'):
        tt = {**t, **A.V[vv][l]} if vv else t
        name = f'arawa-{("villa-" + vv.lower()) if vv else "residence"}-{l}'
        open(os.path.join(TMP, name + '.html'), 'w').write(doc(l, tt, vv))
        jobs.append(name)
plans = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} .pg{{background:#fff}} .pg img{{width:100%;height:240mm;object-fit:contain}}</style></head><body>' +
         ''.join(f'<section class="pg"><p class="k">Arawa Villas · Balangan · {c}</p><img src="{IMG}{f}"><div class="foot"><span>Unaya Bali · WhatsApp +62 851 9021 1324</span><span>{"indicatif / indicative"}</span></div></section>'
                 for f, c in [('arawa-plan-masse.jpg', 'Plan de masse / Site plan'), ('arawa-plan-rdc.jpg', 'Rez-de-chaussée / Ground floor'), ('arawa-plan-etage.jpg', 'Étage / Upstairs')]) + '</body></html>')
open(os.path.join(TMP, 'arawa-plans.html'), 'w').write(plans); jobs.append('arawa-plans')
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();for(const n of %s){await p.goto('file://%s/'+n+'.html',{waitUntil:'networkidle'});await p.pdf({path:'%s/'+n+'.pdf',format:'A4',printBackground:true});}await b.close()})()" % (json.dumps(jobs), os.path.abspath(TMP), OUT)
subprocess.run(['node', '-e', js], check=True)
for n in jobs: print(n, os.path.getsize(os.path.join(OUT, n + '.pdf')) // 1024, 'Ko')
