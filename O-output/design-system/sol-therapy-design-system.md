# Sol Therapy Design System

> מסמך פנימי לסוכנים - מערכת עיצוב אחודה לכל פורמטי הפלט.
> מקורות: illustrator-taste-profile.md, sol-therapy-knowledge-base.md, voice-dna.md

---

## 1. יסודות - Foundation

---

### 1.1 מערכת צבעים - Color System

> **מקור אחיד ומוסכם.** הפלטה הזו מחליפה כל הגדרת צבע קודמת. כל סוכן שמייצר תוכן ויזואלי - משתמש בזה.

#### פלטה ראשית - Primary Palette

| תפקיד | שם | HEX | RGB | שימוש | אחוז משטח |
|--------|-----|-----|-----|-------|-----------|
| **Paper Base** | Washi | `#E0DDD3` | 224, 221, 211 | רקע ברירת מחדל, שטחים גדולים | 50-70% |
| **Paper Highlight** | Rice Paper | `#EEEEE7` | 238, 238, 231 | אזורי נשימה, הבהרות | חלק מהנייר |
| **Warm Parchment** | Koyori | `#E0D3BC` | 224, 211, 188 | קלף חם, רקע משני, headers | חלק מהנייר |
| **Ink Primary** | Sumi | `#283335` | 40, 51, 53 | טקסט ראשי, קווים, אלמנטים כבדים | 5-15% |
| **Vermilion Seal** | Beni | `#AE2C2C` | 174, 44, 44 | אקסנט יחיד - חותמת, CTA, תאריכים | **3-8% מקסימום** |

#### פלטה משנית - Secondary Palette

| תפקיד | שם | HEX | RGB | שימוש |
|--------|-----|-----|-----|-------|
| **Neutral Shadow** | Usuzumi | `#CECCC7` | 206, 204, 199 | צללים עדינים, מפרידים |
| **Neutral Mid** | Hai | `#BDBAB2` | 189, 186, 178 | טקסט משני, captions |
| **Neutral Deep** | Nezumi | `#A8A195` | 168, 161, 149 | ערפל, שכבות מעומעמות |
| **Cool Ink** | Tetsu | `#7B817D` | 123, 129, 125 | רקע קריר, topography |
| **Deep Indigo** | Ai | `#264348` | 38, 67, 72 | מים, צללים, לילה, heroes כהים |
| **Prussian Blue** | Kon | `#314D59` | 49, 77, 89 | גלים, שמיים, שכבות עומק |
| **Teal Water** | Seiji | `#257167` | 37, 113, 103 | מוטיבי מים בלבד |
| **Print Blue** | Ruri | `#98B0D6` | 152, 176, 214 | מוטיבי topography בלבד |
| **Pine Green** | Matsu | `#4F6F52` | 79, 111, 82 | עלים, יער, גבעות |

#### Aged Cream (לרקעים בהירים מורחבים)

| שם | HEX | שימוש |
|----|-----|-------|
| **Aged Cream Light** | `#FAF6F0` | רקע website, מצגות |
| **Aged Cream** | `#F2EAD3` | רקע מודפסים, כרטיסי ביקור |

#### חוקי צבע - Color Rules

1. **חוק הזהב:** כשאדום (Beni) מופיע - כל השאר שותק. אין כחול + אדום חזק ביחד. אם יש Beni, הרקע חייב להיות נייר/neutral בלבד.
2. **חוק הנייר:** לפחות 50% מכל קומפוזיציה חייב להיות Paper/Cream/Neutral. אף פעם לא צבע עז על צבע עז.
3. **חוק הדיו:** Sumi (`#283335`) הוא הצבע היחיד לטקסט body. אין טקסט באדום (חוץ מתאריכי אירועים). אין טקסט בכחול.
4. **חוק Dark Mode:** לעולם לא שחור טהור (`#000000`). ה-"שחור" שלנו הוא Deep Indigo (`#264348`) או Sumi (`#283335`).
5. **מגבלת צבעי אקסנט:** מקסימום 2 צבעי אקסנט בקומפוזיציה אחת (למשל Beni + Ai, או Beni + Matsu). אף פעם 3.

---

### 1.2 מערכת טיפוגרפיה - Typography System

#### פונטים מומלצים

| שפה | שימוש | פונט ראשי | פונט חלופי | הערות |
|-----|-------|-----------|-----------|-------|
| **עברית - כותרות** | Headlines, titles | **Heebo** (700, 800) | Rubik (700) | Clean, geometric, modern |
| **עברית - גוף** | Body text | **Heebo** (300, 400) | Rubik (400) | ניקיון, קריאות |
| **אנגלית - כותרות** | Headlines | **Inter** (600, 700) | DM Sans (600) | Pairs well with Heebo |
| **אנגלית - גוף** | Body | **Inter** (300, 400) | DM Sans (400) | Clean geometric sans |
| **אנגלית - Editorial** | Captions, labels | **DM Mono** (400) | Space Mono (400) | Museum-label feel, editorial |
| **מספרים / תאריכים** | Dates, stats | **DM Mono** (400) | Tabular Inter | Monospace for alignment |

