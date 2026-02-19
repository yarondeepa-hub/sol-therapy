# GSAP - GreenSock Animation Platform - דוח מחקר מקיף

> תאריך מחקר: 2026-02-12
> גרסה נוכחית: **3.14.2**
> רישיון: חינמי לחלוטין (כולל כל ה-plugins) - בזכות רכישת Webflow

---

## 1. מה זה GSAP?

GSAP (GreenSock Animation Platform) היא ספריית JavaScript לאנימציה שנחשבת לתקן התעשייה לאנימציות web. היא framework-agnostic - עובדת עם כל framework או בלי framework בכלל.

### מה היא עושה

- אנימציה של CSS properties (transform, opacity, colors, ועוד)
- אנימציה של SVG, Canvas, WebGL
- אנימציות מבוססות scroll (עם ScrollTrigger)
- שליטה מלאה על timelines - sequencing, staggering, looping
- אנימציות מורכבות עם שורה אחת של קוד

### למה היא תקן התעשייה

- פועלת על **יותר מ-12 מיליון אתרים**
- ביצועים עדיפים על CSS animations ברוב המקרים
- API פשוט ואינטואיטיבי
- עובדת על כל הדפדפנים
- פותרת בעיות אמיתיות שב-CSS animations פשוט אי אפשר - sequencing מורכב, scroll-based animations, morphing
- מתוחזקת ע"י הצוות המקורי (עכשיו חלק מ-Webflow)

### ההיסטוריה הקצרה

GSAP פותחה ע"י GreenSock ב-2008. ב-2024 נרכשה ע"י Webflow. השינוי הגדול: כל ה-plugins שהיו בתשלום (Club GreenSock) - עכשיו **חינמיים לחלוטין**, כולל שימוש מסחרי.

---

## 2. התקנה - Installation Methods

### א. CDN - Script Tags (ללא build system)

**הגרסה האחרונה: 3.14.2**

**jsDelivr (מומלץ):**

```html
<!-- GSAP Core -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>

<!-- ScrollTrigger - הכי חשוב לאתר scroll-based -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>

<!-- ScrollSmoother - smooth scrolling -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollSmoother.min.js"></script>

<!-- SplitText - אנימציות טקסט -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/SplitText.min.js"></script>

<!-- DrawSVGPlugin - אנימציות stroke ב-SVG -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/DrawSVGPlugin.min.js"></script>

<!-- MorphSVGPlugin - morphing של SVG shapes -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/MorphSVGPlugin.min.js"></script>
```

**cdnjs (גרסה 3.13.0 - מפגרת קצת):**

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
```

> **המלצה:** להשתמש ב-jsDelivr - תמיד הגרסה הכי עדכנית.

### ב. npm

```bash
npm install gsap
```

### ג. ESM Import (עם build system)

```javascript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollSmoother } from "gsap/ScrollSmoother";
import { SplitText } from "gsap/SplitText";
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";

// חובה לרשום plugins
gsap.registerPlugin(ScrollTrigger, ScrollSmoother, SplitText);
```

### ד. UMD Import (build systems ישנים יותר)

```javascript
import { gsap } from "gsap/dist/gsap";
import { ScrollTrigger } from "gsap/dist/ScrollTrigger";
```

---

## 3. Core API

### gsap.to() - אנימציה לכיוון ערך

מגדיר את **היעד** - מאיפה שהאלמנט נמצא עכשיו, לאן שאתה רוצה.

```javascript
// הזז קופסה 300px ימינה עם סיבוב
gsap.to(".box", {
  x: 300,
  rotation: 360,
  duration: 1,
  ease: "power2.out"
});

