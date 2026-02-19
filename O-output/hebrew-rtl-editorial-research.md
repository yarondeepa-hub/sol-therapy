# Hebrew RTL Editorial Blog Design - Actionable Patterns & CSS

> Companion to `editorial-blog-design-research.md`. This document covers everything specific to Hebrew RTL editorial layouts - typography, bidi handling, layout mirroring, and the cultural/typographic conventions that differ from Latin-based editorial design.

---

## 1. HEBREW TYPOGRAPHY SYSTEM

### 1.1 Foundation: How Hebrew Differs from Latin

Hebrew characters are structurally different from Latin letters in ways that directly affect CSS values:

- **Taller x-height** - Hebrew letters occupy more vertical space at the same font-size, so the same `font-size: 20px` renders visually larger in Hebrew than English
- **No true italic** - Hebrew tradition uses bold or letter-spacing for emphasis, not slant. Italic Hebrew fonts exist but are controversial and rarely used in premium editorial
- **No uppercase/lowercase** - no `text-transform: uppercase` equivalent; emphasis through bold, spacing, or size only
- **Denser character width** - Hebrew words tend to be shorter but characters are wider, changing the `ch` unit relationship
- **Right-to-left reading direction** - affects every layout assumption from float direction to margin placement

### 1.2 Hebrew Font Selection for Editorial

```css
/* === HEBREW EDITORIAL FONT STACK === */

:root {
  /* OPTION A: Classic Editorial (Serif) */
  /* Frank Ruhl Libre - THE Hebrew editorial serif.
     Most recognized Hebrew typeface in print. Used by
     virtually every Israeli newspaper and book publisher. */
  --font-body-he: 'Frank Ruhl Libre', 'Noto Serif Hebrew', 'David', serif;

  /* OPTION B: Modern Editorial (Sans-Serif) */
  /* Heebo - Hebrew adaptation of Roboto. Clean, modern,
     excellent screen readability. Best for digital-first. */
  --font-body-he: 'Heebo', 'Noto Sans Hebrew', 'Arial Hebrew', sans-serif;

  /* OPTION C: Warm/Friendly (Sans with character) */
  /* Rubik - slightly rounded corners. Approachable yet
     professional. Good for wellness/lifestyle editorial. */
  --font-body-he: 'Rubik', 'Heebo', 'Noto Sans Hebrew', sans-serif;

  /* Display/Headlines - Hebrew */
  --font-display-he: 'Frank Ruhl Libre', 'Noto Serif Hebrew', serif;

  /* UI/Captions - Hebrew */
  --font-ui-he: 'Heebo', 'Rubik', 'Noto Sans Hebrew', sans-serif;

  /* Latin companion for mixed content */
  --font-body-en: 'Inter', 'Roboto', sans-serif;
  --font-display-en: 'Playfair Display', 'Georgia', serif;
}

/* Google Fonts loading for Hebrew */
/*
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300..900&family=Heebo:wght@100..900&family=Rubik:wght@300..900&display=swap" rel="stylesheet">
*/
```

**Font comparison for Sol Therapy editorial:**

| Font | Character | Best For | Weight Range |
|------|-----------|----------|-------------|
| Frank Ruhl Libre | Classic, authoritative, literary | Long-form articles, deep editorial | 300-900 |
| Heebo | Clean, modern, neutral | Digital-first content, UI-heavy pages | 100-900 |
| Rubik | Warm, approachable, rounded | Wellness, lifestyle, personal content | 300-900 |
| Noto Sans Hebrew | Universal, reliable | Fallback, accessibility-first | 100-900 |
| Noto Serif Hebrew | Formal, classic | Serif body text alternative | 100-900 |

**Recommendation for Sol Therapy:** Rubik for body text (warmth aligns with therapy/wellness tone), Frank Ruhl Libre for display headlines (authority and depth). Heebo for UI elements.

### 1.3 Hebrew-Specific Typography Values

```css
/* === HEBREW TYPOGRAPHY VALUES === */
/* These differ significantly from the Latin values in the companion doc */

:root {
  /* Body Text - Hebrew needs LARGER than Latin */
  --body-size-he-mobile: 1.1875rem;   /* 19px - Hebrew needs ~1px more than Latin */
  --body-size-he-desktop: 1.375rem;   /* 22px - Hebrew reads best slightly larger */

  /* Line Height - Hebrew needs MORE than Latin */
  /* Hebrew has taller ascenders relative to the baseline,
     and diacritics (niqqud) can clip with tight line-height */
  --body-lh-he: 1.8;                  /* vs 1.65 for Latin */
  --body-lh-he-with-niqqud: 2.0;      /* When vowel marks are present */

  /* Letter Spacing - Hebrew is DIFFERENT */
  /* Standard Hebrew body: no extra tracking */
  --body-ls-he: normal;               /* Hebrew doesn't need the 0.01em Latin uses */
  /* Emphasis via spacing (replaces italic in Hebrew tradition) */
  --emphasis-ls-he: 0.08em;           /* letter-spacing for emphasis */

  /* Measure - Hebrew lines are shorter in character count */
  /* Hebrew characters are wider, so fewer characters fit per line.
     The optimal line length in Hebrew is 55-65 characters,
     slightly less than the 60-70 for Latin */
  --measure-he: 60ch;
  --measure-he-narrow: 45ch;
  --measure-he-wide: 72ch;

  /* Paragraph Spacing */
  --paragraph-spacing-he: 1.75em;     /* Slightly more generous than Latin */
  --section-spacing-he: 4.5rem;
}
```

