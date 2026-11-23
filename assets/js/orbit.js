(function () {
  'use strict';
  var stage = document.getElementById('stage'); if (!stage) return;
  var PRODUCTS = [
    { img: 'weld-neck', tag: 'Flanges', title: 'Weld neck flanges', text: 'WNRF and RTJ for high-pressure and critical service.', alt: 'Black forged weld neck flange', url: '/flanges/weld-neck/', prod: 'Flanges' },
    { img: 'threaded', tag: 'Flanges', title: 'Threaded flanges', text: 'NPT screwed flanges where welding isn’t allowed – shown in stainless.', alt: 'Stainless steel threaded flange with four bolt holes', url: '/flanges/threaded/', prod: 'Flanges' },
    { img: 'slip-on', tag: 'Flanges', title: 'Slip-on flanges', text: 'SORF for low-pressure lines where cost and fit-up matter.', alt: 'Black forged slip-on flange', url: '/flanges/slip-on/', prod: 'Flanges' },
    { img: 'tees', tag: 'Buttweld fittings', title: 'Buttweld tees', text: 'Equal and reducing tees for branch lines – seamless to 24″, welded to 72″.', alt: 'Polished stainless steel buttweld tees', url: '/buttweld-fittings/tees/', prod: 'Buttweld fittings' },
    { img: 'blind', tag: 'Flanges', title: 'Blind flanges', text: 'Close pipe ends, valves and vessel nozzles.', alt: 'Black forged blind flange', url: '/flanges/blind/', prod: 'Flanges' },
    { img: 'b1647', tag: 'Flanges', title: 'Large-diameter flanges', text: 'ASME B16.47 for NPS 26 to 60 – packed for export.', alt: 'Large-diameter flanges stacked in the warehouse', url: '/flanges/', prod: 'Flanges' },
    { img: 'large-flange', tag: 'Flanges', title: 'Forged to 60″ and Class 2500', text: 'Every type, up to 60″ – in stainless, duplex, carbon, alloy and nickel alloys.', alt: 'Large black forged flange', url: '/flanges/', prod: 'Flanges' }
  ];
  var dotsEl = document.getElementById('dots');
  var n = PRODUCTS.length, step = 360 / n, rot = 0, vel = 0, dragging = false, moved = 0, lastX = 0, lastT = 0, idleUntil = 0, anim = null, active = -1, visible = true, hoverPause = false;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var autoSpeed = reduce ? 0 : 7;
  var cards = [], dots = [];

  PRODUCTS.forEach(function (p, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'orb-card'; b.setAttribute('aria-label', p.title);
    b.innerHTML = '<span class="frame"><img alt="" draggable="false"></span>';
    var im = b.querySelector('img'); im.src = '/assets/img/' + p.img + '.jpg'; im.alt = p.alt; im.width = 640; im.height = 640;
    if (i > 1) im.loading = 'lazy';
    var pic = document.createElement('picture');
    ['avif', 'webp'].forEach(function (t) { var so = document.createElement('source'); so.type = 'image/' + t; so.srcset = '/assets/img/' + p.img + '.' + t; pic.appendChild(so); });
    im.parentNode.insertBefore(pic, im); pic.appendChild(im);
    stage.appendChild(b); cards.push(b);
    b.addEventListener('click', function () { if (moved < 6) goTo(i); });
    var d = document.createElement('button'); d.type = 'button'; d.setAttribute('aria-label', 'Show ' + p.title);
    d.addEventListener('click', function () { goTo(i); }); dotsEl.appendChild(d); dots.push(d);
  });

  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function norm(a) { a = a % 360; return a < 0 ? a + 360 : a; }
  function layout() {
    var W = stage.clientWidth, cs = clamp(W * .27, 150, 280), Rx = Math.min(W * .37, 480), Ry = cs * .17, best = -1, bestC = -2;
    stage.style.setProperty('--cs', cs + 'px');
    for (var i = 0; i < n; i++) {
      var a = (i * step - rot) * Math.PI / 180, s = Math.sin(a), c = Math.cos(a), depth = (c + 1) / 2;
      var sc = .52 + .48 * depth, x = s * Rx, y = c * Ry - cs * .02, el = cards[i];
      el.style.transform = 'translate(-50%,-50%) translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px) scale(' + sc.toFixed(3) + ')';
      el.style.zIndex = Math.round(depth * 100);
      el.style.filter = 'brightness(' + (.34 + .66 * Math.pow(depth, 1.25)).toFixed(2) + ')';
      el.tabIndex = c > .85 ? 0 : -1;
      if (c > bestC) { bestC = c; best = i; }
    }
    if (best !== active) setActive(best);
  }
  function setActive(i) {
    active = i; var p = PRODUCTS[i];
    cards.forEach(function (el, k) { el.classList.toggle('is-front', k === i); el.setAttribute('aria-current', k === i ? 'true' : 'false'); });
    dots.forEach(function (d, k) { d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
    document.getElementById('capTag').textContent = p.tag;
    document.getElementById('capTitle').textContent = p.title;
    document.getElementById('capText').textContent = p.text;
    var l = document.getElementById('capLink'); l.href = p.url; l.dataset.prod = p.prod; l.dataset.title = p.title;
    var q = document.getElementById('capQuote'); if (q) q.href = '/request-a-quote/?product=' + encodeURIComponent(p.title);
  }
  function goTo(i) {
    var target = i * step, cur = norm(rot), delta = ((target - cur + 540) % 360) - 180;
    vel = 0; anim = { from: rot, to: rot + delta, t0: performance.now(), dur: reduce ? 1 : 650 }; idleUntil = performance.now() + 4500;
  }
  function stepBy(k) { goTo((active + k + n) % n); }
  var last = performance.now();
  function frame(now) {
    var dt = Math.min((now - last) / 1000, .05); last = now;
    if (anim) { var t = clamp((now - anim.t0) / anim.dur, 0, 1), e = 1 - Math.pow(1 - t, 3); rot = anim.from + (anim.to - anim.from) * e; if (t >= 1) anim = null; }
    else if (dragging) { }
    else if (Math.abs(vel) > 1) { rot += vel * dt; vel *= Math.pow(.04, dt); idleUntil = now + 2500; }
    else if (visible && now > idleUntil && !hoverPause) { rot += autoSpeed * dt; }
    rot = norm(rot); layout(); requestAnimationFrame(frame);
  }
  stage.addEventListener('mouseenter', function () { hoverPause = true; });
  stage.addEventListener('mouseleave', function () { hoverPause = false; });
  stage.addEventListener('focusin', function () { hoverPause = true; });
  stage.addEventListener('focusout', function () { hoverPause = false; });
  stage.addEventListener('pointerdown', function (e) {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    dragging = true; moved = 0; lastX = e.clientX; lastT = performance.now(); vel = 0; anim = null; stage.classList.add('dragging');
  });
  window.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    var dx = e.clientX - lastX, now = performance.now(), dtm = Math.max(now - lastT, 1);
    moved += Math.abs(dx);
    if (moved > 6 && !stage.hasPointerCapture(e.pointerId)) { try { stage.setPointerCapture(e.pointerId); } catch (_) { } }
    var deg = dx * .32; rot = norm(rot - deg); vel = -(deg / dtm) * 1000; lastX = e.clientX; lastT = now; idleUntil = now + 2500;
  });
  function endDrag() { if (!dragging) return; dragging = false; stage.classList.remove('dragging'); if (moved < 6) vel = 0; setTimeout(function () { moved = 0; }, 0); }
  window.addEventListener('pointerup', endDrag); window.addEventListener('pointercancel', endDrag);
  stage.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') { e.preventDefault(); stepBy(-1); } if (e.key === 'ArrowRight') { e.preventDefault(); stepBy(1); } });
  document.getElementById('prev').addEventListener('click', function () { stepBy(-1); });
  document.getElementById('next').addEventListener('click', function () { stepBy(1); });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(stage);
  window.addEventListener('resize', layout);
  layout(); requestAnimationFrame(frame);
})();
