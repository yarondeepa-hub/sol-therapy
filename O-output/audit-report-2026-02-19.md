# דוח ביקורת אתר - סול תרפי
## 19 בפברואר 2026

3 סוכנים ביקרו במקביל: Illustrator (ויזואל), CTO (טכני), Copywriter (תוכן). Gatekeeper איחד ותעדף.

---

### דשבורד

| מדד | ערך |
|-----|-----|
| סה"כ ממצאים (אחרי איחוד) | 42 |
| P0 - תקן עכשיו | 8 |
| P1 - תקן השבוע | 14 |
| P2 - ספרינט הבא | 12 |
| P3 - בקלוג | 8 |

---

### P0 - תקן עכשיו (8)

1. **וידאו 80MB בגלריה** (CTO) - gallery-wide-bottom.mp4 הורס מובייל. סה"כ 97MB וידאו באוטופליי.
   - STATUS: pending

2. **שכבת סומי-א לא קיימת ב-HTML** (Illustrator + CTO) - 200 שורות CSS מוכנות, אפס אלמנטים משתמשים.
   - STATUS: pending

3. **CTA "להזמנת חדרים" - מסגור שגוי** (Copywriter) - סותר "מזמינים, לא מוכרים".
   - STATUS: fixing now

4. **לינק "ארכיון" שבור** (3 סוכנים) - אין id="archive" באתר.
   - STATUS: pending

5. **כל alt בגלריה גנריים** (3 סוכנים) - כל תמונה = "סול תרפי".
   - STATUS: fixing now

6. **7 סקריפטי GSAP חוסמים רנדור** (CTO) - 3 plugins לא בשימוש.
   - STATUS: pending

7. **תפריט מובייל ללא focus trap** (CTO) - אין Escape, אין לכידת פוקוס.
   - STATUS: fixing now

8. **סלקטורים מתים ב-JS** (CTO) - 7 קריאות querySelector לאלמנטים שלא קיימים.
   - STATUS: fixing now

---

### P1 - תקן השבוע (14)

9. אין structured data - JSON-LD לאירועים ולעסק
10. אין canonical URL + OG חלקי
11. **4/7 מעברים קשיחים** - dissolve רק ב-3 סקשנים
    - STATUS: fixing now
12. אין breathing spaces
13. DM Mono נטען ולא בשימוש
14. תוויות באנגלית
15. גלריה ללא כותרת
16. תמונות ללא width/height - CLS
17. Hero ב-JPG
18. טופס ניוזלטר לא עובד
19. פונטים OTF
20. לינק "סרטון" שבור
21. ניגודיות spec strip
22. כותרת ניוזלטר גנרית

---

### P2 - ספרינט הבא (12)

23. Favicon
24. robots/sitemap
25. ארכיטקטורה מונוליתית
26. DRY CSS
27. var->const
28. CDN preconnect
29. scroll snap proximity
30. blog dissolve
31. קטגוריות בלוג
32. blog hover
33. מפריד שותפים-ניוזלטר
34. "ללא ספאם" דפנסיבי

---

### P3 - בקלוג (8)

35. Entry context
36. Footer קליל
37. Tagline כפילות
38. Washi GPU
39. will-change מת
40. Email scraping
41. Blog scroll affordance
42. מניפסטו ארוך

---

### מה חסר באתר

| תוכן חסר | חשיבות |
|-----------|--------|
| דף אודות | גבוהה |
| ביוגרפיות אמנים | גבוהה |
| תיאורי אירועים מפורטים | גבוהה |
| עמוד ארכיון | בינונית |
| שכבת איורי סומי-א + breathing spaces | בינונית |
| Structured data | בינונית |
