# Fiches PDF des terrains (2 pages, FR/EN), à partir des données de tools/land2.py.
import os, sys, json, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__)); SITE = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE); sys.path.insert(0, '/tmp/claude-0/-home-claude/fb21bd82-28de-566e-9e55-058e68a3af45/scratchpad/gen')
import land2 as T
import arawa_pdf_css as C
IMG = 'file://' + SITE + '/assets/images/'
OUT = os.path.join(SITE, 'assets', 'docs'); TMP = os.path.join(SITE, '..', 'land-pdf-tmp'); os.makedirs(TMP, exist_ok=True)
jobs = []
for l, ds in T.DATA.items():
    fr = l == 'fr'
    for d in ds:
        name = f'terrain-{"melasti-795" if d["page"].endswith("795") else "melasti-500"}-{l}'
        url = 'https://unayabali.com' + json.load(open(SITE + '/src/routes.json'))[d['page']][l]
        foot = f'<div class="foot"><span>Unaya Bali · PT Unaya Bali Grup · WhatsApp +62 851 9021 1324 · info@unayabali.com</span><span>{html.escape(url)}</span></div>'
        facts = ''.join(f'<div><span class="k">{a}</span><b>{b}</b><span class="small">{c}</span></div>' for k, a, b, c in d['facts'])
        pr = ''.join(f'<div><span class="k" style="color:#D2A48C">{n}</span><b style="font-size:16pt">{T.idr(v, fr)}</b><span>{T.usd(v / T.FX, fr)}</span></div>' for n, v in d['prices'])
        imgs = (d['mosaic'] or [d['hero']])
        p1 = (f'<section class="pg"><img class="logo" src="file://{SITE}/assets/logos/unaya-management-horizontal.svg"><img class="cover" style="height:95mm" src="{IMG}{imgs[0]}">'
              f'<p class="k">{d["kick"]}</p><h1 style="font-size:28pt">{d["h1"]}</h1><p style="font-size:11.5pt;margin:3mm 0">{d["sub"]}</p>'
              f'<div class="facts">{facts}</div><div class="price">{pr}</div><p class="small" style="margin-top:2mm">{d["pe"]} · {("Dollars au taux du " if fr else "Dollars at the rate of ") + T.FXD[l]}</p>{foot}</section>')
        desc = ''.join(f'<p>{x}</p>' for x in d['dp'])
        tbl = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in d['tbl'])
        p2 = (f'<section class="pg"><h2>{d["dh"]}</h2>{desc}<div style="display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin:4mm 0">'
              f'<div style="background:#fff;border:1px solid #E6DCD4;padding:2mm">{d["plan"]}</div><img src="{IMG}{d["rdtr"]}" style="width:100%;height:62mm;object-fit:contain;background:#fff;border:1px solid #E6DCD4"></div>'
              f'<dl>{tbl}</dl><p class="small" style="margin-top:2mm">' + ' · '.join(f'{a} {b}' for a, b in d['dist']) + '</p>'
              f'<p style="margin-top:4mm"><b style="font-weight:500">{"Visite, questions :" if fr else "Viewing, questions:"}</b> WhatsApp +62 851 9021 1324 · info@unayabali.com</p>'
              f'<p class="small">{T.L0.T[l]["legal"]}</p>{foot}</section>')
        open(os.path.join(TMP, name + '.html'), 'w').write(f'<!doctype html><html lang="{l}"><head><meta charset="utf-8"><style>{C.CSS}</style></head><body>{p1}{p2}</body></html>')
        jobs.append(name)
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();for(const n of %s){await p.goto('file://%s/'+n+'.html',{waitUntil:'networkidle'});await p.pdf({path:'%s/'+n+'.pdf',format:'A4',printBackground:true});}await b.close()})()" % (json.dumps(jobs), os.path.abspath(TMP), OUT)
subprocess.run(['node', '-e', js], check=True)
for n in jobs: print(n, os.path.getsize(os.path.join(OUT, n + '.pdf')) // 1024, 'Ko')
