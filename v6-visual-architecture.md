# Sol Therapy v6 - Visual Architecture Specification

**Author:** Illustrator Agent
**Date:** 2026-02-15
**Status:** Ready for CTO handoff
**Purpose:** Complete visual architecture for building the Sol Therapy website from scratch. Every decision here is mobile-first. Every layout description assumes a phone screen unless stated otherwise.

---

## 0. The Core Problem and the Principle That Solves It

The Board diagnosed the disease: template DNA. Five versions of the site followed the same WordPress skeleton - Hero, About, Cards, Gallery, Footer - regardless of what aesthetic was layered on top. Sumi-e illustrations, GSAP animations, paper textures - none of it matters when the bones are the same as ten million other websites.

**The governing principle for v6:**

> Radical structure, conventional usability.

The space between interactions should feel like walking through an art exhibition. But navigation and booking must be immediately clear to anyone who lands on the page.

**What this means technically:**
- The scroll journey IS the design. Not sections containing design.
- Photography IS the visual identity. Not illustrations decorated with photography.
- Hebrew typography IS the architecture. Not type sitting inside containers.
- Every viewport-height is a composition. Not a container holding content.

---

## 1. Site Architecture - The Scroll Journey

There are no "sections" in v6. There is a single continuous vertical scroll - a journey that moves through distinct visual states. Think of it as a vertical exhibition where each room has its own atmosphere, but the walls between rooms have dissolved.

### The Journey Map (top to bottom):

```
ENTRY (100vh)
  Dark. Photography. Brand name massive. One line of text. Silence.

  |  scroll  |
  v          v

MANIFESTO THREAD (variable height, ~60vh)
  Washi. Single sentences from Yaron's manifesto appear large.
  Not a block of text. Typographic moments with breathing room.

  |  scroll  |
  v          v

EVENT 1 - UPCOMING (100vh minimum, can extend)
  Full-bleed photography. Dark. Event name massive.
  Date, location, artist names. Booking CTA.
  Manifesto fragment woven in.

  |  scroll  |
  v          v

BREATHING SPACE (30-50vh)
  Washi. A single Sumi-e brushstroke or vermilion seal.
  Maybe one sentence. Maybe nothing. Just air.

  |  scroll  |
  v          v

EVENT 2 - UPCOMING or PAST (100vh minimum)
  Different photo, different color temperature.
  Same structural logic but distinct visual world.

  |  scroll  |
  v          v

BREATHING SPACE (30-50vh)

  |  scroll  |
  v          v

VIDEO MOMENT (100vh)
  Full-viewport video. Autoplay, muted, with invitation to unmute.
  The documentary or "Between Frequencies."

  |  scroll  |
  v          v

PAST EVENTS - CONDENSED
  A denser rhythm. 3-5 past events stacked.
  Each gets 70-80vh with photography but less text.
  Washi backgrounds between them.

  |  scroll  |
  v          v

CLOSING (100vh)
  Dark. The brand name again. Contact/newsletter.
  Minimal. Bookend that mirrors the Entry.
```

### Why This Architecture

- **No standalone About section.** Yaron's manifesto is threaded through the entire page - a sentence here, a fragment there, woven between events. The visitor absorbs the philosophy through proximity to the events, not through a wall of text.
- **Events are full-viewport experiences.** Each event takes over the screen completely. When you are inside an event, nothing else exists.
- **Breathing spaces create rhythm.** The washi pauses between events prevent the experience from becoming a slideshow. They give the eye and mind a moment of rest - the Ma principle applied to scroll architecture.
- **Two color states alternate.** Dark (photography/events) and washi (breathing/manifesto). The alternation creates visual rhythm without boxes or dividers.

### Mobile Scroll Behavior

- Natural, native scroll. No scroll hijacking.
- No snap-to-section (feels jarring on mobile).
- Scroll progress indicator: a thin 2px line at the top of the viewport, using --green, tracking scroll position. Subtle, not decorative.
- No horizontal scroll anywhere.

---

## 2. Typography System

Typography is the PRIMARY visual identity of v6. Not Sumi-e. Not animations. The Hebrew letterforms themselves create the architecture of the page.

### The Font Stack

| Font | Role | Where Used |
|------|------|------------|
| **Masada** (self-hosted) | Display / Architectural | Brand name, event names, manifesto sentences, section-scale type |
| **Heebo** (Google) | Body / Reading | Descriptions, details, navigation labels |
| **Inter** (Google) | English / Data | Dates, locations, English text, metadata |
| **Guttman Haim** (self-hosted) | Stamp / Signature | Logo lockup accent only - used very sparingly |

### Type Scale - Mobile First

```css
:root {
  /* Architectural type - the big Hebrew that IS the design */
  --type-monument: clamp(3rem, 2rem + 8vw, 12rem);
  /* ~48px on 375px phone, ~192px on 1440px desktop */

  /* Event names - large but readable */
  --type-event: clamp(2.2rem, 1.5rem + 4.5vw, 6rem);
  /* ~35px mobile, ~96px desktop */

  /* Manifesto sentences - medium-large, room to breathe */
  --type-manifesto: clamp(1.6rem, 1.2rem + 2.5vw, 3.5rem);
  /* ~26px mobile, ~56px desktop */

  /* Sub-headings */
  --type-sub: clamp(1.1rem, 0.9rem + 1vw, 1.8rem);

  /* Body text */
  --type-body: clamp(0.9rem, 0.85rem + 0.25vw, 1.05rem);

  /* Small / metadata / dates */
  --type-small: clamp(0.7rem, 0.65rem + 0.2vw, 0.8rem);

  /* Micro / labels */
  --type-micro: clamp(0.55rem, 0.5rem + 0.15vw, 0.65rem);
}
```

