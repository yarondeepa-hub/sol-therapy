#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
בדיקת עקביות אתר קלאוד - "אזל" שמופיע כשיש סבב פתוח לא יחזור (ירון 5.9.2026, תקרית פרידום פייטרס).
מה נבדק (מקומי או חי):
  1. אירוע ראשי שאזל ויש לו סבב מוקדם פתוח (cloud-events.json: state sold + round_state open):
     עמוד השיתוף share/<slug>.html חייב: body data-state="live", דגל "--last" עם "סבב מוקדם", CTA עם קישור
     הסבב המוקדם (לא --sold), sticky לסבב המוקדם, סכמה InStock + url של הסבב המוקדם.
  1ב. שער הצמד (תקרית 9.9.2026, שי בן צור - "כרטיס אחרון - 20:30" עם כפתור אחד ל-20:30 בעוד סבב 18:30 פתוח עם 41 מקומות):
     לכל צמד ראשי+מוקדם (round_slug/main_slug, או אותו תאריך + שעות שונות + אותו בסיס שם):
     - סבב מוקדם פתוח => עמוד השיתוף של הראשי חייב לקשר לקוד האיוונטר של המוקדם (CTA + sticky).
     - שני הסבבים פתוחים => שני הקודים ב-CTA, שני הקודים ב-sticky, שני Offers בסכמה, כרטיסי שני הסבבים בלי "אזל".
     - דגל עם "אחרון"/"אזל" חייב לציין שעה (או "שני סבבים"); כששני הסבבים פתוחים - שתי השעות או "שני סבבים".
       דגל מחסור לא מוצג לבד: חייב כפתור לסבב שיש בו מלאי.
  2. אירוע שאזל בלי סבב פתוח: עמוד השיתוף במצב sold, הכרטיס ב-cloud.html עם lp-soldout.
  3. כרטיס עם lp-soldout ב-cloud.html -> cloud-events.json חייב לומר sold (ולהפך).
  4. כרטיס סבב (-b) -> כפתור "כרטיסים" ולא "אזל" כל עוד הסבב פתוח.
  5. הצלבה עם snapshot איוונטר: sold באתר בעוד approved < cap-1, או approved >= cap בלי sold -> אזהרה.
שימוש:
  python3 cloud-site-consistency-check.py            # העותק המקומי O-output/website-sol-therapy
  python3 cloud-site-consistency-check.py --live     # האתר החי sol-therapy.com
  python3 cloud-site-consistency-check.py --dir <תיקייה>   # עותק אחר (למשל קלון של גרסה ישנה לבדיקת רגרסיה)
