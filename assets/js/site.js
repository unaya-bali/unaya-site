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
    function show(n) { cur = (n + imgs.length) % imgs.length; big.src = imgs[cur].getAttribute('data-full') || imgs[cur].currentSrc || imgs[cur].src; big.alt = imgs[cur].alt; }
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

// Prix « à partir de » des pages villas : lus automatiquement dans Beds24 (le prix écrit dans la page sert de secours)
(function () {
  var boxes = document.querySelectorAll('[data-prices]');
  if (!boxes.length || !window.fetch) return;
  fetch('/api/prices').then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
    if (!d) return;
    var fr = document.documentElement.lang === 'fr';
    var fmt = function (n) { return 'IDR ' + (fr ? String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') : Number(n).toLocaleString('en-US')); };
    boxes.forEach(function (box) {
      var v = d[box.getAttribute('data-prices')];
      if (!v) return;
      ['villa', 'room'].forEach(function (k) {
        box.querySelectorAll('[data-price="' + k + '"]').forEach(function (el) {
          if (v[k] > 0) el.textContent = fmt(v[k]);
          var idr = v[k] > 0 ? v[k] : +el.textContent.replace(/[^\d]/g, '');
          if (!d.fx || !d.fx.EUR || !idr || box.classList.contains('bk-bar')) return;
          var r5 = function (x) { return Math.max(5, Math.round(x / 5) * 5); };
          var e = r5(idr * d.fx.EUR), u = r5(idr * d.fx.USD), a = r5(idr * d.fx.AUD);
          var t = fr ? '≈ ' + e + ' € · ' + u + ' US$ · ' + a + ' A$' : '≈ €' + e + ' · US$' + u + ' · A$' + a;
          var s = el.parentNode.querySelector('.fx[data-for="' + k + '"]');
          if (!s) { s = document.createElement('span'); s.className = 'fx'; s.setAttribute('data-for', k); el.parentNode.appendChild(s); }
          s.textContent = t;
        });
      });
    });
  }).catch(function () {});
})();
// Barre de réservation mobile : masquée quand l'encadré de réservation est à l'écran
(function () {
  var bar = document.querySelector('.bk-bar'), box = document.getElementById('reserver');
  if (!bar || !box || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(function (e) { document.body.classList.toggle('bk-inview', e[0].isIntersecting); }, { threshold: 0.15 }).observe(box);
})();
// Passeport : afficher les fichiers choisis / photos prises
(function () {
  document.querySelectorAll('.sv-files').forEach(function (box) {
    var out = box.parentNode.querySelector('.sv-file-n'), fr = document.documentElement.lang !== 'en';
    box.querySelectorAll('input[type=file]').forEach(function (i) {
      i.addEventListener('change', function () {
        var n = 0, names = [];
        box.querySelectorAll('input[type=file]').forEach(function (x) { for (var k = 0; k < x.files.length; k++) { n++; names.push(x.files[k].name); } });
        out.textContent = n ? '✓ ' + n + (fr ? (n > 1 ? ' fichiers ajoutés' : ' fichier ajouté') : (n > 1 ? ' files added' : ' file added')) : '';
      });
    });
  });
})();

// Passeport obligatoire : bloquer l'envoi tant qu'aucune photo / aucun fichier n'est ajouté
(function () {
  document.querySelectorAll('.sv-files').forEach(function (box) {
    var form = box.closest('form'); if (!form) return;
    var out = box.parentNode.querySelector('.sv-file-n'), fr = document.documentElement.lang !== 'en';
    form.addEventListener('submit', function (e) {
      var n = 0; box.querySelectorAll('input[type=file]').forEach(function (x) { n += x.files.length; });
      if (!n) {
        e.preventDefault(); e.stopImmediatePropagation();
        out.style.color = '#B3261E';
        out.textContent = fr ? 'Merci d\'ajouter une photo du passeport (prenez une photo ou choisissez un fichier).' : 'Please add a photo of the passport (take a photo or choose a file).';
        box.scrollIntoView({ behavior: 'smooth', block: 'center' });
      } else { out.style.color = ''; }
    }, true);
  });
})();

// Fiches villas à vendre : date minimale des visites, partage et copie du lien
(function () {
  var today = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('input[data-mindate]').forEach(function (i) { i.min = today; });
  document.querySelectorAll('.ar-share').forEach(function (box) {
    var url = box.getAttribute('data-share-url'), title = box.getAttribute('data-share-title');
    if (navigator.share && window.matchMedia('(max-width: 760px)').matches) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'ar-native'; b.textContent = document.documentElement.lang === 'fr' ? 'Partager…' : 'Share…';
      b.addEventListener('click', function () { navigator.share({ title: title, url: url }).catch(function () {}); });
      box.appendChild(b);
    }
    var c = box.querySelector('.ar-copy');
    if (c) c.addEventListener('click', function () {
      var done = function () { var t = c.textContent; c.textContent = c.getAttribute('data-ok'); c.classList.add('is-ok'); setTimeout(function () { c.textContent = t; c.classList.remove('is-ok'); }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, done); else { var ta = document.createElement('textarea'); ta.value = url; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch (e) {} ta.remove(); done(); }
    });
  });
})();

// Vidéos de présentation : lecture quand elles sont à l'écran, bouton son
(function () {
  document.querySelectorAll('video[data-vid]').forEach(function (v) {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if ('IntersectionObserver' in window && !reduce) {
      new IntersectionObserver(function (e) { if (e[0].isIntersecting) { var p = v.play(); if (p) p.catch(function () {}); } else v.pause(); }, { threshold: 0.3 }).observe(v);
    } else { v.controls = true; }
    var box = v.closest('section'), b = box && box.querySelector('.ar-vid__snd');
    if (b) b.addEventListener('click', function () { v.muted = !v.muted; if (!v.muted) { var p = v.play(); if (p) p.catch(function () {}); } b.textContent = v.muted ? b.getAttribute('data-on') : b.getAttribute('data-off'); });
  });
})();
