# Editorial Blog Design Research - Actionable Patterns & CSS Techniques

> Research compiled from analysis of NYT Interactive, Bloomberg Features, Kinfolk, Cereal Magazine, Monocle, It's Nice That, and industry-leading editorial design resources.

---

## 1. TYPOGRAPHY SYSTEM

### 1.1 The Foundation: Reading Experience Typography

The single most important differentiator between a basic blog and an editorial experience is typography. Here are the exact values used by world-class publications:

```css
/* === EDITORIAL TYPOGRAPHY FOUNDATION === */

:root {
  /* Type Scale - Editorial */
  --font-body: 'Freight Text Pro', 'Georgia', serif;        /* Serif for body */
  --font-display: 'Canela', 'Playfair Display', serif;      /* Display serif for headlines */
  --font-sans: 'Neue Haas Unica', 'Inter', sans-serif;      /* Sans for UI, captions, meta */
  --font-mono: 'JetBrains Mono', monospace;                  /* Code, data */

  /* Body Text */
  --body-size-mobile: 1.125rem;     /* 18px - minimum for editorial reading */
  --body-size-desktop: 1.25rem;     /* 20px - NYT/Atlantic standard */
  --body-line-height: 1.65;         /* Generous for long-form reading */
  --body-letter-spacing: 0.01em;    /* Slight tracking for readability */

  /* Measure (Line Length) - THE critical number */
  --measure: 65ch;                  /* 60-70ch is the editorial sweet spot */
  --measure-narrow: 50ch;           /* For pull quotes, captions */
  --measure-wide: 80ch;             /* For wider contexts */

  /* Paragraph Spacing */
  --paragraph-spacing: 1.5em;       /* Space between paragraphs */
  --section-spacing: 4rem;          /* Space between major sections */
  --section-spacing-large: 8rem;    /* Space for dramatic section breaks */
}
```

### 1.2 Heading Hierarchy for Long-Form Articles

```css
/* === HEADING HIERARCHY === */

/* Article Title - the hero */
.article-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 5vw + 1rem, 4.5rem);  /* 40px to 72px fluid */
  line-height: 1.1;
  letter-spacing: -0.02em;                          /* Tight tracking on display */
  font-weight: 400;                                 /* Light weight = editorial elegance */
  max-width: 20ch;                                  /* Short lines for drama */
  margin-bottom: 1.5rem;
}

/* Subtitle / Deck */
.article-deck {
  font-family: var(--font-sans);
  font-size: clamp(1.125rem, 1.5vw + 0.5rem, 1.5rem);  /* 18px to 24px */
  line-height: 1.5;
  letter-spacing: 0.01em;
  color: #555;
  max-width: var(--measure);
  margin-bottom: 3rem;
}

/* Section Heading (H2) - within article body */
.article-body h2 {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 2.5vw + 0.5rem, 2.5rem);  /* 28px to 40px */
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin-top: var(--section-spacing);
  margin-bottom: 1.5rem;
  font-weight: 400;
}

/* Sub-section Heading (H3) */
.article-body h3 {
  font-family: var(--font-sans);
  font-size: clamp(1.125rem, 1vw + 0.75rem, 1.375rem);  /* 18px to 22px */
  line-height: 1.3;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-top: 3rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

/* Kicker / Category Label (above title) */
.article-kicker {
  font-family: var(--font-sans);
  font-size: 0.75rem;                /* 12px */
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #e63946;                    /* Accent color */
  margin-bottom: 1rem;
  font-weight: 600;
}
```

### 1.3 Body Text - The Reading Engine

```css
/* === BODY TEXT === */

.article-body {
  font-family: var(--font-body);
  font-size: var(--body-size-desktop);
  line-height: var(--body-line-height);
  color: #1a1a1a;                            /* Not pure black - softer on eyes */
  max-width: var(--measure);
  margin: 0 auto;

  /* OpenType Features - editorial quality */
  font-feature-settings:
    'kern' 1,        /* Kerning */
    'liga' 1,        /* Standard ligatures (fi, fl, ff) */
    'clig' 1,        /* Contextual ligatures */
    'onum' 1,        /* Oldstyle numerals - blend with text */
    'pnum' 1;        /* Proportional numerals */

  /* Alternative high-level syntax (better browser support) */
  font-variant-ligatures: common-ligatures contextual;
  font-variant-numeric: oldstyle-nums proportional-nums;

  /* Optical sizing for variable fonts */
  font-optical-sizing: auto;

  /* Hyphenation for justified text */
  hyphens: auto;
  hyphenate-limit-chars: 6 3 2;              /* Min word length, before break, after break */
  hyphenate-limit-lines: 2;                  /* Max consecutive hyphenated lines */
  hyphenate-limit-zone: 8%;

  /* Hanging punctuation (Safari only, progressive enhancement) */
  hanging-punctuation: first allow-end last;

  /* Text rendering */
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.article-body p {
  margin-bottom: var(--paragraph-spacing);
}

.article-body p + p {
  text-indent: 0;                            /* No indent with spaced paragraphs */
}

/* Alternative: Traditional book-style (no spacing, indent instead) */
.article-body--book p + p {
  margin-bottom: 0;
  text-indent: 1.5em;
}

/* First paragraph after heading - no indent */
.article-body h2 + p,
.article-body h3 + p {
  text-indent: 0;
}
```

### 1.4 Drop Caps

