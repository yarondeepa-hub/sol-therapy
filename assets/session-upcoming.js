/* session-upcoming.js - הבלוק "מפגשים קרובים" בעמודי ההקלטה (cloud-session-*, session-*). נבנה 26.10.2026.
   אותה שיטה כמו assets/upcoming-sessions.js במדריך /sound-healing:
     השורות הסטטיות נכתבות ב-T-tools/scripts/session-upcoming-sync.py (לגוגל ולמי שאין לו JS), וכאן הן מתחדשות
     בכל טעינה, כך שהבלוק לא מצביע על ערב שעבר גם אם הסקריפט לא רץ.
   המקורות (זהים לסקריפט):
     /cloud-events.json = המצב. נכנס רק אירוע עם visibility=listed, sale_status=open, event_status=scheduled, state=open,
       ושעת ההתחלה שלו עוד לא עברה (שעון ישראל).
     /cloud.html = גריד הליינאפ (#lineupGrid) בלבד: שם, קישור עמוד הערב, שורת הכרטיס. כרטיס עם "אזל" / "האירוע הסתיים"
       לא נכנס. סדנאות (#workshopsGrid) לא נכנסות.
   הבחירה: שורה אחת לכל ערב (הסבב הראשי אם פתוח, אחרת הסבב המוקדם). קודם הערב הקרוב של האמן של ההקלטה
     (data-artist = תחיליות slug, data-artist-name = שם האמן בכרטיס), ואחריו הערבים הקרובים לפי השעה, עד data-max.
   הנוסח מגיע מהעמוד עצמו, בתבניות שכבר היו בעמודי ההקלטה - אין כאן נוסח חדש (מ-27.10.2026 בלי הסיפא שירון הוריד:
   "שלושה מפגשים קרובים בקלאוד ספייס:" / "שני מפגשים קרובים בקלאוד ספייס:"):
     data-note-own  = שורת הפתיחה כשיש לאמן ערב קרוב ({month} = "ב" + שם החודש של הערב שלו)
     data-note-none = שורת הפתיחה כשאין (המספר "שלושה" מתחלף ב"שני" כשנשארו רק שני ערבים; פחות מזה - הבלוק מוסתר)
     data-own-badge = התווית ליד שם האמן בשורה שלו
   אם המשיכה נכשלת - נשארות השורות הסטטיות, בלי שורות שהשעה שלהן כבר עברה. */
