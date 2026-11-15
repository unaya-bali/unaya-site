# Bibliothèque de composants HTML pour le site Unaya (classes u-* définies dans assets/css/site.css)
S='stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
P = {
 'report':'<rect x="9" y="6" width="30" height="36" rx="2"/><path d="M16 34V26M24 34V18M32 34v-12"/>',
 'nofee':'<circle cx="24" cy="24" r="16"/><path d="M29 18c-1.2-1.6-3-2.5-5-2.5-3 0-5 1.6-5 4s2 3.4 5 4 5 1.6 5 4-2 4-5 4c-2.2 0-4-1-5.2-2.6M24 12.5v3M24 32.5v3"/><path d="M12 36 36 12"/>',
 'support':'<path d="M10 26v-4a14 14 0 0 1 28 0v4"/><rect x="7" y="25" width="7" height="11" rx="2"/><rect x="34" y="25" width="7" height="11" rx="2"/><path d="M37 36c0 4-4 6-9 6h-3"/>',
 'clock':'<circle cx="24" cy="24" r="16"/><path d="M24 14v10l7 5"/>',
 'team':'<circle cx="17" cy="17" r="5.5"/><circle cx="32" cy="19" r="4.5"/><path d="M6 39c1-7 5.5-10.5 11-10.5S27 32 28 39M27 31c1.4-1.6 3.2-2.5 5-2.5 4.5 0 8 3 9 9"/>',
 'shield':'<path d="M24 5 39 11v11c0 10-6.5 17.5-15 21-8.5-3.5-15-11-15-21V11Z"/><path d="m17 24 5 5 9-10"/>',
 'megaphone':'<path d="M8 20v8l6 1 18 9V11l-18 9Z"/><path d="M14 29l2 10h5l-2-9.5M36 19c2 1.2 3 3 3 5s-1 3.8-3 5"/>',
 'care':'<path d="M24 40s-14-8.4-14-18a8 8 0 0 1 14-5.3A8 8 0 0 1 38 22c0 9.6-14 18-14 18Z"/>',
 'wallet':'<path d="M7 14h30a4 4 0 0 1 4 4v18a4 4 0 0 1-4 4H11a4 4 0 0 1-4-4V12a4 4 0 0 1 4-4h22v6"/><path d="M41 24h-8a3 3 0 0 0 0 6h8"/>',
 'globe':'<circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c5 5 7 11 7 17s-2 12-7 17c-5-5-7-11-7-17s2-12 7-17Z"/>',
 'sync':'<path d="M38 16a16 16 0 0 0-28 2M10 32a16 16 0 0 0 28-2"/><path d="M38 8v8h-8M10 40v-8h8"/>',
 'price':'<path d="M6 40h36"/><path d="M8 18l10-7 8 5 13-9"/><path d="M34 7h5v5"/><rect x="9" y="28" width="6" height="12"/><rect x="21" y="22" width="6" height="18"/><rect x="33" y="16" width="6" height="24"/>',
 'star':'<path d="m24 6 5.4 11.2 12.1 1.6-8.8 8.4 2.2 12.1L24 33.5l-10.9 5.8 2.2-12.1-8.8-8.4 12.1-1.6Z"/>',
 'home':'<path d="M6 24 24 10l18 14"/><path d="M10 21v19h28V21"/><path d="M20 40V29h8v11"/>',
 'camera':'<path d="M6 16h8l3-5h14l3 5h8v22H6Z"/><circle cx="24" cy="26" r="7"/>',
 'key':'<circle cx="16" cy="30" r="8"/><path d="M22 24 38 8M32 14l5 5M28 18l4 4"/>',
 'chat':'<path d="M8 10h32v22H20l-8 7v-7H8Z"/><path d="M15 19h18M15 25h12"/>',
 'car':'<path d="M8 30v-6l4-9h24l4 9v6"/><path d="M6 30h36v7H6z"/><circle cx="14" cy="37" r="3"/><circle cx="34" cy="37" r="3"/><path d="M12 24h24"/>',
 'staff':'<circle cx="24" cy="14" r="6"/><path d="M12 41c0-8 5-13 12-13s12 5 12 13"/><path d="M20 28l4 6 4-6"/>',
 'broom':'<path d="M30 6 22 22"/><path d="M14 24h14l4 16H10Z"/><path d="M17 40l1-8M23 40v-8M29 40l-1-8"/>',
 'box':'<path d="M6 15 24 7l18 8v18l-18 8-18-8Z"/><path d="M6 15l18 8 18-8M24 23v18"/>',
 'tools':'<path d="M28 8a8 8 0 0 0 10 10L22 34l-6 6-8-8 6-6Z"/><path d="M10 10l8 8M6 14l8-8"/>',
 'pool':'<path d="M6 34c3 0 3 2 6 2s3-2 6-2 3 2 6 2 3-2 6-2 3 2 6 2 3-2 6-2M6 41c3 0 3 2 6 2s3-2 6-2 3 2 6 2 3-2 6-2 3 2 6 2 3-2 6-2"/><path d="M14 30V10a4 4 0 0 1 8 0M30 30V10a4 4 0 0 1 8 0M14 16h16M14 23h16"/>',
 'leaf':'<path d="M10 38C10 20 22 10 40 8c-2 18-12 30-30 30Z"/><path d="M10 38 28 20"/>',
 'calc':'<rect x="10" y="6" width="28" height="36" rx="3"/><rect x="15" y="11" width="18" height="8"/><path d="M16 26h.5M24 26h.5M32 26h.5M16 33h.5M24 33h.5M32 33h.5"/>',
 'mail':'<rect x="6" y="11" width="36" height="26" rx="2"/><path d="m7 13 17 13 17-13"/>',
 'pin':'<path d="M24 42s13-12 13-23a13 13 0 0 0-26 0c0 11 13 23 13 23Z"/><circle cx="24" cy="19" r="5"/>',
 'phone':'<rect x="14" y="5" width="20" height="38" rx="3"/><path d="M21 37h6"/>',
 'bed':'<path d="M6 36V12M6 28h36v8M6 22h36v6"/><circle cx="13" cy="19" r="3"/><path d="M18 22v-5h16a8 8 0 0 1 8 8"/>',
 'bath':'<path d="M6 24h36v5a9 9 0 0 1-9 9H15a9 9 0 0 1-9-9Z"/><path d="M11 24V11a4 4 0 0 1 8 0M13 38l-2 4M35 38l2 4"/>',
 'guests':'<circle cx="17" cy="16" r="6"/><circle cx="32" cy="18" r="5"/><path d="M6 40c1-8 5.5-12 11-12s10 4 11 12M27 30c1.5-1.7 3.2-2.5 5-2.5 5 0 8.5 3.5 9.5 10"/>',
 'wifi':'<path d="M6 19a26 26 0 0 1 36 0M12 26a17 17 0 0 1 24 0M18 32a8 8 0 0 1 12 0"/><circle cx="24" cy="38" r="1.5"/>',
 'kitchen':'<path d="M14 6v14a4 4 0 0 0 8 0V6M18 6v36M34 6c-4 2-6 7-6 14h6v22"/>',
 'snow':'<path d="M24 6v36M8.4 15l31.2 18M8.4 33l31.2-18"/><path d="m19 9 5 4 5-4M19 39l5-4 5 4"/>',
 'parking':'<rect x="7" y="7" width="34" height="34" rx="4"/><path d="M19 34V14h7a6 6 0 0 1 0 12h-7"/>',
 'sun':'<circle cx="24" cy="24" r="8"/><path d="M24 4v5M24 39v5M4 24h5M39 24h5M10 10l3.5 3.5M34.5 34.5 38 38M10 38l3.5-3.5M34.5 13.5 38 10"/>',
 'wave':'<path d="M4 30c5 0 5-6 10-6s5 6 10 6 5-6 10-6 5 6 10 6"/><path d="M4 38c5 0 5-6 10-6s5 6 10 6 5-6 10-6 5 6 10 6"/><path d="M14 18c2-6 7-10 14-10 4 0 7 1 9 3-5 0-8 3-8 7"/>',
 'temple':'<path d="M24 4v6M16 16h16l-2-6H18ZM12 24h24l-3-8H15ZM8 34h32l-3-10H11Z"/><path d="M6 40h36M20 40v-6h8v6"/>',
 'cocktail':'<path d="M8 8h32L24 26Z"/><path d="M24 26v14M16 40h16M30 8l6-4"/>',
 'pet':'<circle cx="14" cy="18" r="3.5"/><circle cx="22" cy="11" r="3.5"/><circle cx="32" cy="12" r="3.5"/><circle cx="38" cy="20" r="3.5"/><path d="M26 22c-6 0-12 8-12 13 0 3 2 5 5 5 3 0 4-2 7-2s4 2 7 2c3 0 5-2 5-5 0-5-6-13-12-13Z"/>',
 'nosmoke':'<rect x="6" y="26" width="28" height="6"/><path d="M38 26v6M34 18c0-4 4-4 4-8"/><path d="M8 8l32 32"/>',
 'noparty':'<circle cx="24" cy="24" r="16"/><path d="M13 13l22 22"/><path d="M19 30l4-12 6 6Z"/>',
 'door':'<path d="M12 42V6h24v36"/><path d="M8 42h32M30 24v.5"/>',
 'scooter':'<circle cx="12" cy="34" r="5"/><circle cx="37" cy="34" r="5"/><path d="M17 34h12l4-14h-6M29 20l-3-8h-5M12 29l5-9h10"/>',
 'plane':'<path d="M6 30l14-4 10-16a3 3 0 0 1 5 2l-4 13 11 3v5l-12-1-6 9h-4l2-10-14 3Z"/>',
 'doc':'<path d="M14 6h16l8 8v28H14z"/><path d="M30 6v8h8"/><path d="M19 22h14M19 28h14M19 34h8"/>',
 'check':'<circle cx="24" cy="24" r="16"/><path d="m16 24 6 6 10-12"/>',
 'quote':'<path d="M10 30c0-8 4-14 10-16M26 30c0-8 4-14 10-16"/><circle cx="14" cy="32" r="5"/><circle cx="30" cy="32" r="5"/>',
 'map':'<path d="M6 10l12-4 12 4 12-4v32l-12 4-12-4-12 4z"/><path d="M18 6v32M30 10v32"/>',
 'eye':'<path d="M4 24s7-12 20-12 20 12 20 12-7 12-20 12S4 24 4 24Z"/><circle cx="24" cy="24" r="6"/>',
 'arch':'<path d="M10 42V22a14 14 0 0 1 28 0v20"/><path d="M17 42V23a7 7 0 0 1 14 0v19"/><circle cx="24" cy="18" r="1.8" fill="currentColor"/>',
}
def ic(name, size=40): return f'<svg aria-hidden="true" class="u-ic" width="{size}" height="{size}" viewBox="0 0 48 48" {S}>{P[name]}</svg>'
def esc(s): return s
def btn(label, href, kind='solid'): return f'<a class="u-btn u-btn--{kind}" href="{href}">{label}</a>'
def src(img): return img if img.startswith("http") else "/assets/images/"+img
def hero(img, h1, sub, buttons='', chips='', kicker='', tall=False):
    k=f'<p class="u-hero__k">{kicker}</p>' if kicker else ''
    return (f'<section class="u-hero{" u-hero--tall" if tall else ""}"><img src="{src(img)}" alt="" fetchpriority="high"><div class="u-hero__in">{k}<h1>{h1}</h1>'
            f'<p class="u-hero__sub">{sub}</p>' + (f'<div class="u-btns">{buttons}</div>' if buttons else '') + chips + '</div></section>\n')