```css
/* === DROP CAPS === */

/* Method 1: Cross-browser float approach */
.article-body > p:first-of-type::first-letter {
  font-family: var(--font-display);
  font-size: 4.5rem;
  float: left;
  line-height: 0.8;
  padding-right: 0.125em;
  padding-top: 0.1em;
  font-weight: 700;
  color: #1a1a1a;
}

/* Method 2: initial-letter (Chrome 110+, Safari 9+) */
@supports (initial-letter: 3) {
  .article-body > p:first-of-type::first-letter {
    initial-letter: 3;          /* Spans 3 lines */
    font-family: var(--font-display);
    font-weight: 700;
    margin-right: 0.1em;
    color: #1a1a1a;
    /* Reset float fallback */
    float: none;
    font-size: unset;
    line-height: unset;
    padding: 0;
  }
}

/* Decorative drop cap with background */
.drop-cap-accent > p:first-of-type::first-letter {
  initial-letter: 3;
  font-family: var(--font-display);
  font-weight: 700;
  color: white;
  background: #1a1a1a;
  padding: 0.25em 0.35em;
  margin-right: 0.15em;
  border-radius: 2px;
}
```

### 1.5 Pull Quotes

```css
/* === PULL QUOTES === */

/* Style 1: Large centered pull quote (NYT/Atlantic style) */
.pull-quote {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 3vw, 2.25rem);      /* 24px to 36px */
  line-height: 1.35;
  text-align: center;
  max-width: 75%;
  margin: var(--section-spacing) auto;
  padding: 2rem 0;
  border-top: 1px solid #1a1a1a;
  border-bottom: 1px solid #1a1a1a;
  font-style: italic;
  color: #1a1a1a;
}

.pull-quote cite {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-style: normal;
  margin-top: 1rem;
  color: #666;
}

/* Style 2: Left-aligned editorial pull quote (Bloomberg style) */
.pull-quote--editorial {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 2.5vw, 2.5rem);
  line-height: 1.3;
  border-left: 3px solid #1a1a1a;
  padding-left: 1.5rem;
  margin: 3rem 0 3rem -2rem;                   /* Negative margin for visual weight */
  max-width: 85%;
  font-weight: 300;
}

/* Style 3: Oversized quote mark (Kinfolk/Cereal style) */
.pull-quote--minimal {
  position: relative;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2vw, 1.75rem);
  line-height: 1.5;
  max-width: var(--measure-narrow);
  margin: var(--section-spacing) auto;
  padding-left: 3rem;
  font-style: italic;
}

.pull-quote--minimal::before {
  content: '\201C';                              /* Opening smart quote */
  font-family: var(--font-display);
  font-size: 5rem;
  position: absolute;
  left: -0.25rem;
  top: -1rem;
  color: rgba(0, 0, 0, 0.15);
  line-height: 1;
}

/* Style 4: Full-width highlight quote (Magazine style) */
.pull-quote--highlight {
  font-family: var(--font-display);
  font-size: clamp(2rem, 4vw, 3.5rem);
  line-height: 1.2;
  text-align: center;
  margin: var(--section-spacing-large) 0;
  padding: var(--section-spacing) 5%;
  background: #f5f0eb;                          /* Warm off-white */
  grid-column: 1 / -1;                         /* Full-bleed in grid layout */
}
```

### 1.6 Section Transitions

```css
/* === SECTION TRANSITIONS === */

/* Subtle horizontal rule */
.article-body hr {
  border: none;
  height: 1px;
  background: #ddd;
  max-width: 5rem;
  margin: var(--section-spacing) auto;
}

/* Three-dot separator (NYT style) */
.section-break {
  text-align: center;
  margin: var(--section-spacing) 0;
  font-size: 1.5rem;
  letter-spacing: 0.5em;
  color: #999;
}
.section-break::before {
  content: '...';
}

/* Ornamental separator */
.section-break--ornament {
  text-align: center;
  margin: var(--section-spacing) 0;
}
.section-break--ornament::before {
  content: '\2756';            /* Decorative diamond */
  font-size: 0.75rem;
  color: #aaa;
}

/* Number-based section divider */
.section-number {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  text-align: center;
  margin: var(--section-spacing-large) 0 2rem;
  color: #999;
}
.section-number span {
  display: block;
  font-family: var(--font-display);
  font-size: 3rem;
  letter-spacing: 0;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}
```

---

## 2. IMAGE/ILLUSTRATION INTEGRATION

### 2.1 The Full-Bleed Grid Layout (Foundation)

This is the single most important CSS pattern for editorial layouts. It enables contained body text alongside full-width images in the same flow:

```css
/* === THE EDITORIAL GRID === */

.article-wrapper {
  display: grid;
  grid-template-columns:
    1fr
    min(var(--measure), calc(100% - 4rem))
    1fr;
  /* Three columns: gutter | content | gutter */
}

/* All children default to center column */
.article-wrapper > * {
  grid-column: 2;
}

/* Full-bleed: spans all three columns */
.full-bleed {
  width: 100%;
  grid-column: 1 / -1;
}

/* Wide: breaks out of measure but not full-bleed */
.wide {
  grid-column: 1 / -1;
  max-width: min(90rem, 90%);
  margin-left: auto;
  margin-right: auto;
}

/* Popout: slightly wider than text (for figures, asides) */
.popout {
  grid-column: 1 / -1;
  max-width: min(calc(var(--measure) + 10rem), 90%);
  margin-left: auto;
  margin-right: auto;
}
```

### 2.2 Image Sizing Patterns