#### סולם גדלים - Type Scale

> מבוסס על Major Third ratio (1.25). כל הגדלים ב-`clamp()` לרספונסיביות.

| Token | Mobile | Desktop | Line-height | Letter-spacing | שימוש |
|-------|--------|---------|-------------|---------------|-------|
| `--text-hero` | 40px | 80-120px | 0.9 | -0.03em | כותרת hero בלבד |
| `--text-display` | 32px | 56px | 1.0 | -0.02em | כותרות סקשנים |
| `--text-h1` | 28px | 40px | 1.1 | -0.01em | כותרות ראשיות |
| `--text-h2` | 22px | 28px | 1.2 | 0 | כותרות משניות |
| `--text-h3` | 18px | 22px | 1.3 | 0 | כותרות תת-סקשן |
| `--text-body` | 16px | 18px | 1.6 | 0 | טקסט גוף |
| `--text-body-sm` | 14px | 16px | 1.5 | 0.01em | טקסט משני |
| `--text-caption` | 11px | 12px | 1.4 | 0.08em | תוויות, captions, metadata |
| `--text-micro` | 9px | 10px | 1.3 | 0.12em | Museum labels, timestamps |

#### כללי טיפוגרפיה

1. **כותרות עבריות:** תמיד `font-weight: 700` או `800`. אף פעם regular בכותרות.
2. **גוף עברית:** תמיד `font-weight: 300` או `400`. Light weight יוצר תחושת שקט.
3. **RTL:** כל הטקסט העברי ב-`direction: rtl; text-align: right`.
4. **Captions באנגלית:** `uppercase`, `letter-spacing: 0.08-0.12em`, `font-size: text-caption`. כמו תווית מוזיאון.
5. **מספר שורות:** כותרות - מקסימום 2 שורות. גוף - פסקאות קצרות (3-5 שורות).
6. **אסור:** פונטים script/handwriting, פונטים דקורטיביים, bold בגוף טקסט, underline כמודגש.

---

### 1.3 מרחב ונשימה - Spacing & Grid

> עקרון Ma (מה, 間) - החלל הריק הוא אלמנט אקטיבי, לא "רווח שנשאר".

#### סולם ריווח - Spacing Scale

| Token | ערך | שימוש |
|-------|-----|-------|
| `--space-xs` | 4px | בין אותיות, micro-gaps |
| `--space-sm` | 8px | בין אלמנטים צמודים |
| `--space-md` | 16px | padding פנימי |
| `--space-lg` | 32px | בין אלמנטים |
| `--space-xl` | 64px | בין סקשנים קטנים |
| `--space-2xl` | 96px | בין סקשנים |
| `--space-3xl` | 128px | section padding |
| `--space-4xl` | 192px | hero spacing, dramatic breaks |

#### כללי Grid

| כלל | ערך | הערה |
|-----|-----|------|
| **Container max-width** | 1200px | לתוכן טקסטואלי |
| **Full-bleed** | 100vw | לתמונות image breaks |
| **Side margins** | 6-10% מכל צד | שוליים שקטים |
| **Grid columns (desktop)** | 12 columns | עם 24px gutter |
| **Grid columns (mobile)** | 4 columns | עם 16px gutter |
| **Content width** | 8/12 (66%) | לטקסט גוף |
| **Narrow content** | 6/12 (50%) | לציטוטים, pull quotes |
| **Asymmetric split** | 60/40 או 40/60 | לtwo-column layouts |

#### חוק הנשימה

- **בין סקשנים:** לפחות `space-3xl` (128px). עדיף `space-4xl` (192px).
- **בין כותרת לתוכן:** `space-lg` (32px) עד `space-xl` (64px).
- **בין פסקאות:** `space-md` (16px) עד `space-lg` (32px).
- **Image breaks:** תמיד full-bleed, ללא margins. גובה מינימלי 40vh.
- **אף פעם:** אלמנטים צמודים ללא ריווח. תמיד לפחות `space-sm`.

---

### 1.4 סגנון צילום - Photography Style

> לא איורים - תמונות אמיתיות של אירועים, אמנים, מיקומים.

#### מאפיינים