### 1.4 Body Text for Hebrew Editorial

```css
/* === HEBREW BODY TEXT === */

.article-body[lang="he"],
.article-body:lang(he) {
  font-family: var(--font-body-he);
  font-size: var(--body-size-he-desktop);
  line-height: var(--body-lh-he);
  direction: rtl;
  text-align: right;                   /* Explicit right-align for Hebrew */
  color: #1a1a1a;
  max-width: var(--measure-he);
  margin: 0 auto;

  /* OpenType features for Hebrew */
  font-feature-settings:
    'kern' 1,                          /* Kerning */
    'liga' 1;                          /* Ligatures (Hebrew has some) */

  /* Hebrew does NOT use oldstyle numerals -
     Hebrew text traditionally uses lining figures */
  font-variant-numeric: lining-nums proportional-nums;

  /* Text rendering */
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;

  /* NO hyphenation for Hebrew */
  /* Hebrew hyphenation is not well-supported in browsers
     and not a strong tradition in Hebrew typography */
  hyphens: none;

  /* Word break handling for Hebrew */
  word-break: normal;
  overflow-wrap: break-word;
}

.article-body[lang="he"] p {
  margin-bottom: var(--paragraph-spacing-he);
}
```

### 1.5 Heading Hierarchy - Hebrew

```css
/* === HEBREW HEADINGS === */

/* Article Title */
.article-title[lang="he"] {
  font-family: var(--font-display-he);
  font-size: clamp(2.25rem, 5vw + 1rem, 4rem);
  line-height: 1.25;                  /* Hebrew needs more line-height on display too */
  letter-spacing: -0.01em;            /* Slight tightening, less than Latin */
  font-weight: 700;                   /* Hebrew display text often bolder than Latin */
  text-align: right;
  direction: rtl;
}

/* Subtitle / Deck */
.article-deck[lang="he"] {
  font-family: var(--font-ui-he);
  font-size: clamp(1.125rem, 1.5vw + 0.5rem, 1.5rem);
  line-height: 1.6;
  color: #555;
  text-align: right;
  direction: rtl;
}

/* Section Heading (H2) */
.article-body[lang="he"] h2 {
  font-family: var(--font-display-he);
  font-size: clamp(1.625rem, 2.5vw + 0.5rem, 2.25rem);
  line-height: 1.3;
  font-weight: 700;
  margin-top: var(--section-spacing-he);
  margin-bottom: 1.5rem;
}

/* Sub-heading (H3) */
.article-body[lang="he"] h3 {
  font-family: var(--font-ui-he);
  font-size: clamp(1.125rem, 1vw + 0.75rem, 1.375rem);
  line-height: 1.4;
  font-weight: 700;
  /* Hebrew uses letter-spacing instead of text-transform for distinction */
  letter-spacing: var(--emphasis-ls-he);
  margin-top: 3rem;
  margin-bottom: 1rem;
}

/* Kicker / Category Label */
.article-kicker[lang="he"] {
  font-family: var(--font-ui-he);
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: var(--emphasis-ls-he);
  color: #c44536;                      /* Warm accent */
  margin-bottom: 1rem;
  text-align: right;
}
```

### 1.6 Hebrew Emphasis - Bold Instead of Italic

```css
/* === HEBREW EMPHASIS CONVENTIONS === */

/* In Hebrew typography, emphasis is conveyed through:
   1. Bold weight (primary)
   2. Letter-spacing / tracking (secondary)
   3. A different typeface (tertiary)
   NEVER through italic/slanted text */

.article-body[lang="he"] strong,
.article-body[lang="he"] b {
  font-weight: 700;                   /* Standard bold for emphasis */
}

/* Hebrew does NOT use italic for emphasis */
.article-body[lang="he"] em {
  font-style: normal;                 /* Override default italic */
  font-weight: 700;                   /* Use bold instead */
  /* OR use letter-spacing emphasis: */
  /* letter-spacing: var(--emphasis-ls-he); */
}

/* If you absolutely need a visual distinction beyond bold: */
.article-body[lang="he"] .emphasis-spacing {
  letter-spacing: var(--emphasis-ls-he);
  font-weight: 400;                   /* Normal weight, spaced out */
}

/* Book/person/concept names - Hebrew tradition uses spacing */
.article-body[lang="he"] cite,
.article-body[lang="he"] .name-reference {
  letter-spacing: var(--emphasis-ls-he);
}
```

---

## 2. RTL LAYOUT FOUNDATION

### 2.1 HTML Base Setup

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Preload Hebrew fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Rubik:wght@300..900&family=Frank+Ruhl+Libre:wght@300..900&display=swap" as="style">
  <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300..900&family=Frank+Ruhl+Libre:wght@300..900&display=swap" rel="stylesheet">
</head>
<body>
  <article dir="rtl" lang="he">
    <!-- Content here -->
  </article>
</body>
</html>
```

### 2.2 CSS Logical Properties - The RTL Foundation

```css
/* === RTL-SAFE CSS WITH LOGICAL PROPERTIES === */
/* These properties automatically flip for RTL - no separate RTL stylesheet needed */

