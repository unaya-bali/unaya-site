/* Graphiques des fiches villas à vendre (Arawa). Sans bibliothèque : SVG + CSS.
   Données lues dans les attributs data-* posés par le générateur (tools/arawa.py). */
(function () {
  'use strict';
  var cfgEl = document.querySelector('[data-arawa]');
  if (!cfgEl) return;
  var root = document;
  var FR = document.documentElement.lang === 'fr';
  var cfg = JSON.parse(cfgEl.getAttribute('data-arawa'));
  var NS = 'http://www.w3.org/2000/svg';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var COL = { net: '#0E9180', ota: '#7B4374', tax: '#C9753F', ink: '#2E2429', muted: '#7A6A72', grid: '#E6DCD4', main: '#3F2A3A', soft: '#D2A48C' };

  function fmt(n, d) { return Number(n).toLocaleString(FR ? 'fr-FR' : 'en-US', { maximumFractionDigits: d || 0, minimumFractionDigits: d || 0 }).replace(/ /g, ' '); }
  function usd(n) { return FR ? fmt(n) + ' $' : '$' + fmt(n); }
  function el(tag, attrs, parent) { var e = document.createElementNS(NS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function onView(node, fn) {
    if (!('IntersectionObserver' in window) || reduce) { fn(); return; }
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); fn(); } }, { threshold: 0.25 });
    io.observe(node);
  }
  function countUp(node, to, render) {
    var from = parseFloat(node.getAttribute('data-v') || '0');
    node.setAttribute('data-v', to);
    if (reduce || document.hidden) { node.textContent = render(to); return; }
    clearTimeout(node._cxT); node._cxT = setTimeout(function () { node.textContent = render(to); }, 900); // sécurité si l'animation ne tourne pas
    var t0 = null, dur = 650;
    function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3); node.textContent = render(from + (to - from) * e); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }

  // Infobulle partagée
  var tip = document.createElement('div'); tip.className = 'cx-tip'; tip.setAttribute('role', 'status'); document.body.appendChild(tip);
  function showTip(html, x, y) { tip.innerHTML = html; tip.classList.add('is-on'); var r = tip.getBoundingClientRect(); var left = Math.min(window.innerWidth - r.width - 8, Math.max(8, x - r.width / 2)); var top = y - r.height - 14; if (top < 8) top = y + 18; tip.style.transform = 'translate(' + left + 'px,' + top + 'px)'; }
  function hideTip() { tip.classList.remove('is-on'); }
  function bindTip(node, html) {
    node.addEventListener('mousemove', function (e) { showTip(typeof html === 'function' ? html() : html, e.clientX, e.clientY); });
    node.addEventListener('mouseleave', hideTip);
    node.addEventListener('focus', function () { var r = node.getBoundingClientRect(); showTip(typeof html === 'function' ? html() : html, r.left + r.width / 2, r.top); });
    node.addEventListener('blur', hideTip);
  }

  /* ---------- 1. Simulateur de revenus locatifs ---------- */
  var sim = root.querySelector('.cx-sim:not(.ld-calc)');
  if (sim) {
    var price = cfg.price, years = cfg.lease;
    var rate = sim.querySelector('[name=rate]'), occ = sim.querySelector('[name=occ]');
    var outRate = sim.querySelector('[data-out=rate]'), outOcc = sim.querySelector('[data-out=occ]'), outNights = sim.querySelector('[data-out=nights]');
    var k = { rev: sim.querySelector('[data-k=rev]'), net: sim.querySelector('[data-k=net]'), yld: sim.querySelector('[data-k=yld]'), pay: sim.querySelector('[data-k=pay]') };
    var donut = sim.querySelector('.cx-donut'), legend = sim.querySelector('.cx-dleg'), area = sim.querySelector('.cx-area');
    var SPLIT = [{ id: 'net', share: 0.5, c: COL.net, l: FR ? 'Revenu net pour vous' : 'Net income for you' },
                 { id: 'ota', share: 0.3, c: COL.ota, l: FR ? 'Plateformes (15 %) et gestion (15 %)' : 'Platforms (15%) and management (15%)' },
                 { id: 'tax', share: 0.2, c: COL.tax, l: FR ? 'Taxe (10 %) et frais d’exploitation (10 %)' : 'Tax (10%) and running costs (10%)' }];

    // donut
    var dsv = el('svg', { viewBox: '0 0 200 200', role: 'img', 'aria-label': FR ? 'Répartition des revenus annuels' : 'Split of annual revenue' }, donut);
    var R = 78, C = 2 * Math.PI * R, GAP = 2.5;
    el('circle', { cx: 100, cy: 100, r: R, fill: 'none', stroke: '#F3ECE6', 'stroke-width': 26 }, dsv);
    var arcs = SPLIT.map(function (s) {
      var a = el('circle', { cx: 100, cy: 100, r: R, fill: 'none', stroke: s.c, 'stroke-width': 26, 'stroke-dasharray': '0 ' + C, transform: 'rotate(-90 100 100)', tabindex: 0, class: 'cx-arc' }, dsv);
      return a;
    });
    var dc = el('text', { x: 100, y: 96, 'text-anchor': 'middle', class: 'cx-dc-v' }, dsv);
    var dl = el('text', { x: 100, y: 120, 'text-anchor': 'middle', class: 'cx-dc-l' }, dsv); dl.textContent = FR ? 'revenus / an' : 'revenue / year';
    legend.innerHTML = SPLIT.map(function (s, i) { return '<li data-i="' + i + '"><i style="background:' + s.c + '"></i><span>' + s.l + '</span><b data-leg="' + s.id + '"></b></li>'; }).join('');

    var cur = {};
    function drawDonut(rev, animate) {
      var off = 0;
      SPLIT.forEach(function (s, i) {
        var len = Math.max(0, s.share * C - GAP);
        arcs[i].style.transition = animate && !reduce ? 'stroke-dasharray .8s cubic-bezier(.2,.7,.2,1), stroke-dashoffset .8s cubic-bezier(.2,.7,.2,1)' : 'none';
        arcs[i].setAttribute('stroke-dasharray', len + ' ' + (C - len));
        arcs[i].setAttribute('stroke-dashoffset', -off);
        off += s.share * C;
        legend.querySelector('[data-leg=' + s.id + ']').textContent = usd(Math.round(rev * s.share));
      });
      dc.textContent = usd(Math.round(rev));
    }
    SPLIT.forEach(function (s, i) {
      bindTip(arcs[i], function () { return '<b>' + s.l + '</b><br>' + usd(Math.round(cur.rev * s.share)) + (FR ? ' / an · ' : ' / year · ') + Math.round(s.share * 100) + ' %'; });
      [arcs[i], legend.querySelector('[data-i="' + i + '"]')].forEach(function (n) {
        n.addEventListener('mouseenter', function () { sim.classList.add('is-focus'); arcs[i].classList.add('is-hl'); legend.querySelector('[data-i="' + i + '"]').classList.add('is-hl'); });
        n.addEventListener('mouseleave', function () { sim.classList.remove('is-focus'); arcs[i].classList.remove('is-hl'); legend.querySelector('[data-i="' + i + '"]').classList.remove('is-hl'); });
      });
    });

    // courbe cumulée sur la durée du bail
    function drawArea(net, animate) {
      area.innerHTML = '';
      var W = Math.max(320, area.clientWidth), H = W < 520 ? 240 : Math.max(280, Math.min(420, area.clientHeight || 280)), m = { l: 56, r: 16, t: 18, b: 34 };
      var sv = el('svg', { viewBox: '0 0 ' + W + ' ' + H, width: '100%', height: H, role: 'img', 'aria-label': FR ? 'Revenu net cumulé sur la durée du bail' : 'Cumulative net income over the lease' }, area);
      var maxY = Math.max(price * 1.15, net * years), x = function (y) { return m.l + (W - m.l - m.r) * (y / years); }, yv = function (v) { return H - m.b - (H - m.t - m.b) * (v / maxY); };
      var step = maxY > 1e6 ? 250000 : maxY > 400000 ? 100000 : 50000;
      for (var g = 0; g <= maxY; g += step) {
        el('line', { x1: m.l, x2: W - m.r, y1: yv(g), y2: yv(g), stroke: COL.grid, 'stroke-width': 1 }, sv);
        var t = el('text', { x: m.l - 8, y: yv(g) + 4, 'text-anchor': 'end', class: 'cx-ax' }, sv); t.textContent = g === 0 ? '0' : (FR ? fmt(g / 1000) + ' k$' : '$' + fmt(g / 1000) + 'k');
      }
      [0, 5, 10, 15, 20, 25, years].forEach(function (yy) { if (yy > years) return; var t = el('text', { x: x(yy), y: H - m.b + 20, 'text-anchor': 'middle', class: 'cx-ax' }, sv); t.textContent = yy === 0 ? '' : (FR ? 'an ' + yy : 'yr ' + yy); });
      // ligne du prix
      el('line', { x1: m.l, x2: W - m.r, y1: yv(price), y2: yv(price), stroke: COL.main, 'stroke-width': 1.5, 'stroke-dasharray': '5 5' }, sv);
      var pl = el('text', { x: W - m.r, y: yv(price) - 8, 'text-anchor': 'end', class: 'cx-ax cx-ax--b' }, sv); pl.textContent = (FR ? 'Prix de la villa · ' : 'Villa price · ') + usd(price);
      // aire
      var pts = []; for (var y = 0; y <= years; y++) pts.push([x(y), yv(net * y)]);
      var d = 'M' + pts.map(function (p) { return p[0].toFixed(1) + ' ' + p[1].toFixed(1); }).join(' L');
      var gid = 'cxg' + Math.random().toString(36).slice(2, 7);
      var defs = el('defs', {}, sv), lg = el('linearGradient', { id: gid, x1: 0, y1: 0, x2: 0, y2: 1 }, defs);
      el('stop', { offset: '0%', 'stop-color': COL.net, 'stop-opacity': 0.28 }, lg); el('stop', { offset: '100%', 'stop-color': COL.net, 'stop-opacity': 0.02 }, lg);
      var clip = el('clipPath', { id: gid + 'c' }, defs), cr = el('rect', { x: 0, y: 0, width: animate && !reduce ? 0 : W, height: H }, clip);
      el('path', { d: d + ' L' + x(years) + ' ' + yv(0) + ' L' + x(0) + ' ' + yv(0) + ' Z', fill: 'url(#' + gid + ')', 'clip-path': 'url(#' + gid + 'c)' }, sv);
      el('path', { d: d, fill: 'none', stroke: COL.net, 'stroke-width': 2, 'clip-path': 'url(#' + gid + 'c)' }, sv);
      if (animate && !reduce) { cr.style.transition = 'width 1.1s cubic-bezier(.2,.7,.2,1)'; requestAnimationFrame(function () { requestAnimationFrame(function () { cr.setAttribute('width', W); }); }); }
      // point d'équilibre
      var be = price / net;
      if (be <= years) {
        var bx = x(be), by = yv(price);
        el('line', { x1: bx, x2: bx, y1: by, y2: H - m.b, stroke: COL.net, 'stroke-width': 1, 'stroke-dasharray': '2 4' }, sv);
        el('circle', { cx: bx, cy: by, r: 6, fill: '#fff', stroke: COL.net, 'stroke-width': 2.5, class: 'cx-be' }, sv);
        var bt = el('text', { x: Math.min(W - m.r - 4, Math.max(m.l + 4, bx)), y: by - 14, 'text-anchor': bx > W - 140 ? 'end' : bx < m.l + 120 ? 'start' : 'middle', class: 'cx-ax cx-ax--n' }, sv);
        bt.textContent = (FR ? 'Prix couvert en ' : 'Price covered in ') + fmt(be, 1) + (FR ? ' ans' : ' yrs');
      }
      // survol : réticule + infobulle par année
      var cross = el('line', { y1: m.t, y2: H - m.b, stroke: COL.ink, 'stroke-width': 1, opacity: 0 }, sv);
      var dot = el('circle', { r: 5, fill: COL.net, stroke: '#fff', 'stroke-width': 2, opacity: 0 }, sv);
      var hit = el('rect', { x: m.l, y: m.t, width: W - m.l - m.r, height: H - m.t - m.b, fill: 'transparent' }, sv);
      function at(ev) {
        var r = sv.getBoundingClientRect(), px = (ev.clientX - r.left) * (W / r.width);
        var yy = Math.max(1, Math.min(years, Math.round((px - m.l) / (W - m.l - m.r) * years)));
        cross.setAttribute('x1', x(yy)); cross.setAttribute('x2', x(yy)); cross.setAttribute('opacity', 0.25);
        dot.setAttribute('cx', x(yy)); dot.setAttribute('cy', yv(net * yy)); dot.setAttribute('opacity', 1);
        showTip('<b>' + (FR ? 'Année ' : 'Year ') + yy + '</b><br>' + (FR ? 'Net cumulé : ' : 'Cumulative net: ') + usd(Math.round(net * yy)) + '<br><span>' + (net * yy >= price ? (FR ? 'Prix couvert' : 'Price covered') : (FR ? 'Reste ' : 'Remaining ') + usd(Math.round(price - net * yy))) + '</span>', ev.clientX, r.top + (dot.getAttribute('cy') * r.height / H));
      }
      hit.addEventListener('mousemove', at); hit.addEventListener('touchmove', function (e) { at(e.touches[0]); }, { passive: true });
      hit.addEventListener('mouseleave', function () { cross.setAttribute('opacity', 0); dot.setAttribute('opacity', 0); hideTip(); });
    }

    function update(animate) {
      var r = +rate.value, o = +occ.value / 100, nights = Math.round(365 * o), rev = r * nights, net = rev * 0.5;
      cur = { rev: rev, net: net };
      outRate.textContent = usd(r); outOcc.textContent = Math.round(o * 100) + ' %'; outNights.textContent = fmt(nights);
      [rate, occ].forEach(function (s) { s.style.setProperty('--p', ((s.value - s.min) / (s.max - s.min) * 100) + '%'); });
      countUp(k.rev, rev, function (v) { return usd(Math.round(v)); });
      countUp(k.net, net, function (v) { return usd(Math.round(v)); });
      countUp(k.yld, net / price * 100, function (v) { return fmt(v, 1) + ' %'; });
      countUp(k.pay, price / net, function (v) { return fmt(v, 1) + (FR ? ' ans' : ' yrs'); });
      drawDonut(rev, animate); drawArea(net, animate);
      sim.querySelectorAll('[data-preset]').forEach(function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-preset') === Math.round(o * 100) && r === 175 ? 'true' : 'false'); });
    }
    var raf;
    [rate, occ].forEach(function (s) { s.addEventListener('input', function () { cancelAnimationFrame(raf); raf = requestAnimationFrame(function () { update(false); }); }); });
    sim.querySelectorAll('[data-preset]').forEach(function (b) { b.addEventListener('click', function () { occ.value = b.getAttribute('data-preset'); rate.value = 175; update(true); }); });
    var rw; window.addEventListener('resize', function () { clearTimeout(rw); rw = setTimeout(function () { drawArea(cur.net, false); }, 150); });
    update(false);
    onView(sim, function () { drawDonut(0, false); requestAnimationFrame(function () { update(true); }); });
  }

  /* ---------- 1 bis. Calculateur de prix des terrains ---------- */
  var lc = root.querySelector('.ld-calc');
  if (lc) {
    var c = JSON.parse(lc.getAttribute('data-calc')), ar = lc.querySelector('[name=ares]'), mode = 'lease';
    var kk = { tot: lc.querySelector('[data-k=tot]'), usd: lc.querySelector('[data-k=usd]'), foot: lc.querySelector('[data-k=foot]'), floor: lc.querySelector('[data-k=floor]') };
    var bar = lc.querySelector('.ld-calc__bar'), built = lc.querySelector('.ld-calc__built'), freeNote = lc.querySelector('.ld-calc__free');
    var idr = function (n) { return 'IDR ' + fmt(Math.round(n)); };
    function upd() {
      var a = mode === 'free' ? c.max : +ar.value; if (mode === 'free') ar.value = c.max;
      ar.disabled = mode === 'free'; freeNote.hidden = mode !== 'free';
      ar.style.setProperty('--p', ((ar.value - ar.min) / (ar.max - ar.min) * 100) + '%');
      var tot = mode === 'free' ? a * c.free : a * c.rate * c.years, m2v = a * 100;
      lc.querySelector('[data-out=ares]').textContent = fmt(a, 2) + (FR ? ' ares' : ' ares');
      lc.querySelector('[data-out=m2]').textContent = fmt(m2v);
      countUp(kk.tot, tot, idr);
      countUp(kk.usd, tot / c.fx, function (v) { return usd(Math.round(v / 100) * 100); });
      countUp(kk.foot, m2v * 0.5, function (v) { return fmt(Math.round(v)) + ' m²'; });
      countUp(kk.floor, m2v * 2, function (v) { return fmt(Math.round(v)) + ' m²'; });
      var w = 400 * a / c.max; bar.setAttribute('width', w); built.setAttribute('width', w / 2);
      lc.querySelectorAll('[data-mode]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-mode') === mode ? 'true' : 'false'); });
    }
    ar.addEventListener('input', upd);
    lc.querySelectorAll('[data-mode]').forEach(function (b) { b.addEventListener('click', function () { mode = b.getAttribute('data-mode'); upd(); }); });
    upd();
  }

  /* ---------- 2. Barres horizontales animées (comparaison, surfaces, distances) ---------- */
  root.querySelectorAll('.cx-bars').forEach(function (box) {
    var rows = JSON.parse(box.getAttribute('data-rows')), unit = box.getAttribute('data-unit') || '';
    var max = Math.max.apply(null, rows.map(function (r) { return r.v; }));
    box.innerHTML = rows.map(function (r, i) {
      return '<div class="cx-br' + (r.hl ? ' is-hl' : '') + '" tabindex="0" data-i="' + i + '"><span class="cx-br__l">' + r.l + '</span><span class="cx-br__t"><span class="cx-br__f" style="--w:' + (r.v / max * 100).toFixed(1) + '%;--d:' + (i * 70) + 'ms"></span></span><span class="cx-br__v">' + (r.t || fmt(r.v, r.dec || 0) + unit) + '</span></div>';
    }).join('');
    box.querySelectorAll('.cx-br').forEach(function (n) { var r = rows[+n.getAttribute('data-i')]; if (r.tip) bindTip(n, r.tip); });
    onView(box, function () { box.classList.add('is-in'); });
  });

  /* ---------- 3. Avancement du chantier ---------- */
  root.querySelectorAll('.cx-ring').forEach(function (box) {
    var pct = +box.getAttribute('data-pct'), sv = el('svg', { viewBox: '0 0 120 120', role: 'img', 'aria-label': box.getAttribute('data-label') }, box);
    var R2 = 50, C2 = 2 * Math.PI * R2;
    el('circle', { cx: 60, cy: 60, r: R2, fill: 'none', stroke: '#EFE6DF', 'stroke-width': 10 }, sv);
    var a = el('circle', { cx: 60, cy: 60, r: R2, fill: 'none', stroke: COL.net, 'stroke-width': 10, 'stroke-linecap': 'round', 'stroke-dasharray': '0 ' + C2, transform: 'rotate(-90 60 60)' }, sv);
    var t = el('text', { x: 60, y: 66, 'text-anchor': 'middle', class: 'cx-ring__v' }, sv); t.textContent = box.getAttribute('data-text');
    onView(box, function () { a.style.transition = reduce ? 'none' : 'stroke-dasharray 1.4s cubic-bezier(.2,.7,.2,1)'; a.setAttribute('stroke-dasharray', (C2 * pct / 100) + ' ' + C2); box.closest('.cx-prog').classList.add('is-in'); });
  });
})();
