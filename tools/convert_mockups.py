"""One-time conversion: canvas mockups (.dc.html) -> page bodies in src/pages/{fr,en}/.
Run once; afterwards edit src/pages directly."""
import re, sys, os, json

MOCK = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLOB = {
 '09dbb359c33c6eac879b0d5424470606': '/assets/logos/unaya-management-horizontal.svg',
 '32192212594fd5d685d757f022cb4a44': '/assets/logos/unaya-management-vertical-fonce.svg',
}
for k, v in {
 '3ff98812f4837e23ac78b9c122c1784b':'suma-piscine','b635447a295897b06814edd0baa0cc50':'suma-piscine-2','f071a0b4739c66c44237588391177efd':'suma-entree',
 '795f3ac9eaf8803dc1903c7d87b1b0be':'suma-jardin','049be5df043b4fce1997930875d18c52':'suma-piscine-drone','affb171ae4cedb3b49b1ba23778a29ef':'suma-terrasse',
 'bc0434e13175a90a1ba66368749ca2e8':'suma-chambre-1','dad85cad5bff2f3944628576b42224ff':'suma-chambre-2','f3e445a83c503f15153d320be27be0c2':'suma-chambre-twin',
 'fa1d313455786140e385283b78942ff8':'suma-sdb','2f94f69e0482a570715f3950a682ea48':'yuga-drone','083fe336ef80086dcd382d997de93551':'rumah-jambu-jardin',
 '5f3c097b5f4e83d085f841398ecb047e':'umalas-rizieres','f2de46dc70c9c5c96c39dbba49262d18':'yuga-piscine','6f7f4691f71edcd865309cf71e6d5648':'yuga-piscine-2',
 'b210ff537c6a20318674f8d8996e897c':'yuga-entree','ea7d0aa92c671aa3a31ebf45a3880ceb':'yuga-chambre','d3e3b465e89ba8cc035bf951dc7a2351':'yuga-sdb',
 '76406147fdacfaba0994a6ad52347d55':'yuga-nuit','d8e06f21890684f4fb2e3ae4f79b920c':'yuga-terrasse','3efffe66750c266d5ebca7f3e1bd02a1':'yuga-transats',
 '3dc4f8926ec9f9f261fc2dfb55f861f0':'rj-salon','fcd46d69ae5283cb1dc524795ba02e9b':'rj-chambre','c37333080ff3866e8520a3633fd5ea39':'rj-cuisine',
 '5c7acdb762ec0f9edc8d590ab2f6eb07':'rj-jardin','746ec6aaaaeffd854aded55cb03edf44':'rj-sdb','dbb168641b9bcd13019d98a044aaa30c':'rj-maison'}.items():
    BLOB[k] = f'/assets/images/{v}.jpg'

ROUTES = json.load(open(os.path.join(ROOT, 'src', 'routes.json')))

def route(name, lang):
    return ROUTES[name][lang]

pages = {}
for fn in sorted(os.listdir(MOCK)):
    if not fn.endswith('.dc.html'): continue
    lang = 'en' if fn.startswith('EN_') else 'fr'
    name = fn[3:-8] if lang == 'en' else fn[:-8]
    s = open(os.path.join(MOCK, fn), encoding='utf-8').read()
    title = re.search(r'<title>([^<]+)</title>', s).group(1)
    # body between header (and owners sub-nav) and footer
    start = s.index('</header>') + len('</header>')
    sub = re.match(r'\s*<nav aria-label="(Propriétaires|Owners)".*?</nav>\n', s[start:], re.S)
    if sub: start += sub.end()
    end = s.index('<!-- PIED DE PAGE') if '<!-- PIED DE PAGE' in s else s.index('<footer')
    body = s[start:end].strip()
    for k, v in BLOB.items():
        body = body.replace(f'/_blob/{k}', v)
    # links between pages
    def fix(m):
        target, anchor = m.group(1), m.group(2) or ''
        t = target[3:] if target.startswith('EN_') else target
        t = t[:-8]
        return f'href="{route(t, lang)}{anchor}"'
    body = re.sub(r'href="((?:EN_)?[A-Za-z]+\.dc\.html)(#[a-z-]+)?"', fix, body)
    pages[(lang, name)] = dict(title=title, body=body)

for (lang, name), p in pages.items():
    out = os.path.join(ROOT, 'src', 'pages', lang, f'{name}.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(f'<!-- title: {p["title"]} -->\n' + p['body'] + '\n')
print(len(pages), 'pages converted')