/* MARGIN */
/* Instead of margin-left/right, use: */
.element {
  margin-inline-start: 1rem;          /* Right in RTL, Left in LTR */
  margin-inline-end: 2rem;            /* Left in RTL, Right in LTR */
  margin-block-start: 1rem;           /* Top (same in both) */
  margin-block-end: 2rem;             /* Bottom (same in both) */
}

/* Shorthand */
.element {
  margin-inline: 1rem 2rem;           /* start end */
  margin-block: 1rem 2rem;            /* start end */
}

/* PADDING */
.element {
  padding-inline-start: 1.5rem;
  padding-inline-end: 1.5rem;
  padding-block: 1rem 2rem;
}

/* BORDER */
.element {
  border-inline-start: 3px solid #1a1a1a;  /* Right border in RTL */
  border-inline-end: 1px solid #eee;       /* Left border in RTL */
}

/* Border radius */
.element {
  border-start-start-radius: 8px;    /* Top-right in RTL */
  border-start-end-radius: 0;        /* Top-left in RTL */
  border-end-start-radius: 8px;      /* Bottom-right in RTL */
  border-end-end-radius: 0;          /* Bottom-left in RTL */
}

/* POSITIONING */
.element {
  position: absolute;
  inset-inline-start: 0;              /* Right: 0 in RTL */
  inset-inline-end: auto;             /* Left: auto in RTL */
  inset-block-start: 1rem;            /* Top (same) */
}

/* TEXT ALIGNMENT */
.element {
  text-align: start;                   /* Right in RTL, Left in LTR */
  text-align: end;                     /* Left in RTL, Right in LTR */
}

/* FLOAT (logical) */
.element {
  float: inline-start;                 /* Float right in RTL */
  float: inline-end;                   /* Float left in RTL */
}

/* SIZE (logical) */
.element {
  inline-size: 300px;                  /* Width (horizontal in both) */
  block-size: 200px;                   /* Height */
  max-inline-size: 65ch;               /* Max-width */
}
```

### 2.3 The Editorial Grid - RTL Version

```css
/* === RTL EDITORIAL GRID === */
/* Grid and Flexbox automatically respect dir="rtl" */

.article-wrapper {
  display: grid;
  grid-template-columns:
    1fr
    min(var(--measure-he), calc(100% - 4rem))
    1fr;
  direction: rtl;
  /* Grid columns automatically start from the right in RTL */
}

/* All children center column */
.article-wrapper > * {
  grid-column: 2;
}

/* Full-bleed */
.full-bleed {
  width: 100%;
  grid-column: 1 / -1;
}

/* Wide breakout */
.wide {
  grid-column: 1 / -1;
  max-inline-size: min(90rem, 90%);
  margin-inline: auto;
}

/* Popout */
.popout {
  grid-column: 1 / -1;
  max-inline-size: min(calc(var(--measure-he) + 10rem), 90%);
  margin-inline: auto;
}
```

---

## 3. RTL-SPECIFIC EDITORIAL ELEMENTS

### 3.1 Pull Quotes - Hebrew RTL

```css
/* === HEBREW PULL QUOTES === */

/* Style 1: Centered pull quote (works identically in RTL) */
.pull-quote[lang="he"] {
  font-family: var(--font-display-he);
  font-size: clamp(1.5rem, 3vw, 2.25rem);
  line-height: 1.45;                  /* More line-height for Hebrew */
  text-align: center;
  max-inline-size: 75%;
  margin-inline: auto;
  margin-block: var(--section-spacing-he);
  padding-block: 2rem;
  border-block-start: 1px solid #1a1a1a;
  border-block-end: 1px solid #1a1a1a;
  font-weight: 700;                   /* Bold instead of italic for Hebrew */
  color: #1a1a1a;
}

.pull-quote[lang="he"] cite {
  display: block;
  font-family: var(--font-ui-he);
  font-size: 0.8rem;
  letter-spacing: var(--emphasis-ls-he);
  font-weight: 400;
  margin-block-start: 1rem;
  color: #666;
}

/* Style 2: Right-aligned editorial pull quote (Hebrew = right border) */
.pull-quote--editorial[lang="he"] {
  font-family: var(--font-display-he);
  font-size: clamp(1.5rem, 2.5vw, 2.25rem);
  line-height: 1.4;
  border-inline-start: 3px solid #1a1a1a;  /* RIGHT border in RTL */
  padding-inline-start: 1.5rem;             /* RIGHT padding in RTL */
  margin-block: 3rem;
  margin-inline-start: -2rem;               /* Negative RIGHT margin for visual weight */
  max-inline-size: 85%;
  font-weight: 700;
}

/* Style 3: Quote marks - Hebrew uses different quote marks */
.pull-quote--marks[lang="he"] {
  position: relative;
  font-family: var(--font-display-he);
  font-size: clamp(1.25rem, 2vw, 1.75rem);
  line-height: 1.6;
  max-inline-size: var(--measure-he-narrow);
  margin-inline: auto;
  margin-block: var(--section-spacing-he);
  padding-inline-start: 3rem;
  font-weight: 700;
}

.pull-quote--marks[lang="he"]::before {
  content: '\201D';                    /* Hebrew uses reversed quote marks */
  font-family: var(--font-display-he);
  font-size: 5rem;
  position: absolute;
  inset-inline-start: -0.25rem;       /* Right side in RTL */
  inset-block-start: -1rem;
  color: rgba(0, 0, 0, 0.12);
  line-height: 1;
}
```

### 3.2 Image Float in RTL

```css
/* === RTL IMAGE FLOATS === */

