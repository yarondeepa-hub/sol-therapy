# Board Deliberation Brief: Why Doesn't the Website Meet Yaron's Standard?

**Date:** 2026-02-14
**Requested by:** Yaron (CEO of Sol Therapy)
**Status:** AWAITING YARON'S APPROVAL BEFORE DISPATCH

---

## The Problem

Yaron has built 5 versions of the Sol Therapy website. None meet his standard. His exact words across versions:

- v1: "נחמד אבל לא מאוחד גווני ופשוט גרפית"
- v2: "זה מה שלמדת? נשמע מאוד מאוד בסיסי"
- v3: "אפילו לא בכיוון", "בנאלי", "חובנני ותבנתי כמו וורדפרס"
- v4: spec written but never built (pivot to research-first approach)
- v5: built with GSAP animations, Sumi-e illustrations, full content - Gatekeeper approved 9/10 - but Yaron hasn't seen it yet and we suspect it still won't meet his bar

**The core question: What is the gap between what we're building and what Yaron envisions? And how do we close it?**

---

## Context: What We've Tried

### The Investment
- 5 website versions across 4 days
- Deep research: 6 reference sites analyzed (40KB research doc)
- Chrome visual analysis of 4 reference sites
- GSAP 3.14.2 + Three.js r182 installed
- 7 CTO skill files written (19,584 lines of technical knowledge)
- Illustrator taste profile with 10 style tokens
- 14 AI illustrations generated and evaluated
- Design system created (650 lines)
- RCS Exposure 25 full design analysis
- Waking Up full design analysis

### The Approach Evolution
1. **v1-v2:** Standard web design approach (sections, cards, grids) -> "בסיסי"
2. **v3:** Stripped everything - 2 colors, text-only hero, full-bleed images -> "בנאלי"
3. **v4 spec:** Dark canvas concept, asymmetric layouts, massive type -> never built
4. **v5:** Washi paper concept, GSAP scroll animations, Sumi-e illustrations, pinned sound section -> current version

### Key Insight Discovered During Research
"The best sites don't think 'nice design on top of content.' They think 'content IS the design.'"
- migdalor: time IS the UI (LED clock like a train station)
- exhibition: content IS the UI (ancient manuscripts as full-bleed)
- rotemcohensoaye: work IS the UI (zero decoration)

---

## About Sol Therapy (Brand Context)

We produce sound meditation events and retreats with leading artists - musicians, researchers, Buddhist practitioners, and visual artists. Our audience: independent professionals 30+, thoughtful, body-mind aware, appreciate art and quality. Based in Israel.

**Visual language:** Neo-Japonism. Sumi-e ink, Washi paper textures, Ma (negative space), vermilion Hanko seals. The aesthetic is museum-catalog meets meditation center - sophisticated, quiet, rich in texture.

**Voice:** Sophisticated but accessible. No emoji. No marketing speak. Yaron writes like a cultural curator - long sentences that build layers, specific references, historical context, musical vocabulary.

---

## Reference Sites (Yaron's Benchmarks)

### 1. rotemcohensoaye.com (Graphic Design Portfolio)
- **Platform:** Cargo.site
- **Design philosophy:** "Less interface, more work" - zero decoration, work IS the design
- **Key features:** Black background as canvas, justified grid gallery with variable aspect ratios, overlay system for project details, Monument Grotesk Mono as sole font, zero hover effects on grid (trust in visual work)
- **No external animation libraries** - only CSS keyframes
- **Screenshots available:** Hero, scroll positions 1-2

### 2. wakingup.com (Meditation App by Sam Harris)
- **Platform:** Next.js + React, Styled Components, Vercel
- **Design philosophy:** "MOMA Experience" - museum-quality presentation
- **Key features:** Decorative SVGs as metaphors (birds, clouds), glassmorphism, gradient atmosphere, fade-up CSS animations (1.2-1.5s), no external animation libraries
- **Yaron specifically liked:** the moving animations
- **Screenshots available:** Hero, scroll positions 1-2

### 3. migdalor.nli.org.il (National Library Digital)
- **Design philosophy:** Time as UI, content as interaction
- **Key feature:** LED clock counting down, treats cultural content as the interface itself
- **Note:** Blocked by Cloudflare during screenshot capture - described from prior research

