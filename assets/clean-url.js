/* ניקוי פרמטרי מעקב משורת הכתובת - כדי שמה שמעתיקים ומשתפים יהיה קצר ונקי.
   פייסבוק ואינסטגרם מדביקים fbclid ארוך לכל קישור שנפתח מהאפליקציה; מי שמשתף
   הלאה מהדפדפן גורר את הזנב, פלטפורמות מסוימות דוחות את הקישור כארוך מדי,
   ושיתוף-של-שיתוף מנפח אותו עוד. הסקריפט מחכה עד שכל תג מדידה שבעמוד נטען וקרא
   את הפרמטרים, ורק אז מחליף את שורת הכתובת בגרסה נקייה. (עד 24.11.2026 הניקוי
   רץ 600ms אחרי load; בנייד התגים נטענים רק אחרי load, ולכן הגיעו לכתובת נקייה
   ואיבדו את מקור הביקור.) */
(function () {
  var JUNK = /^(fbclid|gclid|gbraid|wbraid|dclid|msclkid|twclid|ttclid|li_fat_id|mc_eid|mc_cid|igshid|igsh|mibextid|aem|utm_[a-z]+|_hsenc|_hsmi|ck_subscriber_id|vero_[a-z_]+|oly_[a-z_]+)$/i;

  function cleaned(href) {
    try {
      var u = new URL(href);
      var junky = false;
      var keep = [];
      u.searchParams.forEach(function (v, k) {
        if (JUNK.test(k)) { junky = true; } else { keep.push([k, v]); }
      });
      if (!junky) return null;
      var q = keep.map(function (p) {
        return encodeURIComponent(p[0]) + '=' + encodeURIComponent(p[1]);
      }).join('&');
      return u.origin + u.pathname + (q ? '?' + q : '') + (u.hash || '');
    } catch (e) { return null; }
  }

  function scrub() {
    var c = cleaned(location.href);
    if (c && window.history && history.replaceState) {
      try { history.replaceState(history.state, document.title, c); } catch (e) {}
    }
  }

  /* הכתובת הנכונה לשיתוף: הקנונית של העמוד, ואם אין - הנוכחית אחרי ניקוי */
  window.__solShareUrl = function () {
    var l = document.querySelector('link[rel="canonical"]');
    if (l && l.href) return l.href;
    return cleaned(location.href.split('#')[0]) || location.href.split('#')[0];
  };

  /* מתי מותר לנקות. לכל תג שיש לו סטאב בעמוד בודקים שהתחיל להיטען (תגית הסקריפט
     שלו קיימת) ושכבר קרא את הכתובת:
     גוגל - כל מזהה מ-gtag('config') רשום ב-google_tag_manager (בשלב הזה יוצא
       page_view של GA4 ונשמר gclid של גוגל אדס);
     מטא - fbevents.js נטען (callMethod) והפיקסל כבר ירה אירוע (eventCount), ובו
       נקראו fbclid וכתובת העמוד. fbq.loaded לא מעיד על כלום: הסטאב מסמן אותו מיד;
     לינקדאין - insight.min.js רץ (_already_called_lintrk) וקרא את li_fat_id.
     כשכולם קראו - עוד שנייה לביטחון, ומנקים. תקרה: 20 שניות מהרגע שהאחרון שבהם
     התחיל להיטען (למשל תג שחוסם פרסומות עצר; בבדיקת 3G איטי פיקסל מטא ירה רק
     כ-10.5 שניות אחרי שהתחיל להיטען, ולכן לא 10). תג שלא התחיל להיטען בכלל - לא
     מנקים. עדיף כתובת לא נקייה ממדידה שאבדה. */
  var SETTLE = 1000, CAP = 20000, STEP = 250, GIVE_UP = 60000;

  function tagState() {
    var w = window, started = true, read = true;
    function tag(src, done) {
      if (!document.querySelector('script[src*="' + src + '"]')) started = false;
      if (!done) read = false;
    }
    if (typeof w.gtag === 'function') {
      tag('googletagmanager.com/gtag/js', (function () {
        var g = w.google_tag_manager, dl = w.dataLayer || [];
        if (!g) return false;
        for (var i = 0; i < dl.length; i++) {
          if (dl[i] && dl[i][0] === 'config' && !g[dl[i][1]]) return false;
        }
        return true;
      })());
    }
    if (typeof w.fbq === 'function') {
      tag('connect.facebook.net', (function () {
        try {
          var px = w.fbq.callMethod && w.fbq.getState().pixels;
          return !!(px && px.length) && px.every(function (p) { return p.eventCount > 0; });
        } catch (e) { return false; }
      })());
    }
    if (w._linkedin_data_partner_ids && w._linkedin_data_partner_ids.length) {
      tag('snap.licdn.com', !!w._already_called_lintrk);
    }
    return { started: started, read: read };
  }

  var t0 = Date.now(), startedAt = 0, readAt = 0;
  function scrubWhenTagsRead() {
    if (!cleaned(location.href)) return; /* אין מה לנקות */
    var now = Date.now(), s = tagState();
    if (s.started && !startedAt) startedAt = now;
    if (s.read && !readAt) readAt = now;
    if ((readAt && now - readAt >= SETTLE) || (startedAt && now - startedAt >= CAP)) { scrub(); return; }
    if (!startedAt && now - t0 >= GIVE_UP) return; /* התגים לא התחילו להיטען - משאירים */
    setTimeout(scrubWhenTagsRead, STEP);
  }

  if (document.readyState === 'complete') { scrubWhenTagsRead(); }
  else { window.addEventListener('load', scrubWhenTagsRead, { once: true }); }
})();