/* Float image to the "start" side (RIGHT in Hebrew) */
.figure--float-start {
  float: inline-start;                /* Floats RIGHT in RTL */
  inline-size: 45%;
  margin-inline-end: 2rem;            /* Space on the LEFT (text side) */
  margin-block: 0.5rem 1.5rem;
  shape-outside: margin-box;
}

/* Float image to the "end" side (LEFT in Hebrew) */
.figure--float-end {
  float: inline-end;                  /* Floats LEFT in RTL */
  inline-size: 45%;
  margin-inline-start: 2rem;          /* Space on the RIGHT (text side) */
  margin-block: 0.5rem 1.5rem;
  shape-outside: margin-box;
}

/* Important: In Hebrew editorial, floating an image to the LEFT
   (inline-end) is the equivalent of floating RIGHT in English.
   It creates the same visual rhythm of text wrapping. */

@media (max-width: 48rem) {
  .figure--float-start,
  .figure--float-end {
    float: none;
    inline-size: 100%;
    margin-inline: 0;
    margin-block: 2rem;
    shape-outside: none;
  }
}
```

### 3.3 Captions - RTL

```css
/* === RTL CAPTIONS === */

figcaption[lang="he"],
[dir="rtl"] figcaption {
  font-family: var(--font-ui-he);
  font-size: 0.8125rem;
  line-height: 1.6;
  color: #666;
  margin-block-start: 0.75rem;
  padding-block-end: 0.75rem;
  border-block-end: 1px solid #eee;
  text-align: right;                   /* Explicit for captions */
  direction: rtl;
}

figcaption[lang="he"] .credit {
  color: #999;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.03em;
}

/* Caption with right bar (RTL version of left-bar Bloomberg style) */
figcaption.caption--bar[lang="he"] {
  border-block-end: none;
  border-inline-start: 2px solid #1a1a1a;  /* RIGHT bar in RTL */
  padding-inline-start: 0.75rem;
  padding-block-end: 0;
  margin-block-start: 1rem;
}
```

### 3.4 Drop Caps in Hebrew

```css
/* === HEBREW DROP CAPS === */

/* Drop caps DO work in Hebrew, but with caveats:
   1. The ::first-letter pseudo-element correctly selects
      the rightmost letter in RTL
   2. Float direction must be inline-start (right in RTL)
   3. If niqqud (vowel marks) are present, they MUST be
      included in the drop cap styling
   4. Some Hebrew letters have descenders that need extra space */

/* Method 1: Float approach (most reliable for Hebrew) */
.article-body[lang="he"] > p:first-of-type::first-letter {
  font-family: var(--font-display-he);
  font-size: 4rem;
  float: inline-start;                /* Float RIGHT in RTL */
  line-height: 0.85;
  padding-inline-end: 0.15em;         /* Space to the LEFT of drop cap */
  padding-block-start: 0.1em;
  font-weight: 900;
  color: #1a1a1a;
}

/* Method 2: initial-letter (modern browsers) */
@supports (initial-letter: 3) {
  .article-body[lang="he"] > p:first-of-type::first-letter {
    initial-letter: 3;
    font-family: var(--font-display-he);
    font-weight: 900;
    margin-inline-end: 0.1em;
    color: #1a1a1a;
    /* Reset float fallback */
    float: none;
    font-size: unset;
    line-height: unset;
    padding: 0;
  }
}

/* For text with niqqud (vowel marks) - needs more vertical space */
.article-body[lang="he"].has-niqqud > p:first-of-type::first-letter {
  font-size: 5rem;                     /* Larger to accommodate marks */
  line-height: 0.7;
  padding-block-end: 0.2em;           /* Extra space for marks below */
}
```

### 3.5 Callout Boxes - RTL

```css
/* === RTL CALLOUT BOXES === */

.callout[lang="he"],
[dir="rtl"] .callout {
  font-family: var(--font-ui-he);
  font-size: 0.9375rem;
  line-height: 1.7;
  background: #f8f9fa;
  border-inline-start: 3px solid #1a1a1a;  /* RIGHT border in RTL */
  padding: 1.5rem 2rem;
  margin-block: var(--space-lg);
  text-align: right;
}

.callout__title[lang="he"] {
  font-weight: 700;
  font-size: 0.8125rem;
  letter-spacing: var(--emphasis-ls-he);
  margin-block-end: 0.75rem;
  color: #1a1a1a;
}

/* Sidebar that floats into LEFT margin (RTL equivalent of right margin) */
@media (min-width: 75rem) {
  .aside-box[lang="he"] {
    float: inline-end;                 /* Float LEFT in RTL */
    inline-size: 18rem;
    margin-inline-start: 2rem;         /* Space on RIGHT */
    margin-inline-end: -10rem;         /* Pull into LEFT margin */
  }
}
```

### 3.6 Footnotes & Sources - RTL

```css
/* === RTL FOOTNOTES === */

/* Footnote reference - position is the same in RTL,
   superscript is direction-independent */
[dir="rtl"] .footnote-ref {
  font-family: var(--font-ui-he);
  font-size: 0.7em;
  vertical-align: super;
  line-height: 0;
  color: #c44536;
  cursor: pointer;
  text-decoration: none;
}