def sec(inner, mod='', id=''): return f'<section class="u-sec{" u-sec--"+mod if mod else ""}"{f" id={chr(34)}{id}{chr(34)}" if id else ""}><div class="u-wrap">{inner}</div></section>\n'
def head(h2, lead='', center=False): return f'<div class="u-head{" u-head--c" if center else ""}"><h2>{h2}</h2>' + (f'<p>{lead}</p>' if lead else '') + '</div>'
def feats(items, cols=3): return f'<div class="u-feats u-feats--{cols}">' + ''.join(f'<div class="u-feat">{ic(k)}<h3>{h}</h3><p>{t}</p></div>' for k,h,t in items) + '</div>'
def rows(items): return '<div class="u-rows">' + ''.join(f'<div class="u-row">{ic(k)}<div><h3>{h}</h3><p>{t}</p></div>' + (f'<span class="u-pill">{pl}</span>' if pl else '<span></span>') + '</div>' for k,h,t,pl in items) + '</div>'
def path(items): return '<div class="u-path u-path--'+str(len(items))+'">' + ''.join(f'<div class="u-path__s"><span class="u-path__dot">{ic(k,34)}</span><div><h3>{h}</h3><p>{t}</p></div></div>' for k,h,t in items) + '</div>'
def checks(items): return '<ul class="u-checks">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def split(img, inner, reverse=False, arch=True): return f'<div class="u-split{" u-split--rev" if reverse else ""}"><div class="u-split__img{" u-arch" if arch else ""}"><img src="{src(img)}" alt="" loading="lazy"></div><div class="u-split__txt">{inner}</div></div>'
def band(icon, inner): return f'<div class="u-band">{ic(icon,52)}<div>{inner}</div></div>'
def cta(img, h2, p, buttons): return f'<section class="u-cta"><img src="{src(img)}" alt="" loading="lazy"><div class="u-cta__in"><h2>{h2}</h2><p>{p}</p><div class="u-btns">{buttons}</div></div></section>\n'
def stats(items): return '<div class="u-stats">' + ''.join(f'<div class="u-stat">{ic(k,34)}<strong>{n}</strong><span>{l}</span></div>' for k,n,l in items) + '</div>'
def faq(items): return '<div class="u-faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items) + '</div>'
def link(label, href): return f'<a class="u-link" href="{href}">{label}</a>'
