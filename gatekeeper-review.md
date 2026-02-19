# Gatekeeper Review: Sol Therapy Website v5 Prototype

**Status:** APPROVED WITH NOTES
**Date:** 13.02.2026
**Review Round:** 1/3

---

## Context Card Reference

- **Original Request:** Complete redesign from v4 to v5 - "break the spec and be original." Yaron's directive: "keep working until there's something to show me and all agents stand behind it."
- **Agents Involved:** Team Sync (coordination), Illustrator (Replicate asset generation), CTO (full HTML/CSS/JS build), Gatekeeper (this review)
- **Plan:** inherited-rolling-brooks.md (v5 redesign plan - approved)
- **Output:** O-output/website-sol-therapy/index.html (single-file prototype, ~2,090 lines)
- **Visual Inspection:** Complete - all 8 sections verified in Chrome MCP
- **Console:** Clean - zero site errors (60 extension errors only)

---

## v5 Plan Compliance - Section by Section

### Section 1: Hero - "The Threshold"
- [x] Zero images - pure typography + shader
- [x] Three.js WebGL shader with FBM noise, mouse-reactive mist
- [x] "Sol Therapy" as HTML text, Frank Ruhl Libre 300
- [x] SplitText chars reveal with stagger 0.06s
- [x] Scroll-dissolve: chars scatter with random y/x offsets + blur, scrubbed to scroll (30% start)
- [x] Tagline as museum caption, vertical writing-mode, bottom-left
- [x] Ink drop scroll indicator with drip animation
- [x] Bokashi gradient 28vh at bottom (adjusted from 40vh for visibility)
- [x] Brand centered on indigo (justify-content: center, padding-top: 12vh)

### Section 2: About - "The Wall Text"
- [x] Single-column layout (removed v4 two-column grid)
- [x] Massive pull quote: Frank Ruhl Libre 300 at clamp(2.5rem, 5vw, 4.5rem)
- [x] SplitText word-level reveal, stagger 0.04s
- [x] Manifesto body at --step-0, opacity 0.6, max-width 480px
- [x] Vermilion Hanko seal positioned absolute, bottom-left, rotated -5deg
- [x] back.out(3) elastic stamp animation
- [x] Breathing micro-animation (scale 1.003, 4s, yoyo)

### Section 2.5: Image Break 1 - "The Mist"
- [x] Full-viewport (70vh) Sumi-e mountain illustration
- [x] Generated via Replicate Flux Pro Ultra (assets/image-break-mountains.jpg)
- [x] mask-image gradient fade at top and bottom edges (30% height)
- [x] Parallax scrub (yPercent: -15)
- [x] clip-path reveal animation on scroll (inset 0 0 0 100% to 0%)
- [x] ScrollTrigger once: true (verified - fires correctly)

### Section 3: Events - "The Calendar Stone"
- [x] Complete rework from v4 - no grid, typographic monument style
- [x] Each event is full-width row with massive name (var(--step-event))
- [x] Date as margin note (top-left in RTL, 0.65rem, Beni, letter-spacing 0.3em)
- [x] Details below name (0.75rem, muted, middle-dot separated)
- [x] CTA hidden by default, fades in on hover
- [x] Hover: letter-spacing expands, underline grows, ink fill sweep
- [x] Separator lines with scaleX animation (right origin for RTL)
- [x] 2 events: Pastoral retreat (live link) + Moa (Sold Out)
- [x] Trust colophon integrated: venue names single line, 0.65rem, slash-separated, opacity 0.35

### Section 4: Gallery - "The Scroll Painting"
- [x] Emakimono horizontal strip with infinite GSAP drift
- [x] Dynamic JS cloning (removed hardcoded HTML clones)
- [x] Drag/touch/wheel interaction
- [x] Edge masks (CSS mask-image)
- [x] Hover slows drift to 0
- [x] Velocity skew on items (max 3deg)
- [x] Captions as persistent museum labels below images
- [x] Section label as vertical text on right edge, rotated 90deg
- [x] 6 gallery items (portrait/landscape/wide mix)
- [x] direction: ltr on strip and track (RTL fix for GSAP wrap)