/* Footnote tooltip - needs position adjustment for RTL */
[dir="rtl"] .footnote-tooltip .tooltip-content {
  /* In RTL, tooltip should open toward the left (end direction) */
  inset-inline-start: 50%;
  transform: translateX(50%) translateY(-0.5rem);  /* Reversed for RTL */
}

[dir="rtl"] .footnote-tooltip:hover .tooltip-content {
  transform: translateX(50%) translateY(0);
}

/* Source list at bottom of article */
.sources-list[lang="he"] {
  font-family: var(--font-ui-he);
  font-size: 0.875rem;
  line-height: 1.6;
  border-block-start: 1px solid #ddd;
  padding-block-start: 2rem;
  margin-block-start: var(--section-spacing-he);
}

.sources-list[lang="he"] li {
  margin-block-end: 0.5rem;
  padding-inline-start: 1.5rem;
  position: relative;
}

.sources-list[lang="he"] li::before {
  content: counter(source-counter) '.';
  position: absolute;
  inset-inline-start: 0;              /* Right-aligned number in RTL */
  font-weight: 700;
}
```

---

## 4. BIDI (BIDIRECTIONAL) TEXT HANDLING

### 4.1 Mixed Hebrew/English Content

```css
/* === BIDI TEXT HANDLING === */

/* The Unicode Bidirectional Algorithm (UBA) handles most
   mixed text automatically, but you need to help it sometimes */

/* Base direction for the article */
.article-body[lang="he"] {
  direction: rtl;
  unicode-bidi: plaintext;            /* Let UBA handle inline bidi */
}

/* Inline English terms within Hebrew text */
/* Usually handled automatically by the browser's bidi algorithm.
   For example: "הגישה של Somatic Experiencing מציעה..."
   The "Somatic Experiencing" will automatically display LTR
   within the RTL flow. */

/* When you need to force direction on a span: */
.ltr-inline {
  direction: ltr;
  unicode-bidi: isolate;              /* Isolate prevents bidi leakage */
  display: inline;
}

.rtl-inline {
  direction: rtl;
  unicode-bidi: isolate;
  display: inline;
}

/* For isolated bidi content (prevents context from affecting it) */
.bdi {
  unicode-bidi: isolate;              /* Same as <bdi> element */
}

/* Override for when auto-detection gets it wrong */
.bidi-override {
  unicode-bidi: bidi-override;        /* Force direction regardless of content */
}
```

### 4.2 Common Bidi Patterns in Therapy/Wellness Content

```html
<!-- Pattern: Hebrew sentence with English term -->
<p dir="rtl" lang="he">
  הגישה של <span lang="en">Somatic Experiencing</span> מציעה דרך
  ייחודית לעבודה עם הגוף.
</p>
<!-- The browser handles this correctly with UBA -->

<!-- Pattern: Hebrew with English name and Hebrew continuation -->
<p dir="rtl" lang="he">
  <bdi lang="en">Peter Levine</bdi> פיתח את הגישה בשנות ה-70.
</p>
<!-- Use <bdi> to isolate the English name -->

<!-- Pattern: Mixed paragraph with URLs or technical terms -->
<p dir="rtl" lang="he">
  ניתן לקרוא עוד באתר
  <a href="..." dir="ltr"><bdi>www.example.com</bdi></a>.
</p>
<!-- URLs must be LTR with isolation -->

<!-- Pattern: Parenthetical English within Hebrew -->
<p dir="rtl" lang="he">
  טראומה (<bdi lang="en">Trauma</bdi>) היא תגובה
  טבעית של מערכת העצבים.
</p>
<!-- Parentheses can be tricky with bidi - use <bdi> -->

<!-- Pattern: Hebrew quotation with English source -->
<blockquote dir="rtl" lang="he">
  <p>"הגוף שומר את הניקוד"</p>
  <cite dir="ltr" lang="en">
    <bdi>Bessel van der Kolk, "The Body Keeps the Score"</bdi>
  </cite>
</blockquote>
```

### 4.3 CSS for Bidi-Safe Typography

```css
/* === BIDI-SAFE TYPOGRAPHY === */

/* Links in mixed content */
[dir="rtl"] a[href] {
  unicode-bidi: isolate;
  /* Prevents URL from breaking the bidi context */
}

/* Numbers in Hebrew text */
/* Arabic numerals (1, 2, 3) are naturally LTR even in RTL text.
   The UBA handles them correctly. No special CSS needed. */

/* Phone numbers, dates, prices */
[dir="rtl"] .number,
[dir="rtl"] .phone,
[dir="rtl"] .date,
[dir="rtl"] .price {
  unicode-bidi: isolate;
  direction: ltr;
  display: inline;
}

/* Punctuation handling */
/* Parentheses (), brackets [], and quotes "" automatically
   mirror in RTL. The UBA handles this.
   However, for nested mixed content, explicit marks help: */

/* When mixing quote styles */
[dir="rtl"] q {
  quotes: '\201D' '\201C' '\2019' '\2018';
  /* Hebrew: closing quote first (right side), opening second (left side) */
  /* Renders as: "text" with correct visual order */
}

/* Article meta with mixed date formats */
.article-meta[lang="he"] {
  direction: rtl;
  unicode-bidi: plaintext;
}

