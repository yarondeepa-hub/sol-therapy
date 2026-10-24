/* upcoming-sessions.js - הבלוק "מפגשים קרובים בקלאוד ספייס" (המדריך /sound-healing, נבנה 24.10.2026).
   הנוסח אושר על ידי ירון 24.10.2026 (COPY-sound-healing-v1.md סעיף א5).

   המיכל בעמוד:
     <div class="upcoming" id="upcoming" data-max="4" data-btn="cloud"> ... <ul class="upc-list">שורות</ul>
       <p class="upcoming__empty" hidden>...</p> <p class="upcoming__all">...</p> </div>
   השורות הסטטיות בתוך ה-ul נכתבות בסקריפט T-tools/scripts/sound-healing-upcoming-sync.py (לגוגל ולמי שאין לו JS).
   כאן הן מתחדשות בכל טעינה, כך שהבלוק לא מתיישן גם אם הסקריפט לא רץ:
     - /cloud-events.json = המצב (פתוח / אזל / סגור / עבר). מוצג רק אירוע עם visibility=listed, sale_status=open,
       event_status=scheduled, state=open, ושעת ההתחלה שלו עוד לא עברה.
     - /cloud.html = גריד הליינאפ (#lineupGrid): שם האמן, שורת הכרטיס, קישור עמוד הערב, תוויות (סבב מוקדם / בוקר שישי /
       כרטיסים אחרונים), ומחיר מתוך ההצעות בנתונים לגוגל לפי קוד האיוונטר. כרטיס שמסומן "אזל" או "האירוע הסתיים" לא מוצג.
       סדנאות (#workshopsGrid) לא נכנסות - רק הליינאפ.
     - בלי מחיר אמין (אין הצעה עם קוד האיוונטר) - השורה מוצגת בלי מחיר.
   לאן מובילים שם האמן והכפתור "כרטיסים" (data-btn על המיכל):
     cloud (ברירת המחדל, החלטת ירון 24.10) = לליינאפ בעמוד קלאוד (/cloud#lineupGrid, אותו יעד של "לליינאפ המלא").
       אין בעמוד קלאוד עוגן לכרטיס בודד, ולכן לראש הליינאפ.
     share = לעמוד הערב. eventer = הכפתור ישר לאיוונטר, השם לעמוד הערב.
   בנתונים לגוגל הרשימה מצביעה תמיד על עמודי הערבים (עמוד לכל ערב, עם האירוע והמחיר), בלי קשר לכפתור.
   אם המשיכה נכשלת - נשארות השורות הסטטיות, בלי שורות שהשעה שלהן כבר עברה. אם לא נשאר כלום - ההודעה "כרגע אין סשנים פתוחים".
   הנתונים לגוגל (#upcoming-ld, רשימת עמודי הערבים) מתעדכנים יחד עם השורות. */