```css
/* === IMAGE PATTERNS === */

/* Standard inline image (within text measure) */
.article-body figure {
  margin: 2.5rem 0;
}

.article-body figure img {
  width: 100%;
  height: auto;
  display: block;
}

/* Full-bleed image */
.figure--full-bleed {
  grid-column: 1 / -1;
  margin: var(--section-spacing) 0;
}

.figure--full-bleed img {
  width: 100%;
  height: 75vh;                    /* Dramatic hero-style height */
  object-fit: cover;
  object-position: center;
}

/* Contained image with generous margin */
.figure--contained {
  max-width: var(--measure);
  margin: var(--section-spacing) auto;
}

/* Side-by-side images */
.figure-pair {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  max-width: min(75rem, 90%);
  margin: var(--section-spacing) auto;
}

/* Three-image strip */
.figure-trio {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  margin: var(--section-spacing) 0;
}

/* Asymmetric pair (2/3 + 1/3) */
.figure-pair--asymmetric {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 0.5rem;
  max-width: min(75rem, 90%);
  margin: var(--section-spacing) auto;
}

@media (max-width: 48rem) {
  .figure-pair,
  .figure-trio,
  .figure-pair--asymmetric {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
```

### 2.3 Caption Styling

```css
/* === CAPTIONS === */

/* Standard caption (below image) */
figcaption {
  font-family: var(--font-sans);
  font-size: 0.8125rem;            /* 13px */
  line-height: 1.5;
  color: #666;
  margin-top: 0.75rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid #eee;
}

figcaption .credit {
  color: #999;
  font-size: 0.6875rem;            /* 11px */
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Caption with left bar (Bloomberg style) */
figcaption.caption--bar {
  border-bottom: none;
  border-left: 2px solid #1a1a1a;
  padding-left: 0.75rem;
  padding-bottom: 0;
  margin-top: 1rem;
}

/* Overlay caption on image */
.figure--overlay {
  position: relative;
}

.figure--overlay figcaption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem 1.5rem 1rem;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  color: white;
  border: none;
  font-size: 0.875rem;
}

/* Side caption (text next to image) */
.figure--side {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 1.5rem;
  align-items: end;
}

.figure--side figcaption {
  font-size: 0.875rem;
  border: none;
  margin: 0;
  padding: 0;
}
```

### 2.4 Text Wrapping Around Images

```css
/* === TEXT WRAP === */

/* Float image left with text wrap */
.figure--float-left {
  float: left;
  width: 45%;
  margin: 0.5rem 2rem 1.5rem 0;
  shape-outside: margin-box;       /* Text flows around the margin box */
}

/* Float image right */
.figure--float-right {
  float: right;
  width: 45%;
  margin: 0.5rem 0 1.5rem 2rem;
  shape-outside: margin-box;
}

/* Custom shape text wrap (for circular/irregular images) */
.figure--shaped {
  float: left;
  width: 300px;
  margin-right: 2rem;
  shape-outside: circle(50%);      /* Text wraps around circle */
  clip-path: circle(50%);
}

@media (max-width: 48rem) {
  .figure--float-left,
  .figure--float-right,
  .figure--shaped {
    float: none;
    width: 100%;
    margin: 2rem 0;
    shape-outside: none;
    clip-path: none;
  }
}
```

### 2.5 Horizontal Gallery Strip

```css
/* === GALLERY STRIP === */

.gallery-strip {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  padding: var(--section-spacing) 0;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;           /* Firefox */
}

.gallery-strip::-webkit-scrollbar {
  display: none;                   /* Chrome/Safari */
}

.gallery-strip figure {
  flex: 0 0 auto;
  width: 70vw;
  max-width: 50rem;
  scroll-snap-align: center;
}

.gallery-strip figure img {
  width: 100%;
  height: 60vh;
  object-fit: cover;
}

.gallery-strip figcaption {
  padding: 0.75rem 0;
  font-family: var(--font-sans);
  font-size: 0.8125rem;
}

/* Gallery counter */
.gallery-strip-counter {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-align: center;
  color: #999;
  margin-top: 1rem;
}
```

---

## 3. LAYOUT RHYTHM - The "Breathing" Patterns

### 3.1 Section Spacing Cadence

```css
/* === RHYTHM SYSTEM === */

/*
  Editorial layouts use a rhythmic spacing system:
  - Small gap: between related items (paragraphs, list items)
  - Medium gap: between sub-sections
  - Large gap: between major sections
  - Hero gap: for dramatic section breaks

  The ratio is approximately 1 : 2 : 4 : 8
*/

:root {
  --space-xs: 0.5rem;     /* 8px */
  --space-sm: 1rem;       /* 16px */
  --space-md: 1.5rem;     /* 24px - paragraph spacing */
  --space-lg: 3rem;       /* 48px - sub-section */
  --space-xl: 4.5rem;     /* 72px - section break */
  --space-2xl: 6rem;      /* 96px - major section */
  --space-3xl: 9rem;      /* 144px - dramatic break */
  --space-hero: 12rem;    /* 192px - hero spacing */
}

/* Applying rhythm to article body */
.article-body > * + * {
  margin-top: var(--space-md);
}

.article-body > h2 {
  margin-top: var(--space-2xl);
}

.article-body > h3 {
  margin-top: var(--space-xl);
}

.article-body > figure {
  margin-top: var(--space-xl);
  margin-bottom: var(--space-xl);
}

.article-body > .full-bleed {
  margin-top: var(--space-2xl);
  margin-bottom: var(--space-2xl);
}

.article-body > blockquote {
  margin-top: var(--space-xl);
  margin-bottom: var(--space-xl);
}
```

### 3.2 Dark/Light Section Alternation