### Typography Rules

**Masada at monument scale (--type-monument):**
- Used for the brand name "sol therapy" in Entry and Closing
- Used for manifesto pull-quotes
- Line-height: 0.9 to 0.95 (tight - letters should almost touch)
- Letter-spacing: -0.02em to -0.03em (slightly tightened)
- Weight: 600 (Demi) or 700 (Bold)
- Color: always either --washi (on dark) or --green-dark (on washi)
- On mobile, this type should fill the width of the screen. It should feel massive even on a phone.

**Masada at event scale (--type-event):**
- Used for event names
- Line-height: 1.0 to 1.1
- Weight: 500 (Medium) or 600 (Demi)
- Can break across 2-3 lines on mobile - that is fine and intended

**Heebo for body:**
- Weight: 300 (Light) for body text, 400 (Regular) for emphasis
- Line-height: 1.8 to 2.0 (generous for Hebrew readability)
- Max-width for body text blocks: 540px (never wider, even on desktop)
- Opacity: 0.65 to 0.8 on washi backgrounds, 0.5 to 0.7 on dark backgrounds

**Inter for data/English:**
- Weight: 300 or 400
- Letter-spacing: 0.1em to 0.3em (tracking opened up)
- Text-transform: uppercase for dates and metadata
- Size: always --type-small or --type-micro
- Used for: dates, "SOLD OUT", location names in English, navigation labels

**Direction and bidi:**
- html lang="he" dir="rtl"
- English elements get `direction: ltr; unicode-bidi: isolate;`
- Dates are always LTR
- Navigation labels in Hebrew, RTL

### The Manifesto-as-Typography Approach

Instead of a block of manifesto text in an About section, individual sentences from Yaron's manifesto appear as large typographic moments throughout the scroll. Example treatment:

```
[Washi background, full viewport width minus gutters]

         שימוש במוזיקה
       ככלי להרחבת תודעה

[Masada, --type-manifesto, --green, centered or right-aligned]
[Below it: a thin 3px vermilion line, 40px tall, as a pause mark]
```

These manifesto moments appear between events, occupying 40-60vh each. They are NOT paragraphs. They are 1-2 sentences maximum, set large enough to be read slowly. The typography IS the content - no illustration needed.

---

## 3. Color System

### Two States

The page alternates between two color states. There is no toggle. The color state changes as you scroll through the journey.

**State 1: DARK (ink on night)**
Used for: Entry, events with photography, video moment, closing.

```css
.state-dark {
  --bg: #1a1a1a;           /* Near-black, warmer than pure black */
  --bg-photo: #0d0d0d;     /* Behind full-bleed photos */
  --text-primary: #F2EAD3;  /* Washi cream on dark */
  --text-secondary: rgba(242, 234, 211, 0.5);
  --text-muted: rgba(242, 234, 211, 0.3);
  --accent: #D3381C;        /* Vermilion */
  --cta: #BE5069;           /* Beni - for booking buttons */
}
```

**State 2: WASHI (ink on aged paper)**
Used for: Manifesto threads, breathing spaces, past events condensed.

```css
.state-washi {
  --bg: #F2EAD3;            /* Washi cream */
  --bg-warm: #EDE5CE;       /* Slightly warmer variant */
  --text-primary: #264348;  /* Indigo-dark */
  --text-secondary: #3B514B; /* Green-dark */
  --text-muted: rgba(38, 67, 72, 0.4);
  --accent: #D3381C;         /* Vermilion */
  --cta: #BE5069;            /* Beni */
}
```

### Transition Between States

The transition between dark and washi is NOT a hard cut. It happens through a CSS gradient that fades the background over 20-30vh of scroll distance. Think of it as bokashi - the traditional Japanese graduated wash technique.

```css
/* Between a dark event and a washi breathing space */
.transition-dark-to-washi {
  height: 30vh;
  background: linear-gradient(to bottom,
    var(--state-dark-bg) 0%,
    var(--state-washi-bg) 100%
  );
}
```

On the washi state, maintain the paper texture overlay (SVG noise filter at 0.06-0.09 opacity, fixed position). This gives the washi areas a physical, tactile quality.

### Color Rules

