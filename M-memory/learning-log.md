# Learning Log

This is the team's collective memory. Every agent reads this before working. Every review adds to it. We get better together.

---

## How This Works

**Before working:** Every agent reads the relevant sections
**After working:** Gatekeeper logs patterns from each review session
**Periodically:** Consolidate insights into agent instruction files

---

## Why Memory Matters

> "Brain is what you feed the system. Memory is what the system learns."

Most AI systems are stateless — every conversation starts from zero. This file is what makes your system **compound over time**.

Every pattern logged here makes future work better.

---

## Active Patterns (Apply These Now)

### Copy Patterns

**What Works:**
| Do This | Not This |
|---------|----------|
| Start with a specific moment or action | Start with a generic statement |
| Use contrast frames: "Old way... New way..." | Use abstract explanations |
| Include numbers that can be visualized | Use vague claims |
| Write short lines. Punchy rhythm. | Write long flowing paragraphs |

**Voice Markers (Must Be Present):**
- Personal pronouns (I, my, me, you)
- Specific numbers (20 hours → 7 hours)
- Sensory/visual details
- Conversational tone

**Voice Violations (Must Be Absent):**
- Corporate jargon (leverage, optimize, synergy)
- Vague superlatives (best, leading, top-tier)
- Generic claims that competitors could use
- Passive voice overuse
- Long explanatory sentences

---

## Common Mistakes to Avoid

### Copy Mistakes
1. Opening with a lesson instead of a moment
2. Using "best" or "leading" without proof
3. Writing headlines that could apply to any competitor
4. Over-explaining the insight (let it land)
5. Missing the natural brand callback

---

## Quality Shortcuts

**Copy Quick Checks:**
1. Read it aloud — does it flow?
2. Count specific numbers — aim for 2+ per piece
3. Check first line — is it a moment or an explanation?
4. Check last line — is it memorable standalone?
5. Apply the test: Visual? Provable? Unique?

---

## Iteration Log

*Add entries below after each review session*

---

## 2026-02-19 - Blog Post HTML/CSS Template (Desktop Typography Fix)

**What happened:** Fixed desktop typography in both blog posts. Mobile was perfect, desktop font was too small and hard to read. Two issues found: (1) font-size too small (18px -> 20px), (2) font-weight 300 (light) on washi background = hard to read.

**Blog CSS Architecture Template (for all future blog posts):**

### Design Tokens (:root)
```css
:root {
    --body-size: clamp(0.9375rem, 0.45vw + 0.82rem, 1.125rem);
    --body-lh: 1.65;
    --measure: 62ch;
    --h2-size: clamp(1.35rem, 1vw + 1rem, 1.75rem);
    /* Colors */
    --washi: #F2EAD3;
    --green-dark: #3B514B;
    --dark: #1a1a1a;
    --ink: rgba(0,0,0,0.85);
}
```

### Desktop Override (@media min-width: 64rem)
```css
@media (min-width: 64rem) {
    .nav { height: 60px; }
    :root {
        --body-size: 1.25rem;      /* flat, not clamp */
        --body-lh: 1.75;           /* more spacious */
        --measure: 66ch;           /* wider reading */
        --h2-size: 1.95rem;        /* larger headings */
    }
    .article-body { font-weight: 400; }  /* regular, not light */
    .pull-quote { font-size: 1.85rem; }
    .article-hero__deck { font-size: 1.2rem; line-height: 1.7; }
}
```

### Font Stack
- **Body:** Heebo (weight 300 mobile, 400 desktop)
- **Display/Headings:** Masada
- **Section markers:** Hadassah Friedlaender
- **English text:** Inter
- **Meta/code:** DM Mono

### Layout Structure
- `.article-grid` - 3-column CSS grid (1fr min(var(--measure),90%) 1fr)
- `.article-body` - main text column
- `.section-marker` - decorative section dividers
- `.pull-quote` - large quote blocks

### Section Transitions
- `.transition--washi-dark` - gradient from washi to dark
- `.transition--dark-washi` - gradient from dark to washi
- Uses `background: linear-gradient(to bottom, ...)` with bokashi style

