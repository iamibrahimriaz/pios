/* ==========================================================================
   PIOS — Product Intelligence OS
   Landing page behaviour
   ========================================================================== */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------------
     Theme toggle — remembers the viewer's choice, defaults to the OS
     ------------------------------------------------------------------ */
  var root = document.documentElement;

  // Three states, cycled in this order. "system" is the default and is stored
  // as the absence of data-theme, so the media query decides.
  var MODES = ['system', 'light', 'dark'];
  var LABEL = {
    system: 'Theme: follow system. Switch to light.',
    light: 'Theme: light. Switch to dark.',
    dark: 'Theme: dark. Switch to follow system.'
  };

  var mode = 'system';
  try {
    var saved = localStorage.getItem('pios-theme');
    if (MODES.indexOf(saved) !== -1) mode = saved;
  } catch (e) { /* private mode — stay on system */ }

  var themeBtn = document.getElementById('theme');

  function applyMode(next, persist) {
    mode = next;
    if (mode === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', mode);
    if (themeBtn) themeBtn.setAttribute('aria-label', LABEL[mode]);
    if (persist) {
      try { localStorage.setItem('pios-theme', mode); } catch (e) { /* ignore */ }
    }
    if (window.piosGraph) window.piosGraph.recolor();
  }

  applyMode(mode, false);

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      applyMode(MODES[(MODES.indexOf(mode) + 1) % MODES.length], true);
    });
  }

  /* ------------------------------------------------------------------
     Mobile menu
     ------------------------------------------------------------------ */
  (function () {
    var toggle = document.getElementById('navToggle');
    var panel = document.getElementById('navLinks');
    if (!toggle || !panel) return;

    function setOpen(open) {
      panel.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    panel.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    // The panel is a mobile affordance only; never leave it open on a wide screen.
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 860) setOpen(false);
    });
  })();

  /* ------------------------------------------------------------------
     Scrollspy — mark the section currently being read, and show how far
     through the page the reader is. Both read the same scroll position.
     ------------------------------------------------------------------ */
  (function () {
    var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a[href^="#"]'));
    var prog = document.getElementById('navProg');
    if (!links.length && !prog) return;

    var targets = links.map(function (a) {
      return { link: a, el: document.querySelector(a.getAttribute('href')) };
    }).filter(function (t) { return t.el; });

    var navH = 62;
    var ticking = false;
    var activeLink = null;

    function apply() {
      ticking = false;
      var y = window.pageYOffset || document.documentElement.scrollTop;
      var docH = document.documentElement.scrollHeight - window.innerHeight;

      if (prog) {
        var p = docH > 0 ? Math.min(1, Math.max(0, y / docH)) : 0;
        prog.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      }

      // The current section is the last one whose top has passed the nav.
      var probe = y + navH + 24;
      var found = null;
      for (var i = 0; i < targets.length; i++) {
        if (targets[i].el.offsetTop <= probe) found = targets[i];
      }
      // At the very bottom the last section wins even if it is short.
      if (docH > 0 && y >= docH - 2) found = targets[targets.length - 1];

      var next = found ? found.link : null;
      if (next === activeLink) return;
      if (activeLink) { activeLink.classList.remove('active'); activeLink.removeAttribute('aria-current'); }
      if (next) { next.classList.add('active'); next.setAttribute('aria-current', 'true'); }
      activeLink = next;
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(apply);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    apply();
  })();

  /* ------------------------------------------------------------------
     Copy the install commands
     ------------------------------------------------------------------ */
  Array.prototype.forEach.call(document.querySelectorAll('.copy'), function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy') || '';
      var done = function () {
        btn.textContent = 'Copied';
        btn.classList.add('done');
        setTimeout(function () {
          btn.textContent = 'Copy';
          btn.classList.remove('done');
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { /* ignore */ });
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); } catch (e) { /* ignore */ }
        document.body.removeChild(ta);
      }
    });
  });

  /* ------------------------------------------------------------------
     Count up the figures once they are on screen
     ------------------------------------------------------------------ */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && !reduced && 'IntersectionObserver' in window) {
    var cObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        cObs.unobserve(el);
        var target = parseInt(el.getAttribute('data-count'), 10);
        if (isNaN(target)) return;
        var t0 = performance.now();
        var dur = 900;
        (function step(now) {
          var k = Math.min(1, (now - t0) / dur);
          var eased = 1 - Math.pow(1 - k, 3);
          el.textContent = String(Math.round(target * eased));
          if (k < 1) requestAnimationFrame(step);
        })(t0);
      });
    }, { threshold: 0.6 });
    Array.prototype.forEach.call(counters, function (el) { cObs.observe(el); });
  }

  /* ------------------------------------------------------------------
     Reveal on scroll — added by JS only, so no-JS keeps everything visible
     ------------------------------------------------------------------ */
  if (!reduced && 'IntersectionObserver' in window) {
    var targets = document.querySelectorAll('section > .wrap > *');
    if (targets.length) {
      root.classList.add('js-reveal');
      Array.prototype.forEach.call(targets, function (el) { el.classList.add('reveal'); });
      var showAll = function () {
        Array.prototype.forEach.call(targets, function (el) { el.classList.add('in'); });
      };
      var rObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); rObs.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      Array.prototype.forEach.call(targets, function (el) { rObs.observe(el); });
      // Failsafe: never leave content hidden if anything goes wrong.
      setTimeout(showAll, 2600);
    }
  }

  /* ==================================================================
     Dependency graph
     The nodes, stages and edges below are the framework's real run
     order, read from each module.yaml under framework/modules —
     14 modules, 30 dependency edges. Nothing here is illustrative.
     ================================================================== */
  var canvas = document.getElementById('graph');
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext('2d');

  var STAGES = ['Frame', 'Research', 'Decide', 'Specify', 'Operationalise'];

  var NODES = [
    { id: '01', name: 'idea',        stage: 0, row: 0, rows: 1, check: true  },
    { id: '02', name: 'market',      stage: 1, row: 0, rows: 4 },
    { id: '03', name: 'user',        stage: 1, row: 1, rows: 4 },
    { id: '04', name: 'problem',     stage: 1, row: 2, rows: 4 },
    { id: '05', name: 'competition', stage: 1, row: 3, rows: 4 },
    { id: '06', name: 'business',    stage: 2, row: 0, rows: 2 },
    { id: '07', name: 'strategy',    stage: 2, row: 1, rows: 2, check: true },
    { id: '08', name: 'product',     stage: 3, row: 0, rows: 3 },
    { id: '09', name: 'technology',  stage: 3, row: 1, rows: 3 },
    { id: '14', name: 'ai',          stage: 3, row: 2, rows: 3 },
    { id: '10', name: 'execution',   stage: 4, row: 0, rows: 4 },
    { id: '11', name: 'growth',      stage: 4, row: 1, rows: 4 },
    { id: '12', name: 'metrics',     stage: 4, row: 2, rows: 4 },
    { id: '13', name: 'operations',  stage: 4, row: 3, rows: 4, check: true }
  ];

  var DEPS = {
    '02': ['01'],
    '03': ['01', '02'],
    '04': ['03'],
    '05': ['02', '03', '04'],
    '06': ['02', '03', '05'],
    '07': ['04', '05', '06'],
    '08': ['03', '07'],
    '09': ['02', '08'],
    '10': ['08', '09'],
    '11': ['03', '06', '08'],
    '12': ['08', '11'],
    '13': ['02', '09', '10'],
    '14': ['03', '08', '09']
  };

  // A valid topological order — the sequence a real run advances through.
  var ORDER = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '14', '10', '11', '12', '13'];

  var byId = {};
  NODES.forEach(function (n) { byId[n.id] = n; });

  var C = {};
  function recolor() {
    var cs = getComputedStyle(root);
    var get = function (k, fb) { return (cs.getPropertyValue(k) || fb).trim(); };
    C.accent = get('--accent', '#1B62E8');
    C.cyan = get('--cyan', '#22D3EE');
    C.amber = get('--amber', '#B45309');
    C.rule = get('--rule-strong', '#CBD7EA');
    C.faint = get('--rule', '#E3EAF5');
    C.ink = get('--ink', '#0B1220');
    C.dim = get('--slate-2', '#7286A3');
    C.surface = get('--surface', '#FFFFFF');
  }
  recolor();

  var W = 0, H = 0, R = 13, vertical = false;

  function layout() {
    var cssW = canvas.clientWidth || 520;
    // Narrow screens get the stages stacked top-to-bottom instead of squeezed
    // into five columns. The threshold must sit below the desktop graph column
    // (540px) or the wide layout never runs.
    vertical = cssW < 430;
    var cssH = Math.round(vertical ? Math.max(430, cssW * 1.32) : cssW * 0.76);
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
    canvas.style.height = cssH + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    W = cssW; H = cssH;
    R = vertical ? Math.max(12, Math.min(15, cssW / 26)) : Math.max(11, Math.min(15, cssW / 40));

    if (vertical) {
      var padX = R + 24;
      var band = H / STAGES.length;
      NODES.forEach(function (n) {
        n.x = padX + (W - padX * 2) * ((n.row + 0.5) / n.rows);
        n.y = band * n.stage + band * 0.62;
        n.bandTop = band * n.stage;
      });
    } else {
      var pX = Math.max(34, cssW * 0.095);
      var top = 44, bottom = 26;
      NODES.forEach(function (n) {
        n.x = pX + (W - pX * 2) * (n.stage / (STAGES.length - 1));
        var h = H - top - bottom;
        n.y = top + h * ((n.row + 0.5) / n.rows);
      });
    }
  }

  // Control points for the curve between two nodes, shared by the stroked
  // edge and the spark that travels along it so the two never diverge.
  function ctrl(a, b) {
    if (vertical) {
      var my = (a.y + b.y) / 2;
      return { c1x: a.x, c1y: my, c2x: b.x, c2y: my };
    }
    var mx = (a.x + b.x) / 2;
    return { c1x: mx, c1y: a.y, c2x: mx, c2y: b.y };
  }

  function edgePath(a, b) {
    var c = ctrl(a, b);
    ctx.beginPath();
    ctx.moveTo(a.x, a.y);
    ctx.bezierCurveTo(c.c1x, c.c1y, c.c2x, c.c2y, b.x, b.y);
  }

  function bezierAt(t, p0, p1, p2, p3) {
    var u = 1 - t;
    return u * u * u * p0 + 3 * u * u * t * p1 + 3 * u * t * t * p2 + t * t * t * p3;
  }

  var passedTo = 0;      // how many of ORDER have passed their gate
  var pulse = 0;         // 0..1 progress into the current transition
  var holdUntil = 0;     // timestamp for the pause at a checkpoint

  function draw(now) {
    ctx.clearRect(0, 0, W, H);

    // stage headers
    ctx.font = '500 9.5px "IBM Plex Mono", monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = C.dim;
    STAGES.forEach(function (s, i) {
      var label = s.toUpperCase();
      var first = NODES.filter(function (n) { return n.stage === i; })[0];
      if (vertical) {
        ctx.textAlign = 'left';
        ctx.fillText(label, 4, first.bandTop + 16);
      } else {
        ctx.textAlign = 'center';
        // Keep the outermost headers inside the canvas rather than clipping them.
        var half = ctx.measureText(label).width / 2;
        ctx.fillText(label, Math.max(half + 4, Math.min(W - half - 4, first.x)), 20);
      }
    });
    ctx.textAlign = 'center';

    var doneSet = {};
    for (var i = 0; i < passedTo; i++) doneSet[ORDER[i]] = true;
    var current = ORDER[Math.min(passedTo, ORDER.length - 1)];

    // edges
    Object.keys(DEPS).forEach(function (to) {
      DEPS[to].forEach(function (from) {
        var a = byId[from], b = byId[to];
        var live = doneSet[from] && doneSet[to];
        edgePath(a, b);
        ctx.strokeStyle = live ? C.accent : C.faint;
        ctx.globalAlpha = live ? 0.5 : 1;
        ctx.lineWidth = live ? 1.6 : 1.1;
        ctx.stroke();
        ctx.globalAlpha = 1;
      });
    });

    // travelling spark on the edges feeding the current module
    if (!reduced && DEPS[current]) {
      DEPS[current].forEach(function (from) {
        if (!doneSet[from]) return;
        var a = byId[from], b = byId[current];
        var t = pulse, c = ctrl(a, b);
        var x = bezierAt(t, a.x, c.c1x, c.c2x, b.x);
        var y = bezierAt(t, a.y, c.c1y, c.c2y, b.y);
        ctx.beginPath();
        ctx.arc(x, y, 2.6, 0, Math.PI * 2);
        ctx.fillStyle = C.cyan;
        ctx.fill();
      });
    }

    // nodes
    NODES.forEach(function (n) {
      var done = !!doneSet[n.id];
      var isCur = n.id === current;

      if (isCur && !reduced) {
        var halo = R + 5 + Math.sin(now / 260) * 2.4;
        ctx.beginPath();
        ctx.arc(n.x, n.y, halo, 0, Math.PI * 2);
        ctx.fillStyle = n.check ? C.amber : C.accent;
        ctx.globalAlpha = 0.15;
        ctx.fill();
        ctx.globalAlpha = 1;
      }

      ctx.beginPath();
      ctx.arc(n.x, n.y, R, 0, Math.PI * 2);
      ctx.fillStyle = done ? (n.check ? C.amber : C.accent) : C.surface;
      ctx.fill();
      ctx.lineWidth = 1.6;
      ctx.strokeStyle = done ? (n.check ? C.amber : C.accent) : C.rule;
      ctx.stroke();

      ctx.font = '600 10px "IBM Plex Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = done ? '#FFFFFF' : C.dim;
      ctx.fillText(n.id, n.x, n.y + 0.5);

      ctx.font = '400 9px "IBM Plex Mono", monospace';
      ctx.textBaseline = 'alphabetic';
      ctx.fillStyle = done ? C.ink : C.dim;
      ctx.fillText(n.name, n.x, n.y + R + 12);
    });
  }

  var stateEl = document.getElementById('gState');
  function setState() {
    if (!stateEl) return;
    var idx = Math.min(passedTo, ORDER.length - 1);
    var n = byId[ORDER[idx]];
    var label = n.id + '-' + n.name;
    if (passedTo >= ORDER.length) label = 'artifact set — review';
    else if (n.check && passedTo === ORDER.indexOf(n.id)) label = label + '  · checkpoint';
    stateEl.textContent = label;
  }

  var STEP = 820, CHECK_HOLD = 1500;
  var last = 0;

  function frame(now) {
    if (!last) last = now;
    var dt = now - last;
    last = now;

    if (now >= holdUntil) {
      pulse += dt / STEP;
      if (pulse >= 1) {
        pulse = 0;
        var justPassed = ORDER[passedTo];
        passedTo++;
        if (passedTo > ORDER.length) {
          passedTo = 0;
          holdUntil = now + 900;
        } else if (justPassed && byId[justPassed] && byId[justPassed].check) {
          holdUntil = now + CHECK_HOLD;
        }
        setState();
      }
    }

    draw(now);
    requestAnimationFrame(frame);
  }

  var booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    layout();
    if (reduced) passedTo = ORDER.length;   // show the finished graph, no motion
    setState();
    draw(0);                                // always paint one frame up front
    if (!reduced) requestAnimationFrame(frame);
  }

  var rt;
  window.addEventListener('resize', function () {
    clearTimeout(rt);
    rt = setTimeout(function () { layout(); if (reduced) draw(0); }, 140);
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    recolor(); if (reduced) draw(0);
  });

  window.piosGraph = { recolor: function () { recolor(); if (reduced) draw(0); } };

  // Draw as soon as we can; redraw once webfonts land so the labels are set
  // in IBM Plex Mono rather than the fallback.
  boot();
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { layout(); draw(0); });
  }
})();