```css
/* === SECTION ALTERNATION === */

/* Light section (default) */
.section--light {
  background: #ffffff;
  color: #1a1a1a;
  padding: var(--space-2xl) 0;
}

/* Warm section (off-white, Kinfolk/Cereal style) */
.section--warm {
  background: #f5f0eb;
  color: #1a1a1a;
  padding: var(--space-2xl) 0;
  grid-column: 1 / -1;
}

/* Dark section */
.section--dark {
  background: #1a1a1a;
  color: #e8e8e8;
  padding: var(--space-2xl) 0;
  grid-column: 1 / -1;
}

.section--dark h2,
.section--dark h3 {
  color: #ffffff;
}

.section--dark figcaption {
  color: #999;
}

/* Accent section */
.section--accent {
  background: #e63946;            /* Or brand color */
  color: #ffffff;
  padding: var(--space-2xl) 0;
  grid-column: 1 / -1;
}

/* Pattern: alternating sections within article */
/*
  text -> full-bleed-image -> text -> warm-bg-quote -> text ->
  dark-section -> text -> image-pair -> text
  This creates visual rhythm that prevents reader fatigue
*/
```

### 3.3 Callout Boxes & Sidebars

```css
/* === CALLOUT BOXES === */

/* Info box (side note) */
.callout {
  font-family: var(--font-sans);
  font-size: 0.9375rem;
  line-height: 1.6;
  background: #f8f9fa;
  border-left: 3px solid #1a1a1a;
  padding: 1.5rem 2rem;
  margin: var(--space-lg) 0;
}

.callout__title {
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
  color: #1a1a1a;
}

/* Number callout (statistics highlight) */
.callout--stat {
  text-align: center;
  background: none;
  border: none;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  padding: var(--space-lg) 0;
  margin: var(--space-xl) 0;
}

.callout--stat .stat-number {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5vw, 5rem);
  line-height: 1;
  font-weight: 700;
  display: block;
  margin-bottom: 0.5rem;
}

.callout--stat .stat-label {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  color: #666;
  letter-spacing: 0.05em;
}

/* Timeline/process box */
.callout--timeline {
  font-family: var(--font-sans);
  font-size: 0.9375rem;
  border: 1px solid #eee;
  padding: 2rem;
  margin: var(--space-xl) 0;
}

/* Sidebar info box (floats alongside text on desktop) */
.aside-box {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  line-height: 1.5;
  background: #f5f0eb;
  padding: 1.5rem;
  margin: var(--space-md) 0;
}

@media (min-width: 75rem) {
  .aside-box {
    float: right;
    width: 18rem;
    margin-left: 2rem;
    margin-right: -10rem;          /* Pull into margin */
  }
}

.aside-box__title {
  font-weight: 700;
  font-size: 0.6875rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #ddd;
}
```

### 3.4 Reading Progress Indicator

```css
/* === READING PROGRESS BAR === */

.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: transparent;
  z-index: 1000;
  transform-origin: left;
  transform: scaleX(0);
  background: #1a1a1a;

  /* CSS-only scroll-driven animation (Chrome 116+) */
  animation: progressBar linear;
  animation-timeline: scroll();
}

@keyframes progressBar {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}

/* Fallback: JS-based progress */
/*
  const progressBar = document.querySelector('.progress-bar');
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.body.scrollHeight - window.innerHeight;
    const scrollPercent = scrollTop / docHeight;
    progressBar.style.transform = `scaleX(${scrollPercent})`;
  });
*/
```

---

## 4. MICRO-INTERACTIONS & ANIMATION

### 4.1 Scroll-Triggered Reveals (CSS-only)

```css
/* === SCROLL REVEALS === */

/* CSS Scroll-Driven Animations (Chrome 116+, Edge 116+) */

/* Fade in on scroll */
.reveal {
  opacity: 0;
  transform: translateY(2rem);
  animation: revealIn linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}

@keyframes revealIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Staggered reveal for multiple items */
.reveal-stagger:nth-child(1) { animation-delay: 0ms; }
.reveal-stagger:nth-child(2) { animation-delay: 100ms; }
.reveal-stagger:nth-child(3) { animation-delay: 200ms; }

/* Fallback: Intersection Observer approach */
/*
  CSS:
  .reveal-io {
    opacity: 0;
    transform: translateY(2rem);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  .reveal-io.is-visible {
    opacity: 1;
    transform: translateY(0);
  }

  JS:
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.reveal-io').forEach(el => observer.observe(el));
*/
```

### 4.2 Image Lazy-Load Transitions

```css
/* === LAZY LOAD TRANSITIONS === */

/* Blur-up technique */
.lazy-image-wrapper {
  position: relative;
  overflow: hidden;
  background: #f0f0f0;
}

.lazy-image-wrapper img {
  opacity: 0;
  transition: opacity 0.4s ease;
}

.lazy-image-wrapper img.loaded {
  opacity: 1;
}

/* Low-quality placeholder (LQIP) */
.lazy-image-wrapper .lqip {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: blur(20px);
  transform: scale(1.1);          /* Hide blur edges */
  transition: opacity 0.4s ease 0.1s;
}

.lazy-image-wrapper img.loaded ~ .lqip {
  opacity: 0;
}

/* Skeleton loading placeholder */
.image-skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### 4.3 Parallax Depth Effects

```css
/* === PARALLAX === */