### 4. exhibition.nli.org.il (National Library Exhibitions)
- **Design philosophy:** Content IS the UI
- **Key feature:** Ancient manuscripts displayed full-bleed as the design itself
- **Note:** Blocked by Cloudflare during screenshot capture - described from prior research

---

## Current Website (v5) - What Exists Now

**Architecture:** 8 sections in a single-page scroll:
1. Hero - teal gradient with "Sol Therapy" in Hebrew, tagline
2. About - Yaron's 3-paragraph manifesto + pull quote
3. Image Break 1 - Sumi-e mountain illustration with clip-path reveal
4. Events - 2 events (Pastoral retreat, Moa) with full-width layout
5. Gallery - Horizontal scroll strip (Emakimono) with Unsplash placeholders
6. Sound - "The sound that accompanies us" + audio player
7. Image Break 2 - Green hills illustration
8. Footer - Newsletter signup, email, social links

**Technology:**
- GSAP ScrollTrigger for all animations (fade-up, stagger, parallax, SplitText)
- Custom audio player with canvas waveform
- Responsive images (srcset, 3 sizes)
- Paper texture via SVG filter
- Floating CTA button

**What the Gatekeeper said (9/10):**
- Animations work, content is complete, code is clean
- Gallery uses stock photos (placeholder)
- SoundCloud embed uses placeholder URL
- Mobile nav not implemented yet

**Screenshots available:** Hero, About, Events, Gallery, Sound, Image Breaks, Footer, Full page

---

## Visual Evidence

### How Each Board Member Will See the Images

Each Board member will receive the actual screenshots through their native image capabilities:
- **GPT-5.2:** base64-encoded images via vision API
- **Gemini 3 Pro:** local file analysis via gemini-analyze-image
- **Claude Opus:** local file reading

### Screenshot Inventory

**Sol Therapy v5 (current site):**
| Screenshot | File | What it shows |
|-----------|------|---------------|
| Hero | `sol-v2-hero.jpg` | Teal gradient, "Sol Therapy" Hebrew title, tagline |
| About | `sol-v2-about.jpg` | Manifesto text, pull quote, Washi texture |
| Events | `sol-v2-events.jpg` | Event cards, full-width layout |
| Gallery | `sol-v2-gallery.jpg` | Horizontal scroll strip with photos |
| Sound | `sol-v2-sound.jpg` | Audio section with waveform player |
| Footer | `sol-v2-footer.jpg` | Newsletter, social, colophon |
| Full Page | `sol-v2-fullpage.jpg` | Complete page (compressed) |

**Reference Sites:**
| Screenshot | File | What it shows |
|-----------|------|---------------|
| RCS Hero | `ref-rcs-hero.jpg` | Black bg, bold portfolio grid |
| RCS Scroll 1 | `ref-rcs-scroll1.jpg` | Project thumbnails, justified layout |
| Waking Up Hero | `ref-wakingup-hero.jpg` | Clean meditation app homepage |
| Waking Up Scroll 1 | `ref-wakingup-scroll1.jpg` | Feature sections, gradient atmosphere |

---

## Constraints

- **Budget:** Zero (Yaron builds everything himself with AI agents)
- **Timeline:** No hard deadline, but 5 versions = growing frustration
- **Technology:** HTML/CSS/JS single file, GSAP available, Three.js available
- **Content:** All content exists (manifesto, events, artist bios)
- **Assets:** Sumi-e illustrations available (Flux Pro Ultra), real event photos not yet available
- **Non-negotiable:** Washi/Sumi-e aesthetic, Hebrew RTL, no stock-template feel

---

## The Question for the Board

**Why does the website still feel "basic" and "WordPress-like" despite:**
1. Deep research of 6 high-quality reference sites
2. Custom Sumi-e illustrations
3. GSAP scroll animations
4. Responsive design
5. Complete, authentic content written by Yaron himself

**What is the fundamental gap?**

**And: What specific, actionable direction should we take for v6 that will finally meet Yaron's standard?**

---

## Response Format

Respond with:
1. **Your diagnosis** - What's the real problem? (2-3 sentences)
2. **Your proposed direction** - What would you recommend for v6? (3-5 sentences, specific and actionable)
3. **The risk you see** - What could go wrong with your recommendation?
4. **What you'd want to know** - What information would change your recommendation?
