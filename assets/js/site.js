// Unaya Management — scripts du site (sans dépendance)
(function () {
  // Menu mobile
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-toggle');
  if (toggle && header) {
    toggle.addEventListener('click', function () {
      var open = header.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Bloc réservation -> moteur Beds24
  document.querySelectorAll('form[data-beds24]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var inD = f.querySelector('[name=checkin]').value;
      var outD = f.querySelector('[name=checkout]').value;
      var guests = f.querySelector('[name=numadult]').value;
      var url = 'https://beds24.com/booking2.php?propid=' + f.dataset.beds24 + '&lang=' + document.documentElement.lang + '&numadult=' + guests;
      if (inD) url += '&checkin=' + inD;
      if (inD && outD) {
        var n = Math.round((new Date(outD) - new Date(inD)) / 86400000);
        if (n > 0) url += '&numnight=' + n;
      }
      window.open(url, '_blank', 'noopener');
    });
    var i = f.querySelector('[name=checkin]'), o = f.querySelector('[name=checkout]');
    var today = new Date().toISOString().slice(0, 10);
    i.min = today; o.min = today;
    i.addEventListener('change', function () { o.min = i.value; if (o.value && o.value <= i.value) o.value = ''; });
  });

  // Visionneuse photos des pages villas
  var imgs = Array.prototype.slice.call(document.querySelectorAll('[data-gallery] img'));
  if (imgs.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.innerHTML = '<button class="lb-close" aria-label="Fermer">×</button><button class="lb-prev" aria-label="Précédente">‹</button><img alt=""><button class="lb-next" aria-label="Suivante">›</button>';
    document.body.appendChild(lb);
    var big = lb.querySelector('img'), cur = 0;
    function show(n) { cur = (n + imgs.length) % imgs.length; big.src = imgs[cur].src; big.alt = imgs[cur].alt; }
    function open(n) { show(n); lb.classList.add('is-open'); lb.querySelector('.lb-close').focus(); }
    function close() { lb.classList.remove('is-open'); }
    imgs.forEach(function (im, n) { im.style.cursor = 'zoom-in'; im.addEventListener('click', function () { open(n); }); });
    document.querySelectorAll('[data-open-gallery]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); open(0); }); });
    lb.querySelector('.lb-close').onclick = close;
    lb.querySelector('.lb-prev').onclick = function () { show(cur - 1); };
    lb.querySelector('.lb-next').onclick = function () { show(cur + 1); };
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
  }

  // Fenêtres de demande (Services voyageurs)
  document.querySelectorAll('[data-open-dialog]').forEach(function (b) {
    b.addEventListener('click', function () {
      var d = document.getElementById(b.getAttribute('data-open-dialog'));
      if (d && d.showModal) { d.showModal(); var f = d.querySelector('input:not([type=hidden])'); if (f) f.focus(); }
    });
  });
  document.querySelectorAll('dialog.svc-dialog').forEach(function (d) {
    d.querySelectorAll('[data-close-dialog]').forEach(function (c) { c.addEventListener('click', function () { d.close(); }); });
    d.addEventListener('click', function (e) { if (e.target === d) d.close(); });
  });
  if (location.hash) {
    var h = document.getElementById('d-' + location.hash.slice(1));
    if (h && h.showModal) h.showModal();
  }
})();