.article-meta[lang="he"] time {
  unicode-bidi: isolate;
  /* Keeps "15 Feb 2026" or "15.2.2026" correctly ordered */
}
```

---

## 5. RTL NAVIGATION & ARTICLE META

### 5.1 Article Header - Hebrew

```css
/* === HEBREW ARTICLE HEADER === */

.article-header[lang="he"] {
  text-align: right;
  direction: rtl;
  margin-block-end: var(--space-xl);
}

/* Reading time and meta info */
.article-meta[lang="he"] {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
  font-family: var(--font-ui-he);
  font-size: 0.875rem;
  color: #666;
  direction: rtl;
  /* Flexbox auto-reverses in RTL - items flow right-to-left */
}

.article-meta[lang="he"] .separator {
  color: #ddd;
}

/* Author info */
.article-meta[lang="he"] .author {
  font-weight: 700;
  color: #1a1a1a;
}
```

### 5.2 Navigation Elements

```css
/* === RTL NAVIGATION === */

/* Breadcrumb - separator direction reverses */
.breadcrumb[dir="rtl"] {
  display: flex;
  gap: 0.5rem;
  font-family: var(--font-ui-he);
  font-size: 0.8125rem;
}

.breadcrumb[dir="rtl"] .separator {
  /* Arrow points LEFT in RTL (toward next item) */
  transform: scaleX(-1);              /* Flip arrow icon */
}

/* Or use CSS logical approach: */
.breadcrumb[dir="rtl"] .separator::after {
  content: '\203A';                    /* > character */
  transform: scaleX(-1);              /* Becomes < in RTL */
}

/* Back button / link */
[dir="rtl"] .back-link svg,
[dir="rtl"] .back-link .arrow {
  transform: scaleX(-1);              /* Arrow points RIGHT in RTL (= "back") */
}

/* Reading progress bar - must reverse direction */
[dir="rtl"] .progress-bar {
  transform-origin: right;            /* Grows from RIGHT in RTL */
}

