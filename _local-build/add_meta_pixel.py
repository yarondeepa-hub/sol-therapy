#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_meta_pixel.py - התקנת פיקסל מטא + אירועי אופטימיזציה + תיוג קישורים יוצאים
==============================================================================
רץ פעם אחת על כל עמודי ה-HTML הפרוסים של sol-therapy.com (המקור המקומי).
אושר על ידי ירון 17.7.2026. אין פריסה מהסקריפט - עריכת קבצים מקומית בלבד.

מה הסקריפט עושה:
1. פיקסל מטא (902345231064039) בכל עמוד פרוס שיש בו gtag:
   - עמודים עם טעינת gtag דחויה (loadGtag) - הפיקסל נטען באותו מנגנון דחייה.
   - עמודים עם gtag async רגיל - קטע הפיקסל הסטנדרטי (async מובנה).
   - בלי noscript img (אתר סטטי). מיקום: head, מיד אחרי בלוק ה-gtag.
2. ViewContent: עמודי share/* (content_name=slug, content_category=cloud_session)
   ו-cloud-card (content_name=punch-card).
3. TicketClick (trackCustom): קליק CTA בעמודי share (+ gtag ticket_click_artist
   שלא היה שם), קליק כרטיסים ב-cloud/cloud-en (לצד מאזין gtag קיים),
   וקישור הגיבוי ב-cloud-card.
4. תיוג יציאות לאיוונטר: סקריפט אחיד שמוסיף utm_source/medium/campaign/content
   ו-fbclid שמור מ-sessionStorage לקליקים חיים בלבד (לא נוגע ב-JSON-LD).
   עמיד לכשלים - אם משהו נשבר הקליק ממשיך כרגיל.

הרצה חוזרת בטוחה: הסקריפט מדלג על קבצים שכבר מכילים את הסמנים.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIXEL_ID = "902345231064039"

# ---------------------------------------------------------------- קטעי קוד

FBQ_STUB = (
    "!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?"
    "n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;"
    "n.push=n;n.loaded=!0;n.version='2.0';n.queue=[]}(window);"
)

FBQ_FULL = (
    "!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?"
    "n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;"
    "n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;"
    "t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}"
    "(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
)


def pixel_block_deferred(extra_events=""):
    """פיקסל בדפוס הטעינה הדחויה של gtag - stub מיד, הסקריפט אחרי LCP/אינטראקציה."""
    return f"""    <!-- Meta Pixel {PIXEL_ID} - deferred like gtag above; events queue in the fbq stub so nothing is lost. -->
    <script>
      {FBQ_STUB}
      fbq('init', '{PIXEL_ID}');
      fbq('track', 'PageView');
{extra_events}      (function(){{
        function loadFbq(){{ if(window.__fbqLoaded) return; window.__fbqLoaded=1;
          var s=document.createElement('script'); s.async=true;
          s.src='https://connect.facebook.net/en_US/fbevents.js';
          document.head.appendChild(s); }}
        if(document.readyState==='complete'){{ setTimeout(loadFbq,1); }}
        else {{ window.addEventListener('load', function(){{ ('requestIdleCallback' in window) ? requestIdleCallback(loadFbq,{{timeout:3000}}) : setTimeout(loadFbq,1500); }}); }}
        ['scroll','pointerdown','keydown','touchstart'].forEach(function(e){{ window.addEventListener(e, loadFbq, {{once:true, passive:true}}); }});
      }})();
    </script>
"""


def pixel_block_async(extra_events=""):
    """פיקסל סטנדרטי לעמודים עם gtag async רגיל (הטעינה async מובנית בקטע)."""
    return f"""    <!-- Meta Pixel {PIXEL_ID} - Facebook/Instagram -->
    <script>
      {FBQ_FULL}
      fbq('init', '{PIXEL_ID}');
      fbq('track', 'PageView');
{extra_events}    </script>
"""


# תיוג יציאות לאיוונטר - סקריפט אחיד. כשל בכל שלב = הקליק ממשיך כרגיל.
UTM_SCRIPT = """    <!-- Outbound Eventer tagging: utm + saved fbclid on live clicks only (JSON-LD untouched). Fails open. -->
    <script>
      (function(){
        try{
          var KEY='solAttr', attr={};
          try{ attr=JSON.parse(sessionStorage.getItem(KEY)||'{}'); }catch(_){ attr={}; }
          try{
            var qs=new URLSearchParams(location.search), changed=false;
            qs.forEach(function(v,k){ if(k==='fbclid'||k.indexOf('utm_')===0){ attr[k]=v; changed=true; } });
            if(changed) sessionStorage.setItem(KEY,JSON.stringify(attr));
          }catch(_){}
          document.addEventListener('click',function(e){
            try{
              if(!e.target||!e.target.closest) return;
              var a=e.target.closest('a[href*="eventer.co.il"]'); if(!a) return;
              var u=new URL(a.href,location.href);
              var set=function(k,v){ if(v&&!u.searchParams.has(k)) u.searchParams.set(k,v); };
              set('utm_source','sol-website');
              set('utm_medium','referral');
              set('utm_campaign','cloud-2026');
              var card=a.closest('[data-slug]');
              var slug=(card&&card.getAttribute('data-slug'))||(location.pathname.split('/').pop()||'index').replace(/\\.html?$/,'')||'index';
              set('utm_content',slug);
              set('fbclid',attr.fbclid);
              a.href=u.toString();
            }catch(_){}
          },true);
        }catch(_){}
      })();
    </script>
"""


def share_click_script(slug):
    """עמודי share: TicketClick למטא + ticket_click_artist ל-GA4 על CTA חי (כולל sticky)."""
    return f"""<script>
(function(){{
  var SLUG='{slug}';
  document.addEventListener('click',function(e){{
    try{{
      if(!e.target||!e.target.closest) return;
      var a=e.target.closest('a.sp-cta[href], .sp-sticky a[href]'); if(!a||!a.href) return;
      if(typeof window.fbq==='function'){{ try{{ fbq('trackCustom','TicketClick',{{content_name:SLUG}}); }}catch(_){{}} }}
      if(typeof window.gtag==='function'){{ try{{ gtag('event','ticket_click_artist',{{artist_name:SLUG,link:a.href}}); }}catch(_){{}} }}
    }}catch(_){{}}
  }},true);
}})();
</script>
"""


CARD_CLICK_SCRIPT = """<script>
(function(){
  document.addEventListener('click',function(e){
    try{
      if(!e.target||!e.target.closest) return;
      if(!e.target.closest('.card-buy__fallback')) return;
      if(typeof window.fbq==='function'){ try{ fbq('trackCustom','TicketClick',{content_name:'punch-card'}); }catch(_){} }
    }catch(_){}
  },true);
})();
</script>
"""

# שורה שמתווספת בתוך המאזין הקיים ticket_click_artist ב-cloud.html / cloud-en.html
CLOUD_FBQ_LINE = (
    "    var slugEl=a.closest('[data-slug]');\n"
    "    if(typeof window.fbq==='function'){ try{ fbq('trackCustom','TicketClick',"
    "{content_name: slugEl?slugEl.getAttribute('data-slug'):(nameEl?nameEl.textContent.trim():'')}); }catch(_){} }\n"
)


# ---------------------------------------------------------------- עזרי עריכה

def find_gtag_insert_pos(html):
    """מחזיר את המיקום מיד אחרי סגירת בלוק ה-gtag ב-head (כולל שורת newline)."""
    anchors = [html.rfind("googletagmanager.com"), html.rfind("gtag('config'")]
    anchor = max(anchors)
    if anchor < 0:
        return -1
    close = html.find("</script>", anchor)
    if close < 0:
        return -1
    end = close + len("</script>")
    if end < len(html) and html[end] == "\n":
        end += 1
    return end


def insert_before_body_close(html, snippet):
    idx = html.rfind("</body>")
    if idx < 0:
        return None
    return html[:idx] + snippet + html[idx:]


def process_file(path, utm_pages_rel):
    rel = path.relative_to(ROOT).as_posix()
    html = path.read_text(encoding="utf-8")
    if PIXEL_ID in html:
        return rel, "skip: pixel already present"
    if "G-C5VRCQ9M6V" not in html:
        return rel, "skip: no gtag on page (not instrumented)"

    changes = []
    deferred = "loadGtag" in html
    slug = path.stem

    # --- ViewContent extras (inside the pixel block, right after PageView)
    extra = ""
    if rel.startswith("share/"):
        extra = ("      fbq('track', 'ViewContent', {content_name: '%s', "
                 "content_category: 'cloud_session'});\n" % slug)
        changes.append("ViewContent:%s" % slug)
    elif rel == "cloud-card.html":
        extra = "      fbq('track', 'ViewContent', {content_name: 'punch-card'});\n"
        changes.append("ViewContent:punch-card")

    # --- 1. base pixel in head, after the gtag block
    pos = find_gtag_insert_pos(html)
    if pos < 0:
        return rel, "ERROR: gtag block end not found"
    block = pixel_block_deferred(extra) if deferred else pixel_block_async(extra)
    html = html[:pos] + block + html[pos:]
    changes.append("pixel(%s)" % ("deferred" if deferred else "async"))

    # --- 3. outbound eventer tagging (in head, after the pixel block)
    if rel in utm_pages_rel:
        pos2 = html.find("</script>", html.find(PIXEL_ID))
        # מיקום אחרי בלוק הפיקסל שהוזח הרגע
        pos2 = html.find("\n", pos2) + 1
        html = html[:pos2] + UTM_SCRIPT + html[pos2:]
        changes.append("utm-outbound")

    # --- 2. click events
    if rel.startswith("share/"):
        out = insert_before_body_close(html, share_click_script(slug))
        if out is None:
            return rel, "ERROR: </body> not found"
        html = out
        changes.append("TicketClick+gtag CTA")
    elif rel == "cloud-card.html":
        out = insert_before_body_close(html, CARD_CLICK_SCRIPT)
        if out is None:
            return rel, "ERROR: </body> not found"
        html = out
        changes.append("TicketClick fallback-link")
    elif rel in ("cloud.html", "cloud-en.html"):
        marker = "track('ticket_click_artist',"
        i = html.find(marker)
        if i < 0:
            return rel, "ERROR: existing ticket_click_artist listener not found"
        line_end = html.find("\n", i) + 1
        html = html[:line_end] + CLOUD_FBQ_LINE + html[line_end:]
        changes.append("TicketClick beside gtag listener")

    path.write_text(html, encoding="utf-8")
    return rel, "OK: " + ", ".join(changes)


def main():
    pages = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        parts = rel.parts
        if any(part.startswith("_") for part in parts):
            continue
        pages.append(p)

    # עמודים שמקבלים את סקריפט תיוג היציאות (יש בהם קישורי eventer חיים/דינמיים)
    utm_pages = {"index.html", "cloud.html", "cloud-en.html", "cloud-card.html"}
    utm_pages |= {p.relative_to(ROOT).as_posix() for p in pages
                  if p.relative_to(ROOT).parts[0] == "share"}

    ok = skipped = errors = 0
    for p in pages:
        rel, status = process_file(p, utm_pages)
        print(f"{rel}: {status}")
        if status.startswith("OK"):
            ok += 1
        elif status.startswith("skip"):
            skipped += 1
        else:
            errors += 1
    print(f"\nsummary: changed={ok} skipped={skipped} errors={errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
