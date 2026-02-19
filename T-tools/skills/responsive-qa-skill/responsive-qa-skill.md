# Responsive QA Skill - Sol Therapy Website

> **Gatekeeper's complete checklist for responsive website quality assurance.**
> 10 sections, 130+ checkpoints. Sol Therapy specific.

---

## How to Use This Skill

1. Open the website in Chrome MCP
2. Test at each breakpoint (Desktop 1440, Desktop 1024, Tablet 768, Mobile 390, Mobile 320)
3. Go through each section below
4. Mark each checkpoint PASS/FAIL
5. Any FAIL = document with screenshot + description
6. Report findings in Gatekeeper review format

### Breakpoints Reference (Sol Therapy)

| Name | Width | CSS Trigger |
|------|-------|-------------|
| Desktop Large | 1440px | Default styles |
| Desktop | 1024px | `@media (min-width: 1024px)` |
| Tablet | 640px - 1023px | `@media (max-width: 1023px)` |
| Mobile | 390px | `@media (max-width: 639px)` |
| Mobile Small | 320px | `@media (max-width: 639px)` |

### Tools

- **Chrome MCP** - `resize_window` for exact viewport sizes
- **Chrome MCP** - `screenshot` at each breakpoint
- **Chrome MCP** - `read_page` for accessibility tree
- **Chrome MCP** - `javascript_tool` for computed styles check

---

## Section 1: Layout & Grid Integrity

> Does the layout hold together at every breakpoint?

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| L-01 | No horizontal overflow (body wider than viewport) | [ ] | [ ] | [ ] |
| L-02 | No content bleeding outside containers | [ ] | [ ] | [ ] |
| L-03 | Grid columns collapse correctly (3->2->1) | [ ] | [ ] | [ ] |
| L-04 | Container padding increases on mobile | [ ] | [ ] | [ ] |
| L-05 | No overlapping elements at any breakpoint | [ ] | [ ] | [ ] |
| L-06 | Sections stack vertically on mobile without gaps | [ ] | [ ] | [ ] |
| L-07 | Max-width constraints respected (container, text blocks) | [ ] | [ ] | [ ] |
| L-08 | Flex/grid items wrap correctly when space runs out | [ ] | [ ] | [ ] |
| L-09 | No empty white/black bars at viewport edges | [ ] | [ ] | [ ] |
| L-10 | Sticky/fixed elements don't obstruct content on small screens | [ ] | [ ] | [ ] |
| L-11 | Full-bleed sections span 100% width at all sizes | [ ] | [ ] | [ ] |
| L-12 | About grid: switches from 2-col to 1-col on tablet | [ ] | [ ] | [ ] |
| L-13 | Events grid: 3-col -> 2-col -> 1-col | [ ] | [ ] | [ ] |
| L-14 | Gallery grid: 3-col -> 2-col -> 1-col | [ ] | [ ] | [ ] |
| L-15 | Footer grid: 3-col -> 2-col -> 1-col | [ ] | [ ] | [ ] |

**Sol Therapy Specific:**
- About section: image reorders to top on mobile (order: 1)
- Trust bar: switches from row to column on mobile
- Event card actions: stack vertically on mobile

---

## Section 2: Typography & Readability

> Is text readable and properly scaled at every size?

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| T-01 | Body text readable without zooming (min 16px equivalent) | [ ] | [ ] | [ ] |
| T-02 | Headings scale down proportionally on smaller screens | [ ] | [ ] | [ ] |
| T-03 | Hero title: doesn't overflow or wrap awkwardly | [ ] | [ ] | [ ] |
| T-04 | Line length: max 65-75 characters per line (desktop) | [ ] | [ ] | [ ] |
| T-05 | Line height: adequate spacing (1.5-1.7 for body) | [ ] | [ ] | [ ] |
| T-06 | No text truncation or hidden overflow | [ ] | [ ] | [ ] |
| T-07 | Hebrew text: proper RTL alignment everywhere | [ ] | [ ] | [ ] |
| T-08 | Hebrew text: no mixed-direction issues (numbers, English terms) | [ ] | [ ] | [ ] |
| T-09 | Font loading: no FOUT/FOIT (flash of unstyled/invisible text) | [ ] | [ ] | [ ] |
| T-10 | Section titles: don't break at awkward points | [ ] | [ ] | [ ] |
| T-11 | Button text: fully visible, not clipped | [ ] | [ ] | [ ] |
| T-12 | Masada font renders correctly at all sizes | [ ] | [ ] | [ ] |
| T-13 | Heebo font renders correctly for body text | [ ] | [ ] | [ ] |

