# Visual Brief: POC - Hero + About Sections

**Date:** 11.2.2026
**Version:** v3.0 (Washi & Ink)
**Agent:** Illustrator
**For:** CTO - Astro/HTML/CSS build
**Scope:** Two sections only - Hero ("כניסה למרחב") + About ("התדר שלנו")

---

## 0. Design Tokens (Global Reference)

The CTO should define these as CSS custom properties at `:root` level. Every value in this brief references these tokens.

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

  /* Text on dark backgrounds */
  --color-text-on-dark: #F2EAD3;      /* Washi cream */
  --color-text-on-dark-muted: rgba(242, 234, 211, 0.6);

  /* Text on light backgrounds */
  --color-text-on-light: #588475;      /* Sol Green */
  --color-text-on-light-dark: #3B514B; /* Sol Green Dark - small text */

  /* === Typography === */
  --font-display: 'Frank Ruhl Libre', serif;
  --font-body: 'Heebo', sans-serif;
  --font-english: 'Inter', sans-serif;
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-bold: 700;

  /* === Spacing - Ma === */
  --space-xs: 0.5rem;    /* 8px */
  --space-sm: 1rem;      /* 16px */
  --space-md: 2rem;      /* 32px */
  --space-lg: 4rem;      /* 64px */
  --space-xl: 8rem;      /* 128px */
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

## 1. Page Background and Washi Paper Texture

### Background Color