| מאפיין | ערך |
|--------|-----|
| **גוון כללי** | חמים, מעט desaturated, לא פלאש ישיר |
| **טמפרטורת צבע** | חם (warm white balance), גוונים של amber/gold |
| **ניגודיות** | בינונית-נמוכה. לא חד. לא HDR. |
| **עומק שדה** | רדוד (f/1.8-2.8) - פוקוס על נושא אחד, רקע מטושטש |
| **תאורה** | טבעית או ambient חמה. אור נמוך מועדף. אור שעת זהב. |
| **קומפוזיציה** | שליש אחד נושא, שני שלישים חלל. אסימטריה. |
| **נושאים מועדפים** | ידיים על כלים, עיניים עצומות, מרחבים ריקים, פרטים (מיתרים, כפתורים) |
| **נושאים אסורים** | חיוכים מצולמים, קבוצות עם "cheese", selfies, תמונות סטוק גנריות |

#### עיבוד (Post-processing)

| פעולה | ערך |
|-------|-----|
| **Saturation** | -15% עד -25% |
| **Contrast** | -10% |
| **Grain** | עדין (5-10%) |
| **Shadows** | הבהרה קלה (lift blacks) |
| **Highlights** | ריכוך (pull highlights) |
| **Color grade** | warm shadows (amber), cool highlights (slight blue) |
| **Vignette** | עדין (-15% בפינות) |

#### מה צילום טוב נראה אצלנו

- אדם שוכב עם עיניים עצומות, תאורה חמה, הרבה רקע ריק
- ידיים של DJ על mixing board, shallow depth, ambient light
- חלל ריק (אולם מוזיאון, חדר מדיטציה) לפני שהקהל מגיע
- נוף צפון (גולן, ירדן, חרמון) בשעת golden hour, מעט ערפל
- פרט קטן: קערת סאונד, נר, מזרון שכיבה

#### מה צילום רע נראה אצלנו

- פלאש ישיר, עיניים אדומות, צבעים צורחים
- קבוצה גדולה מחייכת למצלמה
- Stock photo של "מדיטציה" (אישה בלבן על חוף)
- HDR מוגזם, ניגודיות גבוהה, saturation גבוה
- Selfie style, זווית תחתונה, wide angle מעוות

---

### 1.5 סגנון איור - Illustration Style (סיכום)

> **למידע מלא: `M-memory/illustrator-taste-profile.md`**
> זהו סיכום בלבד - לכל סוכן שאינו Illustrator.

#### 10 אסימוני סגנון (Style Tokens)

כל איור חייב לכלול לפחות 5 מתוך:

| # | Token | חשיבות |
|---|-------|--------|
| 1 | רקע נייר חם (לא לבן סטרילי) | קריטי |
| 2 | דיו שחור/אפור עם מכחול נראה | קריטי |
| 3 | לפחות 60-75% חלל ריק | קריטי |
| 4 | חותמת אדומה קטנה (Hanko) | גבוהה |
| 5 | פורמט אנכי (תחושת scroll) | גבוהה |
| 6 | הר/מים/ערפל כצורות מהותיות | קריטי |
| 7 | מקצב במבוק - חזרה אורגנית | בינונית |
| 8 | טקסטורות topography בכחול-אפור | בינונית |
| 9 | טיפוגרפיה זעירה (תווית מוזיאלית) | בינונית |
| 10 | Wabi-sabi - ריסון, טבעיות, חוסר-שלמות | גבוהה |

#### מה עובד

- שכבות עומק (3+ שכבות)
- ווריאציית גוון בתוך אותו צבע
- טקסטורת מכחול/נייר נראית
- אווירה אטמוספרית (ערפל/מיסט)
- תחושת "יד אנושית" - לא דיגיטלי חלק

#### מה נדחה

- שטיחות, flat design
- AI-generated look גנרי
- הפשטה טהורה ללא צורות מזוהות
- glossy, 3D, פלסטי, neon
- עומס פרטים, cluttered
- "Japan cliche" עם עודף קישוטים/זהב

---

## 2. תבניות פורמט - Format Templates

---

### 2.1 Instagram Post (1:1 / 4:5)

#### מפרט טכני

| פרמטר | ערך |
|-------|-----|
| **מימדים (1:1)** | 1080 x 1080 px |
| **מימדים (4:5)** | 1080 x 1350 px |
| **רזולוציה** | 72 dpi (מסך) |
| **פורמט קובץ** | PNG (שקיפות) או JPG (צילום) |
| **Safe zone** | 60px מכל צד (אזור שלא נחתך) |
| **פורמט מועדף** | 4:5 (יותר שטח, יותר niche space בפיד) |

#### רשת Layout

