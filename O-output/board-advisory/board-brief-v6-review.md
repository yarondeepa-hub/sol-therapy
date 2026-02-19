# Board Deliberation Brief: Website v6 - Harsh Criticism Round

**Date:** 2026-02-15
**Requested by:** Yaron (CEO of Sol Therapy)
**Type:** Follow-up to Board deliberation of 2026-02-14

---

## The Question

You previously analyzed our website (v5) and diagnosed "template DNA" as the core problem - the same Hero-About-Cards-Gallery-Footer skeleton as every WordPress theme, regardless of surface treatment.

We rebuilt the entire site from scratch based on your recommendations. v6 is live.

**We need harsh criticism:**
1. Where does the site still fall short?
2. What is missing?
3. How do we elevate this to an exceptional level?

Do not be polite. Be specific. Tell us what needs to change and why.

---

## Live URLs - Analyze These

**v5 (before your recommendations):**
https://sol-therapy.netlify.app/index-v5-backup.html

**v6 (after rebuild based on your recommendations):**
https://sol-therapy.netlify.app/

Both are live, fully functional, with all assets and animations. Scroll through each completely. Compare the structural DNA, not just the surface.

---

## What You Said Last Time (Summary)

### Your Diagnosis (unanimous)
The problem was 100% structural/architectural, not decorative. The v5 site followed standard website DNA: Hero -> About section -> Image break -> Event cards -> Gallery strip -> Audio section -> Footer. No amount of Sumi-e textures, GSAP animations, or paper filters would change what it fundamentally IS.

### Your 6 Consensus Points
1. The problem is structural/architectural, not decorative - template DNA cannot be fixed with surface treatment
2. Abolish the standalone "About" section - weave Yaron's manifesto into event descriptions
3. Events should be full-viewport experiences (magazine spread / exhibition poster), not cards in a grid
4. Massive structural Hebrew typography as the primary visual identity
5. Continuous vertical flow rather than stacked boxed sections
6. Photography quality is a critical gap

### Your Contested Points
1. How experimental should interactions be? (Gemini: ink-bleed-on-scroll / Claude: "developer's fever dream" / GPT: sided with Claude on usability)
2. Auto-playing ambient sound (Claude proposed, Gemini flagged as "UX hostility")
3. Grid layouts (GPT recommended, both Gemini and Claude rejected as "another template trap")

### Your Guiding Principle
"Radical structure, conventional usability" - the spatial experience should feel like nothing else, but the user should always know where they are and how to act.

### Your Open Questions
1. Photography situation? Stock vs real
2. Portfolio site or product site?
3. Mobile experience? 70%+ traffic
4. Does Yaron have a "dream URL"?
5. Content inventory for events?

---

## What Changed: v5 vs v6

### Structural Architecture

| Aspect | v5 (Before) | v6 (After) |
|--------|-------------|------------|
| **Architecture** | 8 discrete sections stacked vertically: Hero, About, Image Break, Events, Gallery, Sound, Image Break, Footer | Continuous scroll journey with no sections - Entry, Manifesto Thread, Events as full-viewport experiences, Breathing Spaces, Closing |
| **About section** | Standalone section with 3-paragraph manifesto + pull quote | Abolished. Manifesto woven as single sentences between events (Manifesto Thread) |
| **Events** | Two event cards side by side in a grid | Full-viewport cinematic experiences - each event takes over the entire screen with full-bleed photography |
| **Gallery** | Horizontal scroll strip (Emakimono) with stock Unsplash photos | Removed as separate section. Photography IS the events, not a gallery beside them |
| **Sound** | Dedicated audio section with custom canvas waveform player | Integrated into event context, not a standalone section |
| **Footer** | Standard footer with newsletter, email, social links | Closing section that mirrors Entry - dark, brand name, minimal |

### Visual Identity