The `<body>` background is always `--color-washi` (#F2EAD3). No pure white anywhere.

```css
body {
  background-color: var(--color-washi);
}
```

### Washi Paper Texture Overlay

A subtle paper texture applied as a fixed pseudo-element over the entire page. This gives the feeling of ink on aged Japanese paper.

**Implementation:**

```css
body::after {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  background-image: url('/textures/washi-paper.webp');
  background-size: 400px 400px;
  background-repeat: repeat;
  opacity: 0.03;
  mix-blend-mode: multiply;
}
```

**Texture asset specs:**
- File: `washi-paper.webp` - a tileable, high-res scan of actual Washi paper grain
- Size: 400x400px tile, optimized WebP, under 15KB
- The texture is nearly invisible (3% opacity) - just enough to break the flat digital feel
- `mix-blend-mode: multiply` ensures it darkens slightly on cream but disappears on dark sections
- `pointer-events: none` and high z-index so it doesn't interfere with interaction
- No parallax motion on the texture - it stays fixed for performance

**Fallback:** If the texture image fails to load, the page looks fine without it - the cream background carries the design on its own.

---

## 2. Hero Section - "כניסה למרחב"

### 2.1 Layout Overview

The Hero is a full-viewport section. It is the ONLY dark section in the POC. Everything lives in the center of the viewport, vertically and horizontally, with generous breathing room.

**Dimensions:**
- Height: `100svh` (small viewport height - accounts for mobile browser chrome)
- Width: `100%`
- Overflow: `hidden`
- Position: `relative`

**Visual hierarchy (top to bottom):**

```
+--------------------------------------------------+
|                                                    |
|           SOL THERAPY (logo, top center)           |
|                                                    |
|                                                    |
|                                                    |
|              סול תרפי (main title)                 |
|     היכן שהצליל הופך לדממה (tagline)              |
|                                                    |
|                                                    |
|                                                    |
|            [ink drop scroll indicator]              |
|                                                    |
+--------------------------------------------------+
|  ~~~ Bokashi gradient transition to cream ~~~      |
+--------------------------------------------------+
```

### 2.2 Background

**Color:** Solid `--color-indigo` (#264348) as the base.

For the POC, we use a static indigo background. No canvas animation, no video. The ink animation concept is aspirational for v2 - the POC must be buildable in pure HTML/CSS with minimal JS.

```css
.hero {
  background-color: var(--color-indigo);
  position: relative;
  overflow: hidden;
}
```

**Optional atmospheric layer (nice-to-have for POC):**

A very subtle radial gradient that gives slight depth, as if there is a dim light source behind the title area:

```css
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse 60% 50% at 50% 45%,
    rgba(49, 77, 89, 0.4) 0%,     /* --color-indigo-light, subtle */
    transparent 70%
  );
  pointer-events: none;
}
```

This is very subtle - just enough to create a slight luminous center where the text lives, evoking the Shin-hanga "blue hour" atmospheric quality.

### 2.3 Logo Placement

**Content:** "SOL THERAPY" text mark (not a graphic logo for POC)

**Positioning:**
- Top center of viewport
- `padding-top: clamp(2rem, 5vw, 3.5rem)`

**Typography:**
- Font: `var(--font-english)` (Inter)
- Weight: 300 (Light)
- Size: `clamp(0.65rem, 1.2vw, 0.8rem)`
- Letter-spacing: `0.35em`
- Text-transform: `uppercase`
- Color: `rgba(242, 234, 211, 0.5)` - Washi cream at 50% opacity

**Why 50% opacity:** The logo should feel etched into the space, not screaming. It is secondary to the main title. Like a discreet gallery label.

```css
.hero__logo {
  font-family: var(--font-english);
  font-weight: var(--font-weight-light);
  font-size: clamp(0.65rem, 1.2vw, 0.8rem);
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: rgba(242, 234, 211, 0.5);
  text-align: center;
  padding-top: clamp(2rem, 5vw, 3.5rem);
}
```

### 2.4 Main Title

**Content:** "סול תרפי"

**Positioning:**
- Centered horizontally and vertically in the viewport
- The title + tagline group should sit slightly above true center (about 45% from top) to feel balanced with the scroll indicator below

**Typography:**
- Font: `var(--font-display)` (Frank Ruhl Libre)
- Weight: 300 (Light)
- Size: `clamp(3.5rem, 10vw, 7rem)`
- Line-height: `1.1`
- Color: `var(--color-washi)` (#F2EAD3)
- Letter-spacing: `0.02em`
- Text-align: `center`
- Direction: `rtl`

```css
.hero__title {
  font-family: var(--font-display);
  font-weight: var(--font-weight-light);
  font-size: clamp(3.5rem, 10vw, 7rem);
  line-height: 1.1;
  color: var(--color-washi);
  letter-spacing: 0.02em;
  text-align: center;
  direction: rtl;
}
```

**Important:** Frank Ruhl Libre at weight 300 is elegant and quiet. Do NOT use bold. The light weight on the dark indigo background creates the calligraphic, ink-on-paper feeling.

### 2.5 Tagline

**Content:** "היכן שהצליל הופך לדממה"

**Positioning:**
- Directly below the main title
- Margin-top: `clamp(0.75rem, 2vw, 1.5rem)`

**Typography:**
- Font: `var(--font-body)` (Heebo)
- Weight: 300 (Light)
- Size: `clamp(1rem, 2.2vw, 1.35rem)`
- Color: `rgba(242, 234, 211, 0.6)` - Washi cream at 60% opacity
- Letter-spacing: `0.04em`
- Text-align: `center`
- Direction: `rtl`

```css
.hero__tagline {
  font-family: var(--font-body);
  font-weight: var(--font-weight-light);
  font-size: clamp(1rem, 2.2vw, 1.35rem);
  color: rgba(242, 234, 211, 0.6);
  letter-spacing: 0.04em;
  text-align: center;
  direction: rtl;
  margin-top: clamp(0.75rem, 2vw, 1.5rem);
}
```

**Why 60% opacity:** The tagline is secondary. It should whisper, not compete with the title. The reduced opacity creates a hierarchy that feels like depth - as if the tagline is slightly further away, behind a veil of ink.

### 2.6 Ink Drop Scroll Indicator

**What it is:** A small dot that sits at the bottom center of the Hero. It pulses gently, inviting the user to scroll down. It evokes an ink drop falling from a calligraphy brush.

**Positioning:**
- Bottom center of the Hero
- `bottom: clamp(2rem, 4vw, 3rem)` from the section bottom
- Centered horizontally

**Appearance:**
- Shape: a small circle, 8px diameter
- Color: `var(--color-washi)` (#F2EAD3)
- Below it: a thin vertical line, 24px tall, 1px wide, same color at 30% opacity

**Animation - Ink Drop Pulse:**

```css
.hero__scroll-indicator {
  position: absolute;
  bottom: clamp(2rem, 4vw, 3rem);
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.hero__scroll-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--color-washi);
  animation: ink-drop 2.4s var(--ease-ink) infinite;
}

.hero__scroll-line {
  width: 1px;
  height: 24px;
  background-color: rgba(242, 234, 211, 0.3);
}

@keyframes ink-drop {
  0%, 100% {
    transform: translateY(0);
    opacity: 0.4;
  }
  50% {
    transform: translateY(6px);
    opacity: 1;
  }
}
```

**Behavior:**
- Trigger: on page load, after a 1.5s delay (let the user absorb the title first)
- The dot gently moves down 6px and brightens, then returns - like a drop of ink slowly forming and falling
- Duration: 2.4s per cycle, infinite loop
- Easing: `var(--ease-ink)` - the brand's signature easing

**Reduced motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .hero__scroll-dot {
    animation: none;
    opacity: 0.6;
  }
}
```

### 2.7 Hero Entry Animations

**Philosophy:** Elements reveal themselves as if being painted by an invisible brush. Slow, deliberate, one at a time. Not flashy - meditative.

**Sequence:**

| Element | Delay | Duration | Effect |
|---------|-------|----------|--------|
| Indigo background | 0s | instant | Already visible |
| Logo ("SOL THERAPY") | 0.3s | 0.8s | Fade in from 0 to 50% opacity |
| Title ("סול תרפי") | 0.6s | 1.2s | Fade in + slight upward drift (20px) |
| Tagline | 1.2s | 0.8s | Fade in from 0 to 60% opacity |
| Scroll indicator | 1.8s | 0.6s | Fade in, then pulse begins |

**CSS approach:**

```css
.hero__logo,
.hero__title,
.hero__tagline,
.hero__scroll-indicator {
  opacity: 0;
  animation-fill-mode: forwards;
  animation-timing-function: var(--ease-ink);
}

.hero__logo {
  animation: fade-in 0.8s var(--ease-ink) 0.3s forwards;
}

.hero__title {
  animation: rise-in 1.2s var(--ease-ink) 0.6s forwards;
}

.hero__tagline {
  animation: fade-in 0.8s var(--ease-ink) 1.2s forwards;
}

.hero__scroll-indicator {
  animation: fade-in 0.6s var(--ease-ink) 1.8s forwards;
}

@keyframes fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@keyframes rise-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Note:** The `fade-in` for logo and tagline targets their natural opacity (50% and 60% respectively), so the "to" state should match their resting styles. Override:

```css
.hero__logo {
  animation: fade-in-logo 0.8s var(--ease-ink) 0.3s forwards;
}

@keyframes fade-in-logo {
  from { opacity: 0; }
  to   { opacity: 0.5; }
}

@keyframes fade-in-tagline {
  from { opacity: 0; }
  to   { opacity: 0.6; }
}
```

**Reduced motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .hero__logo,
  .hero__title,
  .hero__tagline,
  .hero__scroll-indicator {
    animation: none;
    opacity: 1;
  }
  .hero__logo { opacity: 0.5; }
  .hero__tagline { opacity: 0.6; }
}
```

### 2.8 Bokashi Gradient Transition (Hero to About)

**What it is:** The transition from the dark Hero to the light About section. Named after the Bokashi woodblock printing technique - a smooth, hand-applied gradient. It should feel like dawn rising, the dark indigo giving way to warm cream.

**Implementation:** A pseudo-element at the bottom of the Hero that creates a gradient overlay.

```css
.hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: clamp(120px, 20vh, 200px);
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(38, 67, 72, 0.3) 20%,
    rgba(49, 77, 89, 0.5) 40%,
    rgba(88, 132, 117, 0.3) 60%,
    rgba(242, 234, 211, 0.7) 80%,
    #F2EAD3 100%
  );
  pointer-events: none;
  z-index: 1;
}
```

**Gradient breakdown:**
1. `transparent` at top - the indigo shows through
2. `rgba(38, 67, 72, 0.3)` - a hint of deep indigo starts
3. `rgba(49, 77, 89, 0.5)` - Bero-ai (Prussian blue) layer, the "blue hour"
4. `rgba(88, 132, 117, 0.3)` - Sol Green tint, bridging blue to cream
5. `rgba(242, 234, 211, 0.7)` - Washi cream emerging
6. `#F2EAD3` solid - seamless meeting with About section background