```
4:5 Layout (1080 x 1350):

+----------------------------------+
|          BREATHING ROOM          |  <- 120px top
|            (Paper bg)            |
|                                  |
|     +----------------------+     |
|     |                      |     |
|     |    FOCAL ELEMENT     |     |  <- 25-40% of height
|     |  (illustration /     |     |     centered or
|     |   photograph)        |     |     slightly above center
|     |                      |     |
|     +----------------------+     |
|                                  |
|          BREATHING ROOM          |  <- 60-75% total
|            (Paper bg)            |
|                                  |
|  [micro-caption]                 |  <- bottom margin, 12px
|                                  |
|  [HANKO]                         |  <- bottom-left, 5% of width
+----------------------------------+
     ^                        ^
     |-- 80px side margins ---|
```

#### כללי טקסט

| שכבה | גודל | פונט | צבע |
|------|------|------|-----|
| **כותרת (אם יש)** | 42-56px | Heebo 700 | Sumi `#283335` |
| **תת-כותרת** | 24-28px | Heebo 400 | Hai `#BDBAB2` |
| **גוף** | 18-20px | Heebo 300 | Sumi `#283335` |
| **Caption (EN)** | 10-11px uppercase | DM Mono 400 | Tetsu `#7B817D` |
| **תאריך** | 14-16px | DM Mono 400 | Beni `#AE2C2C` |

#### כללי צבע

- **רקע:** תמיד Washi (`#E0DDD3`) או Aged Cream (`#F2EAD3`). אף פעם לבן טהור.
- **טקסט ראשי:** Sumi (`#283335`).
- **אקסנט אדום:** תאריך בלבד, או חותמת Hanko קטנה.
- **אם יש צילום:** הצילום על רקע Washi עם 6-10% margins. לא edge-to-edge.

#### DO

- רקע Washi חם עם אלמנט מרכזי אחד
- חותמת Hanko קטנה בפינה (bottom-left)
- micro-caption באנגלית (uppercase, tiny)
- הרבה חלל ריק - הפוסט "נושם"
- טקסט בצד אחד (לא ממורכז - אסימטריה)

#### DON'T

- טקסט על תמונה (overlay)
- כותרות גדולות שתופסות חצי מהמסגרת
- רקע שחור או צבעוני חי
- frames, borders, drop shadows
- כמה תמונות באותו פוסט (collage)
- פילטרים של Instagram

---

### 2.2 Instagram Story (9:16)

#### מפרט טכני

| פרמטר | ערך |
|-------|-----|
| **מימדים** | 1080 x 1920 px |
| **Safe zone (top)** | 250px (UI של Instagram) |
| **Safe zone (bottom)** | 200px (swipe up / reply) |
| **Safe zone (sides)** | 60px |
| **Area for content** | 960 x 1470 px (center) |

#### Layout

```
+----------------------------------+
|  [INSTAGRAM UI - DO NOT USE]     |  <- 250px
|                                  |
|                                  |
|      MAIN CONTENT AREA           |
|                                  |
|      Option A: Full-bleed image  |
|      (photograph/illustration)   |
|      with text overlay on        |
|      dark area                   |
|                                  |
|      Option B: Washi background  |
|      with centered element       |
|      + text below                |
|                                  |
|                                  |
|  [SWIPE / REPLY - DO NOT USE]    |  <- 200px
+----------------------------------+
```

#### סוגי Stories

**Type A - הכרזה על אירוע:**
- רקע: צילום אטמוספרי (dark, ambient) עם overlay gradient
- טקסט: שם האירוע (Heebo 700, 48px, white) + תאריך (DM Mono, Beni)
- "Link in bio" בתחתית

**Type B - ציטוט / מחשבה:**
- רקע: Washi (`#E0DDD3`)
- ציטוט: Heebo 400, 28-32px, Sumi, ממורכז
- חותמת Hanko קטנה מתחת

**Type C - Behind the scenes:**
- צילום אורגני (לא staged)
- טקסט מינימלי - שם + location בלבד
- DM Mono, 14px, white עם text-shadow עדין

#### אנימציות מומלצות

- **Fade in:** אלמנטים מופיעים ב-fade (0.5-1s). לא slide-in מהירים.
- **Ken Burns:** תזוזה איטית על צילום (zoom-in 5% ב-5 שניות).
- **טקסט:** מילה-מילה fade, לא "typing effect".
- **אסור:** glitch effects, neon, stickers של Instagram, GIFs.

---

### 2.3 LinkedIn Post Image

#### מפרט טכני

| פרמטר | ערך |
|-------|-----|
| **מימדים (single image)** | 1200 x 627 px (1.91:1) |
| **מימדים (square)** | 1080 x 1080 px |
| **מימדים מועדף** | 1200 x 627 px |
| **פורמט** | PNG או JPG |
| **Safe zone** | 40px מכל צד |

#### Layout