קוד יציאה 1 אם יש שגיאות. להריץ: לפני כל push של cloud.html/share, אחרי כל push (חי), ובדוח הבוקר.
"""
import re, sys, os, json, urllib.request
BASE="/Users/yaronamor/Documents/yaronamor-vault/sol"
LOCAL=os.path.join(BASE,"O-output/website-sol-therapy")
SNAP=os.path.join(BASE,"O-output/business-advisory/קלאוד-snapshot-אחרון.json")
LIVE="https://sol-therapy.com"
live="--live" in sys.argv
if "--dir" in sys.argv:
    LOCAL=os.path.abspath(sys.argv[sys.argv.index("--dir")+1]); live=False
def read(rel):
    if live:
        try:
            with urllib.request.urlopen(LIVE+"/"+rel, timeout=20) as r: return r.read().decode("utf-8")
        except Exception as e: return None
    p=os.path.join(LOCAL,rel); return open(p,encoding="utf-8").read() if os.path.exists(p) else None
errors=[]; warns=[]
ev_raw=json.loads(read("cloud-events.json") or "{}")
events={}
if isinstance(ev_raw,dict):
    items=ev_raw.get("events",ev_raw)
    if isinstance(items,dict): events=items
    else:
        for e in items: events[e.get("slug") or e.get("id")]=e
else:
    for e in ev_raw: events[e.get("slug") or e.get("id")]=e
import datetime as _dt
_today_str=_dt.date.today().isoformat()
html=read("cloud.html") or ""
cards={}
for m in re.finditer(r'<article class="lp-card[^"]*" data-slug="([^"]+)"(.*?)</article>',html,re.S):
    slug,body=m.group(1),m.group(2)
    btn=re.search(r'<a class="lp-card__btn([^"]*)"[^>]*href="([^"]*)"[^>]*>([^<]*)</a>',body)
    cards[slug]={"soldout":'lp-soldout' in body,"newshow":'lp-newshow' in body,"btn_cls":btn.group(1) if btn else "","btn_href":btn.group(2) if btn else "","btn_txt":btn.group(3).strip() if btn else "",
                 "namelink":(re.search(r'class="lp-card__namelink" href="([^"]+)"',body) or [None,""])[1]}
def share_state(slug):
    s=read(f"share/{slug}.html")
    if s is None: return None
    return {"state":(re.search(r'<body data-state="([^"]+)"',s) or [None,"?"])[1],
            "flag":(re.search(r'<span class="sp-flag ([^"]+)">([^<]*)</span>',s) or [None,"",""]),
            "cta":(re.search(r'<a class="sp-cta([^"]*)" id="cta"([^>]*)>([^<]*)</a>',s) or None),
            "sticky":(re.search(r'<div class="sp-sticky">\s*<a href="([^"]+)"',s) or [None,""])[1],
            "avail":(re.search(r'"availability":\s*"https://schema.org/(\w+)"',s) or [None,"?"])[1],
            "ld_url":(re.search(r'"url":\s*"https://www.eventer.co.il/(\w+)"',s) or [None,""])[1],
            # כל קישורי הרכישה בעמוד, לפי אזור: כפתורי CTA, ה-sticky, ו-Offers בסכמה (תומך בכפתור יחיד ובשניים)
            "cta_hrefs":re.findall(r'<a class="sp-cta[^"]*"[^>]*href="https://www.eventer.co.il/(\w+)"',s),
            "sticky_hrefs":re.findall(r'href="https://www.eventer.co.il/(\w+)"',(re.search(r'<div class="sp-sticky">(.*?)</div>\s*</div>|<div class="sp-sticky">(.*?)</div>',s,re.S) or [None,"",""]).group(0) if re.search(r'<div class="sp-sticky">',s) else ""),
            "ld_urls":re.findall(r'"url":\s*"https://www.eventer.co.il/(\w+)"',"".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)))}
def pairs():
    """צמדי (ראשי, מוקדם) - לפי round_slug/main_slug, ובגיבוי לפי אותו תאריך + שעות שונות + שם שמתחיל באותו שם."""
    out={}
    for slug,e in events.items():
        if e.get("round_slug") and e["round_slug"] in events: out[slug]=e["round_slug"]
    for slug,e in events.items():
        m=e.get("main_slug")
        if m and m in events and m not in out: out[m]=slug
    for slug,e in events.items():
        if slug in out or e.get("main_slug"): continue
        for o,oe in events.items():
            if o!=slug and o not in out.values() and oe.get("date")==e.get("date") and oe.get("time")!=e.get("time") \
               and oe.get("name","").startswith(e.get("name","")) and (o.startswith(slug) or oe.get("main_slug")==slug):
                out[slug]=o
    return out
for slug,e in events.items():
    st=e.get("state"); code=e.get("eventer","")
    if e.get("round_slug"):   # ראשי עם סבב מוקדם
        rs=e.get("round_state"); early=events.get(e["round_slug"],{}); ecode=early.get("eventer","")
        sh=share_state(slug)
        if st=="sold" and rs=="open":
            if not sh: errors.append(f"{slug}: אין עמוד שיתוף"); continue
            cta=sh["cta"]; cta_cls=cta.group(1) if cta else "?"; cta_attrs=cta.group(2) if cta else ""; cta_txt=cta.group(3) if cta else ""
            if sh["state"]!="live": errors.append(f"{slug}: ראשי אזל + סבב פתוח, אבל body data-state={sh['state']} (צריך live)")
            if "--last" not in sh["flag"][1] or not ("סבב" in sh["flag"][2] and "מוקדם" in sh["flag"][2]): errors.append(f"{slug}: הדגל '{sh['flag'][2]}' - צריך '--last' עם 'סבב מוקדם'")
            if "--sold" in cta_cls or ecode not in cta_attrs: errors.append(f"{slug}: ה-CTA '{cta_txt}' לא מקושר לסבב המוקדם ({ecode})")
            if ecode not in sh["sticky"]: errors.append(f"{slug}: ה-sticky מקושר ל-{sh['sticky']} ולא לסבב המוקדם ({ecode})")
            if "SoldOut" in sh["avail"] or sh["ld_url"]!=ecode: errors.append(f"{slug}: סכמה {sh['avail']} / url {sh['ld_url']} - צריך זמינות פתוחה (InStock/LimitedAvailability) + {ecode}")
            bc=cards.get(slug+"-b") or cards.get(e["round_slug"])
            if not bc: errors.append(f"{slug}: אין כרטיס סבב מוקדם ב-cloud.html")
            elif bc["soldout"] or "sold" in bc["btn_cls"] or bc["btn_txt"]=="אזל": errors.append(f"{slug}-b: כרטיס הסבב המוקדם מוצג כאזל בעוד הסבב פתוח")
    if st=="sold" and not (e.get("round_slug") and e.get("round_state")=="open") and not e.get("main_slug"):
        sh=share_state(slug)
        if sh and sh["state"] not in ("sold","done"): errors.append(f"{slug}: אזל ב-json אבל עמוד השיתוף במצב {sh['state']}")
        c=cards.get(slug)
        if c and not c["soldout"]: errors.append(f"{slug}: אזל ב-json אבל הכרטיס בלי lp-soldout")
    c=cards.get(slug)
    if c and c["soldout"] and st!="sold": errors.append(f"{slug}: הכרטיס מסומן אזל אבל ב-json state={st}")
# 1ב. שער הצמד - סבב מוקדם פתוח חייב כפתור בעמוד השיתוף; שני סבבים פתוחים = שני כפתורים (תקרית 9.9.2026)
SCARCE=re.compile(r"אחרו[נן]|אזל")   # אחרון / אחרונים / אזל / אזלו (נון סופית ורגילה)
TIME=re.compile(r"\d{1,2}:\d{2}")
for slug,eslug in pairs().items():
    e=events[slug]; early=events[eslug]
    if e.get("iso","")[:10]<_today_str: continue
    mcode=e.get("eventer",""); ecode=early.get("eventer","")
    early_open=(e.get("round_state") or early.get("state"))=="open" and early.get("state")!="sold"
    main_open=e.get("state")=="open"
    if not early_open: continue
    etime=early.get("time") or e.get("round_time") or ""; mtime=e.get("time","")
    sh=share_state(slug)
    if not sh: errors.append(f"{slug}: סבב מוקדם ({eslug}) פתוח אבל אין עמוד שיתוף share/{slug}.html"); continue
    flag_cls,flag=sh["flag"][1],sh["flag"][2]
    # הדגל נחשב "מוצג" רק כשה-CSS מציג אותו: --last במצב live, --sold במצב sold (הדגל --sold המוסתר בעמוד live לא נספר)
    flag_shown=("--last" in flag_cls and sh["state"]=="live") or ("--sold" in flag_cls and sh["state"]=="sold")
    if not flag_shown: flag=""
    if sh["state"]!="live": errors.append(f"{slug}: סבב מוקדם {etime} פתוח אבל body data-state={sh['state']} (צריך live)")
    if ecode and ecode not in sh["cta_hrefs"]:
        errors.append(f"{slug}: סבב מוקדם {etime} פתוח ({early.get('left','?')} מקומות) אבל אין כפתור רכישה לקוד שלו ({ecode}) בעמוד השיתוף - הכפתורים מקשרים ל-{sh['cta_hrefs'] or 'כלום'}")
    if ecode and ecode not in sh["sticky_hrefs"]:
        errors.append(f"{slug}: ה-sticky בעמוד השיתוף לא מקשר לסבב המוקדם {etime} ({ecode}) - מקשר ל-{sh['sticky_hrefs'] or 'כלום'}")
    if ecode and ecode not in sh["ld_urls"]:
        errors.append(f"{slug}: הסכמה (JSON-LD) בעמוד השיתוף בלי Offer לסבב המוקדם {etime} ({ecode})")
    if SCARCE.search(flag) and not (TIME.search(flag) or "שני סבבים" in flag):
        errors.append(f"{slug}: הדגל '{flag}' מציין מחסור בלי שעה - חייב לומר לאיזה סבב ('כרטיס אחרון - {mtime}') או 'שני סבבים'")
    if SCARCE.search(flag) and ecode and ecode not in sh["cta_hrefs"]:
        errors.append(f"{slug}: הדגל '{flag}' מוצג לבד - דגל מחסור בלי כפתור לסבב שיש בו מלאי ({etime}, {ecode})")
    if main_open:   # שני הסבבים פתוחים = שני כפתורים מפורשים (תקדים: קומיט 8e01e12, שי בן צור 9.9.2026)
        if flag and not ("שני סבבים" in flag or (etime in flag and mtime in flag)):
            errors.append(f"{slug}: שני הסבבים פתוחים ({etime} ו-{mtime}) אבל הדגל '{flag}' לא אומר זאת - חייב 'שני סבבים - {etime} ו-{mtime}'")
        elif not flag: warns.append(f"{slug}: שני הסבבים פתוחים בלי דגל מוצג - התקן (קומיט 8e01e12): 'שני סבבים - {etime} ו-{mtime}'")
        if mcode and mcode not in sh["cta_hrefs"]:
            errors.append(f"{slug}: שני הסבבים פתוחים אבל אין כפתור לסבב {mtime} ({mcode}) בעמוד השיתוף")
        if mcode and mcode not in sh["sticky_hrefs"]:
            errors.append(f"{slug}: שני הסבבים פתוחים אבל ה-sticky בלי קישור לסבב {mtime} ({mcode})")
        if mcode and ecode and not (mcode in sh["ld_urls"] and ecode in sh["ld_urls"]):
            errors.append(f"{slug}: שני הסבבים פתוחים אבל בסכמה אין שני Offers ({ecode} + {mcode}) - יש {sh['ld_urls']}")
        mc=cards.get(slug)
        if mc and (mc["soldout"] or mc["btn_txt"]=="אזל"): errors.append(f"{slug}: הסבב {mtime} פתוח ב-json אבל הכרטיס ב-cloud.html מוצג כאזל")
    ec=cards.get(slug+"-b") or cards.get(eslug)
    if ec and (ec["soldout"] or "sold" in ec["btn_cls"] or ec["btn_txt"]=="אזל"): errors.append(f"{eslug}: כרטיס הסבב המוקדם מוצג כאזל בעוד הסבב פתוח")
# הצלבה עם איוונטר
try:
    snap=json.load(open(SNAP)) if os.path.exists(SNAP) else {"events":{}}; sev=snap.get("events",{})
    if not sev: warns.append("אין סנאפשוט איוונטר (ריצה מחוץ למחשב של ירון) - הצלבת המלאי דולגה")
    for slug,e in events.items():
        key=slug if slug in sev else {"freedom-fighters-early":"freedom-fighters-early"}.get(slug,slug)
        v=sev.get(key)
        if not v: continue
        if e.get("state")=="sold" and v["approved"]<v["cap"]-1: warns.append(f"{slug}: מסומן אזל באתר אבל באיוונטר {v['approved']}/{v['cap']}")
        if e.get("state")=="open" and v["approved"]>=v["cap"]: warns.append(f"{slug}: {v['approved']}/{v['cap']} באיוונטר אבל באתר עדיין פתוח")
except Exception as ex: warns.append(f"אין הצלבה עם snapshot: {ex}")

# 6. עמודי שיתוף שעברו חייבים להיות done (ארכוב סטטי)
import datetime as _dt
_today=_dt.date.today().isoformat()
for slug in list(events.keys()):
    pass
_share_dir=os.path.join(LOCAL,"share") if not live else None
_slugs=[f[:-5] for f in os.listdir(_share_dir)] if _share_dir else [k for k in events.keys()]+["amichai-matias","nitai-hershkovits","maya-dunietz"]
for slug in _slugs:
    sh=read(f"share/{slug}.html")
    if not sh: continue
    m=re.search(r'<body data-state="(\w+)" data-event-date="([^"]+)"',sh)
    if m and m.group(2)<_today and m.group(1)!="done": errors.append(f"{slug}: אירוע עבר ({m.group(2)}) ועמוד השיתוף עדיין {m.group(1)} - להריץ cloud-share-archive-past.py")
# 7. JSON-LD בעמוד קלאוד חייב לכסות כל אירוע פתוח/אזל בעתיד (cloud-jsonld-build.py)
for fname in ("cloud.html","cloud-en.html"):
    h2=read(fname) or ""
    blocks=re.findall(r'<script type="application/ld\+json">(.*?)</script>',h2,re.S)
    urls=set()
    for b in blocks:
        try: d=json.loads(b)
        except Exception: errors.append(f"{fname}: JSON-LD לא תקין"); continue
        for x in (d if isinstance(d,list) else [d]):
            if x.get("@type") in ("Event","MusicEvent") and x.get("offers"): urls.add(x["offers"].get("url","")[-5:])
            if x.get("@type") in ("Event","MusicEvent") and x.get("startDate","")[:10] < _today and x.get("startDate","")!="2026-07-01": errors.append(f"{fname}: JSON-LD עם אירוע שעבר {x.get('name','')[:30]} ({x.get('startDate','')[:10]})")
    for slug,e in events.items():
        if e.get("visibility")=="unlisted": continue
        if e.get("eventer") and e.get("iso","")[:10]>=_today and e["eventer"] not in urls: errors.append(f"{fname}: JSON-LD חסר אירוע {slug} ({e['eventer']}) - להריץ cloud-jsonld-build.py")

# 8. תמונות הדרופדאון: לכל ערך img ב-ART וב-ROUNDB (בפועל: חילוץ מה-HTML), הקובץ assets/cloud/artists-bw/<img>.jpg קיים
#    (תקרית 10.9.2026: ROUNDB כתב img:r.base במקום b.img - ריבוע ירוק בדרופדאון של רז 18:30)
def _head_ok(rel):
    if live:
        try:
            req=urllib.request.Request(LIVE+"/"+rel,method="HEAD",headers={"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req,timeout=20) as r: return r.status==200
        except Exception: return False
    return os.path.exists(os.path.join(LOCAL,rel))
_assets_ok=live or os.path.isdir(os.path.join(LOCAL,"assets/cloud/artists-bw"))
for fname in ("cloud.html","cloud-en.html"):
    h2=read(fname) or ""
    i=h2.find("var ART=[")
    if i<0: continue
    art=h2[i:h2.find("];",i)]
    imgs={}   # slug -> שם קובץ התמונה
    for m in re.finditer(r"\{[^{}]*slug:'([a-z0-9-]+)'[^{}]*\}",art):
        im=re.search(r"img:'([a-z0-9-]+)'",m.group(0))
        imgs[m.group(1)]=im.group(1) if im else m.group(1)
    i=h2.find("ROUNDB=[")
    if i>=0:
        for m in re.finditer(r"slug:'([a-z0-9-]+)',\s*base:'([a-z0-9-]+)'",h2[i:h2.find("];",i)]):
            imgs[m.group(1)]=imgs.get(m.group(2),m.group(2))
    if "img:r.base" in h2.replace(" ",""):
        errors.append(f"{fname}: ROUNDB עם img:r.base - רגרסיה של באג הדרופדאון (10.9.2026), צריך img:b.img||r.base")
    if _assets_ok:
        for slug,img in sorted(imgs.items()):
            if not _head_ok(f"assets/cloud/artists-bw/{img}.jpg"):
                errors.append(f"{fname}: תמונת דרופדאון חסרה לכרטיס {slug}: assets/cloud/artists-bw/{img}.jpg")
    else:
        warns.append(f"{fname}: אין תיקיית assets בעותק הנבדק - בדיקת קבצי הדרופדאון דולגה (רק img:r.base נבדק)")


# ===== שערי QA 10.9.2026 (דוח QA: ממצאים 01, 04, 05, 09, 11, 12) =====
_pages={}
for _f in ("cloud.html","cloud-en.html"):
    _pages[_f]=read(_f) or ""

def _card_slugs(h):
    return re.findall(r'<article class="lp-card"[^>]*data-slug="([a-z0-9-]+)"',h)

# 9. QA-01: סימולציית שיתוף - לכל כרטיס, הכתובת שהקוד בונה חייבת עמוד קיים.
#    הקוד ממפה slug של סבב מוקדם (-b) לעמוד הבסיס; הבדיקה משכפלת את המיפוי ומוודאת שהקוד מכיל אותו.
_share_exists_cache={}
def _share_exists(slug):
    if slug in _share_exists_cache: return _share_exists_cache[slug]
    ok=_head_ok(f"share/{slug}.html") if live else os.path.exists(os.path.join(LOCAL,f"share/{slug}.html"))
    _share_exists_cache[slug]=ok; return ok
for _f,_h in _pages.items():
    if not _h: continue
    if "slug.replace(/-b$/,'')" not in _h:
        errors.append(f"{_f}: קוד השיתוף בלי מיפוי -b לעמוד הבסיס (slug.replace(/-b$/,'')) - כרטיסי סבב מוקדם ישתפו 404 (QA-01)")
    for _slug in set(_card_slugs(_h)):
        _target=re.sub(r'-b$','',_slug)
        if not _share_exists(_target):
            errors.append(f"{_f}: כפתור השיתוף של {_slug} יבנה share/{_target}.html שלא קיים (QA-01)")

# 10. QA-11: לכל כרטיס חייב ביו - כרטיסי הליינאפ מול ה-BIO הראשון, כרטיסי הסדנאות מול השני.
for _f,_h in _pages.items():
    if not _h: continue
    _bios=[m.start() for m in re.finditer(r"var BIO=\{",_h)]
    if not _bios: continue
    def _keys(_i): return set(re.findall(r'"([a-z0-9-]+)":\[',_h[_bios[_i]:_h.find("};",_bios[_i])])) if _i<len(_bios) else set()
    _k1,_k2=_keys(0),_keys(1)
    _wg=_h.find('id="workshopsGrid"')
    for _m in re.finditer(r'<article class="lp-card"[^>]*data-slug="([a-z0-9-]+)"',_h):
        _slug=_m.group(1); _in_ws=_wg>=0 and _m.start()>_wg
        if _slug not in (_k2 if _in_ws else _k1):
            errors.append(f"{_f}: כרטיס {_slug} בלי ביו ב-BIO {'השני (סדנאות)' if _in_ws else 'הראשון (ליינאפ)'} - הדרופדאון ייפתח ריק (QA-11)")

# 11. QA-12: קוד הדרופדאון חייב לנטרל את כפתור הפאנל לכרטיס שאזל/הסתיים.
for _f,_h in _pages.items():
    if _h and not (re.search(r"dBtn\.classList\.toggle\(['\"]--sold",_h) and "aria-disabled" in _h):
        errors.append(f"{_f}: הדרופדאון בלי נטרול כפתור לכרטיס אזל (dBtn --sold + aria-disabled) - הפאנל יציע 'כרטיסים' לאירוע שאזל (QA-12)")

# 12. QA-05: markPast חייב בשני העמודים, מבוסס data-event-iso (לא שנה נוכחית), וכל כרטיס נושא data-event-iso.
for _f,_h in _pages.items():
    if not _h: continue
    if "function markPast" not in _h:
        errors.append(f"{_f}: אין markPast - אירועים שעברו יישארו עם כפתור כרטיסים (QA-05)")
    else:
        _mp=_h[_h.find("function markPast"):_h.find("function markPast")+2500]
        if "data-event-iso" not in _mp:
            errors.append(f"{_f}: markPast בלי data-event-iso - השוואה מול שנה נוכחית תחיה אירועי שנה שעברה ב-1 בינואר (QA-05)")
    for _m in re.finditer(r'<article class="lp-card"([^>]*)>',_h):
        if 'data-slug' in _m.group(1) and 'data-event-iso' not in _m.group(1):
            _sl=re.search(r'data-slug="([a-z0-9-]+)"',_m.group(1))
            errors.append(f"{_f}: כרטיס {_sl.group(1) if _sl else '?'} בלי data-event-iso (QA-05)")
    for _sl,_iso2 in re.findall(r'data-slug="([a-z0-9-]+)" data-event-iso="([0-9-]+)"',_h):
        _base=re.sub(r'-b$','',_sl)
        _ev=events.get(_sl) or events.get(_base)
        if _ev and _ev.get("iso","")[:10] and _ev["iso"][:10]!=_iso2:
            warns.append(f"{_f}: data-event-iso של {_sl} ({_iso2}) לא תואם ל-cloud-events.json ({_ev['iso'][:10]})")

# 13. QA-09: זוגיות CSS - class קריטי שמופיע בעמוד בלי חוק CSS באותו עמוד.
_CRIT=["lp-card__namelink","lp-lastseats","lp-soldout","lp-newshow","lp-flagcombo",
       "lp-card__btn--sold","lp-card__btn--ended","lp-detail__btn"]
for _f,_h in _pages.items():
    if not _h: continue
    _styles="".join(re.findall(r'<style[^>]*>(.*?)</style>',_h,re.S))
    for _c in _CRIT:
        if _c in _h and ("."+_c) not in _styles:
            errors.append(f"{_f}: המחלקה {_c} בשימוש אבל אין לה חוק CSS בעמוד - תוצג בעיצוב דפדפן גולמי (QA-09)")

# 14. QA-04: תאריך שעבר ליד קישור הרשמה/רכישה בעמודי התוכן (מחוץ ל-script) - אזהרה.
if live:
    _scan=["cloud-hr.html","private.html","retreat.html","cloud-card.html"]
else:
    # רק עמודים שבאמת חיים - לפי מפת האתר; קבצים מקומיים (גיבויים, דמו, _*) לא נסרקים
    _sm=os.path.join(LOCAL,"sitemap.xml")
    if os.path.exists(_sm):
        _locs=re.findall(r"<loc>https?://[^/<]+/([^<]*)</loc>",open(_sm,encoding="utf-8").read())
        _scan=[(l or "index.html") if l.endswith(".html") or l=="" else l+".html" for l in _locs if "/" not in l]
        _scan=[f for f in _scan if os.path.exists(os.path.join(LOCAL,f))]
    else:
        _scan=[f for f in os.listdir(LOCAL) if f.endswith(".html") and not f.startswith("_")]
_scan=[f for f in _scan if f.endswith(".html") and "archive" not in f]
for _f in sorted(set(_scan)):
    _h=read(_f)
    if not _h: continue
    _noscript=re.sub(r'<script[^>]*>.*?</script>'," ",_h,flags=re.S)
    _noscript=re.sub(r'<style[^>]*>.*?</style>'," ",_noscript,flags=re.S)
    # מסמנים קישורי הרשמה/רכישה, ואז מפשיטים את כל התגיות - נשאר טקסט גלוי בלבד
    _noscript=re.sub(r'<a\s[^>]*(?:eventer\.co\.il|docs\.google\.com/forms|reg-link)[^>]*>'," [REGLINK] ",_noscript)
    _noscript=re.sub(r'<[^>]*>'," ",_noscript)
    for _m in re.finditer(r'(?<![\d.])(\d{1,2})\.(\d{1,2})(?:\.(\d{2,4}))?(?![\d.])',_noscript):
        _dd,_mm=int(_m.group(1)),int(_m.group(2))
        if not (1<=_dd<=31 and 1<=_mm<=12): continue
        _yy=int(_m.group(3)) if _m.group(3) else _dt.date.today().year
        if _yy<100: _yy+=2000
        try: _d=_dt.date(_yy,_mm,_dd)
        except ValueError: continue
        if _d>=_dt.date.today()-_dt.timedelta(days=3): continue
        _win=_noscript[max(0,_m.start()-400):_m.end()+400]
        if "[REGLINK]" in _win:
            warns.append(f"{_f}: תאריך שעבר {_dd}.{_mm}.{_yy} ליד קישור הרשמה/רכישה - עמוד חי מקדם אירוע שחלף? (QA-04)")

src="האתר החי" if live else "העותק המקומי"

# 12. (15.9.2026, אחרי ביקורת יועץ) סכמת עמוד השיתוף מול הכרטיסים - לפי קוד איוונטר, לא לפי שם:
#     לכל Offer בעמוד שיתוח עתידי: שעת האירוע = שעת הכרטיס שנושא את הקוד; זמינות = תווית הכרטיס; מחיר 135 (מסיבה 70).
_cards_by_code={}
_h=read("cloud.html") or ""
for m in re.finditer(r'<article class="lp-card"[^>]*data-slug="([^"]+)"',_h):
    b=_h[m.start():_h.find("</article>",m.start())]
    code=(re.search(r'class="lp-card__btn[^"]*"[^>]*href="https://www.eventer.co.il/(\w+)"',b) or [None,""])[1]
    t=(re.search(r'class="w-time"[^>]*>([^<]+)<',b) or [None,""])[1]
    sold=("lp-soldout" in b) or ("lp-card__btn--sold" in b)
    combo=re.search(r'class="lp-flagcombo[^"]*"[^>]*>(.*?)</span>',b,re.S)
    last=("lp-lastseats" in b) or bool(combo and "אחרון" in combo.group(1))
    if code: _cards_by_code[code]={"slug":m.group(1),"time":t.strip(),"av":"SoldOut" if sold else ("LimitedAvailability" if last else "InStock")}
_share_dir=os.path.join(LOCAL,"share") if not live else None
_share_files=sorted(os.listdir(_share_dir)) if _share_dir and os.path.isdir(_share_dir) else [f"{slug}.html" for slug in events]
for fn in _share_files:
    if not fn.endswith(".html") or fn.startswith("_"): continue
    sh=read("share/"+fn) or ""
    mb=re.search(r'<body data-state="(\w+)" data-event-date="([^"]+)"',sh)
    if not mb or mb.group(2)<_today: continue
    for blk in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',sh,re.S):
        try: d=json.loads(blk)
        except Exception: errors.append(f"share/{fn}: JSON-LD לא תקין"); continue
        items=d.get("@graph") if isinstance(d,dict) and "@graph" in d else (d if isinstance(d,list) else [d])
        for x in items:
            if not isinstance(x,dict) or x.get("@type") not in ("Event","MusicEvent"): continue
            offs=x.get("offers") or []
            offs=offs if isinstance(offs,list) else [offs]
            for o in offs:
                code=str(o.get("url",""))[-5:]; c=_cards_by_code.get(code)
                if not c: warns.append(f"share/{fn}: קוד {code} בסכמה בלי כרטיס ב-cloud.html"); continue
                st=str(x.get("startDate",""))[11:16]
                if st and c["time"] and st!=c["time"]: errors.append(f"share/{fn}: ההצעה {code} תחת אירוע שמתחיל ב-{st} אבל הכרטיס ({c['slug']}) בשעה {c['time']}")
                av=str(o.get("availability","")).split("/")[-1]
                if av!=c["av"]: errors.append(f"share/{fn}: זמינות {av} להצעה {code} אבל הכרטיס ({c['slug']}) אומר {c['av']}")
                price=str(o.get("price","")); exp="70" if "rak-house" in fn else "135"
                if price and price!=exp: errors.append(f"share/{fn}: מחיר {price} להצעה {code} (צפוי {exp})")
# 13. גיל מקור המלאי: סנאפשוט ישן מ-12 שעות = אזהרה (הבדיקה מצליבה מול מקור שהתיישן)
try:
    import datetime as _dt
    _asof=json.load(open(SNAP)).get("asof","") if os.path.exists(SNAP) else ""
    if _asof:
        _age=(_dt.datetime.now()-_dt.datetime.strptime(_asof,"%Y-%m-%d %H:%M")).total_seconds()/3600
        if _age>12: warns.append(f"סנאפשוט איוונטר בן {_age:.0f} שעות ({_asof}) - למשוך מחדש לפני שמסתמכים על ההצלבה")
except Exception: pass

print(f"בדיקת עקביות קלאוד ({src}): {len(events)} אירועים ב-json, {len(cards)} כרטיסים")
for x in errors: print("  שגיאה:",x)
for x in warns: print("  אזהרה:",x)
if not errors and not warns: print("  תקין - אין סתירות")
sys.exit(1 if errors else 0)