**Sol Therapy Font Stack:**
- Headings: Masada (custom) -> serif fallback
- Body: Heebo -> system sans-serif
- Micro-type: Heebo at smaller weight

---

## Section 3: Navigation & Header

> Does navigation work flawlessly across devices?

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| N-01 | Desktop: horizontal nav fully visible | [ ] | - | - |
| N-02 | Tablet/Mobile: hamburger menu appears | - | [ ] | [ ] |
| N-03 | Mobile menu opens/closes smoothly | - | [ ] | [ ] |
| N-04 | Mobile menu drawer slides from right (RTL) | - | [ ] | [ ] |
| N-05 | Mobile menu backdrop dims background | - | [ ] | [ ] |
| N-06 | Mobile menu: all links visible without scrolling | - | [ ] | [ ] |
| N-07 | Clicking nav link closes mobile menu | - | [ ] | [ ] |
| N-08 | Clicking backdrop closes mobile menu | - | [ ] | [ ] |
| N-09 | Header sticky behavior works on scroll | [ ] | [ ] | [ ] |
| N-10 | Logo readable at mobile size | [ ] | [ ] | [ ] |
| N-11 | Menu toggle animation (hamburger -> X) works | - | [ ] | [ ] |
| N-12 | Focus trap inside open mobile menu | - | [ ] | [ ] |
| N-13 | Escape key closes mobile menu | - | [ ] | [ ] |

---

## Section 4: Images & Media

> Do images and media adapt correctly?

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| M-01 | Images resize proportionally (no distortion) | [ ] | [ ] | [ ] |
| M-02 | Images don't overflow containers | [ ] | [ ] | [ ] |
| M-03 | Responsive images: srcset loads appropriate size | [ ] | [ ] | [ ] |
| M-04 | Lazy loading works (images below fold load on scroll) | [ ] | [ ] | [ ] |
| M-05 | Videos scale down without breaking layout | [ ] | [ ] | [ ] |
| M-06 | Video controls accessible at all sizes | [ ] | [ ] | [ ] |
| M-07 | Gallery images: proper aspect ratios maintained | [ ] | [ ] | [ ] |
| M-08 | Hero background/video covers viewport | [ ] | [ ] | [ ] |
| M-09 | Illustrations (sumi-e) scale appropriately | [ ] | [ ] | [ ] |
| M-10 | Image breaks (illustration dividers) responsive | [ ] | [ ] | [ ] |
| M-11 | Mix-blend-mode effects work on all elements | [ ] | [ ] | [ ] |
| M-12 | No broken image icons visible | [ ] | [ ] | [ ] |
| M-13 | width/height attributes set (CLS prevention) | [ ] | [ ] | [ ] |
| M-14 | decoding="async" on non-critical images | [ ] | [ ] | [ ] |

**Sol Therapy Specific:**
- Sumi-e illustrations use mix-blend-mode: multiply
- Illustration opacity changes between desktop and mobile
- Image breaks scale with clamp() values

---

## Section 5: Touch & Interaction

> Are interactive elements usable on touch devices?

| ID | Checkpoint | Mobile | Tablet |
|----|-----------|--------|--------|
| I-01 | Tap targets minimum 44x44px (WCAG) | [ ] | [ ] |
| I-02 | Buttons have adequate spacing between them | [ ] | [ ] |
| I-03 | Links have sufficient tap area | [ ] | [ ] |
| I-04 | No hover-only interactions (must work on tap) | [ ] | [ ] |
| I-05 | Scroll works naturally (no scroll hijacking) | [ ] | [ ] |
| I-06 | Form inputs easy to tap and fill | [ ] | [ ] |
| I-07 | Newsletter form: fields and button stack on mobile | [ ] | [ ] |
| I-08 | Event card buttons: full width on mobile | [ ] | [ ] |
| I-09 | Gallery filter buttons: adequate size on mobile | [ ] | [ ] |
| I-10 | Modal close button: easy to reach on mobile | [ ] | [ ] |
| I-11 | No accidental double-tap zoom on interactive elements | [ ] | [ ] |
| I-12 | Swipe doesn't interfere with page scroll | [ ] | [ ] |