```
1200 x 627 Layout:

+--------------------------------------------------+
|                                                    |
|  LEFT 60%              |  RIGHT 40%               |
|                        |                           |
|  [Focal visual:        |  [Text block:             |
|   illustration,        |   headline,               |
|   landscape photo,     |   sub-text,               |
|   or abstract          |   date if relevant]       |
|   Sumi-e element]      |                           |
|                        |  [Hanko stamp             |
|                        |   bottom-right]           |
|                                                    |
+--------------------------------------------------+
```

#### מאזן מקצועי-אמנותי

LinkedIn דורש מאזן שונה מ-Instagram. הקהל מקצועי יותר.

| מרכיב | גישה |
|-------|------|
| **צבע רקע** | Washi או Aged Cream Light (`#FAF6F0`). לא כהה. |
| **טיפוגרפיה** | Heebo 600 לכותרות (לא 800 - פחות "צועק") |
| **תוכן** | כותרת + תת-כותרת + מקור/מחבר. לא יותר מ-3 שורות. |
| **ויזואל** | עדיף צילום מקצועי על פני Sumi-e (אם הפוסט עסקי) |
| **Hanko** | קטן, פינה, discretion גבוהה. או ללא. |

#### DO

- כותרת ברורה שנקראת ב-0.5 שנייה (feed scanning)
- מספיק ניגודיות (Sumi על Washi = טוב)
- שם המותג כ-caption קטן (DM Mono, 10px)
- Layout נקי עם hierarchy ברור

#### DON'T

- Sumi-e illustration שתופסת את כל הפריים (נראה כמו art, לא post)
- טקסט קטן מ-18px (לא קריא ב-feed)
- עיצוב שנראה כמו "יפן" ולא כמו "מקצועי"
- Beni על שטח גדול (מדי דרמטי ל-LinkedIn)

---

### 2.4 פלייר אירוע - Event Flyer (A4 / Digital)

#### מפרט טכני

| פרמטר | ערך A4 Print | ערך Digital |
|-------|-------------|-------------|
| **מימדים** | 210 x 297 mm | 1080 x 1527 px (= A4 ratio) |
| **רזולוציה** | 300 dpi | 72 dpi |
| **Bleed (print)** | 3mm מכל צד | N/A |
| **Color mode** | CMYK | RGB |
| **פורמט** | PDF (print) | PNG/JPG (digital) |

#### היררכיית מידע

```
Priority Order (top = most important):

1. EVENT NAME          <- Heebo 800, --text-display (56px+)
2. DATE + TIME         <- DM Mono, Beni red, 28px
3. ARTIST NAMES        <- Heebo 600, 24px, stacked list
4. VENUE NAME          <- Heebo 400, 20px
5. PRICE / TICKETS     <- DM Mono, 16px
6. ADDITIONAL DETAILS  <- Heebo 300, 14px
7. LOGO / HANKO        <- bottom, small
```

#### Layout Zones

```
A4 Layout:

+----------------------------------+
|                                  |
|   ZONE 1 - ATMOSPHERE            |  <- top 35%
|   (Sumi-e illustration or        |     illustration/photo
|    event photograph.              |     with generous
|    Bleeds to edges.)             |     whitespace
|                                  |
+----------------------------------+
|                                  |
|   ZONE 2 - HEADLINE             |  <- 15%
|   Event name in large type       |     Heebo 800
|   Date in Beni red              |     DM Mono
|                                  |
+----------------------------------+
|                                  |
|   ZONE 3 - DETAILS              |  <- 35%
|   Artist names (stacked)         |     Left-aligned
|   Venue                          |     Generous line-
|   Program outline                |     spacing (1.8)
|   Price / Ticket info            |
|                                  |
+----------------------------------+
|                                  |
|   ZONE 4 - FOOTER               |  <- 15%
|   Logo/Hanko + website +         |     Quiet, minimal
|   social handles                 |
|                                  |
+----------------------------------+
```

#### Sumi-e Aesthetic in Print

| עקרון | יישום |
|-------|-------|
| **חלל ריק** | Zone 1 לא חייבת להיות מלאה. אם יש איור - הוא תופס 25-40% מהzone. השאר = נייר. |
| **חותמת** | Hanko stamp בפינה. לא לוגו מודרני, אלא חותמת אדומה כמו אותנטי. |
| **טקסטורת נייר** | רקע: Washi texture (grain visible). לא חלק. |
| **אסימטריה** | שמות אמנים aligned left (RTL: right), לא centered. |
| **מינימליזם** | הפלייר שלנו נראה כמו פוסטר גלריה, לא כמו מודעה. |

---

### 2.5 מצגת שותפים - Presentation Deck

#### מפרט טכני

| פרמטר | ערך |
|-------|-----|
| **יחס מסך** | 16:9 |
| **מימדים** | 1920 x 1080 px |
| **פורמט** | Canva Presentation / PPTX |
| **כמות שקפים** | 10-15 מקסימום |

#### Layouts לשקפים