// Fade in + עלייה
gsap.to(".hero-text", {
  opacity: 1,
  y: 0,
  duration: 0.8,
  delay: 0.3
});
```

**vars - הפרמטרים העיקריים:**

| Property | תיאור | ברירת מחדל |
|----------|--------|-------------|
| `duration` | אורך האנימציה בשניות | 0.5 |
| `delay` | השהיה לפני התחלה | 0 |
| `ease` | סוג ה-easing | "power1.out" |
| `repeat` | חזרות (-1 = אינסוף) | 0 |
| `yoyo` | חזרה הפוכה | false |
| `stagger` | עיכוב בין אלמנטים מרובים | 0 |
| `onComplete` | callback בסיום | null |
| `onStart` | callback בהתחלה | null |
| `onUpdate` | callback בכל frame | null |
| `overwrite` | האם לבטל tweens מתנגשים | false |

### gsap.from() - אנימציה מ-ערך

מגדיר את **נקודת ההתחלה** - האלמנט מונפש מהערכים שתגדיר אל המצב הנוכחי שלו ב-CSS.

```javascript
// אלמנט "נכנס" מלמטה עם fade
gsap.from(".card", {
  opacity: 0,
  y: 100,
  duration: 1,
  ease: "power3.out"
});

// כותרת "נגללת" פנימה מחוץ למסך
gsap.from(".title", {
  x: -200,
  opacity: 0,
  duration: 0.6
});
```

> **ההבדל הקריטי:** `to()` = לאן ללכת. `from()` = מאיפה לבוא. `from()` אידיאלי לאנימציות reveal - האלמנט "מגיע" למצב שהגדרת ב-CSS.

### gsap.fromTo() - שליטה מלאה

מגדיר גם את **ההתחלה** וגם את **הסוף**.

```javascript
gsap.fromTo(".box",
  // From - נקודת התחלה
  { opacity: 0, scale: 0.5, y: 50 },
  // To - נקודת סיום
  { opacity: 1, scale: 1, y: 0, duration: 1, ease: "back.out(1.7)" }
);
```

> שימושי כשאתה רוצה שליטה מלאה על שני הקצוות - לא תלוי במצב הנוכחי של ה-CSS.

### gsap.timeline() - שרשור אנימציות

Timeline הוא container שמאגד אנימציות ברצף מדויק. במקום לחשב delays ידנית - פשוט שורשרים.

```javascript
const tl = gsap.timeline();

tl.from(".hero-title", { opacity: 0, y: 30, duration: 0.6 })
  .from(".hero-subtitle", { opacity: 0, y: 20, duration: 0.4 }, "-=0.2")  // מתחיל 0.2 שניות לפני סיום הקודם
  .from(".hero-cta", { opacity: 0, scale: 0.8, duration: 0.3 })
  .from(".hero-image", { opacity: 0, x: 50, duration: 0.5 }, "<");  // מתחיל ביחד עם הקודם
```

**Position Parameter - שליטה בתזמון:**

| סינטקס | משמעות |
|--------|---------|
| `"+=1"` | שניה אחרי סוף ה-timeline |
| `"-=0.5"` | חצי שניה לפני סוף ה-timeline |
| `"<"` | התחלה של האנימציה הקודמת |
| `">"` | סוף האנימציה הקודמת |
| `"<0.3"` | 0.3 שניות אחרי התחלת הקודמת |
| `2` | בשניה ה-2 של ה-timeline (מוחלט) |

**Timeline עם defaults:**

```javascript
const tl = gsap.timeline({
  defaults: { duration: 0.5, ease: "power2.out" }
});

tl.from(".el-1", { opacity: 0, y: 30 })
  .from(".el-2", { opacity: 0, y: 30 }, "-=0.2")
  .from(".el-3", { opacity: 0, y: 30 }, "-=0.2");
```

**Timeline controls:**

```javascript
const tl = gsap.timeline({ paused: true });
// ... add animations ...

tl.play();       // הפעל
tl.pause();      // עצור
tl.reverse();    // הפוך
tl.restart();    // מההתחלה
tl.progress(0.5); // קפוץ ל-50%
tl.timeScale(2); // מהירות כפולה
```

---

## 4. ScrollTrigger Plugin - הכי חשוב לאתר scroll-based

ScrollTrigger הוא ה-plugin המרכזי של GSAP לאנימציות מבוססות scroll. הוא מאפשר:

- להפעיל אנימציות כשאלמנט נכנס ל-viewport
- לקשר אנימציה ישירות ל-scrollbar (scrub)
- לנעוץ (pin) אלמנטים במקום בזמן scroll
- snap לנקודות מוגדרות
- parallax effects

### התקנה

```html
<!-- CDN -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>

