import os
SITE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FONTS = 'file://' + os.path.join(SITE, 'assets', 'fonts') + '/'
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
