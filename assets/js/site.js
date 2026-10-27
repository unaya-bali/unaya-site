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

  // Formule choisie sur la page Tarifs -> présélection dans « Confier ma villa »
  var fq = new URLSearchParams(location.search).get('formule');
  var fs = document.querySelector('select[name=formule_souhaitee], select[name=preferred_plan]');
  if (fq && fs) {
    fs.selectedIndex = fq === 'marketing' ? 1 : 0;
    var ff = fs.closest('form'); if (ff) ff.scrollIntoView({ block: 'start' });
  }

  // Demande de disponibilité sur WhatsApp (tant que la réservation en ligne n'est pas ouverte)
  document.querySelectorAll('form[data-wa]').forEach(function (f) {
    var i = f.querySelector('[name=checkin]'), o = f.querySelector('[name=checkout]');
    var today = new Date().toISOString().slice(0, 10);
    i.min = today; o.min = today;
    i.addEventListener('change', function () { o.min = i.value; if (o.value && o.value <= i.value) o.value = ''; });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var fr = document.documentElement.lang === 'fr';
      var fmt = function (d) { if (!d) return ''; var p = d.split('-'); return p[2] + '/' + p[1] + '/' + p[0]; };
      var g = f.querySelector('[name=numadult]').value;
      var msg = fr
        ? 'Bonjour, je souhaite réserver ' + f.dataset.villa + ' du ' + fmt(i.value) + ' au ' + fmt(o.value) + ' pour ' + g + ' voyageur(s). Est-ce disponible ? Merci !'
        : 'Hello, I would like to book ' + f.dataset.villa + ' from ' + fmt(i.value) + ' to ' + fmt(o.value) + ' for ' + g + ' guest(s). Is it available? Thank you!';
      window.open('https://wa.me/' + f.dataset.wa + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    });
  });
})();
(function(){var a=document.querySelector('.subnav a[aria-current="page"]');if(a&&a.parentElement.scrollWidth>a.parentElement.clientWidth){a.parentElement.scrollLeft=a.offsetLeft-16;}})();
(function(){var t=String(Date.now());document.querySelectorAll('form[action="/api/form"]').forEach(function(f){var i=document.createElement('input');i.type='hidden';i.name='t_ok';i.value=t;f.appendChild(i);});})();
(function(){var f=document.querySelector('.vl-filters');if(!f)return;var cards=document.querySelectorAll('.vl-card'),none=document.querySelector('.vl-none');
f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var z=b.getAttribute('data-zone'),n=0;
f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
cards.forEach(function(c){var ok=z==='all'||c.getAttribute('data-zone')===z;c.hidden=!ok;if(ok)n++;});if(none)none.hidden=n>0;});})();
(function(){document.querySelectorAll('input[type=file][data-max]').forEach(function(i){i.addEventListener('change',function(){var m=+i.getAttribute('data-max'),t=0;for(var k=0;k<i.files.length;k++)t+=i.files[k].size;var fr=document.documentElement.lang!=='en';if(i.files.length>m||t>10*1024*1024){alert(fr?'Maximum '+m+' photos et 10 Mo au total.':'Maximum '+m+' photos and 10 MB in total.');i.value='';}});});})();