### Image Integration (Sumi-e Style)
- `.sumi-figure` with `mix-blend-mode: multiply` (light bg) or `screen` (dark bg)
- Radial-gradient masks for soft edges
- `.sumi-figure__img` with object-fit: cover

### Animations
- `.reveal` class with IntersectionObserver
- `opacity: 0; transform: translateY(30px)` -> `opacity: 1; transform: translateY(0)`
- `.stagger` for sequential children reveal
- `transition: opacity 0.8s ease, transform 0.8s ease`

### Key Rules
1. **Mobile breakpoints: DON'T TOUCH** - clamp() handles mobile perfectly
2. **Desktop overrides use FLAT values** - no clamp() in the 64rem media query
3. **font-weight 400 on desktop** is critical for readability on washi background
4. **Color contrast:** #3B514B on #F2EAD3 with weight 300 = bad. Weight 400 = good.
5. **Template files:** blog-collective-sync.html (1491 lines) and blog-sound-meditation.html (1466 lines) in O-output/website-sol-therapy/

### Deployment
- GitHub Pages: yarondeepa-hub.github.io/sol-therapy/
- Deploy: clone repo to temp dir, copy files, commit, push, cleanup
- Local git in sol/ is gone (rsync incident) - deploy via temp clone only

---

## 2026-02-19 - Illustrations via Gemini Nano Banana Pro in Chrome

**What happened:** Replaced all 7 blog illustrations (both posts) with images generated via Gemini in Chrome browser using Nano Banana Pro model.

**New iron rule:** ALL illustrations are created in Chrome browser via gemini.google.com using Nano Banana Pro model. NEVER use Replicate/Flux for illustration generation. This overrides the previous Replicate-based workflow.

**Process:** Chrome MCP -> navigate to gemini.google.com -> generate images -> download -> integrate into blog HTML.

---

## 2026-02-14 - New Agent: The Board (External Advisory Council)

**What happened:** Created a new agent - "The Board" - an External Advisory Council providing strategic guidance to the CEO.

**Why:** The CEO needed a structured way to get strategic perspective on business, brand, and growth decisions. Instead of making all decisions alone or escalating everything to Yaron, the CEO can now convene The Board for multi-perspective analysis.

**How it works (v2 - 3 real AI models):**
- 3 Board Members: GPT (OpenAI MCP), Gemini (Gemini MCP), Claude Opus (Task tool)
- All 3 dispatched in parallel with the same advisory brief
- Each model thinks independently - no groupthink
- CEO synthesizes the 3 responses into a Board Advisory
- Deliberate disagreement - different training = different blind spots
- The Board advises, the CEO decides
- Communication flows: Board -> CEO -> Agents (never Board -> Agents directly)
- Yaron can also call The Board directly, bypassing the CEO

**Evolution:** Originally designed with 5 abstract "chairs" (Strategist, Brand Guardian, etc.). Yaron upgraded to 3 real AI models for genuine independent perspectives.

**Technical setup:**
- OpenAI: `@mzxrai/mcp-openai` - user-level MCP, API key from platform.openai.com (separate from ChatGPT Plus)
- Gemini: `@rlabs-inc/gemini-mcp` - user-level MCP, free API key from aistudio.google.com (separate from Gemini Pro subscription)
- Claude: Already running as Opus - use Task tool with `model: "opus"`
- Important: Paid chat subscriptions do NOT give API access. API keys are separate products.

**What it doesn't do:**
- Does not execute work (no writing, designing, coding)
- Does not replace Gatekeeper (strategic, not operational QA)
- Does not interact with other agents directly

**Files created/updated:**
- `A-agents/board-agent.md` - Full agent definition (v2: 3-model architecture)
- `T-tools/skills/connected-tools.md` - Added OpenAI MCP and Gemini MCP
- `A-agents/gatekeeper-agent.md` - Added Board to team reference
- `CLAUDE.md` - Added Board to agent reference table
- `~/.claude.json` - OpenAI and Gemini MCP server configurations

---

## 2026-02-13 - Illustrator Quality Gate: Replicate Model Selection

**What happened:** 14 illustration attempts with Flux Schnell (4 steps) - all generic and flat. Yaron: "דיי גרוע".

**Root cause:** Flux Schnell is a speed-optimized model (4 inference steps). Not suitable for artistic illustration work.

