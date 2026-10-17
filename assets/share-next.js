/* share-next.js - הבלוק "התאריך הבא של [אמן]" + "עוד בקלאוד" בעמודי השיתוף.
   נבנה מחדש 13.10.2026 (המקור מ-8.10 אבד בניקוי /tmp). הנוסח אושר על ידי ירון 17.10.2026 (COPY.md סעיפים 3-4) ונפרס.
   קורא את /cloud-events.json וממלא את המיכל:
     <div class="sp-next" id="sp-next" data-page="<slug>" data-artist="<בסיס האמן>" data-name="<שם>" hidden></div>
   (המיכל ושורת הסקריפט נכנסים דרך T-tools/scripts/share_next_inject.py).
   מצבים: 1 יש כרטיסים / 2 כרטיסים אחרונים / 3 המאוחר אזל והמוקדם פתוח / 4 הכל אזל -> לליינאפ המלא / 5 אין תאריך (רק בעמוד שהתקיים).
   כל הנוסח יושב באובייקט T - אסור לשנות אותו בלי אישור ירון. עמוד שאינו בעברית - הבלוק נשאר מוסתר (אין נוסח אנגלי מאושר). */
(function(){
  'use strict';
  var box = document.getElementById('sp-next');
  if (!box || !window.fetch) return;
  if ((document.documentElement.getAttribute('lang') || 'he').slice(0, 2) !== 'he') return;

  var T = {
    heading:      'התאריך הבא של {name}',
    headingNone:  'התאריך הבא של {name} עוד לא נקבע',
    sub:          'סשן חדש, עם סט חי שנבנה במיוחד לשכיבה.',
    btnOpen:      'לפרטים וכרטיסים',
    btnLast:      'כרטיסים אחרונים',
    btnLastEarly: 'כרטיסים אחרונים לסבב המוקדם - {early}',
    noteLateSold: 'הכרטיסים לסבב {time} אזלו. באותו ערב נפתח סבב מוקדם ב-{early}.',
    noteSoldTwo:  'הכרטיסים לשני הסבבים אזלו.',
    noteSoldOne:  'הכרטיסים אזלו.',
    lineup:       'לליינאפ המלא של קלאוד',
    more:         'עוד בקלאוד'
  };
  var ALIASES = { bentzur: 'shai-ben-tzur' };
  var SUF = /-(?:b|early|en|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d+)$/;
  var EVENTER = 'https://www.eventer.co.il/';
  var MORE_MAX = 3;

  function key(slug){ var s = slug, s2; while ((s2 = s.replace(SUF, '')) !== s) s = s2; return ALIASES[s] || s; }
  function fmt(t, o){ return t.replace(/\{(\w+)\}/g, function(_, k){ return o[k] == null ? '' : o[k]; }); }
  function when(e){ var p = (e.iso || '').split(' '); return new Date(p[0] + 'T' + (p[1] || '23:59') + ':00'); }
  function cleanName(n){ return String(n || '').replace(/\s*\([^)]*\)\s*$/, '').trim(); }
  function el(tag, cls, text){ var x = document.createElement(tag); if (cls) x.className = cls; if (text != null) x.textContent = text; return x; }
  function track(loc, slug, href){ try { if (typeof window.gtag === 'function') window.gtag('event', 'share_next_click', { click_location: loc, target_slug: slug, source_page: page, link: href }); } catch (_) {} }

  var page = box.getAttribute('data-page') || '';
  var artist = box.getAttribute('data-artist') || key(page);
  var body = document.body, now = new Date();
  var ed = new Date((body.getAttribute('data-event-date') || '1970-01-01') + 'T23:59:59');
  var pageState = body.getAttribute('data-state') || 'live';
  if (pageState !== 'done' && now > ed) pageState = 'done';

  function sameEvening(main, early){
    return page === main || page === main + '-b' || page === main + '-early' || (early && page === early);
  }

  // ערבים שעוד לא עברו, מקובצים לפי הסבב הראשי (סבב מוקדם נצמד לראשי שלו)
  function evenings(ev){
    var out = {}, slug, e, main, m, early;
    for (slug in ev) {
      e = ev[slug];
      if (!e || e.visibility !== 'listed' || e.event_status !== 'scheduled' || e.state === 'past' || e.sale_status === 'closed') continue;
      main = e.main_slug || slug;
      m = ev[main];
      if (!m || out[main]) continue;
      early = m.round_slug && ev[m.round_slug] && ev[m.round_slug].state !== 'past' ? m.round_slug : null;
      var tm = when(m), te = early ? when(ev[early]) : null;
      var last = te && te > tm ? te : tm;
      if (last < now) continue;
      out[main] = { main: main, m: m, early: early, e: early ? ev[early] : null,
                    first: te && te < tm && te > now ? te : tm,
                    mainOpen: m.state === 'open' && tm > now,
                    earlyOpen: !!(early && ev[early].state === 'open' && te > now) };
    }
    var list = []; for (main in out) list.push(out[main]);
    list.sort(function(a, b){ return a.first - b.first; });
    return list;
  }

  function lastFlag(main){
    return fetch('/share/' + main + '.html', { cache: 'no-store' }).then(function(r){ return r.ok ? r.text() : ''; })
      // הדגל --last משמש גם ל"נפתח סבב מוקדם" - רק טקסט עם "אחרון/אחרונים" נחשב כרטיסים אחרונים
      .then(function(h){ return /<body[^>]*data-state="live"/.test(h) && /class="sp-flag --last">[^<]*אחרו/.test(h); })
      .catch(function(){ return false; });
  }

  function css(){
    if (document.getElementById('sp-next-css')) return;
    var s = el('style'); s.id = 'sp-next-css';
    s.textContent =
      '.sp-next{max-width:420px;margin:1.8rem auto 0;text-align:center;padding:1.4rem 1.1rem 1.5rem;border:1px solid rgba(242,234,211,.18);border-radius:14px}' +
      '.sp-next h2{font-family:var(--font-display);font-weight:500;font-size:1.32rem;line-height:1.3;margin-bottom:.4rem}' +
      '.sp-next .sp-next-when{font-size:1.05rem;margin-bottom:.35rem}' +
      '.sp-next .sp-next-when .num{direction:ltr;unicode-bidi:isolate}' +
      '.sp-next .sp-next-sub{color:var(--color-muted);font-size:.95rem;margin-bottom:1.1rem}' +
      '.sp-next .sp-next-note{color:var(--color-muted);font-size:.92rem;margin-bottom:1rem}' +
      '.sp-next .sp-cta{max-width:340px}' +
      '.sp-next .sp-next-all{display:inline-block;color:var(--teal);text-decoration:none;font-size:.98rem}' +
      '.sp-next .sp-next-all:hover{text-decoration:underline}';
    document.head.appendChild(s);
  }

  function whenLine(e){
    var w = el('p', 'sp-next-when');
    w.appendChild(document.createTextNode((e.dow || '') + ' '));
    w.appendChild(el('span', 'num', e.date || ''));
    w.appendChild(document.createTextNode(', '));
    w.appendChild(el('span', 'num', e.time || ''));
    return w;
  }

  function button(label, slug, code){
    var a = el('a', 'sp-cta', label);
    a.href = EVENTER + code + '?utm_content=share_next_date';
    a.target = '_blank'; a.rel = 'noopener';
    a.setAttribute('data-slug', slug);
    return a;
  }

  function lineupLink(){
    var a = el('a', 'sp-next-all', T.lineup); a.href = '../cloud';
    a.addEventListener('click', function(){ track('next_date_block', 'cloud', a.href); });
    return a;
  }

  // "עוד בקלאוד" - עד 3 הערבים הקרובים שאפשר לקנות אליהם, בלי הערב של העמוד ובלי הערב שבבלוק
  function refreshMore(list, skipMain){
    var more = document.getElementById('more');
    if (!more) return;
    more.setAttribute('data-click-location', 'more_cloud_block');
    var picks = [];
    for (var i = 0; i < list.length && picks.length < MORE_MAX; i++) {
      var v = list[i];
      if (v.main === skipMain || sameEvening(v.main, v.early)) continue;
      if (!(v.mainOpen || v.earlyOpen)) continue;
      picks.push(v);
    }
    var grid = more.querySelector('.sp-more-grid'), h = more.querySelector('h2');
    if (!picks.length) {
      if (!grid || !grid.querySelector('.sp-mini')) { if (grid) grid.remove(); if (h) h.remove(); }
      return;
    }
    if (!h) { h = el('h2', null, T.more); more.insertBefore(h, more.firstChild); }
    if (!grid) { grid = el('div', 'sp-more-grid'); h.parentNode.insertBefore(grid, h.nextSibling); }
    grid.textContent = '';
    picks.forEach(function(v){
      var e = v.mainOpen ? v.m : v.e;
      var a = el('a', 'sp-mini'); a.href = v.main + '.html';
      a.setAttribute('data-date', (v.m.iso || '').split(' ')[0]);
      var ph = el('span', 'ph'), img = el('img');
      img.src = '../assets/cloud/artists-bw/' + v.main + '.jpg'; img.alt = cleanName(v.m.name); img.loading = 'lazy';
      img.onerror = function(){ ph.remove(); };
      ph.appendChild(img); a.appendChild(ph);
      a.appendChild(el('div', 'nm', cleanName(v.m.name)));
      var wh = el('div', 'wh'); wh.appendChild(document.createTextNode((e.dow || '') + ' ')); wh.appendChild(el('span', 'num', e.date || ''));
      a.appendChild(wh);
      a.addEventListener('click', function(){ track('more_cloud_block', v.main, a.href); });
      grid.appendChild(a);
    });
  }

  function liftMore(){
    var more = document.getElementById('more');
    if (more && box.parentNode) box.parentNode.insertBefore(more, box.nextSibling);
  }

  function render(v, flag, name, lifted){
    css();
    box.setAttribute('data-click-location', 'next_date_block');
    box.textContent = '';
    if (!v) {
      box.appendChild(el('h2', null, fmt(T.headingNone, { name: name })));
      box.hidden = false;
      return;
    }
    box.appendChild(el('h2', null, fmt(T.heading, { name: name })));
    if (v.mainOpen) {
      box.appendChild(whenLine(v.m));
      box.appendChild(el('p', 'sp-next-sub', T.sub));
      box.appendChild(button(flag ? T.btnLast : T.btnOpen, v.main, v.m.eventer));
    } else if (v.earlyOpen) {
      box.appendChild(whenLine(v.e));
      box.appendChild(el('p', 'sp-next-sub', T.sub));
      box.appendChild(el('p', 'sp-next-note', fmt(T.noteLateSold, { time: v.m.time, early: v.e.time })));
      box.appendChild(button(flag ? fmt(T.btnLastEarly, { early: v.e.time }) : T.btnOpen, v.early, v.e.eventer));
    } else {
      box.appendChild(whenLine(v.m));
      box.appendChild(el('p', 'sp-next-note', v.early ? T.noteSoldTwo : T.noteSoldOne));
      // "עוד בקלאוד" שעולה מיד מתחת כבר נושא את הקישור לליינאפ - לא להכפיל
      if (!(lifted && document.querySelector('#more .sp-all'))) box.appendChild(lineupLink());
    }
    box.hidden = false;
  }

  fetch('/cloud-events.json?v=' + Date.now(), { cache: 'no-store' })
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(j){
      var ev = j && j.events; if (!ev) return;
      var list = evenings(ev), mine = null;
      for (var i = 0; i < list.length; i++) {
        if (key(list[i].main) === artist && !sameEvening(list[i].main, list[i].early)) { mine = list[i]; break; }
      }
      var name = box.getAttribute('data-name') || (mine && cleanName(mine.m.name)) || '';
      var notSelling = pageState !== 'live';
      refreshMore(list, mine && mine.main);
      if (!mine) {
        if (pageState === 'done' && name) { render(null, false, name, true); liftMore(); }
        return;
      }
      var p = (mine.mainOpen || mine.earlyOpen) ? lastFlag(mine.main) : Promise.resolve(false);
      return p.then(function(flag){
        render(mine, flag, name || cleanName(mine.m.name), notSelling);
        if (notSelling) liftMore();
      });
    })
    .catch(function(){ /* הקריאה נכשלה - הבלוק נשאר מוסתר והעמוד הסטטי כמו שהוא */ });
})();