(function(){
  'use strict';
  var box = document.querySelector('section.upcoming[data-upcoming="session"]');
  if (!box) return;
  var MAX = parseInt(box.getAttribute('data-max'), 10) || 3;
  var PREF = (box.getAttribute('data-artist') || '').split(/\s+/).filter(Boolean);
  var ANAME = box.getAttribute('data-artist-name') || '';
  var NOTE_OWN = box.getAttribute('data-note-own') || '';
  var NOTE_NONE = box.getAttribute('data-note-none') || '';
  var BADGE = box.getAttribute('data-own-badge') || '';
  var BTN = 'כרטיסים';
  var EVENTER = 'https://www.eventer.co.il/';
  var MONTHS = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר'];
  var NUMW = { 2: 'שני', 3: 'שלושה', 4: 'ארבעה' };
  var invite = (function(){ var p = box.previousElementSibling; return p && p.classList && p.classList.contains('invite') ? p : null; })();
  var now = new Date();

  // שעת קיר בישראל ("2026-11-16 20:30") -> רגע אמיתי, בלי קשר לאזור הזמן של הדפדפן (כמו ב-upcoming-sessions.js)
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
  function mine(slug, name){
    if (ANAME && name === ANAME) return true;
    for (var i = 0; i < PREF.length; i++) { if (slug === PREF[i] || slug.indexOf(PREF[i] + '-') === 0) return true; }
    return false;
  }
  function noteFor(rows){
    var own = null;
    for (var i = 0; i < rows.length; i++) { if (rows[i].own) { own = rows[i]; break; } }
    if (own) {
      var m = parseInt(String(own.iso).split(/[ T]/)[0].split('-')[1], 10);
      return MONTHS[m - 1] ? NOTE_OWN.replace('{month}', 'ב' + MONTHS[m - 1]) : null;
    }
    if (rows.length >= MAX) return NOTE_NONE;
    if (rows.length >= 2 && NUMW[MAX] && NUMW[rows.length]) return NOTE_NONE.replace(NUMW[MAX], NUMW[rows.length]);
    return null;
  }
  function noteEl(){ return box.querySelector('.upcoming__note'); }
  function show(note){
    var hide = !note;
    box.hidden = hide;
    if (invite) invite.hidden = hide;
    var n = noteEl();
    if (n && note && txt(n) !== note) n.textContent = note;
  }

  // 1. מיד: השורות הסטטיות בלי מה שכבר עבר (למקרה שהמשיכה תיכשל)
  (function prune(){
    var items = box.querySelectorAll('.upcoming__item'), left = [], cut = 0;
    for (var i = 0; i < items.length; i++) {
      var st = items[i].getAttribute('data-start');
      if (st && at(st) <= now) { items[i].parentNode.removeChild(items[i]); cut++; }
      else left.push({ own: items[i].getAttribute('data-own') === '1', iso: st || '' });
    }
    if (cut) show(noteFor(left));
  })();

  if (!window.fetch || !window.DOMParser || !window.Promise) return;

  function rowsFrom(ev, html){
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var grid = doc.getElementById('lineupGrid');
    if (!grid) return null;
    var byCode = {};
    for (var k in ev) { if (ev[k] && ev[k].eventer) byCode[ev[k].eventer] = ev[k]; }
    var evenings = {}, order = [];
    var cards = grid.querySelectorAll('article.lp-card[data-slug]');
    for (var j = 0; j < cards.length; j++) {
      var c = cards[j];
      var btn = c.querySelector('a.lp-card__btn[href*="eventer.co.il"]');
      if (!btn || /lp-card__btn--(sold|ended|wait)/.test(btn.className) || c.querySelector('.lp-soldout')) continue;
      var code = (btn.getAttribute('href').match(/eventer\.co\.il\/(\w+)/) || [])[1];
      var e = code && byCode[code];
      if (!e) continue;
      if (e.visibility !== 'listed' || e.sale_status !== 'open' || e.event_status !== 'scheduled' || e.state !== 'open') continue;
      var t = at(e.iso);
      if (!(t > now)) continue;
      var slug = c.getAttribute('data-slug');
      var a = c.querySelector('.lp-card__namelink');
      var name = txt(a) || txt(c.querySelector('.lp-card__name'));
      var href = (a && a.getAttribute('href')) || '';
      var key = href || slug.replace(/-b$/, '');
      var r = { t: t, code: code, slug: slug, iso: e.iso, dow: e.dow || '', date: e.date || '', time: e.time || '',
                name: name, href: href, sub: txt(c.querySelector('.lp-card__sub')), early: /-b$/.test(slug), own: mine(slug, name) };
      var cur = evenings[key];
      if (!cur) { evenings[key] = r; order.push(key); }
      else if (cur.early && !r.early) evenings[key] = r;       // הסבב הראשי קודם לסבב המוקדם
      if (r.own) evenings[key].own = true;
    }
    var list = order.map(function(k){ return evenings[k]; });
    list.sort(function(x, y){ return x.t - y.t; });
    var out = [], own = null;
    for (var i = 0; i < list.length; i++) { if (list[i].own) { own = list[i]; break; } }
    if (own) out.push(own);
    for (var n = 0; n < list.length && out.length < MAX; n++) { if (!list[n].own) out.push(list[n]); }
    return out;
  }

  function rowEl(r){
    var item = el('div', 'upcoming__item');
    item.setAttribute('data-code', r.code);
    item.setAttribute('data-start', String(r.iso).replace(' ', 'T'));
    if (r.own) item.setAttribute('data-own', '1');
    var when = el('span', 'upcoming__when');
    when.appendChild(document.createTextNode(r.dow + ' '));
    var d = el('span', null, r.date); d.setAttribute('dir', 'ltr'); when.appendChild(d);
    when.appendChild(document.createTextNode(' · '));
    var tm = el('span', null, r.time); tm.setAttribute('dir', 'ltr'); when.appendChild(tm);
    item.appendChild(when);
    var body = el('div', 'upcoming__body');
    var a = el('a', 'upcoming__name', r.name);
    a.setAttribute('href', r.href || '/cloud#lineupGrid');
    a.setAttribute('data-track', 'recording_to_event'); a.setAttribute('data-placement', 'upcoming_list'); a.setAttribute('data-event-slug', r.slug);
    body.appendChild(a);
    if (r.own && BADGE) { body.appendChild(document.createTextNode(' ')); body.appendChild(el('span', 'upcoming__own', BADGE)); }
    if (r.sub) body.appendChild(el('p', 'upcoming__sub', r.sub));
    item.appendChild(body);
    var b = el('a', 'upcoming__book', BTN);
    // 29.10.2026: הכפתור לעמוד הערב (שם הפרטים והרכישה, כולל שני סבבים ומצב אזל); בלי עמוד ערב - לאיוונטר כמו קודם
    if (r.href) {
      b.setAttribute('href', r.href);
      b.setAttribute('data-track', 'recording_to_event'); b.setAttribute('data-placement', 'upcoming_button');
    } else {
      b.setAttribute('href', EVENTER + r.code); b.setAttribute('target', '_blank'); b.setAttribute('rel', 'noopener');
      b.setAttribute('data-track', 'ticket_click'); b.setAttribute('data-placement', 'upcoming_list');
    }
    b.setAttribute('data-event-slug', r.slug);
    item.appendChild(b);
    return item;
  }

  Promise.all([
    fetch('/cloud-events.json?v=' + Date.now(), { cache: 'no-store' }).then(function(r){ return r.ok ? r.json() : null; }),
    fetch('/cloud.html', { cache: 'no-cache' }).then(function(r){ return r.ok ? r.text() : null; })
  ]).then(function(res){
    var ev = res[0] && res[0].events;
    if (!ev || !res[1]) return;
    var rows = rowsFrom(ev, res[1]);
    if (!rows) return;               // הגריד לא נמצא - נשארים עם הסטטי
    var note = noteFor(rows);
    var items = box.querySelectorAll('.upcoming__item');
    var same = items.length === rows.length && note && noteEl() && txt(noteEl()) === note;
    for (var i = 0; same && i < rows.length; i++) {
      if (items[i].getAttribute('data-code') !== rows[i].code || (items[i].getAttribute('data-own') === '1') !== !!rows[i].own) same = false;
      var bk = items[i].querySelector('.upcoming__book');   // 29.10.2026: גם יעד הכפתור - שורה סטטית ישנה (לאיוונטר) נבנית מחדש
      if (!bk || bk.getAttribute('href') !== (rows[i].href || (EVENTER + rows[i].code))) same = false;
    }
    if (!same) {
      for (var j = 0; j < items.length; j++) items[j].parentNode.removeChild(items[j]);
      var end = null, walker = box.lastChild;
      while (walker) { if (walker.nodeType === 8 && /UPCOMING:END/.test(walker.nodeValue)) { end = walker; break; } walker = walker.previousSibling; }
      rows.forEach(function(r){ box.insertBefore(rowEl(r), end); });
    }
    show(note);
    box.setAttribute('data-live', '1');
  }).catch(function(){ /* המשיכה נכשלה - נשארות השורות הסטטיות */ });
})();
