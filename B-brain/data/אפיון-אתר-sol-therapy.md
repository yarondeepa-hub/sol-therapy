# בריף לעיצוב ובניית אתר - סול תרפי

אתר חוויה אמנותית + קידום אירועים - סול תרפי
סוג אתר: Multi-page (עמוד ראשי + דפי אירועים + יומן + עיתונות)
**שפה: עברית (פניה לקהל ישראלי)**
**פלטפורמה: Astro + Sanity CMS**

---

## 1. מהות הפרויקט

**חזון:** האתר הוא לא ויטרינה - הוא חלק מהחוויה. כניסה לאתר צריכה להרגיש כמו כניסה למרחב מדיטטיבי. נייר Washi, דיו שזורם, שקט שמדבר.

**שלוש מטרות:**
1. **חוויה אמנותית** - האתר עצמו הוא יצירה, חלק מהזהות של סול תרפי
2. **קידום אירועים** - מכירת כרטיסים לאירועים וריטריטים ספציפיים
3. **סמכות מותגית** - ביסוס מעמד כמוביל בתחום מדיטציות הסאונד בישראל

---

## 2. קהל היעד

- **קהל פרטי ("המחפשים"):** חובבי מוזיקה, וולנס ותרבות, גיל 30+, משכילים, מעריכי איכות
- **B2B / מוסדי:** מנהלי תרבות (מוזיאונים), הפקות, ארגונים, מלונות בוטיק

---

## 3. קונספט עיצובי (Look & Feel)

**אווירה:** "דיו על נייר Washi". האתר צריך להרגיש כמו גלילת מגילה יפנית - כל גלילה חושפת שכבה חדשה. בהיר, חם, שקט - עם רגעים של עוצמה מדודה.

**פילוסופיית עיצוב:**
- **Ma (間)** - החלל הריק הוא חלק מהעיצוב, כמו השתיקה בין הצלילים
- **Wabi-Sabi** - יופי בפשטות ובחומרים טבעיים (טקסטורות נייר, דיו)
- **Kanso** - פשטות מוחלטת, הסרת כל מה שמיותר

### הבדל מגרסה 2.x: בהיר-first

> **שינוי מהותי:** האתר עובר מאסתטיקה כהה (שחור + זהב) לאסתטיקה בהירה (קרם + ירוק). זו הזהות האמיתית של סול תרפי כפי שהיא משתקפת בכל החומרים הגרפיים שנוצרו - כרטיסי מציגים, חומרי ריטריט, עיצובי InDesign.