<script>
  gsap.registerPlugin(ScrollTrigger);
</script>
```

### שימוש בסיסי - Trigger on Scroll

```javascript
// אנימציה שמופעלת כשהאלמנט נכנס ל-viewport
gsap.from(".section-title", {
  scrollTrigger: ".section-title",  // trigger פשוט - selector string
  opacity: 0,
  y: 50,
  duration: 0.8
});
```

### שימוש מתקדם - Configuration Object

```javascript
gsap.to(".parallax-image", {
  y: -100,
  ease: "none",
  scrollTrigger: {
    trigger: ".parallax-section",   // האלמנט שגורם להפעלה
    start: "top bottom",            // [trigger position] [viewport position]
    end: "bottom top",              // מתי האנימציה מסתיימת
    scrub: true,                    // קשירה ישירה ל-scroll
    markers: true                   // debug - נקודות ויזואליות (להוריד ב-production!)
  }
});
```

### Key Properties

| Property | תיאור | דוגמה |
|----------|--------|-------|
| `trigger` | האלמנט שמפעיל | `".section"` |
| `start` | מתי מתחיל | `"top center"`, `"top 80%"` |
| `end` | מתי נגמר | `"bottom top"`, `"+=500"` |
| `scrub` | קשירה ל-scroll | `true`, `1` (smoothing) |
| `pin` | נעיצת אלמנט | `true`, `".element"` |
| `snap` | snap לנקודות | `0.25`, `[0, 0.5, 1]` |
| `markers` | debug markers | `true` |
| `toggleActions` | פעולות בכל מצב | `"play pause resume reset"` |
| `toggleClass` | toggle class | `"active"` |
| `endTrigger` | אלמנט סוף שונה | `".other-element"` |

### toggleActions - 4 מצבים

```javascript
scrollTrigger: {
  toggleActions: "play pause resume reset"
  //             onEnter onLeave onEnterBack onLeaveBack
}
```

ערכים אפשריים: `play`, `pause`, `resume`, `reverse`, `restart`, `reset`, `complete`, `none`

### Scrub - אנימציה צמודה ל-scroll

```javascript
// scrub: true = 1:1 עם ה-scroll
// scrub: 1 = smoothing של שניה אחת
// scrub: 0.5 = smoothing של חצי שניה

gsap.to(".progress-bar", {
  width: "100%",
  ease: "none",
  scrollTrigger: {
    trigger: ".content",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.5
  }
});
```

### Pin - נעיצת אלמנטים

```javascript
gsap.to(".sticky-section", {
  scrollTrigger: {
    trigger: ".sticky-section",
    start: "top top",
    end: "+=1000",      // נעוץ לאורך 1000px של scroll
    pin: true,
    scrub: true
  }
});
```

### Batch - אנימציה של קבוצות

```javascript
ScrollTrigger.batch(".card", {
  onEnter: (elements) => {
    gsap.from(elements, {
      opacity: 0,
      y: 50,
      stagger: 0.15,
      duration: 0.6
    });
  }
});
```

### Callbacks

```javascript
ScrollTrigger.create({
  trigger: ".section",
  start: "top center",
  onEnter: () => console.log("entered!"),
  onLeave: () => console.log("left!"),
  onEnterBack: () => console.log("entered back!"),
  onLeaveBack: () => console.log("left back!")
});
```

---

## 5. Plugins נוספים

### ScrollSmoother

מוסיף smooth scrolling לעמוד שלם. לא "מזייף" scrollbar - משתמש ב-native scroll ומוסיף transforms חלקים.

```javascript
gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

// HTML structure חובה:
// <div id="smooth-wrapper">
//   <div id="smooth-content">
//     ... כל התוכן ...
//   </div>
// </div>