/* CSS-only parallax (scroll-driven animations) */
.parallax-image {
  animation: parallaxShift linear;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

@keyframes parallaxShift {
  from { transform: translateY(-5%); }
  to   { transform: translateY(5%); }
}

/* Parallax container (overflow hidden + oversized image) */
.parallax-container {
  overflow: hidden;
  height: 70vh;
  position: relative;
}

.parallax-container img {
  width: 100%;
  height: 120%;                    /* Oversized to allow movement */
  object-fit: cover;
  animation: parallaxShift linear;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

/* Subtle text parallax (different speed than images) */
.parallax-text {
  animation: textFloat linear;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

@keyframes textFloat {
  from { transform: translateY(-2%); }
  to   { transform: translateY(2%); }
}
```

### 4.4 Hover States for Footnotes & Sources

```css
/* === FOOTNOTES & SOURCES === */

/* Inline footnote reference */
.footnote-ref {
  font-family: var(--font-sans);
  font-size: 0.7em;
  vertical-align: super;
  line-height: 0;                  /* Prevent line-height disruption */
  color: #e63946;
  cursor: pointer;
  text-decoration: none;
  transition: color 0.2s ease;
}

.footnote-ref:hover {
  color: #1a1a1a;
}

/* Tooltip footnote on hover */
.footnote-tooltip {
  position: relative;
  display: inline;
}

.footnote-tooltip .tooltip-content {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-0.5rem);
  background: #1a1a1a;
  color: #fff;
  padding: 0.75rem 1rem;
  font-family: var(--font-sans);
  font-size: 0.8125rem;
  line-height: 1.5;
  border-radius: 4px;
  width: max-content;
  max-width: 20rem;
  z-index: 100;
  transition: opacity 0.2s ease, transform 0.2s ease;
  pointer-events: none;
}

.footnote-tooltip:hover .tooltip-content {
  visibility: visible;
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Source citation link */
.source-link {
  color: inherit;
  text-decoration: underline;
  text-decoration-color: rgba(0, 0, 0, 0.2);
  text-underline-offset: 0.15em;
  text-decoration-thickness: 1px;
  transition: text-decoration-color 0.2s ease;
}

.source-link:hover {
  text-decoration-color: #e63946;
}
```

---

## 5. MOBILE-FIRST READING EXPERIENCE

### 5.1 Responsive Typography Scale

```css
/* === MOBILE-FIRST TYPOGRAPHY === */

/* Base: mobile */
:root {
  --body-size: 1.0625rem;           /* 17px - optimal mobile reading */
  --body-lh: 1.65;
  --h1-size: 2rem;                   /* 32px */
  --h2-size: 1.5rem;                 /* 24px */
  --h3-size: 1.125rem;              /* 18px */
}

/* Tablet (48rem / 768px) */
@media (min-width: 48rem) {
  :root {
    --body-size: 1.1875rem;          /* 19px */
    --h1-size: 2.75rem;              /* 44px */
    --h2-size: 1.875rem;             /* 30px */
  }
}

/* Desktop (64rem / 1024px) */
@media (min-width: 64rem) {
  :root {
    --body-size: 1.25rem;            /* 20px */
    --body-lh: 1.7;
    --h1-size: 3.5rem;               /* 56px */
    --h2-size: 2.25rem;              /* 36px */
    --h3-size: 1.25rem;              /* 20px */
  }
}

/* Large desktop (90rem / 1440px) */
@media (min-width: 90rem) {
  :root {
    --body-size: 1.3125rem;          /* 21px */
    --h1-size: 4rem;                  /* 64px */
    --h2-size: 2.5rem;               /* 40px */
  }
}

/* Alternative: fluid typography with clamp() */
.article-body {
  font-size: clamp(1.0625rem, 0.5vw + 0.9rem, 1.3125rem);
  /* Smoothly scales from 17px to 21px */
}
```

### 5.2 Touch-Friendly Spacing

```css
/* === MOBILE SPACING === */

/* Mobile-specific adjustments */
@media (max-width: 48rem) {

  /* Padding for mobile reading */
  .article-wrapper {
    padding: 0 1.25rem;             /* 20px side padding */
    grid-template-columns:
      0
      minmax(0, 1fr)
      0;
    /* Zero-width gutters, content fills available space */
  }

  /* Touch target sizing */
  .article-body a {
    padding: 0.25em 0;              /* Larger tap area on links */
  }

  /* Reduce section spacing on mobile */
  :root {
    --section-spacing: 3rem;
    --section-spacing-large: 5rem;
  }

  /* Full-bleed images flush to edges */
  .full-bleed {
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    width: calc(100% + 2.5rem);
  }

  /* Pull quotes smaller on mobile */
  .pull-quote {
    font-size: 1.25rem;
    max-width: 100%;
    padding: 1.5rem 0;
  }

  /* Callout boxes full width */
  .callout {
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    padding: 1.5rem;
  }

  /* Image pairs stack on mobile */
  .figure-pair,
  .figure-trio {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }

  /* Gallery strip: wider items */
  .gallery-strip figure {
    width: 85vw;
  }

  /* Reduce drop cap size */
  .article-body > p:first-of-type::first-letter {
    font-size: 3.5rem;
  }
}

/* Input size protection (prevents iOS zoom) */
input, select, textarea {
  font-size: 1rem;                  /* Must be >= 16px on iOS */
}
```

### 5.3 Image Handling on Small Screens

```css
/* === MOBILE IMAGE HANDLING === */

/* Responsive images base */
.article-body img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Aspect ratio containers (prevent layout shift) */
.image-container {
  position: relative;
  aspect-ratio: 16 / 9;            /* or 4/3, 3/2, 1/1 */
  overflow: hidden;
  background: #f0f0f0;
}

.image-container img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Art direction: different crops per breakpoint */
/*
  <picture>
    <source media="(max-width: 48rem)" srcset="image-mobile.jpg">
    <source media="(max-width: 75rem)" srcset="image-tablet.jpg">
    <img src="image-desktop.jpg" alt="..." loading="lazy">
  </picture>
*/

/* Figure caption on mobile */
@media (max-width: 48rem) {
  figcaption {
    font-size: 0.75rem;
    padding: 0.5rem 0;
  }

  /* Side caption -> below on mobile */
  .figure--side {
    grid-template-columns: 1fr;
    gap: 0;
  }
}
```

---

## 6. ADVANCED CSS TECHNIQUES FOR EDITORIAL QUALITY

### 6.1 Complete OpenType Feature Set

```css
/* === OPENTYPE FEATURES === */

.article-body {
  /* High-level properties (preferred - better browser support) */
  font-variant-ligatures: common-ligatures contextual;
  font-variant-numeric: oldstyle-nums proportional-nums;
  font-variant-caps: normal;
  font-kerning: normal;
  font-optical-sizing: auto;

  /* Low-level fallback */
  font-feature-settings:
    'kern' 1,      /* Kerning */
    'liga' 1,      /* Standard ligatures */
    'clig' 1,      /* Contextual ligatures */
    'onum' 1,      /* Oldstyle figures (3, 5, 7 with descenders) */
    'pnum' 1;      /* Proportional figures */
}

/* Tabular (lining) numbers for data/tables */
.data-table,
.article-meta,
.stat-number {
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: 'lnum' 1, 'tnum' 1;
}

/* Small caps for abbreviations */
abbr,
.small-caps {
  font-variant-caps: all-small-caps;
  font-feature-settings: 'smcp' 1, 'c2sc' 1;
  letter-spacing: 0.05em;
}

/* Discretionary ligatures for display text */
.article-title {
  font-variant-ligatures: common-ligatures discretionary-ligatures;
  font-feature-settings: 'liga' 1, 'dlig' 1;
}

/* Fractions */
.fraction {
  font-variant-numeric: diagonal-fractions;
  font-feature-settings: 'frac' 1;
}
```

### 6.2 Optical Margin Alignment

```css
/* === OPTICAL ALIGNMENT === */

/* Hanging punctuation (Safari only but progressively enhanced) */
.article-body p {
  hanging-punctuation: first allow-end last;
}

/* Manual optical margin for quotes */
blockquote p {
  text-indent: -0.4em;            /* Pull opening quote into margin */
}

/* Negative text-indent for list bullets */
.article-body ul {
  list-style-position: outside;
  padding-left: 1.5em;
}

/* First line indent (traditional book style alternative) */
.article-body--book p + p {
  text-indent: 1.5em;
}
```

### 6.3 Hyphenation Control

```css
/* === HYPHENATION === */

/* For justified text (use sparingly) */
.article-body--justified {
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;

  /* Fine control */
  hyphenate-limit-chars: 6 3 2;    /* Word min 6 chars, 3 before break, 2 after */
  hyphenate-limit-lines: 2;        /* Max 2 consecutive hyphenated lines */
  hyphenate-limit-zone: 8%;        /* Zone from right edge where hyphenation starts */

  /* Overflow wrap as safety net */
  overflow-wrap: break-word;
  word-break: normal;
}

/* Prevent hyphenation on headings */
h1, h2, h3 {
  hyphens: none;
}

/* Prevent widows and orphans */
.article-body p {
  widows: 2;
  orphans: 2;
}

/* Non-breaking behavior for critical text */
.no-break {
  white-space: nowrap;
}
```

### 6.4 Variable Font Usage

```css
/* === VARIABLE FONTS === */

/* Loading a variable font */
@font-face {
  font-family: 'Editorial';
  src: url('/fonts/editorial-variable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-stretch: 75% 125%;
  font-display: swap;
}

/* Using weight axis */
.article-title {
  font-family: 'Editorial', serif;
  font-weight: 300;               /* Light for editorial elegance */
}

.article-body strong {
  font-weight: 650;               /* Precise weight instead of binary bold */
}

/* Optical size axis (opsz) - critical for editorial */
.article-title {
  font-variation-settings: 'opsz' 72;    /* Optimized for display */
}

.article-body {
  font-variation-settings: 'opsz' 14;    /* Optimized for reading */
}

figcaption {
  font-variation-settings: 'opsz' 10;    /* Optimized for small text */
}

/* Grade axis (GRAD) - adjust weight without layout shift */
@media (prefers-color-scheme: dark) {
  .article-body {
    font-variation-settings: 'GRAD' 50;  /* Slightly heavier for dark bg */
  }
}
```

### 6.5 Container Queries for Modular Editorial Components

```css
/* === CONTAINER QUERIES === */

/* Define containers */
.article-wrapper {
  container-type: inline-size;
  container-name: article;
}

.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}

/* Callout adapts to its container */
@container article (min-width: 60rem) {
  .callout {
    float: right;
    width: 40%;
    margin-left: 2rem;
    margin-right: -5rem;           /* Pull into margin */
  }
}

@container sidebar (max-width: 25rem) {
  .callout {
    float: none;
    width: 100%;
    margin: 1rem 0;
  }
}

/* Card adapts when placed in sidebar vs main content */
@container (min-width: 40rem) {
  .article-card {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 1.5rem;
  }
}

@container (max-width: 39.99rem) {
  .article-card {
    display: block;
  }

  .article-card img {
    margin-bottom: 1rem;
  }
}
```

---

## 7. COMPLETE HTML STRUCTURE REFERENCE

```html
<!-- === EDITORIAL ARTICLE STRUCTURE === -->

<article class="article-wrapper">

  <!-- Article Header -->
  <header class="article-header">
    <span class="article-kicker">Design & Technology</span>
    <h1 class="article-title">The Art of Meaningful Typography</h1>
    <p class="article-deck">
      How the world's best editorial teams create immersive reading
      experiences through careful typographic choices
    </p>
    <div class="article-meta">
      <span class="author">By Jane Smith</span>
      <time datetime="2026-02-15">February 15, 2026</time>
      <span class="read-time">12 min read</span>
    </div>
  </header>

  <!-- Hero Image (full-bleed) -->
  <figure class="figure--full-bleed">
    <picture>
      <source media="(max-width: 48rem)" srcset="hero-mobile.jpg">
      <img src="hero-desktop.jpg" alt="..." loading="eager">
    </picture>
    <figcaption>
      A description of the image.
      <span class="credit">Photograph by John Doe</span>
    </figcaption>
  </figure>

  <!-- Article Body -->
  <div class="article-body">

    <!-- First paragraph with drop cap -->
    <p>The opening paragraph of the article with a drop cap applied
    via CSS ::first-letter pseudo-element...</p>

    <p>Subsequent paragraphs continue the narrative...</p>

    <!-- Section heading -->
    <h2>The Science of Reading</h2>

    <p>Content continues here...</p>

    <!-- Pull quote -->
    <blockquote class="pull-quote">
      <p>Typography is the craft of endowing human language with
      a durable visual form.</p>
      <cite>Robert Bringhurst</cite>
    </blockquote>

    <p>More body text...</p>

    <!-- Inline figure -->
    <figure>
      <img src="inline-image.jpg" alt="..." loading="lazy">
      <figcaption>An inline image within the text measure.</figcaption>
    </figure>

    <!-- Callout box -->
    <aside class="callout">
      <span class="callout__title">Key Insight</span>
      <p>The optimal line length for body text is 50-75 characters,
      with 65 characters being the ideal target.</p>
    </aside>

    <p>More content...</p>

    <!-- Section break -->
    <div class="section-break" role="separator"></div>

    <h2>Visual Rhythm in Editorial Design</h2>

    <p>Content continues...</p>

  </div>

  <!-- Wide image pair (breaks out of measure) -->
  <div class="figure-pair wide">
    <figure>
      <img src="pair-1.jpg" alt="..." loading="lazy">
      <figcaption>First image caption</figcaption>
    </figure>
    <figure>
      <img src="pair-2.jpg" alt="..." loading="lazy">
      <figcaption>Second image caption</figcaption>
    </figure>
  </div>

  <div class="article-body">
    <p>Text resumes at normal measure...</p>
  </div>

  <!-- Full-bleed dark section -->
  <section class="section--dark full-bleed">
    <div class="article-body">
      <blockquote class="pull-quote--highlight">
        <p>A dramatic quote spanning the full width on a dark
        background creates a powerful visual break.</p>
      </blockquote>
    </div>
  </section>

  <div class="article-body">
    <p>Text resumes...</p>
  </div>

  <!-- Gallery strip -->
  <div class="gallery-strip full-bleed">
    <figure>
      <img src="gallery-1.jpg" alt="..." loading="lazy">
      <figcaption>Gallery caption 1</figcaption>
    </figure>
    <figure>
      <img src="gallery-2.jpg" alt="..." loading="lazy">
      <figcaption>Gallery caption 2</figcaption>
    </figure>
    <figure>
      <img src="gallery-3.jpg" alt="..." loading="lazy">
      <figcaption>Gallery caption 3</figcaption>
    </figure>
  </div>

  <!-- Statistics callout -->
  <aside class="callout--stat">
    <span class="stat-number">73%</span>
    <span class="stat-label">of readers prefer editorial layouts
    with generous whitespace</span>
  </aside>

  <div class="article-body">
    <p>Final section of content...</p>
  </div>

</article>

<!-- Reading Progress Bar -->
<div class="progress-bar" aria-hidden="true"></div>
```

---

## 8. SITE-SPECIFIC DESIGN PATTERNS

### Kinfolk
- **Palette:** Achromatic (black/white only). Photography provides all color.
- **Typography:** Serif body, generous size, extreme whitespace.
- **Images:** Aspect ratios 29:39 and 7:9 (portrait-dominant). Images are primary content anchors.
- **Layout:** Modular card system. Minimal metadata (category, issue number only).
- **Lesson:** Restraint is the ultimate sophistication. Let photography dominate.

### Cereal Magazine
- **Body font:** Adobe Text Pro at 1.2rem.
- **UI font:** Neue Haas Unica Pro.
- **Grid:** Three-column header (33.3% | auto | 33.3%). Results grid: 6 cols to 1 col responsive.
- **Spacing:** 2rem-3rem padding. 5rem row-gap in listings.
- **Animation:** 1-2 second delays create perceived depth on load.
- **Color:** High contrast black/white with cyan accent (#80d9ed) for interactive states.

### Monocle
- **Body font:** Plantin (serif, designed 1910s) for literary authority.
- **Data/caption font:** Helvetica Neue (sans-serif) for neutral information.
- **Grid:** Intricate multi-column system that adapts fluidly.
- **Trend:** Recent redesign increased font size and reduced columns for accessibility.
- **Lesson:** Serif/sans-serif pairing creates clear hierarchy: Plantin for reading, Helvetica for scanning.

### NYT Interactive / Snow Fall
- **Grid:** 5-column system, blocks span 1-5 columns.
- **Text contrast:** Display titles large/light, subtitles small/bold.
- **Technique:** Individual letters wrapped in spans for precise letter-spacing control.
- **Interaction:** Scroll-triggered video, animations, CSS background changes.
- **Lesson:** Scrollytelling (seamless, clickless experience) through scroll-bound media.

---

## 9. PERFORMANCE CONSIDERATIONS

```css
/* === PERFORMANCE === */

/* Font loading strategy */
@font-face {
  font-family: 'Editorial Serif';
  src: url('/fonts/editorial-serif.woff2') format('woff2');
  font-weight: 300 700;
  font-display: swap;              /* Show fallback immediately, swap when loaded */
  unicode-range: U+0000-00FF;      /* Latin only - load other ranges separately */
}

/* Critical above-the-fold styles inlined in <head> */
/* Non-critical styles loaded async */
/*
  <link rel="preload" href="/fonts/editorial.woff2" as="font" crossorigin>
  <link rel="stylesheet" href="/css/above-fold.css">
  <link rel="stylesheet" href="/css/below-fold.css" media="print" onload="this.media='all'">
*/

/* Content visibility for long articles */
.article-body > section {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px;  /* Estimated height for scroll stability */
}

/* Lazy loading images */
/*
  <img src="image.jpg" loading="lazy" decoding="async" alt="...">
*/

/* Responsive images with srcset */
/*
  <img
    src="image-800.jpg"
    srcset="image-400.jpg 400w, image-800.jpg 800w, image-1600.jpg 1600w"
    sizes="(max-width: 48rem) 100vw, 65ch"
    loading="lazy"
    alt="..."
  >
*/
```

---

## 10. DARK MODE SUPPORT

```css
/* === DARK MODE === */

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #141414;
    --color-text: #e0e0e0;
    --color-text-secondary: #999;
    --color-border: #333;
    --color-surface: #1e1e1e;
    --color-accent: #ff6b6b;
  }

  .article-body {
    color: var(--color-text);
    /* Slightly increase weight for dark backgrounds */
    font-weight: 420;              /* Variable font only */
    /* Or use font-variation-settings */
    font-variation-settings: 'GRAD' 50;
  }

  .section--warm {
    background: var(--color-surface);
  }

  .callout {
    background: var(--color-surface);
    border-left-color: var(--color-accent);
  }

  figcaption {
    color: var(--color-text-secondary);
    border-bottom-color: var(--color-border);
  }

  /* Reduce image brightness slightly */
  .article-body img {
    filter: brightness(0.9);
  }
}
```

---

## QUICK REFERENCE: The Numbers That Matter

| Property | Mobile | Desktop | Source |
|----------|--------|---------|--------|
| Body font-size | 17-18px | 20-21px | NYT, Atlantic, Bloomberg |
| Line-height | 1.6-1.65 | 1.65-1.75 | Bringhurst, industry standard |
| Measure (line length) | 35-45ch | 60-70ch (65 ideal) | Bringhurst, Smashing Magazine |
| Paragraph spacing | 1.5em | 1.5em | Industry standard |
| Section spacing | 3rem | 4.5-6rem | Analysis of reference sites |
| H1 display size | 32-36px | 48-72px | NYT, Bloomberg |
| Caption size | 12px | 13px | Kinfolk, Cereal, NYT |
| Side padding (mobile) | 20px | n/a | Touch-friendly standard |
| Touch target min | 48px | n/a | Material Design, Apple HIG |
| Progress bar height | 2-3px | 2-3px | Industry standard |
| Max content width | n/a | 65ch (~720px) | Typography best practice |

---

## SOURCES

- [Designing for Long-Form Articles - CSS-Tricks](https://css-tricks.com/designing-for-long-form-articles/)
- [Modern CSS Techniques for Legibility - Smashing Magazine](https://www.smashingmagazine.com/2020/07/css-techniques-legibility/)
- [Full-Bleed Layout Using CSS Grid - Josh W. Comeau](https://www.joshwcomeau.com/css/full-bleed/)
- [Modern Fluid Typography Using CSS Clamp - Smashing Magazine](https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/)
- [CSS Scroll-Driven Animations - Smashing Magazine](https://www.smashingmagazine.com/2024/12/introduction-css-scroll-driven-animations/)
- [Font Size Guidelines for Responsive Websites - Learn UI Design](https://www.learnui.design/blog/mobile-desktop-website-font-size-guidelines.html)
- [Control Drop Caps with CSS initial-letter - Chrome Developers](https://developer.chrome.com/blog/control-your-drop-caps-with-css-initial-letter)
- [Balancing Line Length and Font Size - Smashing Magazine](https://www.smashingmagazine.com/2014/09/balancing-line-length-font-size-responsive-web-design/)
- [Typographic Design Patterns - Smashing Magazine](https://www.smashingmagazine.com/2009/08/typographic-design-survey-best-practices-from-the-best-blogs/)
- [OpenType Features in CSS - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts)
- [Container Queries in 2026 - LogRocket](https://blog.logrocket.com/container-queries-2026/)
- [Monocle Brand Identity Teardown - Visual Journal Craft](https://visualjournalcraft.com/article/monocle-brand-identity-teardown)
- [How We Made Snow Fall - Source OpenNews](https://source.opennews.org/articles/how-we-made-snow-fall/)