**Slide Type A - Title:**
```
+--------------------------------------------------+
|                                                    |
|                                                    |
|        SOL THERAPY                                 |  <- Heebo 800, 72px
|        [Subtitle in smaller text]                  |  <- Heebo 300, 24px
|                                                    |
|                         [Hanko stamp, bottom-right] |
|                                                    |
+--------------------------------------------------+
Background: Washi texture
```

**Slide Type B - Content (text + image):**
```
+--------------------------------------------------+
|                                                    |
|  LEFT 55%              |  RIGHT 45%               |
|                        |                           |
|  [Headline]            |  [Image:                  |
|  Heebo 700, 36px       |   photograph or           |
|                        |   Sumi-e illustration,    |
|  [Body text]           |   rounded corners 8px,    |
|  Heebo 300, 18px       |   or full-height bleed]   |
|  3-5 bullet points     |                           |
|                        |                           |
+--------------------------------------------------+
Background: Aged Cream Light (#FAF6F0)
```

**Slide Type C - Full Quote:**
```
+--------------------------------------------------+
|                                                    |
|                                                    |
|        "ציטוט ארוך שנושם על המסך                    |
|         עם הרבה חלל ריק מסביב"                      |
|                                                    |
|                        - מקור, שנה                  |
|                                                    |
+--------------------------------------------------+
Background: Deep Indigo (#264348)
Text: Washi (#E0DDD3), Heebo 400, 28px
```

**Slide Type D - Data / Numbers:**
```
+--------------------------------------------------+
|                                                    |
|  [Section title]                                   |
|                                                    |
|  +----------+  +----------+  +----------+          |
|  |   15+    |  |   200+   |  |  25,000  |          |
|  |  סשנים   |  |  אמנים   |  | משתתפים  |          |
|  +----------+  +----------+  +----------+          |
|                                                    |
|  Numbers: Heebo 800, 48px, Beni red               |
|  Labels: Heebo 300, 16px, Sumi                    |
|                                                    |
+--------------------------------------------------+
Background: Washi
```

**Slide Type E - Image Break:**
```
+--------------------------------------------------+
|                                                    |
|    [Full-bleed Sumi-e illustration                 |
|     or atmospheric event photograph                |
|     with 60% opacity dark overlay                  |
|     and one word or short phrase                   |
|     in Heebo 800, 64px, white]                     |
|                                                    |
+--------------------------------------------------+
```

#### איזון זן-עסקי

| עיקרון | יישום |
|--------|-------|
| **פחות שקפים** | 10-15. כל שקף = רעיון אחד. אין עומס. |
| **יותר תמונות** | שקף image break כל 3-4 שקפי תוכן. |
| **מספרים גדולים** | נתונים = Heebo 800 ענק. הטקסט קטן מתחת. |
| **רקע עקבי** | 80% שקפים = Aged Cream Light. 20% = Deep Indigo (ציטוטים, images). |
| **אין אנימציות** | פשוט fade. אין fly-in, spin, bounce. |
| **Hanko** | בשקף כותרת + שקף סיום בלבד. |

---

### 2.6 Email / Newsletter Header

#### מפרט טכני

| פרמטר | ערך |
|-------|-----|
| **רוחב** | 600px (email standard) |
| **גובה** | 200-300px |
| **Max file size** | 200KB (deliverability) |
| **פורמט** | JPG (smaller) or PNG |

#### Layout

```
600 x 250 Layout:

+--------------------------------------------------+
|                                                    |
|   [SOL THERAPY logotype]              [date]       |
|   Heebo 700, 28px                    DM Mono, 11px |
|                                                    |
|   [Editorial headline or                           |
|    issue theme]                                    |
|   Heebo 300, 18px                                  |
|                                                    |
|   [Subtle Sumi-e element: ink wash band,           |
|    mountain silhouette, or simple brushstroke       |
|    at 15-20% opacity as decorative accent]         |
|                                                    |
+--------------------------------------------------+
Background: Aged Cream Light (#FAF6F0) or Washi (#E0DDD3)
```

#### כללים

| כלל | פירוט |
|-----|-------|
| **טון** | Editorial, לא artistic. כמו header של מגזין, לא פוסטר. |
| **איור** | מינימלי. רק accent. קו מכחול, רצועת ink wash, silhouette הר. 15-20% opacity. |
| **צבע** | Washi + Sumi בלבד. אין Beni בheader (שומרים אותו לCTA בגוף). |
| **לוגו** | טקסט "סול תרפי" ב-Heebo 700 בלבד. לא לוגו גרפי. |
| **קו הפרדה** | קו דק (`#CECCC7`, 1px) מתחת לheader. או ink wash band. |

---

## 3. שימוש בלוגו - Logo Usage

---

### מצב נוכחי