(function(){
  'use strict';
  var box = document.getElementById('upcoming');
  if (!box) return;
  var list = box.querySelector('.upc-list');
  var empty = box.querySelector('.upcoming__empty');
  var all = box.querySelector('.upcoming__all');
  if (!list) return;

  var T = { btn: 'כרטיסים', cur: 'ש"ח', early: 'סבב מוקדם', morning: 'בוקר שישי', last: 'כרטיסים אחרונים' };
  var MAX = parseInt(box.getAttribute('data-max'), 10) || 4;
  var BTN = box.getAttribute('data-btn') || 'cloud';
  if (BTN !== 'share' && BTN !== 'eventer') BTN = 'cloud';
  var CLOUD = '/cloud#lineupGrid';
  var SITE = 'https://sol-therapy.com';
  var EVENTER = 'https://www.eventer.co.il/';
  var now = new Date();

  // שעת קיר בישראל ("2026-10-28 20:30") -> רגע אמיתי, בלי קשר לאזור הזמן של הדפדפן (גוגל סורק מארה"ב)
  var IL_FMT = null;
  try { IL_FMT = new Intl.DateTimeFormat('en-US', { timeZone: 'Asia/Jerusalem', hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }); } catch (_) {}
  function at(iso){
    var p = String(iso || '').split(/[ T]/), d = (p[0] || '').split('-'), hm = (p[1] || '23:59').split(':');
    var guess = Date.UTC(+d[0], +d[1] - 1, +d[2], +hm[0], +hm[1]);
    if (IL_FMT && !isNaN(guess)) {
      try {
        var o = {}; IL_FMT.formatToParts(new Date(guess)).forEach(function(x){ o[x.type] = x.value; });
        var shown = Date.UTC(+o.year, +o.month - 1, +o.day, +o.hour % 24, +o.minute);
        if (!isNaN(shown)) return new Date(guess - (shown - guess));
      } catch (_) {}
    }
    return new Date((p[0] || '1970-01-01') + 'T' + (p[1] || '23:59').slice(0, 5) + ':00');
  }
  function txt(n){ return n ? String(n.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
  function el(tag, cls, text){ var x = document.createElement(tag); if (cls) x.className = cls; if (text != null) x.textContent = text; return x; }
  function absPath(h){ if (!h) return ''; if (/^https?:/.test(h)) return h; return '/' + String(h).replace(/^\.?\//, ''); }

  function setEmpty(isEmpty){
    list.hidden = isEmpty;
    if (empty) empty.hidden = !isEmpty;
    if (all) all.hidden = isEmpty;
  }

  // 1. מיד: השורות הסטטיות בלי מה שכבר עבר (למקרה שהמשיכה תיכשל)
  (function prune(){
    var rows = list.querySelectorAll('.upc'), left = 0;
    for (var i = 0; i < rows.length; i++) {
      if (at(rows[i].getAttribute('data-start')) <= now) rows[i].parentNode.removeChild(rows[i]); else left++;
    }
    setEmpty(!left);
  })();

  // מדידה: לחיצה על שם או על כפתור בבלוק (כמו share_next_click בעמודי השיתוף)
  box.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a') : null;
    if (!a || !box.contains(a)) return;
    var row = a.closest('.upc');
    try {
      if (typeof window.gtag === 'function') window.gtag('event', 'upcoming_click', {
        click_location: a.classList.contains('upc__btn') ? 'upcoming_button' : (row ? 'upcoming_name' : 'upcoming_lineup'),
        target_slug: row ? (row.getAttribute('data-slug') || '') : 'cloud',
        source_page: 'sound-healing', link: a.href });
    } catch (_) {}
  });

  if (!window.fetch || !window.DOMParser || !window.Promise) return;

  function rowsFrom(ev, html){
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var grid = doc.getElementById('lineupGrid');
    if (!grid) return null;

    var price = {};
    function walk(x){
      if (!x || typeof x !== 'object') return;
      if (Array.isArray(x)) { x.forEach(walk); return; }
      var o = x.offers;
      if (o) (Array.isArray(o) ? o : [o]).forEach(function(f){
        var m = String((f && f.url) || '').match(/eventer\.co\.il\/(\w+)/);
        if (m && f.price != null && f.price !== '') price[m[1]] = String(f.price);
      });
      if (x['@graph']) walk(x['@graph']);
      if (x.itemListElement) walk(x.itemListElement);
      if (x.item) walk(x.item);
    }
    var lds = doc.querySelectorAll('script[type="application/ld+json"]');
    for (var i = 0; i < lds.length; i++) { try { walk(JSON.parse(lds[i].textContent)); } catch (_) {} }

    var byCode = {};
    for (var k in ev) { if (ev[k] && ev[k].eventer) byCode[ev[k].eventer] = ev[k]; }

    var out = [], seen = {};
    var cards = grid.querySelectorAll('article.lp-card[data-slug]');
    for (var j = 0; j < cards.length; j++) {
      var c = cards[j];
      var btn = c.querySelector('a.lp-card__btn[href*="eventer.co.il"]');
      if (!btn || /lp-card__btn--(sold|ended|wait)/.test(btn.className) || c.querySelector('.lp-soldout')) continue;
      var code = (btn.getAttribute('href').match(/eventer\.co\.il\/(\w+)/) || [])[1];
      var e = code && byCode[code];
      if (!e || seen[code]) continue;
      if (e.visibility !== 'listed' || e.sale_status !== 'open' || e.event_status !== 'scheduled' || e.state !== 'open') continue;
      var t = at(e.iso);
      if (!(t > now)) continue;
      var a = c.querySelector('.lp-card__namelink');
      var combo = c.querySelector('.lp-flagcombo');
      var sub = txt(c.querySelector('.lp-card__sub'));
      var slug = c.getAttribute('data-slug');
      seen[code] = 1;
      out.push({
        t: t, code: code, slug: slug, iso: e.iso,
        dow: e.dow || txt(c.querySelector('.w-dow')), date: e.date || txt(c.querySelector('.w-num')), time: e.time || txt(c.querySelector('.w-time')),
        name: txt(a) || txt(c.querySelector('.lp-card__name')),
        share: absPath(a && a.getAttribute('href')),
        sub: sub,
        early: !!c.querySelector('.lp-round-inline') || /-b$/.test(slug),
        morning: /\blp-card--morning\b/.test(c.className) && sub.indexOf(T.morning) < 0,
        last: !!c.querySelector('.lp-lastseats') || !!(combo && /אחרו/.test(combo.textContent)),
        price: price[code] || ''
      });
    }
    out.sort(function(x, y){ return x.t - y.t; });
    return out.slice(0, MAX);
  }

  function rowEl(r){
    var li = el('li', 'upc');
    li.setAttribute('data-code', r.code);
    li.setAttribute('data-slug', r.slug);
    li.setAttribute('data-start', String(r.iso).replace(' ', 'T'));

    var when = el('div', 'upc__when');
    when.appendChild(el('span', 'upc__dow', r.dow));
    when.appendChild(document.createTextNode(' '));
    var d = el('span', 'upc__num', r.date); d.setAttribute('dir', 'ltr'); when.appendChild(d);
    var sep = el('span', 'upc__sep', ' · '); sep.setAttribute('aria-hidden', 'true'); when.appendChild(sep);
    var tm = el('span', 'upc__num', r.time); tm.setAttribute('dir', 'ltr'); when.appendChild(tm);
    li.appendChild(when);

    var main = el('div', 'upc__main');
    var nm = el('div', 'upc__name');
    var link = BTN === 'cloud' ? CLOUD : (r.share || CLOUD);
    var a = el('a', null, r.name); a.href = link; nm.appendChild(a);
    function tag(cls, label){ nm.appendChild(document.createTextNode(' ')); nm.appendChild(el('span', cls, label)); }
    if (r.early) tag('upc__tag', T.early);
    if (r.morning) tag('upc__tag upc__tag--morning', T.morning);
    if (r.last) tag('upc__tag upc__tag--last', T.last);
    main.appendChild(nm);
    if (r.sub) main.appendChild(el('div', 'upc__line', r.sub));
    li.appendChild(main);

    li.appendChild(el('div', 'upc__price', r.price ? r.price + ' ' + T.cur : ''));

    var b = el('a', 'upc__btn', T.btn);
    if (BTN === 'eventer') { b.href = EVENTER + r.code; b.target = '_blank'; b.rel = 'noopener'; }
    else b.href = link;
    b.setAttribute('aria-label', T.btn + ': ' + r.name);
    li.appendChild(b);
    return li;
  }

  function updateLd(rows){
    var s = document.getElementById('upcoming-ld');
    if (!s) return;
    var items = [], urls = {};
    rows.forEach(function(r){
      if (!r.share || urls[r.share]) return;
      urls[r.share] = 1;
      items.push({ '@type': 'ListItem', position: items.length + 1, url: SITE + r.share, name: r.name + ' - ' + r.dow + ' ' + r.date + ', ' + r.time });
    });
    var name = '';
    try { name = JSON.parse(s.textContent).name || ''; } catch (_) {}
    s.textContent = JSON.stringify({ '@context': 'https://schema.org', '@type': 'ItemList', name: name, itemListOrder: 'https://schema.org/ItemListOrderAscending', numberOfItems: items.length, itemListElement: items });
  }

  Promise.all([
    fetch('/cloud-events.json?v=' + Date.now(), { cache: 'no-store' }).then(function(r){ return r.ok ? r.json() : null; }),
    fetch('/cloud.html', { cache: 'no-cache' }).then(function(r){ return r.ok ? r.text() : null; })
  ]).then(function(res){
    var ev = res[0] && res[0].events;
    if (!ev || !res[1]) return;
    var rows = rowsFrom(ev, res[1]);
    if (!rows) return;               // הגריד לא נמצא - נשארים עם הסטטי
    list.textContent = '';
    rows.forEach(function(r){ list.appendChild(rowEl(r)); });
    setEmpty(!rows.length);
    updateLd(rows);
    box.setAttribute('data-live', '1');
  }).catch(function(){ /* המשיכה נכשלה - נשארות השורות הסטטיות */ });
})();