**New rules:**
1. **ALWAYS use google/nano-banana-pro as default** - never Schnell for illustrations
2. **Fallback chain:** nano-banana-pro -> Flux Pro Ultra -> Flux Pro -> Canva -> never Schnell
3. **Stop after 2 failed attempts** - switch tool, don't keep iterating with same approach
4. **Gatekeeper must compare to benchmark** before showing to Yaron (current benchmark: Canva mockup DAHBFhOLhbA)
5. **nano-banana-pro is an official model** - use create_models_predictions (no version needed)

**Quality benchmark (what works):**
- Canva mockup DAHBFhOLhbA: dramatic indigo mountains with snow/mist, rich green watercolor hills with layer depth
- Key qualities: tonal variation, visible brushwork texture, atmospheric depth, multiple layers

**What failed (don't repeat):**
- Flux Schnell prompts, regardless of how detailed
- Generic prompts ("minimal sumi-e", "abstract ink wash")
- Presenting without Gatekeeper comparison to benchmark

---

## 2026-02-12 - Deep Research: Cultural Website Patterns (6 Reference Sites)

### What Happened
ירון הכניס מחקר מעמיק (40KB) על טיפוגרפיה, תנועה, אינטראקציה ותבניות טכנולוגיות ב-6 אתרי תרבות: migdalor, rotemcohensoaye, docutext, telavivdance, epilogue, exhibition.

### Key Discoveries

**הכל אותו צוות:**
כל אתרי NLI (migdalor, docutext, epilogue, exhibition) נבנו על Webflow ע"י רותם כהן-סואייה (שפה גרפית) + נדב אביגד (פיתוח). זה מערכת עיצוב אחת שחוזרת, לא 4 אתרים שונים.

**תבניות טיפוגרפיות:**

| תבנית | אתר | מה לומדים |
|-------|------|----------|
| Stacked headlines | docutext | שבירות שורה מכוונות ליצירת אפקט פוסטר |
| Tri-script identity | epilogue, exhibition | עברית/ערבית/אנגלית בשורה אחת - אלמנט עיצובי |
| Time-as-UI | migdalor | שעון LED ענק, לוח זמנים כמו תחנת רכבת |
| Zero-UI portfolio | rotemcohensoaye | העבודות הן הממשק, אפס קישוט |

**תבניות טכניות:**

| תבנית | מה זה | למה חשוב |
|-------|-------|---------|
| AVIF pipeline | .tif.avif derivatives | ביצועים מעולים, archival workflow |
| Webflow breakpoints | 991/767/478px | סטנדרט responsive |
| Progressive disclosure | Show/Hide accordions | לא להציף את המשתמש |
| Reduced-motion | prefers-reduced-motion + toggle | WCAG 2.3.3, נגישות אמיתית |
| Design tokens | type/spacing/colour/motion tiers | מערכת עיצוב סדורה |

**Accessibility כ-feature:**
Tel Aviv Dance הוא benchmark - toolbar נגישות בדף עם Disable Animations, Keyboard Navigation, שינוי ניגודיות. לא רק statement נסתר.

### מה חסר ב-v3 של האתר שלנו
1. Reduced-motion support (prefers-reduced-motion)
2. Focus styles מפורשים
3. Skip links
4. ARIA patterns (accordion)
5. Breakpoints: 991px + 478px (יש רק 768px)
6. Design tokens מלאים (type scale)

### Files Updated
- `M-memory/learning-log.md` - הרשומה הזו
- `A-agents/illustrator-agent.md` - visual/typography findings
- `A-agents/cto-agent.md` - technical patterns + accessibility
- `A-agents/researcher-agent.md` - source credits
- `A-agents/gatekeeper-agent.md` - accessibility checklist

### Source
`~/Downloads/Deep research report on typography, motion, interaction, and technology patterns across six cultural.docx`

---

## 2026-01-30 - Deep Writing Analysis: Owner's Complete Style Profile

### What Happened
ירון ייצא מ-ChatGPT ניתוח מקיף של כל היסטוריית הכתיבה שלו — מיפוי מלא של הסגנון, הטכניקות, המוטיבים החוזרים והרפרנסים התרבותיים.

### Key Discoveries — שני מודים מרכזיים