---

## Section 6: RTL (Right-to-Left) Specific

> Hebrew RTL requirements - critical for Sol Therapy.

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| R-01 | `dir="rtl"` set on html element | [ ] | [ ] | [ ] |
| R-02 | Text alignment: right-aligned by default | [ ] | [ ] | [ ] |
| R-03 | Flexbox direction: reversed for RTL (row-reverse or correct logical properties) | [ ] | [ ] | [ ] |
| R-04 | Grid: flows right-to-left | [ ] | [ ] | [ ] |
| R-05 | Icons/arrows: mirrored for RTL where appropriate | [ ] | [ ] | [ ] |
| R-06 | Mobile menu slides from RIGHT (not left) | - | [ ] | [ ] |
| R-07 | Padding/margin: use logical properties (inline-start/end) or flipped correctly | [ ] | [ ] | [ ] |
| R-08 | Modal close button: positioned LEFT (start) for RTL | [ ] | [ ] | [ ] |
| R-09 | Form labels align correctly for RTL | [ ] | [ ] | [ ] |
| R-10 | Breadcrumbs/lists: correct directional markers | [ ] | [ ] | [ ] |
| R-11 | Numbers display correctly within Hebrew text | [ ] | [ ] | [ ] |
| R-12 | Mixed Hebrew/English content doesn't break layout | [ ] | [ ] | [ ] |
| R-13 | Scroll animations respect RTL direction | [ ] | [ ] | [ ] |

---

## Section 7: Performance (Mobile)

> Mobile performance is critical - users on 4G/3G.

| ID | Checkpoint | Target | How to Check |
|----|-----------|--------|-------------|
| P-01 | First Contentful Paint < 2.5s on 4G | < 2.5s | Chrome DevTools Lighthouse |
| P-02 | Largest Contentful Paint < 4s on 4G | < 4s | Chrome DevTools Lighthouse |
| P-03 | Cumulative Layout Shift < 0.1 | < 0.1 | Chrome DevTools Lighthouse |
| P-04 | Total page weight < 3MB (mobile) | < 3MB | Network tab |
| P-05 | Images account for < 60% of page weight | < 60% | Network tab |
| P-06 | No render-blocking resources after critical CSS | [ ] | Coverage tab |
| P-07 | Fonts preloaded | [ ] | Network tab |
| P-08 | CSS minified in production | [ ] | Source check |
| P-09 | JavaScript deferred or async | [ ] | Source check |
| P-10 | GSAP animations don't cause jank (60fps) | [ ] | Performance tab |
| P-11 | Scroll-driven animations smooth on mobile | [ ] | Manual scroll test |
| P-12 | No memory leaks from animations (check after 1min scroll) | [ ] | Performance tab |

**Sol Therapy Specific:**
- GSAP ScrollTrigger used for section animations
- Video autoplay might impact mobile performance
- Custom audio player Canvas rendering

---

## Section 8: Accessibility (Responsive)

> Accessibility at every viewport size.

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| A-01 | Focus indicators visible at all sizes | [ ] | [ ] | [ ] |
| A-02 | Tab order logical after responsive reflow | [ ] | [ ] | [ ] |
| A-03 | Skip-to-content link works | [ ] | [ ] | [ ] |
| A-04 | Color contrast ratio >= 4.5:1 (text) | [ ] | [ ] | [ ] |
| A-05 | Color contrast ratio >= 3:1 (large text, UI) | [ ] | [ ] | [ ] |
| A-06 | Images have alt text | [ ] | [ ] | [ ] |
| A-07 | Decorative images have alt="" | [ ] | [ ] | [ ] |
| A-08 | ARIA landmarks present (main, nav, footer) | [ ] | [ ] | [ ] |
| A-09 | Heading hierarchy correct (h1 -> h2 -> h3, no skips) | [ ] | [ ] | [ ] |
| A-10 | prefers-reduced-motion respected | [ ] | [ ] | [ ] |
| A-11 | prefers-contrast: high supported | [ ] | [ ] | [ ] |
| A-12 | Keyboard navigation works fully | [ ] | [ ] | [ ] |
| A-13 | Screen reader: content order makes sense after reflow | [ ] | [ ] | [ ] |
| A-14 | Zoom to 200% doesn't break layout | [ ] | [ ] | [ ] |
| A-15 | Touch target size meets WCAG 2.5.5 (44x44 min) | - | [ ] | [ ] |