| Aspect | v5 (Before) | v6 (After) |
|--------|-------------|------------|
| **Typography** | Frank Ruhl Libre + Heebo (Google Fonts) | Masada (self-hosted, 3 weights) + Guttman Haim + Hadassah Friedlaender + Heebo + DM Mono - Hebrew typography as architecture |
| **Color** | Teal gradient hero, washi throughout | Two alternating color states: Dark (real photography) and Washi (breathing spaces). No gradients |
| **Photography** | Unsplash stock photos, AI Sumi-e illustrations | Real event photography from Yaron's events (8 optimized photos + 2 videos) |
| **Illustrations** | Sumi-e mountain + hills as primary visual identity | Sumi-e elements as texture/accent, not the visual identity. Photography IS the identity |
| **Animations** | GSAP ScrollTrigger: fade-up, stagger, parallax, SplitText | GSAP ScrollTrigger: parallax on photographs, fade-up on text, clip-path reveals, stagger on manifesto lines |

### Technical

| Aspect | v5 (Before) | v6 (After) |
|--------|-------------|------------|
| **Size** | ~2,205 lines HTML | ~1,587 lines HTML |
| **Fonts** | Google Fonts only | 5 self-hosted Hebrew fonts (Masada, Guttman Haim, Hadassah Friedlaender, HaimG) + Google (Heebo, Inter, DM Mono) |
| **Images** | Unsplash stock + 2 AI illustrations | 8 real event photos (responsive srcset, 3 sizes each) + 2 videos |
| **Dependencies** | GSAP + Three.js | GSAP only (Three.js removed - unnecessary complexity) |
| **Mobile** | Responsive but desktop-first thinking | Mobile-first architecture per Illustrator spec |

### What We Specifically Adopted from Your Recommendations

| Your Recommendation | What We Did |
|---------------------|-------------|
| "Kill the brochure" | Rebuilt from scratch. No Hero-About-Cards-Gallery-Footer skeleton |
| "Abolish About section" | Manifesto Thread - single sentences woven between events |
| "Events as full-viewport cinematic experiences" | Each event is 100vh minimum with full-bleed photography |
| "Massive structural Hebrew typography" | Masada font at massive sizes as the primary visual landmark |
| "Continuous vertical flow" | No boxed sections. Scroll journey with breathing spaces |
| "Two color states (dark + washi)" | Alternating dark (photography) and washi (breathing) states |
| "Real photography, not stock" | 8 real event photos from Yaron + 2 videos |
| "Radical structure, conventional usability" | Governing principle for all decisions |
| "Content IS the design" | Events ARE the visual identity. Photography IS the design |

### What We Did NOT Do (Deliberately)

| Suggestion | Why Not |
|-----------|---------|
| Ink-bleed on scroll velocity (Gemini) | Consensus was this would feel like a tech demo, not a meditation brand |
| Hanko seal replacing navbar (Gemini) | Functionally hostile - visitors need to book retreats, not solve interaction puzzles |
| Auto-playing ambient sound (Claude) | Gemini correctly flagged as UX hostility. Sound is opt-in |
| Justified grid layout (GPT) | Both Gemini and Claude rejected as "another template trap" |
| Horizontal scroll (Gemini R1) | Gemini self-corrected: mobile is primary, horizontal scroll is a desktop luxury |

---

## Answers to Your Open Questions

| Question | Answer |
|----------|--------|
| **Photography situation?** | Resolved. Yaron provided 8 real event photos + 2 videos. All optimized with responsive srcset (800w/1200w/1920w). No more stock photos |
| **Portfolio or product site?** | Both. Showcasing past events AND selling upcoming ones. Current architecture supports both - upcoming events have booking CTAs, past events demonstrate quality |
| **Mobile experience?** | Mobile-first architecture. Illustrator spec was phone-screen-first. Full-viewport events work on both mobile and desktop |
| **Dream URL?** | No single "dream URL" identified. Reference sites remain: rotemcohensoaye.com, wakingup.com, migdalor.nli.org.il, exhibition.nli.org.il |
| **Content inventory?** | 2 upcoming events (Pastoral retreat, Moa performance), 5+ past events, 8 photos, 2 videos, Yaron's full manifesto text |