נכון לתאריך כתיבת מסמך זה, אין לוגו גרפי רשמי. ה"לוגו" הוא:

**Logotype:** "סול תרפי" בפונט Heebo 700-800
**English:** "Sol Therapy" בפונט Inter 600-700

#### כללי שימוש בlogotype

| כלל | ערך |
|-----|-----|
| **גודל מינימלי** | 18px (digital), 8mm (print) |
| **Clear space** | גובה האות "ס" מכל צד (מינימום) |
| **צבע על רקע בהיר** | Sumi (`#283335`) |
| **צבע על רקע כהה** | Washi (`#E0DDD3`) |
| **אסור** | לא לעוות, לא לסובב, לא לשנות צבע לבני/אדום |

#### המלצה: חותמת Hanko כלוגו

במקום לוגו מודרני, ההמלצה היא לפתח **חותמת Hanko** - חותמת אדומה מרובעת בסגנון יפני עם הטקסט "sol" או "סול" בתוכה. זה מתיישר עם:

- הזהות הויזואלית הקיימת (Neo-Japonism)
- ה-Style Token `vermilion_seal_accent`
- השימוש הקיים ב-Hanko stamps באיורים

**מפרט Hanko המלצה:**
- צורה: ריבוע עם פינות מעוגלות קלות (2px radius)
- צבע: Beni (`#AE2C2C`)
- טקסט בפנים: "sol" ב-Inter 700 uppercase, או "סול" ב-Heebo 800
- גודל: 24-48px (digital), 8-15mm (print)
- מיקום: bottom-left או bottom-center

---

## 4. DO / DON'T - דף עזר מהיר

---

### DO - מה לעשות

| # | כלל | למה |
|---|-----|-----|
| 1 | **רקע חם** - Washi/Cream תמיד. לבן טהור = אף פעם. | חום = אותנטי, נייר אמיתי |
| 2 | **חלל ריק = עיצוב** - 50-70% מכל קומפוזיציה = ריק. | Ma - הריק הוא האלמנט הכי חשוב |
| 3 | **אלמנט מרכזי אחד** - כל פריים = דבר אחד שמושך עין. | פוקוס. לא תחרות בין אלמנטים. |
| 4 | **טקסטורה נראית** - grain של נייר, מכחול, חוסר-שלמות. | Wabi-sabi. לא חלק דיגיטלי. |
| 5 | **Beni (אדום) = חותמת בלבד** - קטן, בפינה, discretion. | חוק הזהב: אדום מופיע, השאר שותק. |
| 6 | **טיפוגרפיה נקייה** - Sans-serif, weights ברורים, hierarchy. | אנחנו לא decorative - אנחנו editorial. |
| 7 | **אסימטריה** - טקסט לא ממורכז, אלמנטים off-center. | מוזיאון, לא PowerPoint. |
| 8 | **צילום חם ושקט** - desaturated, shallow depth, ambient. | מרחב מדיטטיבי, לא אירוע מסחרי. |
| 9 | **Hebrew + English** - כותרות בעברית, labels באנגלית. | דו-לשוני אלגנטי, לא מבולגן. |
| 10 | **עקביות** - אותם צבעים, אותם פונטים, אותו Hanko. בכל מקום. | מותג = זיהוי מיידי. |

### DON'T - מה לא לעשות

| # | כלל | למה |
|---|-----|-----|
| 1 | **אף פעם אימוג'י** - אפס. זה deal breaker. | Voice DNA - חוק עליון. |
| 2 | **אין em dash (-)** - מקף רגיל (-) בלבד. | Voice DNA. |
| 3 | **אין רקע שחור טהור** - #000000 = אסור. | Deep Indigo (#264348) או Sumi (#283335) |
| 4 | **אין gradient צבעוני** - לא כחול-לסגול, לא ורוד-לכתום. | Gradients שלנו = ink wash (אפור-לשקוף) |
| 5 | **אין drop shadows** - לא על טקסט, לא על תמונות, לא על כרטיסים. | Flat + texture, לא faux-3D. |
| 6 | **אין borders/frames** - תמונות ללא מסגרת. טקסט ללא boxes. | הריק מפריד, לא קווים. |
| 7 | **אין stock photography** - צילום אמיתי או איור מותאם. | Stock = הפך מאותנטי. |
| 8 | **אין פונטים דקורטיביים** - לא script, לא retro, לא handwriting. | Sans-serif editorial בלבד. |
| 9 | **אין overlays כבדים** - טקסט על תמונה רק עם gradient עדין. | לא banner ads. |
| 10 | **אין יותר מ-3 צבעים** - Paper + Sumi + 1 accent. מקסימום. | פשטות = כוח. |
| 11 | **אין אנימציות מוגזמות** - לא bounce, spin, shake, glitch. | שקט, fade, ease-out בלבד. |
| 12 | **אין "wellness cliches"** - לא lotus, לא mandala, לא chakras, לא rainbow. | אנחנו Neo-Japonism, לא New Age. |