### Section 5: Sound - "The Listening Room"
- [x] Pinned full-viewport (ScrollTrigger pin, 100% distance)
- [x] Bokashi cream-to-indigo before, indigo-to-cream after (25vh each)
- [x] Three.js frequency visualization shader (cream on indigo, opacity 0.06)
- [x] Real SoundCloud embed (placeholder track - needs Yaron's actual URL)
- [x] Asymmetric layout: heading + body + player + link
- [x] Content opacity scrubbed to scroll (0 -> 1 -> 0)
- [x] "Full set on SoundCloud" secondary link

### Section 5.5: Image Break 2 - "The Path"
- [x] Full-viewport (70vh) green hills watercolor
- [x] Generated via Replicate Flux Pro Ultra (assets/image-break-hills.jpg)
- [x] Same mask-image + parallax + clip-path reveal as Break 1
- [x] ScrollTrigger once: true (verified - fires correctly)

### Section 6: Footer - "The Seal"
- [x] Minimal centered layout (removed v4 two-column grid)
- [x] "Join the community" invitation line
- [x] Email form with growing underline on focus
- [x] Contact: plain text link hello@soltherapy.co.il
- [x] Hanko stamp: 56px, stamps down with back.out(3) elastic on scroll-in
- [x] Social + copyright: single tiny line (Instagram, TikTok, Sol Therapy 2026)

### Global Systems
- [x] Custom cursor + magnetic elements (gsap.quickTo)
- [x] Scroll progress bar (thin, Sol Green, top-right)
- [x] Floating CTA "tickets" button (bottom-left, appears after hero)
- [x] Scroll velocity tracker (for speed-dependent effects)
- [x] gsap.matchMedia() wrapping all animations
- [x] Washi paper texture SVG overlay
- [x] Nav: transparent on hero, frosted cream glass after scroll

---

## Voice DNA Compliance

### Hebrew Text Review

| Text | Location | Voice Mode | Verdict |
|------|----------|------------|---------|
| "מדיטציות סאונד עמוקות" | Hero tagline + meta desc | B (manifesto) | PASS - concise, sensory |
| "הגוף הופך לכלי תהודה. הקשב משתנה. משהו משתחרר." | About pull quote | B (manifesto) | PASS - Yaron's vocabulary (תהודה), short rhythmic sentences, sensory |
| "מיזם סול תרפי נשען על פרקטיקה המלווה את התרבות האנושית..." | About manifesto | B (manifesto) | PASS - matches gold standard reference text from voice-dna.md |
| "מסעות קרובים" | Events heading | A (announcement) | PASS - direct, not salesy |
| "ריטריט סול תרפי - פסטורל / מואה" | Event names | A | PASS - plain naming, hyphen not em dash |
| "הצליל שמלווה אותנו" | Sound heading | B | PASS - poetic, intimate |
| "תדרים נמוכים, קערות שירה, שכבות אמביינט" | Sound body | B | PASS - uses "תדרים" (key vocab), sensory layering |
| "שישים שניות שמזמינות להישאר" | Sound body | B | PASS - inviting not selling |
| "הצטרפו לקהילה" | Footer invite | A | PASS - warm, direct |
| "להזמנת חדרים" / "לכרטיסים" | CTAs | A | PASS - functional, not pushy |
| "לסט המלא בסאונדקלאוד" | Sound link | A | PASS - informational |
| "התדר שלנו / מסעות / ארכיון / צליל" | Nav links | - | PASS - minimal, thematic |
| "ארכיון ויזואלי" | Gallery label | - | PASS - museum language |
| "דלג לתוכן" | Skip link | - | PASS - accessibility |
| "ניווט ראשי" | Nav aria-label | - | PASS |

### Voice Rule Compliance
- [x] **No emoji** - zero in entire prototype
- [x] **No em dash** - regular hyphens only (verified: "ריטריט סול תרפי - פסטורל")
- [x] **No superlatives** ("best / number 1 / greatest")
- [x] **No sales pressure** ("hurry! / won't believe!")
- [x] **No wellness cliches** ("energies" / "vibrations")
- [x] Yaron's vocabulary present: תהודה, תדרים, מדיטטיביים, צלילה, אימרסיביות, זן-בודהיזם, מרקמים (via "שכבות אמביינט")
- [x] Sensory descriptions: "הגוף הופך לכלי תהודה", "תדרים נמוכים, קערות שירה, שכבות אמביינט"
- [x] Manifesto text matches Yaron's own writing from voice-dna.md Mode B reference
- [x] Sophisticated but accessible tone
- [x] Hebrew reads naturally
- [x] No hook-style openings in announcements (direct and plain)

---

## Visual / Aesthetic Checklist

### Palette Compliance
- [x] Sol Green primary (#588475) - headings, nav, cursor, CTA, progress bar
- [x] Beni accent (#BE5069) - dates, event CTAs
- [x] Washi background (#F2EAD3) - main bg, hero text color
- [x] Washi-warm (#EDE5CE) - gallery section distinction
- [x] Indigo dark (#264348) - hero bg, sound section bg
- [x] Vermilion (#D3381C) - Hanko stamps only
- [x] **No pure white** (#FFFFFF) - always Washi cream
- [x] **No pure black** (#000000) - darkest is Indigo (#264348)

### Typography
- [x] Frank Ruhl Libre 300 for all display/headings
- [x] Heebo for body text
- [x] Inter for English elements (nav brand, footer meta)
- [x] Fluid type scale with clamp() throughout
- [x] Giant hero: clamp(3rem, 2rem + 5vw, 6rem)
- [x] Giant event names: clamp(2.5rem, 2rem + 3vw, 5.5rem)

### Japanese-Inspired Aesthetic (from taste profile)
- [x] **Ma (negative space)** - generous clamp padding, min-height sections, 60%+ whitespace
- [x] **Washi texture** - SVG fractalNoise overlay on body::before
- [x] **Bokashi gradients** - hero-to-cream, cream-to-indigo, indigo-to-cream (smooth transitions)
- [x] **Hanko stamps** - Vermilion border/text, slight rotation, back.out elastic
- [x] **Easing** - power3.out / power4.out throughout (ink-flow feel)
- [x] **2 Sumi-e illustrations** - mountains (image break 1) + green hills (image break 2)
- [x] **Museum labels** - gallery captions, vertical text, small uppercase with letter-spacing

### 5-Point Visual Check (from taste profile)
| # | Criterion | Pass? |
|---|-----------|-------|
| 1 | **Depth layers** - multiple visual planes | [x] - shader bg, content, bokashi overlays, washi texture |
| 2 | **Tonal variation** - multiple tones of same color | [x] - green/green-dark/green-light, indigo/indigo-light |
| 3 | **Texture** - visible material quality | [x] - washi SVG noise, Sumi-e brushwork in image breaks |
| 4 | **Atmosphere** - sense of space and mood | [x] - hero mist shader, pinned sound room, bokashi gradients |
| 5 | **Human feel** - not "computer generated it" | [x] - typography-driven, hand-picked easing, museum spatial metaphors |

**Result: 5/5 PASS**

---

## Technical / Accessibility Checklist

- [x] **Reduced motion** - `@media (prefers-reduced-motion: reduce)` at line 1065 (CSS) + JS check at line 1300 + gsap.matchMedia() wrapping
- [x] **Semantic HTML** - h1 > h2 > h3 hierarchy, section, nav, footer, article
- [x] **lang="he" dir="rtl"** - on html element
- [x] **ARIA** - nav aria-label, decorative elements aria-hidden, form aria-label, shader containers aria-hidden
- [x] **alt text** - meaningful alt on gallery images, empty alt on decorative image breaks
- [x] **Responsive** - 3 breakpoints: 991px, 767px, 478px
- [x] **Font preconnect** - Google Fonts preconnect headers
- [x] **meta description** - present and meaningful
- [x] **Nav behavior** - transparent on hero, frosted cream glass after scroll
- [x] **Skip-to-content link** - present at line 1082 (sr-only, positioned offscreen)
- [x] **direction: ltr** - on all English text elements (nav brand, gallery strip, footer meta)
- [x] **Custom cursor** - hidden on mobile (767px breakpoint)
- [x] **Console clean** - zero JS errors from site code
- [ ] **Explicit focus styles** - using browser defaults (note for production)
- [ ] **`<picture>` with AVIF/WebP** - not applicable for prototype (Unsplash URLs + local JPGs)
- [ ] **Color contrast audit** - needs WCAG AA verification tool (note for production)

---

## What Changed from v4

| Aspect | v4 | v5 |
|--------|----|----|
| Architecture | 7 sections, same rhythm | 8 moments, varied rhythm with image breaks |
| Hero | Logo PNG + two-line tagline | Pure typography + WebGL shader, no images |
| About | Two-column grid + Sumi-e image | Single pull quote + manifesto |
| Events | 3-column catalog cards | Typographic monument, full-width rows |
| Trust | Separate section | Absorbed into events as colophon line |
| Sound | Fake audio player | Pinned full-viewport room + real SoundCloud |
| Gallery | Hardcoded clones | Dynamic JS cloning + velocity skew |
| Footer | Two-column grid | Minimal centered seal |
| Image breaks | None | 2 new full-bleed Sumi-e illustrations |
| Scroll dissolve | None | Hero chars scatter with blur on scroll |
| WebGL | Basic shader | Mouse-reactive mist (hero) + frequency viz (sound) |

---

## Notes for Production (non-blocking)

1. **Custom focus styles** - add visible focus rings matching Sol Green
2. **`<picture>` element** - Astro Image handles this automatically
3. **Gallery images** - replace Unsplash with actual event photography
4. **SoundCloud embed** - replace placeholder track with Yaron's actual URL
5. **Color contrast** - run WCAG AA audit on all text/background combinations
6. **Image optimization** - compress Replicate-generated JPGs to WebP/AVIF
7. **Newsletter form** - connect to mailing service
8. **Performance** - lazy-load Three.js shaders, consider intersection observer

---

## Decision

**APPROVED WITH NOTES - Ready for presentation to Yaron.**

The v5 prototype successfully transforms the website from "webpage with sections" to "scroll painting you enter." Each of the 8 moments has its own spatial identity:

- **Hero** is a threshold - pure typography dissolving into mist
- **About** is a museum wall - one massive statement
- **Image breaks** are pauses - breathing moments between intense sections
- **Events** is a monument - typography as architecture
- **Gallery** is an emakimono - endless horizontal drift
- **Sound** is a room - you stop, you're immersed, you exit
- **Footer** is a seal - one stamp, done

The Hebrew text faithfully follows Voice DNA Mode B, using Yaron's own vocabulary and phrasing patterns. The manifesto text is drawn directly from Yaron's reference writing. Zero emoji, zero em dashes, zero sales pressure, zero wellness cliches.

The Japanese-inspired aesthetic is cohesive - Washi texture, Bokashi gradients, Sumi-e illustrations, Hanko stamps, Ma negative space, and museum-label typography create a unified visual language.

**Key note:** SoundCloud embed needs Yaron's actual track URL to fully demonstrate the sound section experience.