---

## Known Open Issues

### Section Transitions (Active Problem)
The transitions between dark and washi sections are not resolved. Three rounds of fixes have been attempted and rejected by Yaron:

1. **Round 1:** Gradient divs (25vh tall) between sections - REJECTED ("ugly")
2. **Round 2:** Gradient divs (8vh tall) - REJECTED ("still ugly")
3. **Round 3:** Hard cut (sections meet directly) + ink-edge SVG masks at key points - REJECTED ("too harsh, WordPress look")

Yaron's exact words: "לא טוב המעברים קשים מידי וזה יוצר מראה של תבנית וורדפרס מיושנת"

Currently researching how premium sites handle dark/light section transitions. We need your input on this.

---

## Yaron's Feedback History (For Calibration)

Understanding what Yaron rejects and why:

| Version | His Words | What It Tells Us |
|---------|-----------|------------------|
| v1 | "נחמד אבל לא מאוחד גווני ופשוט גרפית" | Nice but not unified, tonal, graphically simple |
| v2 | "זה מה שלמדת? נשמע מאוד מאוד בסיסי" | Very basic. Higher expectations |
| v3 | "אפילו לא בכיוון", "בנאלי", "חובנני ותבנתי כמו וורדפרס" | Not even close. Banal. Juvenile and templated like WordPress |
| v5 | Gatekeeper approved 9/10 but Yaron rejected structural approach | Surface quality is not enough - the bones must be different |
| v6 transitions | "לא טוב המעברים קשים מידי וזה יוצר מראה של תבנית וורדפרס מיושנת" | Transitions are too harsh, creates an outdated WordPress look |

Pattern: Yaron has a precise eye for when something feels "templated" or "standard." He detects structural conventionality even when the surface is well-crafted.

---

## About Sol Therapy (Brand Context)

**What we do:** Sound meditation events and retreats with leading artists - musicians, researchers, Buddhist practitioners, and visual artists.

**Who we serve:** Independent professionals 30+, thinkers, body-mind aware, appreciate art and quality, seek meaningful relaxation (not generic wellness). Based in Israel.

**Visual language:** Neo-Japonism. Sumi-e ink, Washi paper textures, Ma (negative space), vermilion Hanko seals. Museum-catalog meets meditation center.

**Voice:** Sophisticated but accessible. No emoji. No marketing speak. Yaron writes like a cultural curator - long sentences that build layers, specific references, historical context, musical vocabulary.

---

## Reference Sites (Yaron's Benchmarks)

1. **rotemcohensoaye.com** - Cargo.site. "Less interface, more work." Black canvas, justified grid, zero decoration
2. **wakingup.com** - Next.js + React. "MOMA Experience." Glassmorphism, gradient atmosphere, decorative SVGs
3. **migdalor.nli.org.il** - Time as UI. LED clock, cultural content as the interface itself
4. **exhibition.nli.org.il** - Content IS the UI. Ancient manuscripts full-bleed as the design

---

## Constraints

- **Budget:** Zero (built entirely with AI agents)
- **Technology:** Single HTML file, GSAP available, deployed on Netlify
- **Content:** All content exists (manifesto, events, artist bios, real photography, videos)
- **Non-negotiable:** Washi/Sumi-e aesthetic as texture, Hebrew RTL, no stock-template feel
- **Scope:** Main site only (blog page exists separately, not included in this review)

---

## Response Format

For each Board member, respond with:

1. **Score** - Rate the v5-to-v6 improvement (did we actually improve, and by how much?)
2. **What works** - What specifically is strong in v6? (be specific - cite elements, not generalities)
3. **What fails** - Where does v6 still feel templated, basic, or below the standard? (be harsh)
4. **The transitions problem** - How should we handle dark/light section transitions? (specific technique, not just "make it smoother")
5. **Top 3 changes** - If you could only change 3 things to elevate this site to exceptional, what would they be? (ranked by impact)
6. **What's missing** - What element, approach, or concept is absent that would transform this?
