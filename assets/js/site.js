(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- analytics (optional; set IDs in assets/js/config.js) ---------- */
  var CFG = window.NEO_CONFIG || {};
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  if (CFG.ga4) {
    var s = document.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CFG.ga4);
    document.head.appendChild(s);
    gtag('js', new Date()); gtag('config', CFG.ga4);
  }
  function track(name, params) { if (CFG.ga4) { gtag('event', name, params || {}); } }

  /* ---------- header + nav ---------- */
  var hdr = document.querySelector('header.site');
  function onScroll() { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var btn = document.getElementById('menuBtn'), nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var o = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', o); btn.setAttribute('aria-label', o ? 'Close menu' : 'Open menu');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  /* ---------- mobile submenus ---------- */
  [].forEach.call(document.querySelectorAll('.subtoggle'), function (t) {
    t.addEventListener('click', function () {
      var li = t.parentNode, o = li.classList.toggle('open'); t.setAttribute('aria-expanded', o);
    });
  });

  /* ---------- reveal on scroll ---------- */
  var rv = [].slice.call(document.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: .1, rootMargin: '0px 0px -40px 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- print buttons ---------- */
  [].forEach.call(document.querySelectorAll('[data-print]'), function (b) {
    b.addEventListener('click', function () { track('datasheet_print', { page: location.pathname }); window.print(); });
  });

  /* ---------- lead forms ---------- */
  var ENDPOINT = '/api/enquiry.php';
  var MAXFILE = 8 * 1024 * 1024;
  function qs(name) { var m = new RegExp('[?&]' + name + '=([^&]*)').exec(location.search); return m ? decodeURIComponent(m[1].replace(/\+/g, ' ')) : ''; }

  function setMsg(form, text, kind) {
    var st = form.querySelector('.status'); if (!st) return;
    st.hidden = !text; st.textContent = text || ''; st.className = 'status' + (kind ? ' ' + kind : '');
  }
  function fieldErr(el, text) {
    var msg = el.parentNode.querySelector('.msg');
    el.classList.toggle('err', !!text); el.setAttribute('aria-invalid', text ? 'true' : 'false');
    if (msg) msg.textContent = text || '';
  }
  function validate(form) {
    var ok = true;
    var name = form.elements['name'], email = form.elements['email'];
    var v = (name.value || '').trim();
    fieldErr(name, v ? '' : 'Please enter your name.'); if (!v) ok = false;
    var e = (email.value || '').trim();
    var bad = !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e);
    fieldErr(email, bad ? 'Please enter a valid email address.' : ''); if (bad) ok = false;
    var f = form.elements['boq'];
    if (f && f.files && f.files[0] && f.files[0].size > MAXFILE) { setMsg(form, 'The attached file is larger than 8 MB. Please email it to kartik@neoimpex.com instead.', 'err'); ok = false; }
    return ok;
  }
  function summary(form) {
    var fd = new FormData(form), rows = [];
    ['name', 'company', 'email', 'phone', 'country', 'product', 'material', 'size', 'delivery', 'message'].forEach(function (k) {
      var v = (fd.get(k) || '').toString().trim(); if (v) rows.push(k.charAt(0).toUpperCase() + k.slice(1) + ': ' + v);
    });
    return rows.join('\n');
  }
  function mailtoFallback(form) {
    var subj = 'Quote request – ' + (form.elements['product'] ? form.elements['product'].value : 'Neo Impex') + ' – ' + (form.elements['name'].value || '').trim();
    window.location.href = 'mailto:kartik@neoimpex.com?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(summary(form) + '\n\n(Page: ' + location.href + ')');
  }

  [].forEach.call(document.querySelectorAll('form.lead-form'), function (form) {
    // context fields
    function set(n, v) { var el = form.elements[n]; if (el) el.value = v; }
    set('page', location.href); set('referrer', document.referrer || '');
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'gclid'].forEach(function (k) { set(k, qs(k)); });
    set('started', String(Date.now()));
    var wa = form.querySelector('[data-wa]');
    if (wa) wa.addEventListener('click', function () {
      if (!validate(form)) return;
      track('lead_whatsapp', { page: location.pathname });
      window.open('https://wa.me/919316631458?text=' + encodeURIComponent('Hello Neo Impex, quote request:\n' + summary(form)), '_blank', 'noopener');
    });
    form.addEventListener('submit', function (ev) {
      ev.preventDefault(); setMsg(form, '');
      if (!validate(form)) return;
      var submit = form.querySelector('button[type=submit]'); var label = submit ? submit.textContent : '';
      if (submit) { submit.disabled = true; submit.textContent = 'Sending…'; }
      var started = Number((form.elements['started'] || {}).value) || Date.now();
      var wait = Math.max(0, 2700 - (Date.now() - started));
      var fd = new FormData(form);
      new Promise(function (r) { setTimeout(r, wait); })
        .then(function () { return fetch(ENDPOINT, { method: 'POST', body: fd, headers: { 'Accept': 'application/json' } }); })
        .then(function (r) { return r.json().then(function (j) { return { status: r.status, body: j }; }); })
        .then(function (res) {
          if (res.body && res.body.ok) {
            track('generate_lead', { page: location.pathname, product: (form.elements['product'] || {}).value || '' });
            form.reset(); set('page', location.href); set('started', String(Date.now()));
            setMsg(form, 'Thank you. We have your enquiry and will reply within 24 business hours.', 'ok');
          } else {
            setMsg(form, (res.body && res.body.error) || 'Sorry, we could not send your enquiry. Please try again or email kartik@neoimpex.com.', 'err');
          }
        })
        .catch(function () {
          setMsg(form, 'We could not reach our server. Opening your email app instead…', 'err');
          mailtoFallback(form);
        })
        .then(function () { if (submit) { submit.disabled = false; submit.textContent = label; } });
    });
  });

  /* prefill product from ?product= on the quote page */
  var pre = qs('product');
  if (pre) { [].forEach.call(document.querySelectorAll('form.lead-form'), function (form) {
    var m = form.elements['message']; if (m && !m.value) m.value = 'Enquiry about: ' + pre + '\n';
    var sel = form.elements['product'];
    if (sel) {
      var t = pre.toLowerCase(), want = '';
      if (/data sheet|catalogue/.test(t)) want = 'Data sheet / catalogue';
      else if (/flange/.test(t)) want = /fitting/.test(t) ? 'Buttweld fittings and flanges' : 'Flanges';
      else if (/fitting|elbow|tee|reducer|cap|stub|cross|bend/.test(t)) want = 'Buttweld fittings';
      for (var i = 0; i < sel.options.length; i++) { if (sel.options[i].text === want) sel.selectedIndex = i; }
    }
  }); }

  /* track outbound contact clicks */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]'); if (!a) return;
    var h = a.getAttribute('href');
    if (h.indexOf('wa.me') > -1) track('click_whatsapp', { page: location.pathname });
    else if (h.indexOf('mailto:') === 0) track('click_email', { page: location.pathname });
    else if (h.indexOf('tel:') === 0) track('click_phone', { page: location.pathname });
  });
})();