**סגנון:**
- **רקע ראשי בהיר** - Washi cream (#F2EAD3), לא שחור. הקרם החם הוא ה-DNA.
- **סקשנים כהים כחריג** - רק ל-Hero ולרגעים דרמטיים ספציפיים (אינדיגו #264348)
- **צורות אורגניות** - ה-"Zen Pebble" - blobs טבעיים במקום ריבועים חדים
- טיפוגרפיה אלגנטית ושקטה
- מרחב נדיב בין אלמנטים (Ma)

---

### פלטת צבעים (Washi & Ink)

בהשראת: נייר Washi, דיו סומי-אה, חותמות Hanko, טבע יפני

**רקע ראשי:**

| שם | HEX | שימוש |
|----|-----|-------|
| **Washi Cream** | `#F2EAD3` | רקע ראשי - תמיד. אף פעם לא לבן טהור |
| **Washi Warm** | `#EDE5CE` | רקע משני, כרטיסים |

**צבע ראשי - ירוק:**

| שם | HEX | שימוש |
|----|-----|-------|
| **Sol Green** | `#588475` | טקסט ראשי, כותרות, לינקים |
| **Sol Green Dark** | `#3B514B` | טקסט משני, hover states |
| **Sol Green Light** | `#6A9A89` | אקסנטים עדינים |

**צבע משני - ורוד-אדום:**

| שם | HEX | שימוש |
|----|-----|-------|
| **Beni (ורוד-אדום)** | `#BE5069` | אקסנט, separators, CTA buttons, תאריכים |
| **Beni Light** | `#D4728A` | hover על כפתורים |

**צבעים תומכים:**

| שם | HEX | שימוש |
|----|-----|-------|
| **Ai-iro (אינדיגו)** | `#264348` | רקע Hero, סקשנים כהים |
| **Bero-ai (כחול פרוסי)** | `#314D59` | גרדיינטים בוקאשי, שמיים |
| **Vermilion** | `#D3381C` | חותמת Hanko, אלמנט חתימתי יחיד |
| **Nezumi (אפור)** | `#949495` | טקסט muted, מטאדאטה |

> **חוק ברזל:** הרקע לעולם אינו לבן טהור (#FFFFFF). תמיד Washi cream.
> **חוק שני:** הצבע הדומיננטי הוא ירוק (#588475). הורוד הוא אקסנט בלבד.
> **חוק שלישי:** שחור טהור (#000000) לא מופיע. רק אינדיגו כהה (#264348) לרגעים דרמטיים.

---

### טיפוגרפיה

> **עיקרון מפתח (בהשראת Rotem Cohen-Soaye):** טיפוגרפיה כמנוע זהות - האות אינה רק נשאית טקסט אלא חומר צורני.

**פונטים:**

| שימוש | פונט | משקל | הערה |
|-------|------|------|------|
| כותרות עברית | Frank Ruhl Libre | Light (300) | אלגנטי ושקט |
| גוף עברית | Heebo | Regular (400) | נקי וקריא |
| כותרות אנגלית | Inter | Light (300) | optical weight matching |
| גוף אנגלית | Inter | Regular (400) | התאמה ל-Heebo |
| Branding | Sans-serif (Avenir Next / Inter) | Thin + Bold | uppercase, ל-"SOL THERAPY" |

**עקרונות רב-לשוניות:**
- ריבוד תרבותי מכוון: header אנגלית sans-serif מודרני, תוכן עברית serif קלאסי
- Optical weight matching - לא "להדביק" פונטים לא תואמים
- Font pairing עקבי בכל הפלטפורמות

**ריווח:** נדיב - Ma (間). מינימום 60% negative space בכל section.

---

### אנימציות - דיו במים

> **עיקרון:** כל תנועה באתר צריכה להרגיש כמו דיו שזורם בנייר רטוב - אורגנית, איטית, בלתי הפיכה. לא bouncing. לא sliding. התגלות.

**אנימציות מרכזיות:**

| אנימציה | איפה | תיאור |
|----------|------|--------|
| **Ink Reveal** | Hero | הכותרת מתגלה כאילו מישהו כותב אותה בדיו |
| **Sumi-e Scroll** | כל סקשן | אלמנטים מתגלים בגלילה כמו משיכות מכחול - מקל למעובה |
| **Bokashi Fade** | מעברי סקשנים | גרדיינטים חלקים כמו טכניקת בוקאשי |
| **Zen Pebble Float** | גלריה | צורות אורגניות שצפות עם צל רך |
| **Ink Drop** | אינדיקטור גלילה | טיפת דיו שנופלת לאט |
| **Washi Texture** | רקע | טקסטורת נייר עדינה שנעה מעט בגלילה (parallax) |

**כללים:**
- כל אנימציה נכבדת `prefers-reduced-motion`
- לא יותר מאנימציה אחת פעילה באותו viewport
- מהירות: 0.8s-1.5s, cubic-bezier(0.23, 1, 0.32, 1)
- אנימציה פעם אחת בלבד (לא חוזרת בכל scroll)

**טכנולוגיה:**
- View Transitions API (Astro native)
- GSAP ScrollTrigger לאנימציות מורכבות
- CSS animations לאפקטים פשוטים
- Intersection Observer ל-reveal on scroll

---

### אלמנט חותם: ה-"Zen Pebble"

> **הצורה האורגנית שזוהתה בכרטיסי המציגים של ריטריט פסטורל.**

- צורת "אבן נחל" אורגנית - blob mask לתמונות
- לא עיגול, לא ריבוע - צורה טבעית מעוגלת
- כל שימוש עם וריאציה שונה קלות של הצורה
- צל רך מתחת (floating effect)
- מתחברת למטאפורה של "גינת זן ענקית ופועמת"
- שימוש: תמונות אמנים, תמונות גלריה, avatar elements

---

### נגישות (WCAG AA)
- יחס ניגודיות מינימלי **4.5:1** לטקסט רגיל, **3:1** לכותרות גדולות
- ירוק #588475 על Washi #F2EAD3 = יחס 4.1:1 - מעבר בכותרות, צריך Sol Green Dark (#3B514B = 6.2:1) לטקסט קטן
- ניווט מקלדת מלא, visible focus states
- ARIA labels, semantic headings
- כיבוד `prefers-reduced-motion`

---

## 4. מבנה האתר (Site Architecture)

### ארכיטקטורה

```
/ .......................... עמוד ראשי (7 סקשנים בגלילה)
/אירועים/<slug> ........... דף אירוע ייעודי (דינמי מ-CMS)
/יומן ..................... ארכיון תוכן אוצרותי
/יומן/<slug> .............. פוסט בודד
/לעיתונות ................. ערכת עיתונות
```

### עמוד ראשי - Site Flow

הזרימה: **שקיעה לתוך המרחב -> התדר -> מסעות -> הוכחה -> סאונד -> חיבור**

### כפתור CTA צף (Floating Action Button)
כפתור **"לכרטיסים"** קבוע בפינת המסך.
- צבע: Sol Green (#588475) על רקע שקוף עם blur
- מופיע רק אחרי שהמשתמש גולל מעבר ל-Hero
- מוביל לסקשן האירועים
- נגיש מכל מקום באתר

---

### Section 1: Hero - כניסה למרחב

**רקע:** אינדיגו כהה (#264348) - הסקשן היחיד שהוא כהה-first

**אופציה א' - וידאו:**
וידאו מסך מלא בלופ איטי - אנשים שוכבים, תאורה חמה, חלל מוזיאלי. Overlay של gradient מאינדיגו.

**אופציה ב' - אנימציית דיו (מועדפת):**
קנבס אינטראקטיבי - דיו שזורם בנייר רטוב, מגיב לתנועת העכבר. הכותרת "סול תרפי" מתגלה מתוך הדיו כאילו מישהו כותב אותה. קליגרפיה שמתפתחת לאט.

**אלמנטים:**
- לוגו Sol Therapy בפינה העליונה
- כותרת "סול תרפי" - Frank Ruhl Libre, ענקית, צבע Washi cream
- תגלית "היכן שהצליל הופך לדממה" - מתגלה בעיכוב
- אינדיקטור גלילה - טיפת דיו שנופלת

**מעבר:** גרדיינט בוקאשי מאינדיגו לקרם Washi - כמו שחר שעולה

---

### Section 2: התדר שלנו (אודות)

**רקע:** Washi cream (#F2EAD3)
**צבע טקסט:** Sol Green (#588475)

**עיצוב:** טיפוגרפיה גדולה, אוצרותית, כמו טקסט תערוכה במוזיאון. יישור לא סימטרי - הטקסט לא במרכז, הוא נשען לצד כמו טקסט על קיר גלריה.

**מבנה משפט מיצוב:**
- **שורה 1:** מה זה (חוויות שמע אימרסיביות במרחבים תרבותיים)
- **שורה 2:** מה זה לא - בלי להישמע דפנסיבי (לא טיפול קליני. לא מדיטציה מודרכת.)
- **2-3 שורות:** מה הקהל חווה (הקשבה, גוף ככלי תהודה, קשב משתנה)

**UX:** קצר + "קרא עוד" שפותח מודל עם הפילוסופיה המלאה

---

### Section 3: מסעות קרובים (אירועים)

**רקע:** Washi cream (#F2EAD3)
**צבע טקסט:** Sol Green (#588475)
**צבע אקסנט:** Beni (#BE5069) לתאריכים ול-CTA

**עיצוב:** רשימה טיפוגרפית נקייה - כמו קטלוג תערוכה. לא כרטיסים עם תמונות - טקסט בלבד עם קווים מפרידים עדינים.

**כרטיס אירוע (Catalog Entry):**
```
תאריך (Beni)  |  שם האירוע (Sol Green, serif heavy)  |  מיקום
               |  פורמט - משך - קיבולת (muted)        |
               |  [שמרו לי מקום] (CTA)                |
```

**כפתור רכישה:** "שמרו לי מקום" - צבע Beni (#BE5069)
**מצב רשימת המתנה:** אוטומטי לאירועים שנמכרו

**פס אמון מקוצר (תחת האירועים):**
שורה עדינה מונוכרומטית של לוגואים של שותפים מוסדיים - מוזיאון ת"א, סוזן דלל, הספריה הלאומית, מלון פסטורל.

**טכני:**
- דף קנוני לכל אירוע: `/אירועים/<slug>`
- Schema.org: `Event` + `Offer` + `EventStatus`
- תוכן מגיע מ-Sanity CMS
- מעקב: GA4/Plausible

---

### Section 4: ארכיון ויזואלי (גלריה)

**רקע:** Washi cream (#F2EAD3)

**עיצוב:** גריד אורגני - לא סימטרי, לא מסודר. תמונות בתוך צורות "Zen Pebble" - blobs אורגניים. שילוב של תמונות סטילס ווידאו-שורטס בלופ.

**מטאדאטה אוצרותית:**
- כיתוב ב-hover/tap: `מקום / עיר / שנה`
- פילטור: מוזיאונים | ריטריטים | ליווי מוזיקלי | קהל

**טכני:**
- Lightbox נגיש: focus trap, ESC, swipe במובייל, ARIA
- תמונות: responsive `srcset`, WebP/AVIF, lazy-load
- תמונות מנוהלות ב-Sanity CMS עם metadata fields

---

### Section 5: פס אמון (הוכחה חברתית)

**עיצוב:** שורה עדינה, נקייה. לוגואים בגוון Sol Green (מונוכרומטי, לא צבעוני).

**תוכן:** מוזיאון ת"א, מגדל דוד, סוזן דלל, הספריה הלאומית, מלון פסטורל, Amazon Music

---

### Section 6: זהות סאונד (צליל)

**רקע:** אינדיגו (#264348) - סקשן כהה שני, יוצר רגע דרמטי

**עיצוב:** נגן custom מינימליסטי - לא embed של SoundCloud. UI עצמאי בסגנון vinyl/waveform.

**פונקציונליות:**
- קטע קצר (30-60 שניות) שמתנגן ב-UI עצמאי
- "לסט המלא בסאונדקלאוד" - פעולה משנית
- טיזר ויזואלי ל-Sol Therapy Records

**טכני:**
- Lazy-load לאמבד חיצוני רק אחרי אינטראקציה
- כיבוד `prefers-reduced-motion`
- Audio Web API לנגן custom

---

### Section 7: פוטר - התחברו

**רקע:** Washi cream (#F2EAD3)

**חלוקה ל-2 עמודות:**
- **לקהל:** "הצטרפו לקהילה" - הרשמה לניוזלטר
- **לתעשייה:** "שיתופי פעולה" - כפתור יצירת קשר

**לינקים:** אינסטגרם, טיקטוק

**אלמנט חתימתי:** חותמת Hanko קטנה בצבע Vermilion (#D3381C) - כמו חתימה יפנית

---

## 5. דפים נוספים

### דף אירוע (`/אירועים/<slug>`)

דף שלם לכל אירוע - קריטי ל-SEO ולשיתוף.

**מבנה:**
- Hero עם תמונת האירוע (Zen Pebble mask)
- שם האירוע + תאריך + מיקום
- תיאור מורחב (מ-CMS)
- לינאפ אמנים עם כרטיסי מציג מוקטנים
- CTA ראשי - "שמרו לי מקום"
- מפת מיקום
- Schema.org: Event + Offer

---

### יומן (`/יומן`)

ארכיון תוכן אוצרותי - לא "בלוג".

**סגנון:** כל פיסה קצרה, מובלת-תמונה, ציטוט אחד, רעיון אחד.

**סוגי תוכן:**
- מאמרים על ריפוי בצליל
- סיקור אירועים קודמים
- ראיונות עם אמנים
- רגעים מהשטח (2-4 בחודש)

**טכני:**
- `Article` schema לכל פוסט
- XML sitemap + RSS
- OG tags + meta descriptions
- תוכן מנוהל ב-Sanity CMS

---

### ערכת עיתונות (`/לעיתונות`)

דף ייעודי לעיתונאים, אוצרים ומוסדות.

**תוכן:**
- **טקסט תקני:** 70-120 מילים, רשמי, עובדתי
- **תמונות:** 3-5 תמונות (אופקי + אנכי), עם קרדיט
- **לוגואים:** SVG + PNG + כללי שימוש
- **ציטוט:** אחד חזק בטון אוצרותי
- **פרטי קשר:** יח"צ / הזמנות / שיתופי פעולה

**טכני:**
- קובץ להורדה: `SolTherapy_PressKit.zip`
- תמונות: 3000px wide, JPG + WebP
- `Organization` schema + `sameAs` links

---

### מודל טיפול ובטיחות

מודל קצר עם מידע חשוב למשתתפים:
- רגישויות (עוצמת סאונד)
- למי החוויה עשויה לא להתאים
- מה להביא
- איך ליצור קשר עם צוות

**טון:** רגוע, אחראי, לא-רפואי

---

## 6. דגשים טכניים

### Stack טכנולוגי

| שכבה | טכנולוגיה | למה |
|------|-----------|-----|
| **Framework** | Astro 5.x | Zero JS by default, View Transitions, Islands |
| **CMS** | Sanity | Headless, ויזואלי, מצוין לעברית, real-time preview |
| **Hosting** | Netlify / Vercel | CDN, auto-deploy from git |
| **אנימציות** | GSAP + ScrollTrigger | אנימציות דיו מורכבות |
| **Styling** | CSS custom properties | Design tokens, no framework overhead |
| **Images** | Astro Image + Sanity CDN | Responsive, WebP/AVIF, lazy-load |
| **Analytics** | Plausible | פרטיות-first, בלי cookies |
| **Forms** | Netlify Forms / Formspree | ניוזלטר, יצירת קשר |

### עקרונות כלליים
- **Mobile First:** רוב הטראפיק מאינסטגרם - מובייל חייב להיות מושלם
- **CMS:** Sanity Studio לעדכון עצמאי של אירועים, תמונות, תוכן יומן
- **Performance:** Core Web Vitals מושלמים - Astro מספק את זה out of the box
- **RTL:** תמיכה מלאה בכיוון ימין לשמאל

### Sanity CMS - Content Types

```
Event (אירוע):
  - title (string)
  - slug (slug)
  - date (datetime)
  - location (string)
  - format (string) - "מדיטציית סאונד", "ריטריט", "סדנה"
  - duration (string)
  - capacity (number)
  - price (number)
  - status (string) - "available", "few-left", "soldout"
  - description (rich text)
  - image (image with hotspot)
  - artists (array of references to Artist)
  - purchaseUrl (url)

Artist (אמן):
  - name (string)
  - role (string)
  - bio (rich text)
  - image (image)

JournalPost (פוסט יומן):
  - title (string)
  - slug (slug)
  - date (datetime)
  - category (string) - "מאמר", "סיקור", "ראיון"
  - excerpt (text)
  - body (rich text)
  - featuredImage (image)

GalleryItem (פריט גלריה):
  - image (image) / video (file)
  - venue (string)
  - city (string)
  - year (string)
  - tags (array of strings)

SiteSettings (הגדרות):
  - title (string)
  - description (text)
  - socialLinks (array)
  - pressKit (file)
```

---

### Design System - Design Tokens

```css
:root {
  /* === Colors - Washi & Ink === */

  /* Background */
  --color-washi: #F2EAD3;
  --color-washi-warm: #EDE5CE;

  /* Primary - Sol Green */
  --color-green: #588475;
  --color-green-dark: #3B514B;
  --color-green-light: #6A9A89;

  /* Accent - Beni */
  --color-beni: #BE5069;
  --color-beni-light: #D4728A;

  /* Drama - Indigo */
  --color-indigo: #264348;
  --color-indigo-light: #314D59;

  /* Signature */
  --color-vermilion: #D3381C;

  /* Neutral */
  --color-muted: #949495;

  /* === Typography === */
  --font-display: 'Frank Ruhl Libre', serif;
  --font-body: 'Heebo', sans-serif;
  --font-english: 'Inter', sans-serif;
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-bold: 700;

  /* === Spacing - Ma === */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 2rem;
  --space-lg: 4rem;
  --space-xl: 8rem;
  --space-section: clamp(8rem, 15vw, 14rem);
  --container-max: 1100px;
  --container-padding: clamp(2rem, 8vw, 5rem);

  /* === Transitions === */
  --ease-ink: cubic-bezier(0.23, 1, 0.32, 1);
  --duration-fast: 0.3s;
  --duration-smooth: 0.6s;
  --duration-slow: 1s;
  --duration-reveal: 1.2s;

  /* === Borders === */
  --border-subtle: 1px solid rgba(88, 132, 117, 0.15);
  --border-accent: 1px solid rgba(190, 80, 105, 0.3);
}
```

---

### Component Architecture

```
Components (Astro):

1. Hero.astro
   - Canvas/video background
   - Ink reveal animation
   - Bokashi gradient transition

2. About.astro
   - Museum wall text layout
   - Modal for extended philosophy
   - Asymmetric typography

3. Events.astro
   - Catalog-style event list
   - Dynamic from Sanity CMS
   - Status badges (available/few-left/soldout)
   - Trust bar with partner logos

4. Gallery.astro
   - Organic grid with Zen Pebble masks
   - Lightbox with keyboard navigation
   - Filter by category
   - Lazy-loaded images

5. Sound.astro
   - Custom audio player UI
   - Waveform visualization
   - SoundCloud lazy embed

6. Footer.astro
   - Newsletter signup
   - B2B contact CTA
   - Social links
   - Hanko stamp signature

7. EventPage.astro (layout for /אירועים/<slug>)
   - Full event details
   - Artist cards
   - Purchase CTA
   - Schema markup

8. JournalLayout.astro (layout for /יומן)
   - Archive grid
   - Post page

Shared:
- ZenPebble.astro - organic blob mask component
- SectionTransition.astro - Bokashi gradient between sections
- FloatingCTA.astro - sticky ticket button
```

---

### SEO

- דף קנוני לכל אירוע: `/אירועים/<slug>`
- Schema.org: `Event` + `Offer` + `EventStatus` + `Organization` + `Article`
- XML sitemap + RSS ליומן
- OG tags + Twitter cards לכל דף
- meta titles/descriptions חזקים
- Performance: Astro SSG = 100 Lighthouse

---

### Checklist לפיתוח

```
[ ] RTL support מלא
[ ] Font pairing עקבי (Frank Ruhl Libre + Heebo + Inter)
[ ] רקע Washi cream (#F2EAD3) - לא לבן טהור
[ ] ירוק (#588475) כצבע ראשי - לא שחור, לא זהב
[ ] Zen Pebble masks לתמונות
[ ] Negative space מינימום 60%
[ ] Sanity CMS מחובר עם preview
[ ] דפי אירועים דינמיים מ-CMS
[ ] Schema markup לאירועים
[ ] Ink reveal animations עם GSAP
[ ] View Transitions בין דפים
[ ] Mobile-first responsive
[ ] Image optimization (WebP/AVIF, srcset)
[ ] Plausible analytics
[ ] Core Web Vitals ירוקים
[ ] WCAG AA נגישות
[ ] prefers-reduced-motion support
```

---

## 7. היסטוריית שינויים

### גרסאות 1.0-2.1 (4.2.2026 - 5.2.2026)

ראה ארכיון גרסאות ישנות. עיקרי השינויים:
- v1.0: איפיון ראשוני
- v1.1-1.5: הוספת CTA צף, נגישות, עברית, SEO, ערכת עיתונות
- v2.0: מעבר ל-"Zen Gallery Aesthetic" (כהה + זהב)
- v2.1: Design System בהשראת Rotem Cohen-Soaye

### גרסה 3.0 (11.2.2026)

**שינוי מהותי בקונספט ובטכנולוגיה:**

**עיצוב:**
- מעבר מ-"Dark + Gold" ל-**"Washi Cream + Sol Green"** - התאמה לזהות האמיתית של סול תרפי כפי שמשתקפת בכל החומרים הגרפיים (כרטיסי מציגים, חומרי ריטריט, עיצובי InDesign)
- פלטת צבעים חדשה: Washi (#F2EAD3), Sol Green (#588475), Beni (#BE5069), Indigo (#264348)
- בהיר-first - רקע קרם ראשי, כהה רק ל-Hero וסקשן סאונד
- Zen Pebble - צורות אורגניות במקום גיאומטריה חדה
- אנימציות דיו - ink reveal, sumi-e scroll, bokashi fade
- חותמת Hanko כאלמנט חתימתי

**טכנולוגיה:**
- Sanity CMS - ניהול תוכן דינמי (אירועים, אמנים, גלריה, יומן)
- GSAP + ScrollTrigger - אנימציות מורכבות
- View Transitions API - מעברים חלקים בין דפים
- Multi-page architecture - עמוד ראשי + דפי אירועים + יומן + עיתונות
- Plausible Analytics - פרטיות-first
- Content types מוגדרים ל-Sanity

**תוכן:**
- דפי אירועים עצמאיים עם URL ייחודי
- יומן אוצרותי במקום בלוג
- נגן סאונד custom במקום embed
- Hero אינטראקטיבי (אנימציית דיו) במקום וידאו לופ

**רפרנסים:**
- כרטיסי מציגים של ריטריט פסטורל - Zen Pebble, מונוכרומטי ירוק, Washi cream
- עיצובי InDesign של סול תרפי - ירוק #588475 + ורוד #BE5069
- Rotem Cohen-Soaye - טיפוגרפיה כמנוע זהות
- נאו-ג'פוניזם (Illustrator agent) - Ukiyo-e, Shin-hanga, Sumi-e