ScrollSmoother.create({
  smooth: 1,             // כמה חלק (שניות)
  effects: true,         // מאפשר data-speed ו-data-lag
  smoothTouch: 0.1       // smooth גם על mobile
});
```

שימוש עם data attributes:

```html
<img data-speed="0.5" src="..." />  <!-- scroll במהירות חצי = parallax -->
<div data-speed="1.5">Fast</div>     <!-- scroll מהיר יותר -->
<div data-lag="0.2">Delayed</div>    <!-- עיכוב קל -->
```

### SplitText

מפרק טקסט לתווים, מילים, או שורות - ומאפשר אנימציה של כל חלק בנפרד.

```javascript
gsap.registerPlugin(SplitText);

// פירוק הטקסט
const split = new SplitText(".hero-title", {
  type: "chars, words, lines"
});

// אנימציה של כל תו בנפרד
gsap.from(split.chars, {
  opacity: 0,
  y: 20,
  stagger: 0.03,
  duration: 0.5,
  ease: "power2.out"
});
```

### DrawSVGPlugin

מאפשר אנימציה של "ציור" קווי SVG - stroke שמתגלה בהדרגה.

```javascript
gsap.registerPlugin(DrawSVGPlugin);

// ציור SVG path מ-0% ל-100%
gsap.from(".svg-path", {
  drawSVG: "0%",
  duration: 2,
  ease: "power2.inOut"
});

// ציור חלקי
gsap.fromTo(".line",
  { drawSVG: "0% 0%" },
  { drawSVG: "0% 100%", duration: 1.5 }
);
```

### MorphSVGPlugin

morphing של צורת SVG אחת לאחרת - גם אם מספר הנקודות שונה.

```javascript
gsap.registerPlugin(MorphSVGPlugin);

// morph צורה אחת לאחרת
gsap.to("#diamond", {
  morphSVG: "#lightning-bolt",
  duration: 1.5,
  ease: "power2.inOut"
});
```

---

## 6. חינמי vs. בתשלום

### המצב הנוכחי (2025-2026)

**הכל חינמי.** בזכות רכישת Webflow, כל GSAP - כולל כל ה-plugins - חינמי לגמרי, כולל שימוש מסחרי.

### מה היה לפני

| tier | מחיר שנתי | מה כלל |
|------|-----------|---------|
| Free | $0 | GSAP Core, ScrollTrigger, Draggable |
| Plus | $99 | + SplitText, DrawSVG |
| Premium | $149 | + MorphSVG, ScrollSmoother, Inertia |
| Business | $199 | + Business license |

### מה קורה עכשיו

**הכל חינמי:**
- GSAP Core
- ScrollTrigger, ScrollSmoother, ScrollTo
- SplitText, ScrambleText
- DrawSVG, MorphSVG
- MotionPath
- Flip, Draggable, Inertia, Observer
- Physics2D, PhysicsProps
- GSDevTools
- כל ה-utilities

> הרישיון הוא "no charge" license של GreenSock. מותר לשימוש מסחרי. הפרטים המלאים: gsap.com/standard-license

---

## 7. ביצועים - Performance

### GSAP vs. CSS Animations

| קריטריון | GSAP | CSS Animations |
|----------|------|----------------|
| **מהירות** | מהיר מאוד - לפעמים 5x יותר מ-CSS | מהיר ל-transform/opacity |
| **Main thread** | רץ על ה-main thread | יכול לרוץ על compositor thread |
| **Jank resistance** | פגיע לblocking של main thread | חסין יותר ל-jank |
| **Sequencing** | מובנה, פשוט | מורכב מאוד, דורש delays ידניים |
| **Scroll-based** | מובנה (ScrollTrigger) | מוגבל מאוד |
| **Control** | play/pause/reverse/seek | מוגבל |
| **Easing** | עשרות סוגים מובנים | cubic-bezier בלבד |
| **Browser support** | אחיד לגמרי | הבדלים בין דפדפנים |

### מתי להשתמש ב-CSS

- Hover effects פשוטים
- Transitions בסיסיות (opacity, transform)
- אנימציות שלא דורשות שליטה דינמית
- כשאין צורך ב-sequencing

### מתי להשתמש ב-GSAP

- אנימציות scroll-based
- Sequencing מורכב (timeline)
- אנימציות שדורשות שליטה (play/pause/reverse)
- Staggering של אלמנטים מרובים
- SVG animations (morph, draw)
- טקסט אנימציה (split text)
- כל מה שדורש timing מדויק

### טיפ ביצועים

העדף תמיד אנימציה של `transform` ו-`opacity` - הם GPU-accelerated. הימנע מאנימציה של `box-shadow`, `filter: blur()`, `width/height` - הם יקרים.

```javascript
// טוב - GPU accelerated
gsap.to(".el", { x: 100, opacity: 0.5, scale: 1.2 });