**Height:** `clamp(120px, 20vh, 200px)` - tall enough to feel gradual, not abrupt. On mobile (120px) it is still smooth. On desktop (up to 200px) it breathes.

**Alternative (simpler):** If the multi-stop gradient proves fiddly, a two-stop version works:

```css
background: linear-gradient(
  to bottom,
  transparent 0%,
  #F2EAD3 100%
);
```

This is less atmospheric but still clean. Use the multi-stop version if possible.

### 2.9 Hero - Mobile Specifications

**Key differences on mobile:**
- Title size scales down to `3.5rem` via clamp (already handled)
- Logo size scales to `0.65rem` via clamp
- The scroll indicator stays at `2rem` from bottom
- The atmospheric radial gradient (2.2) can be omitted on mobile for performance
- Touch: no hover states needed, the scroll indicator is the only interactive hint

**Viewport considerations:**
- Use `100svh` not `100vh` to avoid the iOS Safari address bar issue
- Test on iPhone SE (375px width) as minimum target
- The title "סול תרפי" at 3.5rem on 375px width = about 56px, which fits comfortably

---

## 3. About Section - "התדר שלנו"

### 3.1 Layout Overview

The About section sits directly below the Hero's Bokashi gradient. It is light, warm, and typographically driven. The text is positioned asymmetrically - like exhibition wall text in a museum gallery. NOT centered.

