#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""seo-check.py - בדיקות SEO מכניות על עותק האתר (מקומי או קלון). נוצר 15.9.2026 אחרי ביקורת יועץ.
שימוש: python3 seo-check.py [--dir <תיקיית האתר>]   (ברירת מחדל: O-output/website-sol-therapy)
בודק: title/description/canonical בכל עמוד לאינדוקס; קנוניקל = כתובת העמוד; כותרות כפולות; JSON-LD תקין;
EventCompleted אסור; כל loc במפת האתר = קובץ קיים + קנוניקל תואם; קישורים פנימיים יחסיים לקבצים קיימים.
יציאה 1 = יש שגיאות (מיועד לשער פריסה)."""
import os, re, sys, json, glob, argparse, html
ap=argparse.ArgumentParser(); ap.add_argument("--dir", default="/Users/yaronamor/Documents/yaronamor-vault/sol/O-output/website-sol-therapy")
a=ap.parse_args(); D=a.dir.rstrip("/"); BASE="https://sol-therapy.com"
errors=[]; warns=[]
def rd(p):
    try: return open(p,encoding="utf-8",errors="replace").read()
    except Exception: return ""
def url_of(rel):
    rel=rel[:-5] if rel.endswith(".html") else rel
    if rel=="index": rel=""
    return BASE+"/"+rel
files=sorted(glob.glob(D+"/*.html")+glob.glob(D+"/share/*.html"))
titles={}
existing=set(os.path.relpath(p,D) for p in glob.glob(D+"/**/*",recursive=True))
for p in files:
    rel=os.path.relpath(p,D); s=rd(p)
    if os.path.basename(rel).startswith("_"): continue
    noindex=bool(re.search(r'<meta[^>]+name="robots"[^>]+noindex',s,re.I))
    t=re.search(r"<title>(.*?)</title>",s,re.S); d=re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"',s); c=re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)
    if not noindex:
        if not t or not t.group(1).strip(): errors.append(f"{rel}: אין title")
        if not d or not d.group(1).strip(): errors.append(f"{rel}: אין description")
        if not c: errors.append(f"{rel}: אין canonical")
        elif c.group(1) not in (url_of(rel), BASE+"/"+rel) and not (rel=="index.html" and c.group(1).rstrip("/")==BASE): errors.append(f"{rel}: canonical {c.group(1)} לא תואם לכתובת {url_of(rel)}")
        if t: titles.setdefault(t.group(1).strip(),[]).append(rel)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(b)
        except Exception as e: errors.append(f"{rel}: JSON-LD לא תקין ({str(e)[:40]})")
    if "EventCompleted" in s: errors.append(f"{rel}: EventCompleted אינו ערך תקני בסכמה")
    for h in set(re.findall(r'href="([^"#?:]+)"',s)):
        if "'" in h or "+" in h: continue
        if h.startswith(("http","mailto","tel","//","data:")) or h.startswith("/"): 
            if h.startswith("/") and not h.startswith("//"):
                tgt=h.lstrip("/"); tgt=tgt or "index.html"
                if tgt not in existing and tgt+".html" not in existing and not tgt.endswith("/"): warns.append(f"{rel}: קישור פנימי {h} לא נמצא כקובץ")
            continue
        base=os.path.dirname(rel); tgt=os.path.normpath(os.path.join(base,h))
        if tgt not in existing and tgt+".html" not in existing: warns.append(f"{rel}: קישור יחסי {h} לא נמצא")
for t,rels in titles.items():
    if len(rels)>1: errors.append(f"title כפול: '{t[:50]}' -> {', '.join(rels)}")
sm=rd(D+"/sitemap.xml")
locs=re.findall(r"<loc>(.*?)</loc>",sm)
if len(locs)!=len(set(locs)): errors.append("כפילויות במפת האתר")
for u in locs:
    rel=u.replace(BASE,"").lstrip("/"); f=(rel or "index")+(".html" if not rel.endswith(".html") else "")
    if f not in existing and rel+".html" not in existing: errors.append(f"sitemap: {u} - אין קובץ"); continue
    s=rd(os.path.join(D,f if f in existing else rel+".html"))
    c=re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"',s)
    if c and c.group(1).rstrip("/")!=u.rstrip("/"): errors.append(f"sitemap: {u} - הקנוניקל בעמוד הוא {c.group(1)}")
    if re.search(r'<meta[^>]+name="robots"[^>]+noindex',s,re.I): errors.append(f"sitemap: {u} - עמוד noindex במפה")
print(f"בדיקת SEO ({D}): {len(files)} קבצים, {len(locs)} כתובות במפה")
for e in errors: print("  שגיאה:",e)
for w in warns[:25]: print("  אזהרה:",w)
if len(warns)>25: print(f"  ... ועוד {len(warns)-25} אזהרות")
print("תקין" if not errors else f"{len(errors)} שגיאות"); sys.exit(1 if errors else 0)
