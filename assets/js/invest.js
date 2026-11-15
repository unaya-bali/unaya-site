/* Page « Le guide pour investir » : simulateur de revenus, budget de construction, onglets de la FAQ.
   Données lues dans les attributs data-* posés par le générateur (tools/invest2.py). */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FR = (document.documentElement.lang || 'fr').indexOf('fr') === 0;
  function fmt(n, d) { return Number(n).toLocaleString(FR ? 'fr-FR' : 'en-US', { maximumFractionDigits: d || 0, minimumFractionDigits: d || 0 }).replace(/ | /g, ' '); }
  function usd(n) { return FR ? fmt(n) + ' USD' : 'USD ' + fmt(n); }
  function idrM(n) { return FR ? 'IDR ' + fmt(n / 1e6) + ' M' : 'IDR ' + fmt(n / 1e6) + 'M'; }
  function el(tag, attrs, parent) { var e = document.createElementNS(NS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function onView(node, fn) {
    if (!('IntersectionObserver' in window)) { fn(); return; }
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); fn(); } }, { threshold: 0.2 });
    io.observe(node);
  }
  function countUp(node, to, render) {
    if (!node) return;
    var from = parseFloat(node.getAttribute('data-v') || '0');
    node.setAttribute('data-v', to);
    if (reduce || document.hidden) { node.textContent = render(to); return; }
    clearTimeout(node._t); node._t = setTimeout(function () { node.textContent = render(to); }, 900);
    var t0 = null, dur = 650;
    function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3); node.textContent = render(from + (to - from) * e); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  var tip = document.querySelector('.cx-tip');
  if (!tip) { tip = document.createElement('div'); tip.className = 'cx-tip'; tip.setAttribute('role', 'status'); document.body.appendChild(tip); }
  function showTip(h, x, y) { tip.innerHTML = h; tip.classList.add('is-on'); var r = tip.getBoundingClientRect(); var left = Math.min(window.innerWidth - r.width - 8, Math.max(8, x - r.width / 2)); var top = y - r.height - 14; if (top < 8) top = y + 18; tip.style.transform = 'translate(' + left + 'px,' + top + 'px)'; }
  function hideTip() { tip.classList.remove('is-on'); }
  function bindTip(node, fn) {
    node.addEventListener('mousemove', function (e) { showTip(fn(), e.clientX, e.clientY); });
    node.addEventListener('mouseleave', hideTip);
    node.addEventListener('focus', function () { var r = node.getBoundingClientRect(); showTip(fn(), r.left + r.width / 2, r.top); });
    node.addEventListener('blur', hideTip);
    node.addEventListener('touchstart', function (e) { var t = e.touches[0]; showTip(fn(), t.clientX, t.clientY); }, { passive: true });
  }
  function fill(s) { s.style.setProperty('--p', ((s.value - s.min) / (s.max - s.min) * 100) + '%'); }
  var PC = FR ? ' %' : '%';
  var COL = { gross: '#7B4374', ded: '#C9753F', net: '#0E9180' };

  /* ---------- 1. Simulateur de revenus ---------- */
  var sim = document.querySelector('.iv-sim');
  if (sim) (function () {
    var c = JSON.parse(sim.getAttribute('data-iv')), L = c.lbl;
    var rate = sim.querySelector('[name=rate]'), occ = sim.querySelector('[name=occ]'), val = sim.querySelector('[name=val]');
    var wfBox = sim.querySelector('.iv-wf'), ygBox = sim.querySelector('.iv-yg');
    var cur = null;
    function calc() {
      var r = +rate.value, o = +occ.value / 100, nights = Math.round(365 * o), gross = r * nights;
      var comm = gross * c.comm, pbjt = gross / 11, fee = (gross - comm - pbjt) * c.fee, cost = gross * c.cost;
      var net = gross - comm - pbjt - fee - cost;
      return { nights: nights, gross: gross, comm: comm, pbjt: pbjt, fee: fee, cost: cost, net: net, yld: net / c.fx / (+val.value) * 100 };
    }
    /* Cascade (waterfall) */
    var narrow = wfBox.clientWidth < 480, W = narrow ? 380 : 640, H = narrow ? 280 : 300, m = { t: 34, r: 6, b: 46, l: 6 };
    var SHORT = FR ? { gross: 'Brut', comm: 'Comm.', pbjt: 'PBJT', fee: 'Unaya', cost: 'Charges', net: 'Net' } : { gross: 'Gross', comm: 'Comm.', pbjt: 'PBJT', fee: 'Unaya', cost: 'Costs', net: 'Net' };
    var wsv = el('svg', { viewBox: '0 0 ' + W + ' ' + H, preserveAspectRatio: 'xMidYMid meet' }, wfBox);
    var KEYS = ['gross', 'comm', 'pbjt', 'fee', 'cost', 'net'];
    var bw = (W - m.l - m.r) / KEYS.length, gap = narrow ? 10 : 18;
    var base = el('line', { x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b, stroke: '#E6DCD4' }, wsv);
    var bars = KEYS.map(function (k, i) {
      var g = el('g', { tabindex: 0, class: 'iv-wfb' }, wsv);
      var rect = el('rect', { x: m.l + i * bw + gap / 2, width: bw - gap, y: H - m.b, height: 0, rx: 4, fill: k === 'gross' ? COL.gross : k === 'net' ? COL.net : COL.ded }, g);
      var v = el('text', { x: m.l + i * bw + bw / 2, y: H - m.b - 6, 'text-anchor': 'middle', class: 'iv-wfv' }, g);
      var lab = el('text', { x: m.l + i * bw + bw / 2, y: H - m.b + 20, 'text-anchor': 'middle', class: 'iv-wfl' }, g); lab.textContent = narrow ? SHORT[k] : L[k];
      var link = i < KEYS.length - 1 ? el('line', { stroke: '#BBA9A0', 'stroke-dasharray': '3 3', 'stroke-width': 1 }, wsv) : null;
      bindTip(g, function () { if (!cur) return ''; var amt = cur[k]; return '<b>' + L[k] + '</b><br>' + (k === 'gross' || k === 'net' ? '' : '− ') + idrM(amt) + ' ' + L.yr + '<br><span>' + fmt(amt / cur.gross * 100, 1) + PC + ' ' + L.ofg + '</span>'; });
      return { rect: rect, v: v, link: link };
    });
    function drawWf(d) {
      var maxV = d.gross || 1, y = function (v) { return H - m.b - (H - m.t - m.b) * (v / maxV); };
      var run = d.gross;
      KEYS.forEach(function (k, i) {
        var top, bot;
        if (k === 'gross') { top = d.gross; bot = 0; }
        else if (k === 'net') { top = d.net; bot = 0; }
        else { top = run; bot = run - d[k]; run = bot; }
        var b = bars[i];
        b.rect.setAttribute('y', y(top)); b.rect.setAttribute('height', Math.max(1, y(bot) - y(top)));
        b.v.setAttribute('y', y(top) - 8);
        b.v.textContent = (k === 'gross' || k === 'net' ? '' : '−') + fmt(d[k] / 1e6) + (FR ? ' M' : 'M');
        if (b.link) {
          var lv = k === 'gross' ? d.gross : bot;
          b.link.setAttribute('x1', m.l + i * bw + bw - gap / 2); b.link.setAttribute('x2', m.l + (i + 1) * bw + gap / 2);
          b.link.setAttribute('y1', y(lv)); b.link.setAttribute('y2', y(lv));
          if (k === 'cost') b.link.setAttribute('opacity', 0);
        }
      });
    }
    /* Jauge de rendement */
    var GW = 360, GH = 96, gm = 16, MAXY = 15;
    var gsv = el('svg', { viewBox: '0 0 ' + GW + ' ' + GH }, ygBox);
    var gx = function (v) { return gm + (GW - 2 * gm) * Math.min(v, MAXY) / MAXY; };
    el('rect', { x: gm, y: 40, width: GW - 2 * gm, height: 12, rx: 6, fill: '#F3ECE6' }, gsv);
    var band = el('rect', { x: gx(6), y: 40, width: gx(10) - gx(6), height: 12, fill: '#0E9180', opacity: .28 }, gsv);
    bindTip(band, function () { return '<b>' + L.band + '</b><br>6 – 10 %'; });
    var bl = el('text', { x: (gx(6) + gx(10)) / 2, y: 72, 'text-anchor': 'middle', class: 'iv-gl' }, gsv); bl.textContent = L.band;
    [0, 5, 10, 15].forEach(function (v) { var t = el('text', { x: gx(v), y: 90, 'text-anchor': 'middle', class: 'cx-ax' }, gsv); t.textContent = v + PC; });
    var mk = el('g', { class: 'iv-mk' }, gsv);
    el('line', { x1: 0, x2: 0, y1: 26, y2: 58, stroke: '#3F2A3A', 'stroke-width': 2 }, mk);
    el('circle', { cx: 0, cy: 46, r: 7, fill: '#fff', stroke: '#3F2A3A', 'stroke-width': 2.5 }, mk);
    var mt = el('text', { x: 0, y: 18, 'text-anchor': 'middle', class: 'iv-gm' }, mk);
    function drawYg(d) {
      var x = gx(Math.max(0, d.yld));
      mk.style.transform = 'translateX(' + x + 'px)';
      mt.textContent = L.you + ' · ' + fmt(d.yld, 1) + PC;
      mt.setAttribute('text-anchor', x < 60 ? 'start' : x > GW - 60 ? 'end' : 'middle');
      var msg = sim.querySelector('[data-k=ymsg]');
      if (msg) msg.textContent = d.yld < 6 ? (FR ? 'sous la fourchette du marché' : 'below the market range') : d.yld <= 10 ? (FR ? 'dans la fourchette du marché' : 'within the market range') : (FR ? 'au-dessus du marché : vérifiez vos hypothèses' : 'above the market: check your assumptions');
    }
    function update(anim) {
      [rate, occ, val].forEach(fill);
      var d = calc(); cur = d;
      sim.querySelector('[data-out=rate]').textContent = 'IDR ' + fmt(+rate.value);
      sim.querySelector('[data-out=occ]').textContent = occ.value + PC;
      sim.querySelector('[data-out=nights]').textContent = d.nights;
      sim.querySelector('[data-out=val]').textContent = usd(+val.value);
      countUp(sim.querySelector('[data-k=gross]'), d.gross, idrM);
      countUp(sim.querySelector('[data-k=net]'), d.net, idrM);
      countUp(sim.querySelector('[data-k=month]'), d.net / 12, idrM);
      countUp(sim.querySelector('[data-k=yld]'), d.yld, function (v) { return fmt(v, 1) + PC; });
      countUp(sim.querySelector('[data-k=yld2]'), d.yld, function (v) { return fmt(v, 1) + PC; });
      var nu = sim.querySelector('[data-k=netusd]'); if (nu) nu.textContent = '≈ ' + usd(Math.round(d.net / c.fx / 100) * 100);
      drawWf(d); drawYg(d);
      sim.querySelectorAll('[data-occ]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-occ') === occ.value ? 'true' : 'false'); });
    }
    var raf;
    [rate, occ, val].forEach(function (s) { s.addEventListener('input', function () { cancelAnimationFrame(raf); raf = requestAnimationFrame(function () { update(false); }); }); });
    sim.querySelectorAll('[data-occ]').forEach(function (b) { b.addEventListener('click', function () { occ.value = b.getAttribute('data-occ'); update(true); }); });
    update(false);
    onView(sim, function () { sim.classList.add('is-in'); });
  })();

  /* ---------- 2. Budget de construction ---------- */
  var bud = document.querySelector('.iv-bud');
  if (bud) (function () {
    var tiers = JSON.parse(bud.getAttribute('data-tiers')), area = bud.querySelector('[name=area]'), sel = 'hdg';
    var box = bud.querySelector('.iv-rng'), nb = box.clientWidth < 440, W = nb ? 360 : 520, rowH = 58, m = { l: nb ? 112 : 118, r: 14, t: 8, b: 30 }, MAX = 2600;
    var H = m.t + rowH * tiers.length + m.b;
    var sv = el('svg', { viewBox: '0 0 ' + W + ' ' + H }, box);
    var x = function (v) { return m.l + (W - m.l - m.r) * v / MAX; };
    (nb ? [0, 1000, 2000] : [0, 500, 1000, 1500, 2000, 2500]).forEach(function (v) {
      el('line', { x1: x(v), x2: x(v), y1: m.t, y2: H - m.b, stroke: '#F0E8E2' }, sv);
      var t = el('text', { x: x(v), y: H - m.b + 18, 'text-anchor': 'middle', class: 'cx-ax' }, sv); t.textContent = fmt(v);
    });
    var rows = tiers.map(function (t, i) {
      var y = m.t + i * rowH + rowH / 2;
      var g = el('g', { tabindex: 0, class: 'iv-rg' }, sv);
      var lab = el('text', { x: m.l - 12, y: y + 4, 'text-anchor': 'end', class: 'iv-rgl' }, g); lab.textContent = t.l;
      el('rect', { x: m.l, y: y - 3, width: W - m.l - m.r, height: 6, rx: 3, fill: '#F7F2EE' }, g);
      var r = el('rect', { x: x(t.a), y: y - 9, width: 0, height: 18, rx: 9, fill: '#D2A48C', class: 'iv-rgb' }, g);
      var v = el('text', { x: x(t.z) + 8, y: y + 4, class: 'iv-rgv' }, g); v.textContent = '';
      bindTip(g, function () { return '<b>' + t.l + '</b><br>' + fmt(t.a) + ' – ' + fmt(t.z) + ' USD/m²'; });
      g.addEventListener('click', function () { sel = t.id; upd(); });
      return { r: r, v: v, t: t };
    });
    function upd() {
      fill(area);
      var a = +area.value, t = tiers.filter(function (k) { return k.id === sel; })[0];
      bud.querySelector('[data-out=area]').textContent = a + ' m²';
      var lo = fmt(Math.round(a * t.a / 1000) * 1000), hi = fmt(Math.round(a * t.z / 1000) * 1000);
      bud.querySelector('[data-k=bud]').textContent = FR ? lo + ' – ' + hi + ' USD' : 'USD ' + lo + ' – ' + hi;
      bud.querySelector('[data-k=budidr]').textContent = '≈ IDR ' + fmt(a * t.a * 18158 / 1e9, 1) + ' – ' + fmt(a * t.z * 18158 / 1e9, 1) + (FR ? ' Md' : ' bn');
      rows.forEach(function (rw) { var on = rw.t.id === sel; rw.r.setAttribute('fill', on ? '#3F2A3A' : '#D2A48C'); rw.v.textContent = fmt(rw.t.a) + ' – ' + fmt(rw.t.z); var inside = x(rw.t.z) + (nb ? 70 : 90) > W; rw.v.setAttribute('x', inside ? x(rw.t.a) - 8 : x(rw.t.z) + 8); rw.v.setAttribute('text-anchor', inside ? 'end' : 'start'); rw.v.setAttribute('class', 'iv-rgv' + (on ? ' is-on' : '')); });
      bud.querySelectorAll('[data-tier]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-tier') === sel ? 'true' : 'false'); });
    }
    area.addEventListener('input', upd);
    bud.querySelectorAll('[data-tier]').forEach(function (b) { b.addEventListener('click', function () { sel = b.getAttribute('data-tier'); upd(); }); });
    upd();
    function grow() { rows.forEach(function (rw, i) { var w = x(rw.t.z) - x(rw.t.a); if (reduce) { rw.r.setAttribute('width', w); return; } rw.r.style.transition = 'width .9s cubic-bezier(.2,.7,.2,1) ' + (i * 120) + 'ms'; requestAnimationFrame(function () { rw.r.setAttribute('width', w); }); }); }
    onView(bud, grow);
    setTimeout(function () { rows.forEach(function (rw) { if (+rw.r.getAttribute('width') === 0) rw.r.setAttribute('width', x(rw.t.z) - x(rw.t.a)); }); }, 2500);
  })();

  /* ---------- 3. Onglets de la FAQ ---------- */
  var fq = document.querySelector('.iv-faq');
  if (fq) (function () {
    fq.classList.add('is-js');
    var tabs = [].slice.call(fq.querySelectorAll('[role=tab]'));
    function sel(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { sel(t); });
      t.addEventListener('keydown', function (e) {
        var k = e.key, n = null;
        if (k === 'ArrowRight' || k === 'ArrowDown') n = tabs[(i + 1) % tabs.length];
        if (k === 'ArrowLeft' || k === 'ArrowUp') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (n) { e.preventDefault(); sel(n, true); }
      });
    });
    var h = location.hash.slice(1), start = tabs.filter(function (t) { return t.id === 'ivt-' + h; })[0] || tabs[0];
    sel(start);
  })();

  /* ---------- 4. Apparition des étapes et chiffres clés ---------- */
  document.querySelectorAll('.iv-tl, .iv-keys').forEach(function (n) { onView(n, function () { n.classList.add('is-in'); }); });
})();