1. **Never use pure white (#FFFFFF) or pure black (#000000).** Dark backgrounds are #1a1a1a or #0d0d0d. Light backgrounds are #F2EAD3 or #EDE5CE.
2. **Vermilion (#D3381C) appears sparingly** - as accent lines, the Hanko seal mark, hover states on the brand name. Never as a background or large surface.
3. **Beni (#BE5069) is the action color** - booking buttons, active CTAs. It is warm enough to feel inviting, distinct enough to stand out on both states.
4. **Green (#588475) is the structural color** - section type, navigation elements, scroll progress bar, body text on washi.
5. **No gradients on text.** No teal-to-green gradients. No decorative color mixing. Color is flat and intentional.

### Photography Color Treatment

Event photographs are displayed with a subtle treatment to unify them visually:

```css
.event-photo {
  filter: contrast(1.05) saturate(0.85);
  /* Slightly more contrast, slightly less saturation */
  /* This makes the photos feel like exhibition prints */
}
```

On dark backgrounds, photos can have a very subtle dark overlay (rgba(0,0,0,0.15)) to ensure text readability without crushing the image.

---

## 4. Photography Treatment

The photographs are spectacular. They are the single most powerful visual asset Sol Therapy has. The entire v6 design exists to let these photographs work at full power.

### What the Photos Show (and Why It Matters)

Having studied all 8 photographs:

- **orchestra-stage.jpg** - Overhead shot of a full chamber orchestra on a lit stage, blue lighting, audience visible. Scale and gravitas.
- **meditation-hall.jpg** - Hundreds of people lying on white mats, warm golden/pink lighting from above, immersive. The core experience.
- **outdoor-night.jpg** - DJ setup outdoors at night, blue-lit historic building, people on rugs and cushions, candles. Intimate urban ritual.
- **projection-building.jpg** - Purple/pink projection mapping on a large building facade, scattered people below, night scene. Spectacle.
- **museum-meditation.jpg** - People on mats in a museum gallery with a massive digital art projection on the wall. Art-meets-meditation.
- **museum-wide.jpg** - Wider angle of the same museum scene. Shows the architectural space.
- **dj-perspective-bw.jpg** - Black and white, from behind the DJ looking over the mixing equipment toward people lying on mats. The artist's viewpoint.
- **dark-performance.jpg** - A single performer lit in a vast dark space, hundreds of bodies lying on mats. Cinematic. The most powerful image.

### Photo Presentation Rules

**Full-bleed is the default.** Every event photo should fill the viewport edge-to-edge. No rounded corners. No borders. No frames. No padding around photos. The photo IS the section.

```css
.event-photo-container {
  position: relative;
  width: 100vw;
  min-height: 100vh;
  min-height: 100svh; /* Safe viewport height for mobile */
  overflow: hidden;
}

.event-photo-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 40%; /* Slightly above center - better for event photos */
}
```

**Text over photography** uses a gradient overlay, not a flat tint:

```css
.event-photo-container::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.1) 0%,
    rgba(0, 0, 0, 0.0) 30%,
    rgba(0, 0, 0, 0.0) 50%,
    rgba(0, 0, 0, 0.5) 80%,
    rgba(0, 0, 0, 0.75) 100%
  );
  /* Heavy at bottom where text lives, light at top to show the photo */
}
```

**Photo ordering matters.** The most cinematic, highest-impact photo goes first (dark-performance.jpg or museum-meditation.jpg for the entry). Each subsequent event should have a different visual temperature - alternate between:
- Dark/moody (dark-performance, museum-meditation)
- Lit/warm (meditation-hall, orchestra-stage)
- Outdoor/blue (outdoor-night, projection-building)

**The B/W photo (dj-perspective-bw.jpg)** is special. Use it for a manifesto moment or as a background to a typographic section. Its monochrome nature bridges both color states.

**No photo grid. No photo gallery section.** Photos appear only as full-bleed backgrounds for events or as atmospheric elements within the scroll. If additional photos need to be shown for a past event, use a very simple vertical stack (one photo per scroll, full-width) rather than a grid.

### Photo Loading

- Use `loading="lazy"` on all photos except the Entry photo
- Entry photo: preload with `<link rel="preload" as="image">`
- All photos served as WebP with JPEG fallback
- Use `srcset` for responsive sizes: 750w, 1200w, 1920w
- On mobile (< 768px), serve the 750w version
- `object-fit: cover` everywhere - never stretch, never letter-box

---

## 5. Event Presentation

Each event is a complete visual world. When an event fills the viewport, the visitor should feel like they have entered a specific place and time.

### Event Anatomy - Upcoming Event (Full Treatment)

```
+--------------------------------------------------+
|                                                    |
|  [Full-bleed photograph fills entire viewport]     |
|                                                    |
|                                                    |
|                                                    |
|                                                    |
|                                                    |
|  15 MAR 2026                   (Inter, --type-small, |
|                                 LTR, top area,     |
|                                 washi @ 0.5 opacity)|
|                                                    |
|                                                    |
|                                                    |
|       [gradient overlay gets heavier here]         |
|                                                    |
|  סשן מדיטציית סאונד                                 |
|  במוזיאון תל אביב                                   |
|  (Masada, --type-event, washi, right-aligned)      |
|                                                    |
|  שלומי שבן / התזמורת הקאמרית                        |
|  (Heebo, --type-body, washi @ 0.6)                 |
|                                                    |
|  [  לרכישת כרטיסים  ]                               |
|  (Booking button - Beni bg, washi text)            |
|                                                    |
|  "נהפוך את המרחבים הירוקים לגינת זן ענקית ופועמת" |
|  (Heebo Light, --type-small, washi @ 0.4)          |
|  ^ This is a manifesto fragment, not a tagline     |
|                                                    |
+--------------------------------------------------+
```

### Mobile Layout for Events

```css
.event {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; /* Content sits at the bottom */
  padding: 0 1.5rem 2.5rem 1.5rem; /* gutter sides, generous bottom */
}

.event__date {
  position: absolute;
  top: max(env(safe-area-inset-top, 0px) + 5rem, 5rem);
  /* Below the nav bar */
  right: 1.5rem;
  font-family: var(--english);
  font-size: var(--type-micro);
  color: var(--washi);
  opacity: 0.5;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  direction: ltr;
}

.event__name {
  font-family: var(--display);
  font-weight: 600;
  font-size: var(--type-event);
  color: var(--washi);
  line-height: 1.05;
  margin-bottom: 0.75rem;
}

.event__artists {
  font-family: var(--body);
  font-weight: 300;
  font-size: var(--type-body);
  color: var(--washi);
  opacity: 0.6;
  margin-bottom: 1.25rem;
}

.event__location {
  font-family: var(--english);
  font-size: var(--type-small);
  color: var(--washi);
  opacity: 0.4;
  letter-spacing: 0.15em;
  direction: ltr;
  margin-bottom: 1.5rem;
}

.event__cta {
  display: inline-block;
  padding: 0.9rem 2rem;
  background: var(--beni);
  color: var(--washi);
  font-family: var(--body);
  font-weight: 400;
  font-size: var(--type-small);
  letter-spacing: 0.05em;
  border: none;
  border-radius: 0; /* Square - no rounded corners */
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  min-height: 48px; /* Touch target */
  min-width: 160px;
}

.event__manifesto-fragment {
  margin-top: 2rem;
  font-family: var(--body);
  font-weight: 300;
  font-size: var(--type-small);
  color: var(--washi);
  opacity: 0.35;
  max-width: 280px;
  line-height: 1.7;
}
```

### Desktop Layout for Events (min-width: 1024px)

On desktop, the event content moves to the bottom-right third of the viewport. The photograph gets more breathing room.

```css
@media (min-width: 1024px) {
  .event {
    padding: 0 4rem 5rem 4rem;
    align-items: flex-start; /* Content right-aligned in RTL */
  }

  .event__name {
    max-width: 60%;
  }

  .event__manifesto-fragment {
    max-width: 380px;
  }
}
```

### Past Event Treatment

Past events get a reduced treatment - 70-80vh instead of 100vh, with a desaturated photo treatment and no booking CTA. Instead of "buy tickets" they show a "gallery" or "documentation" link.

```css
.event--past .event-photo-container img {
  filter: contrast(1.05) saturate(0.6) brightness(0.9);
  /* More muted - signals "this already happened" */
}

.event--past {
  min-height: 70vh;
}

.event--past .event__cta {
  background: transparent;
  border: 1px solid rgba(242, 234, 211, 0.3);
  color: var(--washi);
  opacity: 0.6;
}
```

### SOLD OUT Treatment

```css
.event__cta--soldout {
  background: transparent;
  border: 1px solid rgba(242, 234, 211, 0.2);
  color: var(--washi);
  opacity: 0.4;
  cursor: default;
  pointer-events: none;
}
```

The text reads "SOLD OUT" in Inter, uppercase, letter-spacing 0.3em.

---

## 6. Navigation and CTA

### The Principle

Navigation is conventional. Clear. Predictable. The revolution is in the space between navigation elements, not in the navigation itself. No Hanko-as-nav. No hidden menus that require discovery. A person landing on this page for the first time should know within 2 seconds how to find events and book tickets.

### Mobile Navigation

```
+--------------------------------------------------+
|  [hamburger]                  SOL THERAPY          |
|                               (Inter, 0.55rem,    |
|                                tracking 0.45em)    |
+--------------------------------------------------+
```

- Fixed position, top of viewport
- On dark sections: transparent background, washi-colored text and hamburger lines
- On washi sections: washi background with blur(14px) backdrop-filter, green-dark text
- The transition between nav styles happens via JavaScript observing which color state the viewport is in (IntersectionObserver on state boundary elements)
- Height: approximately 56px on mobile (including padding)

**Hamburger menu (mobile):** Opens a full-screen overlay.

```css
.mobile-menu {
  position: fixed;
  inset: 0;
  background: #1a1a1a;
  z-index: 99;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

.mobile-menu a {
  font-family: var(--display);
  font-weight: 500;
  font-size: 1.6rem;
  color: var(--washi);
  opacity: 0.6;
  transition: opacity 0.3s;
}
```

Menu items:
1. **אירועים** (Events) - scrolls to first event
2. **אודות** (About) - scrolls to manifesto thread area
3. **סרטון** (Video) - scrolls to video moment
4. **יצירת קשר** (Contact) - scrolls to closing

Plus a prominent booking button if there is an active upcoming event:

```css
.mobile-menu__cta {
  margin-top: 1.5rem;
  padding: 1rem 2.5rem;
  background: var(--beni);
  color: var(--washi);
  font-family: var(--body);
  font-size: var(--type-small);
  min-height: 48px;
}
```

### Desktop Navigation (min-width: 1024px)

```
+--------------------------------------------------+
|  SOL THERAPY          אירועים  אודות  סרטון  קשר  |
+--------------------------------------------------+
```

- Hamburger hidden, horizontal link row visible
- Same fixed/transparent behavior
- Links use Heebo, --type-small, with subtle underline on hover (1px, slides in from right)
- No dropdown menus

### Booking CTA Strategy

The primary conversion action is booking tickets to upcoming events. The CTA appears in THREE places:

1. **Inside each upcoming event** (the event__cta button described above)
2. **In the mobile menu** (prominent booking button)
3. **Floating indicator** - on mobile only, a small fixed indicator appears in the bottom-right corner after the user scrolls past the first event. It is a small circle (40px) with the Beni color, containing a simple arrow or ticket icon. Tapping it scrolls to the nearest upcoming event's CTA.

```css
.floating-cta {
  position: fixed;
  bottom: 1.5rem;
  left: 1.5rem; /* Left in RTL = visual right */
  width: 44px;
  height: 44px;
  background: var(--beni);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 90;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.4s ease, transform 0.4s ease;
  -webkit-tap-highlight-color: transparent;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
}

.floating-cta--visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 7. Mobile-First Layout System

### Gutters and Spacing

```css
:root {
  --gutter: 1.5rem;  /* 24px on mobile */

  --space-xs: clamp(0.5rem, 0.4rem + 0.5vw, 0.75rem);
  --space-s: clamp(1rem, 0.8rem + 1vw, 1.5rem);
  --space-m: clamp(2rem, 1.5rem + 2.5vw, 3.5rem);
  --space-l: clamp(4rem, 3rem + 5vw, 7rem);
  --space-xl: clamp(6rem, 4rem + 10vw, 14rem);
}

@media (min-width: 1024px) {
  :root {
    --gutter: clamp(2rem, 1.5rem + 3vw, 6rem);
  }
}
```

### Safe Areas

```css
/* Respect notch and system UI on iOS */
body {
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
```

### Touch Targets

Every interactive element must be at least 44x44px (Apple HIG) or 48x48px (Material). No exceptions. Links that are text-only get generous padding to expand their tap area.

```css
.nav a, .event__cta, .mobile-menu a, .floating-cta {
  min-height: 48px;
  display: flex;
  align-items: center;
}
```

### Viewport Units

Use `svh` (small viewport height) instead of `vh` for mobile. This prevents the layout from jumping when the browser chrome appears/disappears on scroll.

```css
.event {
  min-height: 100vh;
  min-height: 100svh;
}
```

### Content Width Constraints

Body text and manifesto fragments never exceed a readable measure:

```css
.text-block {
  max-width: min(540px, 100% - 3rem);
  /* On a 375px phone: 342px max width */
  /* On desktop: 540px max width */
}
```

### Image Handling

All images are 100vw on mobile. No side padding on photographs. The photo bleeds to the edges of the screen.

```css
.event-photo-container {
  width: 100vw;
  margin-left: calc(-1 * var(--gutter));
  /* Breaks out of parent padding */
}
```

### Desktop Expansion (min-width: 1024px)

On desktop, the layout gains breathing room but the vertical scroll architecture remains identical. Changes:
- Gutters increase (up to 6rem)
- Typography scales up (clamp functions handle this automatically)
- Event content block positions in the bottom-right third
- Manifesto type can get very large (up to 3.5rem)
- Photos remain full-bleed

There is NO horizontal layout shift. No sidebar. No two-column event presentation. The single-column vertical flow is preserved on all screen sizes. The only difference is scale and breathing room.

---

## 8. Video Integration

### Two Videos

1. **Documentary** - longer format, showcasing the Sol Therapy world
2. **"Between Frequencies"** - shorter, more cinematic/promotional

### Presentation

One video gets the "Video Moment" position in the scroll journey - a full 100vh section with the video as the centerpiece.

```css
.video-moment {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: #0d0d0d;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-m) var(--gutter);
}

.video-moment video {
  width: 100%;
  max-width: 960px;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  background: #000;
}
```

**Behavior:**
- Video autoplays when it enters the viewport (IntersectionObserver, threshold 0.5)
- Autoplays MUTED
- A subtle "tap for sound" invitation appears as text below the video (Heebo Light, --type-micro, washi @ 0.4)
- No custom player controls. Use native HTML5 controls.
- Video pauses when it leaves the viewport

The second video can be embedded within a past event section or linked from the closing area. It does NOT get its own full viewport treatment - one video moment is enough.

### Mobile Video

On phones, the 16:9 video will not fill the full viewport height. That is fine. The surrounding dark space above and below the video becomes part of the composition. Center the video vertically in the viewport.

---

## 9. Spatial Rhythm - Creating the Exhibition Sensation

### What Creates the Feeling

The "art exhibition" sensation comes from THREE things, none of which require complex animations:

1. **Scale contrast.** The alternation between massive full-bleed photography and quiet washi spaces with small text creates the feeling of moving between gallery rooms and corridors.

2. **Generous emptiness.** The breathing spaces (30-50vh of washi with minimal content) are not "dead space" - they are the Ma principle. They make the events feel more impactful by contrast.

3. **Slow reveal.** Content at the bottom of each viewport enters naturally through scroll. No animation required - the act of scrolling a phone already creates a reveal from the bottom edge.

### What Animations to Use (and What Not to Use)

**YES - simple, scroll-triggered opacity transitions:**

```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.fade-in--visible {
  opacity: 1;
  transform: translateY(0);
}
```

Triggered by IntersectionObserver when the element enters the viewport. Used for:
- Manifesto text appearing in breathing spaces
- Event text content (name, artists, CTA)
- The vermilion accent marks

**YES - parallax on photos (desktop only, reduced-motion respecting):**

```css
@media (min-width: 1024px) and (prefers-reduced-motion: no-preference) {
  .event-photo-container img {
    will-change: transform;
    /* GSAP ScrollTrigger: subtle y-axis movement, 10-15% range */
  }
}
```

On mobile, photos are static. No parallax. It drains battery and often looks choppy.

**YES - the Entry brand name reveal:**

The brand name "sol therapy" in the Entry section gets a character-by-character reveal using GSAP SplitText. Each character fades in and slides up, staggered by 30ms. Total animation duration: under 1.5 seconds. This is the ONE moment of theatrical animation on the entire page.

**NO to everything else:**
- No scroll-velocity effects
- No ink-bleed animations
- No scroll-hijacking or snap-scrolling
- No horizontal slide transitions between events
- No cursor-following effects
- No loading screen animation
- No floating particles or ambient elements
- No text that types itself
- No counter/number animations

If `prefers-reduced-motion: reduce` is set, disable ALL animations including the Entry reveal. Show everything in its final state immediately.

### Scroll Rhythm Pattern

The ideal scroll rhythm alternates between "dense" and "sparse" moments:

```
DENSE   (100vh) - Entry, photo, type, lots of information
SPARSE  (40vh)  - Washi, one sentence or nothing
DENSE   (100vh) - Event 1, photo, details, CTA
SPARSE  (30vh)  - Washi, breathing
DENSE   (100vh) - Event 2
SPARSE  (50vh)  - Manifesto fragment, large type
DENSE   (100vh) - Video moment
SPARSE  (30vh)  - Breathing
DENSE   (80vh)  - Past event (slightly shorter)
DENSE   (70vh)  - Past event
SPARSE  (40vh)  - Final manifesto fragment
DENSE   (100vh) - Closing
```

This creates a breathing rhythm. Dense, sparse, dense, sparse. The viewer is never overwhelmed by a continuous wall of content, and never bored by too much empty space.

---

## 10. What NOT to Do

Based on the Board deliberation and 5 failed versions, these are explicit prohibitions:

### Structural

1. **No Hero - About - Cards - Gallery - Footer skeleton.** This is the WordPress DNA we are eliminating. If the page can be described using these section names, start over.
2. **No standalone About section.** The manifesto lives between events, not in its own box.
3. **No event cards in a grid.** Each event is a full-viewport experience. If events are reduced to cards, we have failed.
4. **No horizontal gallery/carousel.** Photos are full-bleed vertical, one at a time.
5. **No boxed sections with visible containers.** No rounded-corner cards, no drop shadows on content boxes, no visible section boundaries.
6. **No equal-height columns or symmetrical grids.** The rhythm is intentionally asymmetric.

### Visual

7. **No Sumi-e illustrations as primary visual elements.** Photography drives the design. Sumi-e is texture/atmosphere ONLY - a faint brushstroke in a breathing space, a subtle texture overlay. Never a hero image, never a section illustration.
8. **No decorative gradients.** Gradients are used only for: photo overlays (for text legibility) and state transitions (dark to washi).
9. **No Three.js scenes or WebGL effects.** They are heavy, drain mobile battery, and add nothing that photography does not already provide.
10. **No paper texture that overpowers the content.** The washi noise overlay should be barely perceptible (0.06-0.09 opacity). If you can see the texture clearly, it is too strong.

### Interaction

11. **No scroll hijacking or scroll snapping.** Native scroll only.
12. **No auto-playing audio.** Sound is opt-in only.
13. **No cursor effects** (custom cursors, cursor followers, ink trails).
14. **No scroll-velocity-based effects.** They feel like tech demos.
15. **No loading screens with animations.** The page should render progressively.
16. **No "discover more" or "scroll down" prompts** beyond the Entry's simple ink-drop indicator.

### Typography

17. **No decorative fonts** beyond the four in the font stack.
18. **No outlined/stroked text.**
19. **No text over busy photo areas without a gradient overlay.**
20. **No centered paragraphs.** Body text is right-aligned (RTL natural alignment). Only manifesto pull-quotes may be centered.

### Content

21. **No stock photography.** Only real Sol Therapy event photos.
22. **No generic wellness imagery** (lotus flowers, chakra diagrams, om symbols, crystals).
23. **No testimonials section.** Social proof comes from the photography and the artist names.
24. **No "our team" section.** This is not a corporate site.
25. **No newsletter popup.** Newsletter signup lives quietly in the Closing section.

---

## 11. The Sumi-e Layer - Texture, Not Protagonist

Sumi-e is NOT eliminated from v6. It is repositioned from protagonist to atmosphere. It appears in three controlled ways:

### 1. Vermilion Seal (Hanko)

A small vermilion mark (the Sol Therapy seal) appears in two places:
- In the Entry section, near the brand name (small, ~24px on mobile)
- In the Closing section, as a signature

It is the brand mark. It is always small. It never pulses, glows, or animates.

```css
.hanko {
  width: 24px;
  height: auto;
  opacity: 0.85;
}

@media (min-width: 1024px) {
  .hanko {
    width: 32px;
  }
}
```

### 2. Breathing Space Accents

In the washi breathing spaces between events, a single Sumi-e element may appear at very low opacity:

- A horizontal brushstroke (SVG, opacity 0.08-0.12)
- A small ink wash shape (SVG, opacity 0.06-0.10)
- A thin vermilion accent line (3px wide, 40-60px tall, opacity 0.5)

These are minimal. They should be barely noticed consciously but contribute to the overall feeling of an art space.

### 3. Washi Paper Texture

The fixed SVG noise overlay that gives washi sections their paper quality:

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,..."); /* fractalNoise filter */
  pointer-events: none;
  z-index: 9997;
  opacity: 0.07;
}
```

This is invisible on dark sections (dark on dark) and subtly visible on washi sections. It gives the entire page a physical, non-digital quality.

---

## 12. Entry Section - Detailed Spec

The Entry is the first impression. It must communicate three things in under 3 seconds: this is Sol Therapy, this is about sound meditation, this is a premium experience.

### Mobile Layout

```
+----------------------------------+
|                                    |
|  [nav: hamburger    SOL THERAPY]   |
|                                    |
|                                    |
|                                    |
|                                    |
|        [dark, atmospheric           |
|         - either the                |
|         dark-performance.jpg        |
|         or a CSS gradient           |
|         on #1a1a1a]                 |
|                                    |
|                                    |
|                                    |
|               סול                  |
|             תרפי                   |
|                                    |
|  (Masada Bold, --type-monument,    |
|   washi color, right-aligned)      |
|                                    |
|  מדיטציות סאונד עמוקות              |
|  (Heebo Light, --type-small,       |
|   washi @ 0.45)                    |
|                                    |
|         [ink drop]                 |
|            |                       |
|            |                       |
+----------------------------------+
```

### The Decision: Photo or Gradient for Entry

**Option A - dark-performance.jpg as background:** The most cinematic photo, showing the lone performer in a vast dark space with hundreds of bodies. Immediately communicates what Sol Therapy is. Risk: slow load.

**Option B - Pure dark with CSS gradient mist:** Faster to load. Creates a stark, minimal opening. The photography punch hits harder when Event 1 appears. Recommendation: this option. Let the first photograph be a surprise.

**CTO Note:** Implement both and let Yaron choose. The Entry should support swapping between a solid dark background and a background image via a single CSS class.

### Animation Sequence (Entry only)

```
t=0ms:    Page loads. Dark background visible.
t=200ms:  Brand name characters begin revealing (GSAP SplitText)
          Each char: opacity 0->1, translateY 20px->0
          Stagger: 40ms between characters
t=800ms:  Tagline fades in (opacity 0->1, 600ms)
t=1200ms: Ink drop begins its loop animation
t=1500ms: Nav fades in (opacity 0->1, 400ms)
```

Total: 1.5 seconds from load to full Entry visible. No preloader.

---

## 13. Closing Section - Detailed Spec

The Closing mirrors the Entry - dark background, brand name, minimal content. It provides:

1. Newsletter signup (email input + submit)
2. Social links (Instagram, Facebook)
3. Contact email
4. The Hanko seal as a signature
5. Copyright / credit line

### Mobile Layout

```
+----------------------------------+
|                                    |
|  [dark background, #1a1a1a]       |
|                                    |
|                                    |
|               סול                  |
|             תרפי                   |
|  (Masada, --type-manifesto,        |
|   washi, right-aligned)           |
|                                    |
|  [vermilion accent line, 3px]     |
|                                    |
|  הישארו מחוברים                     |
|  (Heebo, --type-body, washi@0.5)  |
|                                    |
|  [email input] [submit button]    |
|  (simple, inline, no decorations) |
|                                    |
|                                    |
|  [Instagram icon]  [Facebook]     |
|  (washi @ 0.3, 20px icons)        |
|                                    |
|  hello@soltherapy.co.il           |
|  (Inter, --type-micro, washi@0.3) |
|                                    |
|  [Hanko seal, 20px]               |
|                                    |
|  Sol Therapy 2026                 |
|  (Inter, --type-micro, washi@0.2) |
|                                    |
+----------------------------------+
```

### Email Input Styling

```css
.closing__email-input {
  background: transparent;
  border: none;
  border-bottom: 1px solid rgba(242, 234, 211, 0.2);
  color: var(--washi);
  font-family: var(--body);
  font-size: var(--type-body);
  padding: 0.75rem 0;
  width: 100%;
  max-width: 320px;
  outline: none;
}

.closing__email-input:focus {
  border-bottom-color: var(--beni);
}

.closing__email-input::placeholder {
  color: rgba(242, 234, 211, 0.25);
}

.closing__submit {
  background: transparent;
  border: none;
  color: var(--beni);
  font-family: var(--body);
  font-size: var(--type-small);
  padding: 0.75rem 1rem;
  cursor: pointer;
  min-height: 48px;
}
```

---

## 14. Performance Budget

Mobile performance is non-negotiable. The site must feel instant on a mid-range Android phone over 4G.

| Asset | Budget |
|-------|--------|
| HTML + CSS (initial) | < 80KB gzipped |
| Fonts (all 4 families) | < 150KB total |
| Entry photo (if used) | < 200KB (WebP, 750w) |
| Each additional photo | < 250KB (WebP, lazy-loaded) |
| JavaScript (all) | < 60KB gzipped |
| Total initial payload | < 500KB |
| Largest Contentful Paint | < 2.5s on 4G |
| Cumulative Layout Shift | < 0.05 |
| First Input Delay | < 100ms |

### What This Means for CTO

- **No Three.js.** No WebGL. Zero 3D.
- **Minimal GSAP.** Only for: Entry text reveal + scroll-triggered fade-ins + optional desktop parallax. Total GSAP budget: ScrollTrigger + SplitText + core = ~45KB gzipped.
- **Lazy load everything** below the first viewport.
- **Font subsetting.** Masada contains only the Hebrew characters + basic Latin needed. Heebo and Inter loaded via Google Fonts with `display=swap` and `text=` parameter to subset.
- **No CSS framework.** Hand-written CSS. No Tailwind, no Bootstrap, no CSS-in-JS.
- **Single HTML file** is acceptable for this scale of content. No SPA framework.

---

## 15. Accessibility

- Semantic HTML: header, nav, main, article (for events), footer
- Skip-to-content link
- All images have descriptive alt text in Hebrew
- Color contrast: WCAG AA minimum (4.5:1 for body text, 3:1 for large text)
  - Washi text on dark (#F2EAD3 on #1a1a1a) = contrast ratio ~12:1 (passes)
  - Green-dark text on washi (#3B514B on #F2EAD3) = contrast ratio ~6.5:1 (passes)
  - Beni on washi (#BE5069 on #F2EAD3) = check and adjust if needed
- Focus-visible outlines on all interactive elements (2px solid --green, 3px offset)
- prefers-reduced-motion: reduce disables all animations
- prefers-color-scheme: not used (the site has its own dark/light rhythm)
- Video: captions available
- Touch targets: minimum 48x48px

---

## 16. Design Token Summary

Complete token set for CTO to implement:

```css
:root {
  /* --- COLOR TOKENS --- */

  /* Backgrounds */
  --color-dark: #1a1a1a;
  --color-dark-deep: #0d0d0d;
  --color-washi: #F2EAD3;
  --color-washi-warm: #EDE5CE;

  /* Primary palette */
  --color-green: #588475;
  --color-green-dark: #3B514B;
  --color-green-light: #6A9A89;
  --color-indigo: #264348;
  --color-indigo-light: #314D59;

  /* Accent */
  --color-beni: #BE5069;
  --color-beni-light: #D4728A;
  --color-vermilion: #D3381C;

  /* Neutral */
  --color-muted: #949495;

  /* --- TYPOGRAPHY TOKENS --- */

  --font-display: 'Masada', 'Frank Ruhl Libre', serif;
  --font-body: 'Heebo', sans-serif;
  --font-english: 'Inter', sans-serif;
  --font-stamp: 'Guttman Haim', serif;

  --type-monument: clamp(3rem, 2rem + 8vw, 12rem);
  --type-event: clamp(2.2rem, 1.5rem + 4.5vw, 6rem);
  --type-manifesto: clamp(1.6rem, 1.2rem + 2.5vw, 3.5rem);
  --type-sub: clamp(1.1rem, 0.9rem + 1vw, 1.8rem);
  --type-body: clamp(0.9rem, 0.85rem + 0.25vw, 1.05rem);
  --type-small: clamp(0.7rem, 0.65rem + 0.2vw, 0.8rem);
  --type-micro: clamp(0.55rem, 0.5rem + 0.15vw, 0.65rem);

  /* --- SPACING TOKENS --- */

  --gutter: 1.5rem;
  --space-xs: clamp(0.5rem, 0.4rem + 0.5vw, 0.75rem);
  --space-s: clamp(1rem, 0.8rem + 1vw, 1.5rem);
  --space-m: clamp(2rem, 1.5rem + 2.5vw, 3.5rem);
  --space-l: clamp(4rem, 3rem + 5vw, 7rem);
  --space-xl: clamp(6rem, 4rem + 10vw, 14rem);

  /* --- MOTION TOKENS --- */

  --ease-ink: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-smooth: cubic-bezier(0.45, 0, 0.15, 1);
  --duration-fast: 0.2s;
  --duration-normal: 0.4s;
  --duration-slow: 0.8s;
}

@media (min-width: 1024px) {
  :root {
    --gutter: clamp(2rem, 1.5rem + 3vw, 6rem);
  }
}
```

---

## 17. Content Requirements

For CTO to build the page, the following content is needed per event:

### Upcoming Event
- Event name (Hebrew)
- Date (DD.MM.YYYY format)
- Location name (Hebrew + English)
- Artist names (1-5 names)
- One high-resolution photograph (minimum 1920px wide)
- Booking URL
- One manifesto fragment (1-2 sentences from Yaron's writing)

### Past Event
- Event name (Hebrew)
- Date
- Location
- One photograph
- Optional: link to documentation/gallery

### Global Content
- 5-8 manifesto sentences (extracted from Yaron's About text, broken into individual typographic moments)
- Brand name in Hebrew and English
- Contact email
- Social media URLs
- 1-2 video files (or embed URLs)

---

## 18. File Structure

```
/v6/
  index.html              (single file, all content)
  style.css               (all styles, no preprocessor needed)
  script.js               (GSAP + IntersectionObserver logic)
  /fonts/
    Masada-Medium.otf
    Masada-Demi.otf
    Masada-Bold.otf
    Guttman-Haim-Condensed.ttf
  /assets/
    /events/
      [all event photos, WebP + JPEG fallback]
    hanko-seal.svg          (vermilion seal mark)
    sumi-stroke.svg         (horizontal brushstroke for breathing spaces)
    og-image.jpg            (1200x630, for social sharing)
```

---

## 19. Summary of Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Site structure | Single continuous scroll | Board consensus: abolish section-based architecture |
| Primary visual | Photography | Real event photos are stronger than any illustration |
| Typography role | Architectural / Structural | Hebrew type IS the design, per Board recommendation |
| Sumi-e role | Texture / Atmosphere only | Repositioned from protagonist to supporting cast |
| Color system | Two alternating states (dark + washi) | Creates rhythm without boxes or dividers |
| Animations | Minimal (fade-in + Entry reveal) | "Radical structure, conventional usability" - no tech demos |
| Navigation | Conventional mobile hamburger + desktop links | Usability cannot be sacrificed for aesthetics |
| Event presentation | Full-viewport cinematic | Each event is an exhibition room, not a card |
| About section | Abolished | Manifesto woven between events as typographic moments |
| Gallery section | Abolished | Photos live only as full-bleed event backgrounds |
| Mobile priority | 80% of design decisions | 80% of traffic is mobile |
| Performance | < 500KB initial payload | Mid-range Android on 4G must feel instant |
| 3D / WebGL | None | Heavy, unnecessary, drains mobile battery |
| Scroll behavior | Native, no hijacking | Predictable, accessible, battery-friendly |

---

*This document is the complete visual specification. CTO should be able to build the entire website from this document alone, without needing to consult additional visual references. Every CSS value, every layout decision, every interaction behavior is defined here.*
