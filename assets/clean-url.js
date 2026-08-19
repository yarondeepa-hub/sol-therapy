/* ניקוי פרמטרי מעקב משורת הכתובת - כדי שמה שמעתיקים ומשתפים יהיה קצר ונקי.
   פייסבוק ואינסטגרם מדביקים fbclid ארוך לכל קישור שנפתח מהאפליקציה; מי שמשתף
   הלאה מהדפדפן גורר את הזנב, פלטפורמות מסוימות דוחות את הקישור כארוך מדי,
   ושיתוף-של-שיתוף מנפח אותו עוד. הסקריפט רץ אחרי שהאנליטיקס כבר קראו את
   הפרמטרים (חלון load ועוד רגע), ואז מחליף את שורת הכתובת בגרסה נקייה. */
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

  if (document.readyState === 'complete') { setTimeout(scrub, 600); }
  else { window.addEventListener('load', function () { setTimeout(scrub, 600); }, { once: true }); }
})();