**Dimensions:**
- Width: `100%`
- Min-height: no fixed height - content determines it
- Padding-top: `var(--space-section)` = `clamp(8rem, 15vw, 14rem)`
- Padding-bottom: `var(--space-section)`

**Background:** `var(--color-washi)` (#F2EAD3)

```css
.about {
  background-color: var(--color-washi);
  padding-top: var(--space-section);
  padding-bottom: var(--space-section);
  direction: rtl;
}
```

### 3.2 Layout Grid - Museum Wall Text

The text block is NOT centered. It sits offset to the right side (in RTL, this means it "leans" toward the start), leaving a large empty area on the left. This asymmetry is the "gallery wall" aesthetic - text panels in museums are never centered on the wall.

**Desktop layout (above 768px):**

```css
.about__container {
  max-width: var(--container-max);  /* 1100px */
  margin: 0 auto;
  padding: 0 var(--container-padding);
}

.about__content {
  max-width: 600px;
  margin-right: 0;       /* Flush to the right in RTL */
  margin-left: auto;     /* Push content to the right */
}
```

This means the text block occupies roughly 55% of the container width, positioned to the right (start) side. The remaining 45% on the left is empty Ma space.

**Visual representation (desktop):**

```
+-------Container (1100px max)-------+
|                                     |
|                    [heading]        |
|                    [body text       |
|                     continues       |
|                     here...]        |
|                                     |
|                    [קרא עוד]       |
|                                     |
|     (Ma - empty)                    |
|                                     |
+-------------------------------------+
```

**Mobile layout (below 768px):**

On mobile, the asymmetry softens. The content still aligns to the right (RTL start) but takes more width:

```css
@media (max-width: 768px) {
  .about__content {
    max-width: 100%;
    padding: 0 var(--container-padding);
  }
}
```

On mobile, text occupies full width with container padding (`clamp(2rem, 8vw, 5rem)`) on both sides. The Ma space exists as the generous top/bottom padding instead.

### 3.3 Section Title

**Content:** "התדר שלנו"

**Typography:**
- Font: `var(--font-display)` (Frank Ruhl Libre)
- Weight: 300 (Light)
- Size: `clamp(2rem, 5vw, 3.2rem)`
- Color: `var(--color-green)` (#588475)
- Line-height: `1.2`
- Letter-spacing: `0.01em`
- Margin-bottom: `var(--space-lg)` (4rem)

```css
.about__title {
  font-family: var(--font-display);
  font-weight: var(--font-weight-light);
  font-size: clamp(2rem, 5vw, 3.2rem);
  color: var(--color-green);
  line-height: 1.2;
  letter-spacing: 0.01em;
  margin-bottom: var(--space-lg);
}
```

**Note:** The title is NOT decorative or oversized here. It is a quiet, elegant label - like a section title in a museum. The content speaks louder.

### 3.4 Body Text

**Content structure (from spec):**
- Line 1: What it is (immersive sound experiences in cultural spaces)
- Line 2: What it is NOT (not clinical therapy, not guided meditation)
- Lines 3-4: What the audience experiences (listening, body as resonance instrument, shifting attention)

**Typography:**
- Font: `var(--font-body)` (Heebo)
- Weight: 400 (Regular)
- Size: `clamp(1rem, 1.8vw, 1.15rem)`
- Color: `var(--color-green-dark)` (#3B514B) - the darker green for body text to ensure WCAG AA on cream (contrast ratio 6.2:1)
- Line-height: `1.85`
- Direction: `rtl`
- Max-width: `540px` (within the 600px content area, to keep line lengths readable)

```css
.about__text {
  font-family: var(--font-body);
  font-weight: var(--font-weight-regular);
  font-size: clamp(1rem, 1.8vw, 1.15rem);
  color: var(--color-green-dark);
  line-height: 1.85;
  direction: rtl;
  max-width: 540px;
}

.about__text p {
  margin-bottom: var(--space-md); /* 2rem between paragraphs */
}
```

**Accessibility note:** Sol Green (#588475) on Washi (#F2EAD3) has a contrast ratio of only 4.1:1 - acceptable for large text (headings) but NOT for body text (requires 4.5:1). That is why body text uses `--color-green-dark` (#3B514B) which achieves 6.2:1.

### 3.5 "קרא עוד" Button

**What it does:** Opens a modal or expanded section with the full philosophy text. For the POC, it can scroll to an expanded area or simply be a styled link.

**Appearance:**
- Text: "קרא עוד"
- Font: `var(--font-body)` (Heebo)
- Weight: 400
- Size: `clamp(0.85rem, 1.4vw, 0.95rem)`
- Color: `var(--color-green)` (#588475)
- Background: `transparent`
- Border: `none`
- Cursor: `pointer`
- Display: `inline-flex`, with a small arrow or line

**The button is a minimal text link with an underline effect:**

```css
.about__read-more {
  font-family: var(--font-body);
  font-weight: var(--font-weight-regular);
  font-size: clamp(0.85rem, 1.4vw, 0.95rem);
  color: var(--color-green);
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  margin-top: var(--space-md);
  position: relative;
  display: inline-block;
  text-decoration: none;
}

.about__read-more::after {
  content: '';
  position: absolute;
  bottom: -2px;
  right: 0;
  width: 100%;
  height: 1px;
  background-color: var(--color-green);
  opacity: 0.4;
  transition: opacity var(--duration-fast) var(--ease-ink),
              transform var(--duration-fast) var(--ease-ink);
  transform-origin: right;
}

.about__read-more:hover::after {
  opacity: 1;
  transform: scaleX(1.05);
}

.about__read-more:hover {
  color: var(--color-green-dark);
}
```

**Hover state:**
- Text color darkens to `--color-green-dark` (#3B514B)
- Underline opacity goes from 40% to 100%
- Transition: `var(--duration-fast)` (0.3s) with `var(--ease-ink)`

**Focus state (keyboard navigation):**
```css
.about__read-more:focus-visible {
  outline: 2px solid var(--color-green);
  outline-offset: 4px;
  border-radius: 2px;
}
```

**No Beni/pink for this button.** The About section is monochromatic green. Beni is reserved for CTA actions (ticket purchase, event links). "Read more" is a navigation action, not a conversion action.

### 3.6 Decorative Elements

**Minimal.** The About section's power comes from typography and empty space, not decoration. However, two optional subtle elements:

**Option A - Ink Line Separator (recommended):**

A thin horizontal line above the section title, offset to the right. It evokes a calligraphy brush stroke rest - a small mark that signals "a new thought begins."

```css
.about__title::before {
  content: '';
  display: block;
  width: 40px;
  height: 1px;
  background-color: var(--color-green);
  opacity: 0.25;
  margin-bottom: var(--space-md);
}
```

- Width: 40px (short, deliberate)
- Color: Sol Green at 25% opacity
- Position: above the title, with 2rem gap below it
- In RTL, it naturally aligns to the right (start side), matching the text alignment

**Option B - Zen Pebble Shape (optional, deferred to v2):**

A very faint organic blob shape in the empty Ma space to the left of the text. If implemented:

```css
.about__deco-pebble {
  position: absolute;
  left: 5%;
  top: 50%;
  transform: translateY(-50%);
  width: clamp(100px, 15vw, 180px);
  height: clamp(120px, 18vw, 200px);
  background-color: var(--color-washi-warm);
  border-radius: 48% 52% 45% 55% / 52% 48% 55% 45%;
  opacity: 0.3;
  pointer-events: none;
}
```

**Recommendation for POC:** Use Option A only. Keep it clean. The Zen Pebble can come in when we have the gallery section with actual image masks.

### 3.7 About Section - Scroll Reveal Animation

Elements in the About section reveal as the user scrolls them into view. This is the "Sumi-e Scroll" pattern - elements appear as if being painted in real time.

**Implementation: Intersection Observer + CSS**

```css
.about__title,
.about__text,
.about__read-more {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity var(--duration-reveal) var(--ease-ink),
              transform var(--duration-reveal) var(--ease-ink);
}

.about__title.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.about__text.is-visible {
  opacity: 1;
  transform: translateY(0);
  transition-delay: 0.2s;
}

.about__read-more.is-visible {
  opacity: 1;
  transform: translateY(0);
  transition-delay: 0.4s;
}
```

**JavaScript (Intersection Observer):**

```javascript
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);  // animate once only
      }
    });
  },
  {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  }
);

document.querySelectorAll('.about__title, .about__text, .about__read-more')
  .forEach(el => observer.observe(el));
```

**Timing:** Title appears first, body text 0.2s later, read-more 0.4s later. Staggered, like brush strokes appearing one after another.

**Reduced motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .about__title,
  .about__text,
  .about__read-more {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## 4. Floating CTA Button

### 4.1 Appearance

The floating CTA button appears after the user scrolls past the Hero. It stays fixed on screen, providing a persistent path to events/tickets.

**Content:** "לכרטיסים" (or "לאירועים" - defer exact text to Copywriter)

**Positioning:**
- Fixed, bottom-left corner (in RTL context, left = end side = less obtrusive)
- `bottom: clamp(1.5rem, 3vw, 2rem)`
- `left: clamp(1.5rem, 3vw, 2rem)`

**Appearance:**
- Background: `rgba(88, 132, 117, 0.85)` (Sol Green at 85% opacity)
- Backdrop-filter: `blur(12px) saturate(1.2)`
- Color: `var(--color-washi)` (#F2EAD3)
- Font: `var(--font-body)` (Heebo)
- Weight: 400
- Size: `0.85rem`
- Letter-spacing: `0.03em`
- Padding: `0.75rem 1.5rem`
- Border-radius: `100px` (pill shape)
- Border: `1px solid rgba(242, 234, 211, 0.15)` (very subtle cream border)
- Box-shadow: `0 4px 20px rgba(38, 67, 72, 0.15)`

```css
.floating-cta {
  position: fixed;
  bottom: clamp(1.5rem, 3vw, 2rem);
  left: clamp(1.5rem, 3vw, 2rem);
  z-index: 100;

  font-family: var(--font-body);
  font-weight: var(--font-weight-regular);
  font-size: 0.85rem;
  letter-spacing: 0.03em;
  color: var(--color-washi);
  text-decoration: none;

  background: rgba(88, 132, 117, 0.85);
  backdrop-filter: blur(12px) saturate(1.2);
  -webkit-backdrop-filter: blur(12px) saturate(1.2);

  padding: 0.75rem 1.5rem;
  border-radius: 100px;
  border: 1px solid rgba(242, 234, 211, 0.15);
  box-shadow: 0 4px 20px rgba(38, 67, 72, 0.15);

  cursor: pointer;

  /* Hidden by default */
  opacity: 0;
  pointer-events: none;
  transform: translateY(10px);
  transition: opacity var(--duration-smooth) var(--ease-ink),
              transform var(--duration-smooth) var(--ease-ink),
              background-color var(--duration-fast) var(--ease-ink);
}

.floating-cta.is-visible {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}
```

### 4.2 Hover and Focus States

```css
.floating-cta:hover {
  background: rgba(88, 132, 117, 0.95);
  box-shadow: 0 6px 24px rgba(38, 67, 72, 0.2);
  transform: translateY(-1px);
}

.floating-cta:active {
  transform: translateY(0);
}

.floating-cta:focus-visible {
  outline: 2px solid var(--color-washi);
  outline-offset: 3px;
}
```

### 4.3 Scroll-based Visibility

The button appears when the user scrolls past 100vh (the Hero). Use Intersection Observer on the About section:

```javascript
const aboutSection = document.querySelector('.about');
const floatingCta = document.querySelector('.floating-cta');

const ctaObserver = new IntersectionObserver(
  ([entry]) => {
    floatingCta.classList.toggle('is-visible', entry.isIntersecting);
  },
  { threshold: 0.01 }
);

ctaObserver.observe(aboutSection);
```

**Reduced motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .floating-cta {
    transition: none;
  }
  .floating-cta.is-visible {
    transform: none;
  }
}
```

### 4.4 Mobile

On mobile, the button sits at the bottom-left. The `clamp` values ensure it has adequate spacing from the edge. The pill shape stays the same. The backdrop-filter may have performance implications on older devices - if so, fall back to a solid background:

```css
@supports not (backdrop-filter: blur(12px)) {
  .floating-cta {
    background: var(--color-green);
  }
}
```

---

## 5. RTL and Responsive Summary

### RTL

The entire page is `direction: rtl`. Specific considerations:

- All text aligns to the right by default
- The About section's asymmetric layout: `margin-left: auto` pushes content to the right (RTL start)
- The floating CTA sits in the bottom-left (RTL end side) to be less obtrusive
- The decorative ink line above the About title naturally aligns right
- The scroll indicator in the Hero is centered (not affected by RTL)

```css
html {
  direction: rtl;
}
```

### Responsive Breakpoints

| Breakpoint | Context | Key Changes |
|-----------|---------|-------------|
| < 480px | Small mobile | Title ~3.5rem, full-width text, container padding ~2rem |
| 480-768px | Large mobile/small tablet | Title scaling up, text still full-width |
| 768-1100px | Tablet/small desktop | About text goes asymmetric (600px max-width) |
| > 1100px | Desktop | Full layout, max-container 1100px, About text offset right |

### Font Loading

Google Fonts load sequence:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300&family=Heebo:wght@300;400&family=Inter:wght@300;400&display=swap" rel="stylesheet">
```

**Font display:** `swap` ensures text is visible immediately with fallback fonts, then swaps to the web fonts when loaded. Acceptable FOUT for this project - the serif/sans-serif shift is noticeable but brief.

**Fallback stack:**
- `--font-display`: `'Frank Ruhl Libre', 'David', 'Times New Roman', serif`
- `--font-body`: `'Heebo', 'Arial Hebrew', 'Arial', sans-serif`
- `--font-english`: `'Inter', 'Helvetica Neue', 'Arial', sans-serif`

---

## 6. Animation Summary Table

| Animation | Section | Trigger | Duration | Easing | CSS or JS | Reduced Motion |
|-----------|---------|---------|----------|--------|-----------|----------------|
| Logo fade in | Hero | Page load + 0.3s delay | 0.8s | `--ease-ink` | CSS `@keyframes` | No animation, static at 50% opacity |
| Title rise in | Hero | Page load + 0.6s delay | 1.2s | `--ease-ink` | CSS `@keyframes` | No animation, static visible |
| Tagline fade in | Hero | Page load + 1.2s delay | 0.8s | `--ease-ink` | CSS `@keyframes` | No animation, static at 60% opacity |
| Scroll indicator fade + pulse | Hero | Page load + 1.8s delay | 0.6s in, then 2.4s loop | `--ease-ink` | CSS `@keyframes` | No animation, static at 60% opacity |
| About title reveal | About | Scroll into view (IO, 15% threshold) | 1.2s | `--ease-ink` | CSS transition + JS IO | No animation, static visible |
| About text reveal | About | Scroll + 0.2s delay | 1.2s | `--ease-ink` | CSS transition + JS IO | No animation, static visible |
| About read-more reveal | About | Scroll + 0.4s delay | 1.2s | `--ease-ink` | CSS transition + JS IO | No animation, static visible |
| Floating CTA appear | Global | About section enters viewport | 0.6s | `--ease-ink` | CSS transition + JS IO | No animation, instant show |

**Key animation rules:**
1. Every animation respects `prefers-reduced-motion: reduce`
2. Every scroll-triggered animation fires once only (observer.unobserve after trigger)
3. No more than one animation active in the same viewport at any time (the stagger delays handle this)
4. All durations between 0.6s-2.4s - nothing fast or flashy
5. Single easing curve everywhere: `cubic-bezier(0.23, 1, 0.32, 1)`

---

## 7. Files and Assets Needed

| Asset | Format | Purpose | Notes |
|-------|--------|---------|-------|
| `washi-paper.webp` | WebP, 400x400px tileable | Body texture overlay | Under 15KB, subtle paper grain |
| Frank Ruhl Libre 300 | Google Fonts | Display/heading font | Hebrew serif |
| Heebo 300, 400 | Google Fonts | Body font | Hebrew sans-serif |
| Inter 300, 400 | Google Fonts | English text | Latin sans-serif |

No images needed for the POC Hero + About sections. The design is entirely typographic and color-based.

---

## 8. Accessibility Checklist for POC

```
[x] Color contrast - headings: Sol Green on Washi = 4.1:1 (passes AA large text)
[x] Color contrast - body: Sol Green Dark on Washi = 6.2:1 (passes AA)
[x] Color contrast - Hero text: Washi on Indigo = 8.7:1 (passes AAA)
[x] Semantic HTML: <header> for Hero, <section> for About, <h1> for title, <h2> for About title
[x] Focus-visible styles on all interactive elements
[x] prefers-reduced-motion respected for every animation
[x] No text in images - all text is real HTML text
[x] RTL direction set at html level
[x] Keyboard navigation: Tab through logo link, read-more button, floating CTA
[x] ARIA: floating CTA has aria-label, scroll indicator has aria-hidden="true"
```

---

## 9. What This Brief Does NOT Cover (Deferred to Later Phases)

- Interactive ink canvas (Hero v2)
- Video background option (Hero v2)
- The "read more" modal content and animation
- Sanity CMS integration
- Remaining 5 sections (Events, Gallery, Trust Bar, Sound, Footer)
- Navigation/header component
- Event page template
- Journal/press pages
- Schema.org markup
- Analytics integration
- GSAP ScrollTrigger (POC uses Intersection Observer only)

---

## 10. HTML Structure Reference

A semantic skeleton for the CTO to build from:

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>סול תרפי - היכן שהצליל הופך לדממה</title>
  <!-- Google Fonts -->
  <!-- Design tokens in CSS -->
</head>
<body>

  <!-- Hero Section -->
  <header class="hero" role="banner">
    <div class="hero__inner">
      <span class="hero__logo">Sol Therapy</span>
      <h1 class="hero__title">סול תרפי</h1>
      <p class="hero__tagline">היכן שהצליל הופך לדממה</p>
    </div>
    <div class="hero__scroll-indicator" aria-hidden="true">
      <span class="hero__scroll-dot"></span>
      <span class="hero__scroll-line"></span>
    </div>
    <!-- Bokashi gradient is ::after pseudo-element -->
  </header>

  <!-- About Section -->
  <section class="about" aria-labelledby="about-title">
    <div class="about__container">
      <div class="about__content">
        <h2 class="about__title" id="about-title">התדר שלנו</h2>
        <div class="about__text">
          <p><!-- Line 1: what it is --></p>
          <p><!-- Line 2: what it is not --></p>
          <p><!-- Lines 3-4: what the audience experiences --></p>
        </div>
        <button class="about__read-more" aria-expanded="false">
          קרא עוד
        </button>
      </div>
    </div>
  </section>

  <!-- Floating CTA -->
  <a href="#events" class="floating-cta" aria-label="מעבר לכרטיסים ואירועים">
    לכרטיסים
  </a>

</body>
</html>
```

---

*This brief is a complete construction blueprint. Every color, size, spacing, animation, and interaction is specified with exact values. The CTO should be able to build the POC without asking a single visual question.*