---

## 5. Canva Templates & Integration

---

### 5.1 סוגי עיצוב מומלצים

| פורמט | Canva Design Type | מתי |
|--------|-------------------|-----|
| Instagram Post 1:1 | `instagram_post` | פוסטים לפיד |
| Instagram Post 4:5 | Custom 1080x1350 | פוסטים שרוצים יותר real estate |
| Instagram Story | `your_story` | stories, quick updates |
| LinkedIn Image | Custom 1200x627 | פוסטים מקצועיים |
| Event Flyer A4 | `flyer` | פלייר דיגיטלי |
| Presentation | `presentation` | deck לשותפים |
| Newsletter Header | Custom 600x250 | email headers |
| Facebook Cover | `facebook_cover` | עטיפת Facebook |
| Facebook Post | `facebook_post` | פוסטים לFacebook |
| YouTube Thumbnail | `youtube_thumbnail` | אם יש תוכן וידאו |
| Business Card | `business_card` | כרטיס ביקור |
| Poster | `poster` | פוסטר גדול (אירועים) |

### 5.2 Brand Kit

| פרמטר | ערך |
|-------|-----|
| **Brand Kit ID** | `kAFfB4xlgWc` |
| **שימוש** | להעביר כ-`brand_kit_id` ב-`generate-design` tool |

### 5.3 מוסכמת שמות - Naming Convention

```
Format: sol-[type]-[subject]-[version]

Examples:
- sol-ig-post-pastoral-retreat-v1
- sol-ig-story-event-announcement-v1
- sol-linkedin-retreat-results-v1
- sol-flyer-pastoral-april-v2
- sol-deck-partners-2026-v1
- sol-newsletter-header-march-v1
```

### 5.4 Design Generation Tips (from experience)

| לקח | פירוט |
|-----|-------|
| **Queries קצרים** | "Zen meditation event flyer, warm paper, minimal, Japanese ink style" עובד טוב יותר מ-brief של 200 מילים. |
| **Batch הראשון** | הבatch הראשון של designs בדרך כלל טוב יותר מהשני (over-specification הורסת). |
| **Brand Kit** | תמיד לכלול `brand_kit_id: "kAFfB4xlgWc"` - זה מייצר עקביות. |
| **Hebrew rendering** | RTL/Hebrew לפעמים מתרנדר לא נכון ב-Canva. לבדוק בpreview. |
| **Export** | תמיד `get-export-formats` לפני `export-design`. |

---

## 6. נספחים - Appendices

---

### 6.1 Figma File Reference

| קובץ | Key | תיאור |
|------|-----|-------|
| SOL_THERAPY | `7VDJA54QlyQgvVjMYVygs9` | קובץ העיצוב הראשי |

**שימוש:** `mcp__figma__get_figma_data` לקריאת specs, `mcp__figma__download_figma_images` לייצוא assets.

### 6.2 Replicate Model Reference (לאיורים)

| מודל | שימוש |
|------|-------|
| `google/nano-banana-pro` | ברירת מחדל - כל ייצור איורים |
| `black-forest-labs/flux-1.1-pro-ultra` | Fallback 1 |
| `recraft-ai/recraft-v3` | Style control מתקדם |
| `flux-redux-dev` | IP-Adapter - ייצור בסגנון רפרנס |

**Prompt Template (Master):**
```
Style: warm paper texture, monochrome ink wash, zen negative space,
minimal editorial layout, red seal stamp accent.
Palette: warm off-white paper, charcoal ink, optional accent red seal.
Composition: 70% negative space, one focal subject, vertical scroll feel,
small seal in corner.
Avoid: glossy gradients, neon, photorealism, clutter, decorative fonts.
Subject: <SUBJECT>.
```

### 6.3 צ'ק-ליסט איכות ויזואלית

לפני שמציגים כל output ויזואלי לירון:

```
[ ] רקע חם (לא לבן, לא שחור טהור)?
[ ] חלל ריק 50%+?
[ ] מקסימום 3 צבעים?
[ ] אם יש Beni - הוא קטן ובפינה?
[ ] טקסטורה נראית (grain, brush, imperfection)?
[ ] אין אימוג'י?
[ ] אין em dash?
[ ] פונטים נכונים (Heebo/Inter/DM Mono)?
[ ] טקסט עברי ב-RTL?
[ ] captions באנגלית uppercase קטן?
```

---

*Last updated: 2026-02-14*
*Author: Illustrator Agent*
*References: illustrator-taste-profile.md, sol-therapy-knowledge-base.md, voice-dna.md, project-brief.md, connected-tools.md*