@keyframes progressBarRTL {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

### 5.3 Table of Contents - Sidebar

```css
/* === RTL TABLE OF CONTENTS === */

.toc[dir="rtl"] {
  position: sticky;
  inset-block-start: 2rem;
  font-family: var(--font-ui-he);
  font-size: 0.875rem;
  line-height: 1.6;
  text-align: right;
}

.toc__item[dir="rtl"] {
  padding-inline-start: 1rem;
  border-inline-start: 2px solid transparent;
  transition: border-color 0.2s ease;
}

.toc__item--active[dir="rtl"] {
  border-inline-start-color: #1a1a1a;  /* Active indicator on RIGHT */
  font-weight: 700;
}
```

---

## 6. RESPONSIVE RTL TYPOGRAPHY

### 6.1 Fluid Hebrew Typography Scale

```css
/* === RESPONSIVE HEBREW TYPE === */

/* Mobile-first approach */
:root {
  /* Mobile */
  --body-size-he: 1.0625rem;          /* 17px - mobile minimum for Hebrew */
  --body-lh-he: 1.75;
  --h1-size-he: 2rem;
  --h2-size-he: 1.5rem;
  --h3-size-he: 1.125rem;
}

/* Tablet (48rem / 768px) */
@media (min-width: 48rem) {
  :root {
    --body-size-he: 1.25rem;           /* 20px */
    --h1-size-he: 2.5rem;
    --h2-size-he: 1.75rem;
  }
}

/* Desktop (64rem / 1024px) */
@media (min-width: 64rem) {
  :root {
    --body-size-he: 1.375rem;          /* 22px */
    --body-lh-he: 1.85;
    --h1-size-he: 3.25rem;
    --h2-size-he: 2.125rem;
    --h3-size-he: 1.25rem;
  }
}

/* Large desktop (90rem / 1440px) */
@media (min-width: 90rem) {
  :root {
    --body-size-he: 1.4375rem;         /* 23px */
    --h1-size-he: 3.75rem;
    --h2-size-he: 2.375rem;
  }
}

/* Alternative: fluid with clamp */
.article-body[lang="he"] {
  font-size: clamp(1.0625rem, 0.6vw + 0.9rem, 1.4375rem);
  /* Smoothly 17px to 23px */
}
```

### 6.2 Mobile RTL Adjustments

```css
/* === MOBILE RTL === */

@media (max-width: 48rem) {
  .article-wrapper[dir="rtl"] {
    padding-inline: 1.25rem;
    grid-template-columns: 0 minmax(0, 1fr) 0;
  }

  /* Full-bleed images extend beyond padding */
  [dir="rtl"] .full-bleed {
    margin-inline: -1.25rem;
    inline-size: calc(100% + 2.5rem);
  }

  /* Pull quotes more compact */
  [dir="rtl"] .pull-quote {
    font-size: 1.25rem;
    max-inline-size: 100%;
    padding-block: 1.5rem;
  }

  /* Callout boxes extend to edges */
  [dir="rtl"] .callout {
    margin-inline: -1.25rem;
    padding: 1.5rem;
  }

  /* Drop cap smaller on mobile */
  .article-body[lang="he"] > p:first-of-type::first-letter {
    font-size: 3rem;
  }
}
```

---

## 7. COMPLETE HTML STRUCTURE - HEBREW EDITORIAL ARTICLE

```html
<!-- === HEBREW EDITORIAL ARTICLE STRUCTURE === -->

<article class="article-wrapper" dir="rtl" lang="he">

  <!-- Article Header -->
  <header class="article-header" lang="he">
    <span class="article-kicker">סומטיקה ותרפיה</span>
    <h1 class="article-title">הגוף כמפה של החוויה</h1>
    <p class="article-deck">
      כשאנחנו מפסיקים לחפש תשובות בראש ומתחילים
      להקשיב לגוף - משהו משתנה. על הקשר בין
      תנועה, מגע ושחרור רגשי.
    </p>
    <div class="article-meta" lang="he">
      <span class="author">ירון אמור</span>
      <span class="separator">/</span>
      <time datetime="2026-02-15">15 בפברואר 2026</time>
      <span class="separator">/</span>
      <span class="read-time">קריאה של 8 דקות</span>
    </div>
  </header>

  <!-- Hero Image -->
  <figure class="figure--full-bleed">
    <picture>
      <source media="(max-width: 48rem)" srcset="hero-mobile.jpg">
      <img src="hero-desktop.jpg" alt="ידיים על גב, טיפול סומטי" loading="eager">
    </picture>
    <figcaption lang="he">
      רגע של שקט בתוך סשן.
      <span class="credit">צילום: שם הצלם</span>
    </figcaption>
  </figure>

  <!-- Article Body -->
  <div class="article-body" lang="he">

    <!-- Opening paragraph with drop cap -->
    <p>יש רגע בטיפול שבו הגוף מתחיל לדבר. לא במילים,
    אלא בשפה שקדמה למילים - תנועה קטנה ביד, נשימה
    שמשתחררת, רטט עדין שעובר דרך הרגליים.</p>

    <p>פיטר לוין, מייסד גישת
    <bdi lang="en">Somatic Experiencing</bdi>,
    הבין שטראומה לא חיה בסיפור שאנחנו מספרים
    לעצמנו - היא חיה בגוף.</p>

    <!-- Section heading -->
    <h2>הגוף זוכר מה שהראש שוכח</h2>

    <p>תוכן ממשיך כאן...</p>

    <!-- Pull quote -->
    <blockquote class="pull-quote" lang="he">
      <p>הגוף לא משקר. הוא לא יודע לספר סיפורים -
      הוא יודע רק להרגיש.</p>
    </blockquote>

    <p>עוד טקסט גוף...</p>

    <!-- Image within text flow -->
    <figure>
      <img src="inline-image.jpg"
           alt="תרגול תנועה בקבוצה"
           loading="lazy">
      <figcaption class="caption--bar" lang="he">
        תרגול תנועה אותנטית בסדנה.
      </figcaption>
    </figure>

    <!-- Callout box -->
    <aside class="callout" lang="he">
      <span class="callout__title">נקודה למחשבה</span>
      <p>מחקרים מראים שהגוף מגיב לטראומה ב-0.5 שניות
      לפני שהמוח המודע מזהה את האיום.
      המערכת הסומטית מהירה יותר מהמילים.</p>
    </aside>

    <!-- Mixed bidi content example -->
    <p>בספרו הפורץ דרך
    <bdi lang="en">"The Body Keeps the Score"</bdi>,
    ד"ר <bdi lang="en">Bessel van der Kolk</bdi>
    מתאר כיצד הגוף מאחסן זיכרונות שהתודעה
    אינה מסוגלת להכיל.</p>

    <!-- Section break -->
    <div class="section-break" role="separator"></div>

    <h2>מהגוף אל התודעה</h2>

    <p>תוכן ממשיך...</p>

  </div>

  <!-- Wide image pair -->
  <div class="figure-pair wide">
    <figure>
      <img src="pair-1.jpg" alt="..." loading="lazy">
      <figcaption lang="he">כיתוב תמונה ראשונה</figcaption>
    </figure>
    <figure>
      <img src="pair-2.jpg" alt="..." loading="lazy">
      <figcaption lang="he">כיתוב תמונה שנייה</figcaption>
    </figure>
  </div>

  <!-- Statistics -->
  <aside class="callout--stat" lang="he">
    <span class="stat-number">85%</span>
    <span class="stat-label">מהמטופלים מדווחים על שיפור
    משמעותי תוך 6 סשנים של טיפול סומטי</span>
  </aside>

  <div class="article-body" lang="he">
    <p>טקסט מסכם...</p>
  </div>

</article>
```

---

## 8. QUICK REFERENCE: HEBREW vs LATIN VALUES

| Property | Latin (from companion doc) | Hebrew RTL | Why Different |
|----------|---------------------------|------------|---------------|
| Body font-size (mobile) | 17-18px | 19px | Hebrew characters visually smaller at same px |
| Body font-size (desktop) | 20-21px | 22-23px | Same reason, proportional increase |
| Line-height | 1.65 | 1.8 | Hebrew taller x-height, potential niqqud |
| Line-height with niqqud | n/a | 2.0 | Vowel marks need vertical space |
| Measure (line length) | 65ch | 60ch | Hebrew chars wider, fewer per line |
| Letter-spacing body | 0.01em | normal | Hebrew doesn't need tracking for body |
| Emphasis method | italic | bold or letter-spacing (0.08em) | Hebrew typography convention |
| text-transform: uppercase | yes | no | Hebrew has no case distinction |
| Hyphenation | hyphens: auto | hyphens: none | Poor browser support, not tradition |
| Paragraph spacing | 1.5em | 1.75em | More generous for reading rhythm |
| Drop cap float | float: left | float: inline-start | Logical property for RTL |
| Pull quote border | border-left | border-inline-start | Maps to RIGHT in RTL |
| Image float (wrap) | float: left/right | float: inline-start/end | Logical properties |
| Caption alignment | text-align: left | text-align: right (or: start) | Follows reading direction |
| Quote marks | \201C / \201D | \201D / \201C | Hebrew mirrors quote direction |
| Callout border side | left | inline-start (right in RTL) | Visual weight on reading-entry side |
| Progress bar origin | transform-origin: left | transform-origin: right | Growth follows reading direction |

---

## 9. ISRAELI EDITORIAL SITE PATTERNS

### Haaretz (haaretz.co.il)
- **Font system:** Open Sans (brand font via CSS custom property `--font-brand`)
- **Approach:** Variable weights of a single font family across the site
- **Dark mode:** Full dark mode support via `data-theme="dark"` attribute
- **Custom typography:** Commissioned "Meah Sans" (Shavit Yaakov) for centennial brand identity
- **Grid:** Next.js-based component system, responsive semantic HTML
- **Lesson:** Israeli premium editorial uses clean sans-serif more than serif - differs from Western editorial tradition

### General Israeli Editorial Pattern
- Sans-serif dominates Israeli digital editorial (unlike Western serif tradition)
- Typography tends toward larger sizes than Western equivalents
- Bold is used far more than italic for hierarchy
- Whitespace and breathing room is generous
- Mixed Hebrew/English content is extremely common (therapy terms, names, brands)

---

## 10. PERFORMANCE: HEBREW FONT LOADING

```css
/* === HEBREW FONT LOADING STRATEGY === */

/* Preload the primary Hebrew font */
/*
<link rel="preload"
      href="https://fonts.gstatic.com/s/rubik/v28/..."
      as="font"
      type="font/woff2"
      crossorigin>
*/

/* Font-face with unicode-range for Hebrew subset */
@font-face {
  font-family: 'Rubik';
  src: url('/fonts/rubik-hebrew.woff2') format('woff2');
  font-weight: 300 900;
  font-display: swap;
  /* Hebrew unicode range */
  unicode-range: U+0590-05FF,         /* Hebrew block */
                 U+FB1D-FB4F,         /* Hebrew presentation forms */
                 U+200C-200D,         /* Zero-width joiners */
                 U+25CC;              /* Dotted circle (for marks) */
}

/* Separate Latin subset for mixed content */
@font-face {
  font-family: 'Rubik';
  src: url('/fonts/rubik-latin.woff2') format('woff2');
  font-weight: 300 900;
  font-display: swap;
  unicode-range: U+0000-00FF,         /* Basic Latin */
                 U+0100-024F,         /* Latin Extended */
                 U+2000-206F;         /* General punctuation */
}

/* Fallback chain for Hebrew */
/* System fonts that support Hebrew, in quality order: */
.hebrew-fallback {
  font-family:
    'Rubik',                           /* Primary */
    'Heebo',                           /* Google fallback */
    'Arial Hebrew',                    /* macOS */
    'Segoe UI',                        /* Windows */
    'Noto Sans Hebrew',                /* Android/Linux */
    sans-serif;
}
```

---

## SOURCES

- [W3C Hebrew Layout Requirements (hlreq)](https://w3c.github.io/hlreq/)
- [W3C Hebrew Gap Analysis](https://www.w3.org/International/hlreq/gap-analysis/)
- [RTL Styling 101 - Ahmad Shadeed](https://rtlstyling.com/posts/rtl-styling/)
- [CSS Logical Properties - Ahmad Shadeed](https://ishadeed.com/article/css-logical-properties/)
- [CSS Logical Properties Guide - SitePoint](https://www.sitepoint.com/css-logical-properties-guide/)
- [CSS Direction Property - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
- [Working with Bidirectional Text - W3C](https://www.w3.org/International/questions/qa-html-dir)
- [Structural Markup and RTL Text - W3C](https://www.w3.org/International/questions/qa-html-dir)
- [Frank Ruhl Libre - Google Fonts](https://fonts.google.com/specimen/Frank+Ruhl+Libre)
- [Heebo - Google Fonts](https://fonts.google.com/specimen/Heebo)
- [Rubik - Google Fonts](https://fonts.google.com/specimen/Rubik?subset=hebrew)
- [Noto Sans Hebrew - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans+Hebrew)
- [Noto Serif Hebrew - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Serif+Hebrew)
- [AlefAlefAlef - Hebrew Typography Foundry](https://alefalefalef.co.il/en/)
- [Israeli Font Designers - AlefAlefAlef](https://alefalefalef.co.il/en/israeli-font-designers3/)
- [OpenType Features in Hebrew - AlefAlefAlef](https://alefalefalef.co.il/en/opentype-features/)
- [CSS initial-letter for Drop Caps - Chrome Developers](https://developer.chrome.com/blog/control-your-drop-caps-with-css-initial-letter)
- [CSS Logical Properties - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding)
- [CSS-Tricks RTL Styling 101](https://css-tricks.com/rtl-styling-101/)
- [Font Size Guidelines for Responsive Websites - Learn UI Design](https://www.learnui.design/blog/mobile-desktop-website-font-size-guidelines.html)
- [The Ideal Line Length & Line Height - Pimp My Type](https://pimpmytype.com/line-length-line-height/)