// רע - forces layout/paint
gsap.to(".el", { width: "200px", boxShadow: "0 10px 20px rgba(0,0,0,0.3)" });
```

---

## 8. Best Practices - דפוסים נפוצים

### Hero Section Reveal

```javascript
// Hero entrance animation
const heroTl = gsap.timeline({
  defaults: { duration: 0.8, ease: "power3.out" }
});

heroTl
  .from(".hero-bg", { scale: 1.1, opacity: 0, duration: 1.2 })
  .from(".hero-title", { opacity: 0, y: 40 }, "-=0.4")
  .from(".hero-subtitle", { opacity: 0, y: 30 }, "-=0.5")
  .from(".hero-cta", { opacity: 0, y: 20, scale: 0.9 }, "-=0.3");
```

### Scroll Reveal - אלמנטים שנחשפים בגלילה

```javascript
// Reveal on scroll - pattern חוזר
gsap.utils.toArray(".reveal").forEach(el => {
  gsap.from(el, {
    opacity: 0,
    y: 60,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
      trigger: el,
      start: "top 85%",
      toggleActions: "play none none none"
    }
  });
});
```

### Text Animation עם SplitText

```javascript
gsap.utils.toArray(".animate-text").forEach(el => {
  const split = new SplitText(el, { type: "words, chars" });

  gsap.from(split.chars, {
    opacity: 0,
    y: 20,
    stagger: 0.02,
    duration: 0.4,
    ease: "power2.out",
    scrollTrigger: {
      trigger: el,
      start: "top 80%"
    }
  });
});
```

### Section Pinning

```javascript
// Pin section while content animates
const pinTl = gsap.timeline({
  scrollTrigger: {
    trigger: ".pin-section",
    start: "top top",
    end: "+=2000",
    pin: true,
    scrub: 1
  }
});

pinTl
  .from(".step-1", { opacity: 0, y: 50 })
  .from(".step-2", { opacity: 0, y: 50 })
  .from(".step-3", { opacity: 0, y: 50 });
```

### Parallax Effect

```javascript
gsap.to(".parallax-bg", {
  yPercent: -30,
  ease: "none",
  scrollTrigger: {
    trigger: ".parallax-section",
    start: "top bottom",
    end: "bottom top",
    scrub: true
  }
});
```

### Horizontal Scroll Section

```javascript
const sections = gsap.utils.toArray(".horizontal-panel");

gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: "none",
  scrollTrigger: {
    trigger: ".horizontal-container",
    start: "top top",
    end: () => "+=" + document.querySelector(".horizontal-container").scrollWidth,
    pin: true,
    scrub: 1,
    snap: 1 / (sections.length - 1)
  }
});
```

### Progress Bar

```javascript
gsap.to(".progress-bar", {
  scaleX: 1,
  transformOrigin: "left center",
  ease: "none",
  scrollTrigger: {
    trigger: "body",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.3
  }
});
```

---

## 9. אינטגרציה עם אתר static HTML

### Setup מלא - Copy-Paste Ready

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sol Therapy</title>

  <style>
    /* חשוב: אלמנטים שיונפשו צריכים initial state */
    .reveal {
      opacity: 0;
      transform: translateY(40px);
    }

    /* ScrollSmoother wrapper */
    #smooth-wrapper {
      overflow: hidden;
      position: fixed;
      height: 100%;
      width: 100%;
      top: 0;
      left: 0;
    }
  </style>
</head>
<body>

  <div id="smooth-wrapper">
    <div id="smooth-content">

      <!-- Hero Section -->
      <section class="hero">
        <h1 class="hero-title">Sol Therapy</h1>
        <p class="hero-subtitle">Sound. Ceremony. Transformation.</p>
        <a class="hero-cta" href="#about">Explore</a>
      </section>

      <!-- Content Sections -->
      <section class="about">
        <h2 class="reveal">About</h2>
        <p class="reveal">Content here...</p>
      </section>

      <section class="services">
        <div class="card reveal">Service 1</div>
        <div class="card reveal">Service 2</div>
        <div class="card reveal">Service 3</div>
      </section>

    </div>
  </div>

  <!-- GSAP Scripts - BEFORE closing body tag -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollSmoother.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/SplitText.min.js"></script>

  <script>
    // Register plugins
    gsap.registerPlugin(ScrollTrigger, ScrollSmoother, SplitText);

    // Smooth scrolling
    const smoother = ScrollSmoother.create({
      smooth: 1.5,
      effects: true
    });

    // Hero entrance
    const heroTl = gsap.timeline({
      defaults: { duration: 0.8, ease: "power3.out" }
    });

    heroTl
      .from(".hero-title", { opacity: 0, y: 40 })
      .from(".hero-subtitle", { opacity: 0, y: 30 }, "-=0.4")
      .from(".hero-cta", { opacity: 0, y: 20, scale: 0.9 }, "-=0.3");

    // Scroll reveals
    gsap.utils.toArray(".reveal").forEach(el => {
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: "power2.out",
        scrollTrigger: {
          trigger: el,
          start: "top 85%",
          toggleActions: "play none none none"
        }
      });
    });
  </script>

</body>
</html>
```

### סדר טעינת Scripts

```
1. gsap.min.js          - חובה ראשון, תמיד
2. ScrollTrigger.min.js - חובה לכל אנימציית scroll
3. ScrollSmoother.min.js - אופציונלי, smooth scrolling
4. SplitText.min.js     - אופציונלי, אנימציות טקסט
5. DrawSVGPlugin.min.js - אופציונלי, SVG stroke animations
6. MorphSVGPlugin.min.js - אופציונלי, SVG morphing
7. Your custom script   - תמיד אחרון
```

### חשוב - בלי build system

- **אין צורך ב-registerPlugin עם CDN** - אם טוענים מ-CDN, ה-plugins מתרשמים אוטומטית. אבל מומלץ לרשום בפירוש לבטיחות.
- **סדר ה-script tags חשוב** - GSAP core חייב להיות ראשון.
- **DOMContentLoaded** - עטוף את הקוד ב-`DOMContentLoaded` או שים את ה-scripts לפני `</body>`.

---

## CDN Script Tags - Copy Paste Ready

### Minimum (אנימציות scroll בסיסיות):

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>
```

### Recommended (scroll-based website מלא):

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollSmoother.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/SplitText.min.js"></script>
```

### Full (כל ה-plugins):

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollSmoother.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/DrawSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/MorphSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/Flip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/Draggable.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/MotionPathPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/Observer.min.js"></script>
```

---

## מקורות

- [GSAP Official Site](https://gsap.com/)
- [GSAP GitHub Repository](https://github.com/greensock/GSAP)
- [GSAP on npm](https://www.npmjs.com/package/gsap)
- [jsDelivr GSAP CDN](https://www.jsdelivr.com/gsap)
- [cdnjs GSAP](https://cdnjs.com/libraries/gsap)
- [ScrollTrigger Documentation](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
- [ScrollSmoother Documentation](https://gsap.com/docs/v3/Plugins/ScrollSmoother/)
- [GSAP Installation Docs](https://gsap.com/docs/v3/Installation)
- [GSAP Pricing](https://gsap.com/pricing/)
- [GSAP ScrollTrigger Complete Guide (GSAPify)](https://gsapify.com/gsap-scrolltrigger)