---

## Section 9: Cross-Browser & Device

> Testing across real-world conditions.

| ID | Checkpoint | Chrome | Safari | Firefox |
|----|-----------|--------|--------|---------|
| B-01 | Layout renders correctly | [ ] | [ ] | [ ] |
| B-02 | Fonts render correctly | [ ] | [ ] | [ ] |
| B-03 | Animations play smoothly | [ ] | [ ] | [ ] |
| B-04 | Videos play correctly | [ ] | [ ] | [ ] |
| B-05 | Forms submit correctly | [ ] | [ ] | [ ] |
| B-06 | `100svh` supported (or fallback) | [ ] | [ ] | [ ] |
| B-07 | CSS `clamp()` supported (or fallback) | [ ] | [ ] | [ ] |
| B-08 | CSS custom properties work | [ ] | [ ] | [ ] |
| B-09 | GSAP animations work | [ ] | [ ] | [ ] |
| B-10 | RTL rendering correct | [ ] | [ ] | [ ] |

### Device-Specific

| ID | Checkpoint | iPhone | Android | iPad |
|----|-----------|--------|---------|------|
| D-01 | Safari bottom bar doesn't hide content | [ ] | - | - |
| D-02 | Viewport meta tag correct | [ ] | [ ] | [ ] |
| D-03 | Touch scrolling smooth (momentum) | [ ] | [ ] | [ ] |
| D-04 | Orientation change: landscape works | [ ] | [ ] | [ ] |
| D-05 | Notch/safe-area-inset handled | [ ] | [ ] | - |

---

## Section 10: Sol Therapy Design System Compliance

> Does responsive behavior match our design system?

| ID | Checkpoint | Desktop | Tablet | Mobile |
|----|-----------|---------|--------|--------|
| S-01 | Colors match design tokens (tokens.css) | [ ] | [ ] | [ ] |
| S-02 | Spacing uses design token variables | [ ] | [ ] | [ ] |
| S-03 | Washi paper background visible at all sizes | [ ] | [ ] | [ ] |
| S-04 | Ink wash textures render correctly | [ ] | [ ] | [ ] |
| S-05 | Japanese/Zen aesthetic maintained on mobile (not stripped) | [ ] | [ ] | [ ] |
| S-06 | Negative space preserved (not cramped on mobile) | [ ] | [ ] | [ ] |
| S-07 | Print styles work (`@media print`) | [ ] | - | - |
| S-08 | Dark mode preference doesn't break anything | [ ] | [ ] | [ ] |
| S-09 | Animation feels calm, not hyperactive (Zen pace) | [ ] | [ ] | [ ] |
| S-10 | Overall "museum quality" feel preserved at all sizes | [ ] | [ ] | [ ] |

**Critical Sol Therapy Rule:**
Mobile should feel like a smaller version of the same experience - not a stripped-down alternative. The Zen atmosphere, negative space, and texture must survive the transition to small screens.

---

## QA Report Format

After completing all checks, provide a report:

```markdown
## Responsive QA Report

**URL:** [site URL]
**Date:** [date]
**Tester:** Gatekeeper Agent
**Breakpoints tested:** [list]

### Summary
| Section | Pass | Fail | Total |
|---------|------|------|-------|
| Layout & Grid | X | X | 15 |
| Typography | X | X | 13 |
| Navigation | X | X | 13 |
| Images & Media | X | X | 14 |
| Touch & Interaction | X | X | 12 |
| RTL | X | X | 13 |
| Performance | X | X | 12 |
| Accessibility | X | X | 15 |
| Cross-Browser | X | X | 15 |
| Design System | X | X | 10 |
| **TOTAL** | **X** | **X** | **132** |

### Critical Failures (must fix before deploy)
1. [ID] [description] [screenshot]

### Medium Issues (fix in next iteration)
1. [ID] [description]

### Minor Issues (nice to have)
1. [ID] [description]

### Verdict: APPROVED / REVISIONS NEEDED / BLOCKED
```

---

## Version History

| Date | Change |
|------|--------|
| 2026-02-16 | Created - 10 sections, 132 checkpoints, Sol Therapy specific (Session 52) |
| 2026-02-19 | Rebuilt after file loss - reconstructed from session archive context + website analysis |
