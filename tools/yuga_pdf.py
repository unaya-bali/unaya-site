# Brochure PDF de la Villa Yuga à vendre (FR/EN), mêmes styles que les fiches Arawa (tools/arawa_pdf.py).
# Textes repris de tools/yuga_sale.py. Contact = Unaya. Sortie : assets/docs/villa-yuga-{fr,en}.pdf
import os, sys, json, subprocess, html, re
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import yuga_sale as Y  # noqa: E402  (n'écrit rien à l'import)
src = open(os.path.join(HERE, 'arawa_pdf.py')).read()
IMG = 'file://' + os.path.join(SITE, 'assets', 'images') + '/'
FONTS = 'file://' + os.path.join(SITE, 'assets', 'fonts') + '/'
CSS = eval(re.search(r"CSS = (f'''.*?''')", src, re.S).group(1))
CSS += ".cover{height:100mm}.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm}.box{background:#fff;border:1px solid #E6DCD4;padding:5mm;margin-top:5mm}.map{width:100%;height:62mm;object-fit:cover;border-radius:3mm}"
OUT = os.path.join(SITE, 'assets', 'docs'); TMP = os.path.join(SITE, '..', 'yuga-pdf-tmp'); os.makedirs(TMP, exist_ok=True)
strip = lambda s: re.sub(r'<[^>]+>', '', s)

def im(name, w=1200):
    base = name[:-4]
    return IMG + (f'{base}-{w}.webp' if os.path.exists(os.path.join(SITE, 'assets', 'images', f'{base}-{w}.webp')) else name)

def doc(l):
    x = Y.T[l]; fr = l == 'fr'; url = 'https://unayabali.com' + Y.URL[l]
    foot = f'<div class="foot"><span>Unaya Bali Grup · WhatsApp +62 851 9021 1324 · info@unayabali.com</span><span>{html.escape(url)}</span></div>'
    facts = ''.join(f'<div><span class="k">{a}</span><b>{b}</b><span class="small">{c}</span></div>' for k, a, b, c in x['facts'])
    p1 = (f'<section class="pg"><img class="logo" src="file://{SITE}/assets/logos/unaya-management-horizontal.svg"><img class="cover" src="{im("yuga-piscine.jpg")}">'
          f'<p class="k">{x["kick"]}</p><h1>{x["h1"]}</h1><p style="font-size:12pt;margin:3mm 0">{x["sub"]}</p>'
          '<p>' + ''.join(f'<span class="badge"{"" if i == 0 else " style=\"background:#D2A48C;color:#3F2A3A\""}>{b}</span>' for i, b in enumerate(x['badges'])) + '</p>'
          f'<div class="facts">{facts}</div><div class="price"><div><span class="k" style="color:#D2A48C">{x["pk"]}</span><b>{Y.PRICE[l]}</b><span>{x["usd"]}</span></div></div>'
          f'<p class="small" style="margin-top:2mm">{x["rate"]}</p>{foot}</section>')
    desc = ''.join(f'<p>{p}</p>' for p in x['dp'])
    grid = ''.join(f'<img src="{im(f, 800)}">' for f in ['yuga-g1.jpg', 'yuga-chambre.jpg', 'yuga-g2.jpg', 'yuga-sdb.jpg'])
    p2 = (f'<section class="pg"><h2>{x["dh"]}</h2>{desc}<div class="grid">{grid}</div>'
          f'<h2 style="font-size:16pt">{x["lh"]}</h2><dl>' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in x['lease']) + f'</dl><p class="small" style="margin-top:3mm">{x["lnote"]}</p>{foot}</section>')
    lv = ''.join(f'<div><b style="font-weight:500">{h}</b><ul>' + ''.join(f'<li>{li}</li>' for li in lst) + '</ul></div>' for im_, k, h, lst in x['lv'])
    near = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in x['near'])
    p3 = (f'<section class="pg"><h2>{x["vh"]}</h2><div class="two" style="font-size:9.5pt;line-height:1.4"><div>{lv}</div><div><img class="map" src="{im("yuga-nuit.jpg", 800)}"><p class="k" style="margin-top:4mm">{x["zh"]}</p><dl>{near}</dl></div></div>'
          f'<div class="box"><h2 style="font-size:16pt">{x["rh"]}</h2>' + ''.join(f'<p>{strip(p)}</p>' for p in x['rp']) + '</div>'
          f'<p style="margin-top:6mm"><b style="font-weight:500">{"Visite, questions :" if fr else "Viewing, questions:"}</b> WhatsApp +62 851 9021 1324 · info@unayabali.com · {html.escape(url)}</p>'
          f'<p class="small">{x["legal"]}</p>{foot}</section>')
    return f'<!doctype html><html lang="{l}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{p1}{p2}{p3}</body></html>'

jobs = []
for l in ('fr', 'en'):
    n = f'villa-yuga-{l}'; open(os.path.join(TMP, n + '.html'), 'w').write(doc(l)); jobs.append(n)
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();for(const n of %s){await p.goto('file://%s/'+n+'.html',{waitUntil:'networkidle'});await p.pdf({path:'%s/'+n+'.pdf',format:'A4',printBackground:true});}await b.close()})()" % (json.dumps(jobs), os.path.abspath(TMP), OUT)
subprocess.run(['node', '-e', js], check=True, cwd='/tmp')
for n in jobs: print(n, os.path.getsize(os.path.join(OUT, n + '.pdf')) // 1024, 'Ko')
