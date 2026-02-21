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

## 2026-02-21 - Custom Domain: GoDaddy to GitHub Pages

**What happened:** Connected sol-therapy.com (GoDaddy) to GitHub Pages. Full HTTPS working.

**Key learnings:**

1. **GitHub Pages custom domain flow:** CNAME file in repo -> `gh api repos/.../pages -X PUT -f cname="domain"` -> DNS records -> wait for cert -> `gh api -F https_enforced=true`. Order matters.

2. **SSL cert provisioning trick:** If certificate shows "does not exist yet", remove the cname via API then re-add it. This triggers GitHub's Let's Encrypt provisioning. Certificate approval takes ~60 seconds.

3. **API flag types matter:** `-f https_enforced=true` sends string "true" (fails). `-F https_enforced=true` sends boolean true (works). Capital F = proper JSON typing in gh CLI.

4. **GoDaddy Chrome MCP incompatibility:** GoDaddy's "Add Record" and "Edit" buttons open modal dialogs that redirect to chrome-extension:// URLs, making them inaccessible to Chrome MCP. Workaround: guide user through manual DNS changes.

5. **DNS records for GitHub Pages:** 4 A records (185.199.108-111.153) + CNAME www -> username.github.io. Three of four IPs is enough for the site to work while the fourth propagates.

6. **www redirect works automatically:** GitHub Pages handles www -> apex redirect when CNAME www points to username.github.io and the custom domain is set to the apex (sol-therapy.com).

---

## 2026-02-21 - Plugin Catalog Scan + Morning Scout Update

**What happened:** Yaron asked to scan claude.com/plugins for useful additions and add recurring check to morning report.

**Key learnings:**
1. Plugins (skills) are NOT MCP servers - they run inline, zero process weight. Safe to add freely.
2. Plugin catalog has mix of dev tools and business tools. Most dev tools not relevant for us.
3. Interesting finds: CLAUDE.md Management (audit/learning), Marketing (campaigns), Skill Creator (custom commands), Playground (HTML prototyping).
4. Morning scout now has Plugin Catalog Scan as section 5, with source added to CTO sources table.
5. Connected-tools.md should be updated when plugins are installed so scout can track what we have vs what's new.

---

## 2026-02-21 - Website Contact Button + Session Performance Fix

### Contact Button (Gatekeeper findings)
**What happened:** Yaron rejected a full contact section ("זה מכוער"). CEO process: Team Sync -> Illustrator -> CTO -> Gatekeeper. Illustrator designed a ghost/outline button, CTO built it, Gatekeeper found issues.

**Key learnings:**
1. **Ghost button border contrast matters.** Border opacity 0.25 on dark bg = 2.09:1 contrast ratio. WCAG SC 1.4.11 requires 3:1 for non-text elements. Fix: opacity 0.40 = ~3.5:1.
2. **Orphaned CSS accumulates.** When footer was redesigned from grid layout to simple centered layout, old `.footer__grid` / `.footer__bottom` / `.footer__legal` rules stayed in responsive.css. Gatekeeper caught them. Rule: when redesigning a section, search responsive.css for dead selectors.
3. **Deploy workflow is fragile.** deploy.sh has a known `find` bug. Manual deploy (clone to /tmp, copy files, push) is safer. Consider fixing the script or replacing with rsync-based approach.

### Session Performance (Zombie Process Investigation)
**What happened:** Claude getting stuck and copying text between chats. Root cause: 3 concurrent Claude Code sessions with 17 MCP node processes eating 598MB RAM + 1.8GB swap.

**Key learnings:**
1. **Each Claude Code session spawns 5 node MCP servers** (Canva, Figma, Gemini, Replicate, WebResearch). On 16GB MacBook Air, max 2-3 concurrent sessions before swap kicks in.
2. **Chrome MCP native host is a singleton.** Multiple sessions sharing one Chrome bridge = text bleeding between chats. No fix except: only one session uses Chrome at a time.
3. **Claude Code SessionStart hooks exist.** Can run cleanup scripts automatically when a new session opens. Configured in `.claude/settings.local.json` under `hooks.SessionStart`.
4. **Solution built:** `T-tools/scripts/session-cleanup.sh` - kills zombie sessions (idle >2hrs), preserves active ones. Runs automatically via SessionStart hook.
5. **Daily review now monitors system health** - process count, swap usage, warnings.

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

## 2026-02-21 - ABC-TOM Loop Must Be Mandatory (Process Fix)

**What happened:** Learning-log wasn't updated for 3 sessions straight (Feb 20). Root cause: the Loop was written as a recommendation ("After completing significant work") instead of being part of the mandatory workflow.

**Fix applied:** Loop is now embedded in the mandatory workflow in CLAUDE.md:
- Added to the workflow flow diagram (after "final version")
- Added to the STOP checklist (item 6)
- Added to Session State (before archive/cleanup)
- Added to "mistakes" table

**Rule:** ABC-TOM Loop = part of the process, not a suggestion. No task is "done" until the Loop closes.

---

## 2026-02-20 - CEO Full Process Works Well with 3 Parallel Agents

**What happened:** Session 61 - animation learning plan. Full "yossi" process: Team Sync dispatched Researcher + Illustrator + CTO in parallel. CEO synthesized. Gatekeeper caught 7 issues, round 2 approved.

**Learnings:**
1. 3 agents in parallel for planning/learning tasks is the sweet spot - each brings a different lens
2. CEO synthesis is the critical step - raw agent outputs overlap and contradict; synthesis resolves that
3. Gatekeeper on learning plans catches practical gaps (missing timelines, vague next steps) that agents skip
4. The full process for a planning task took one session - not slower than skipping steps

---

## 2026-02-20 - Context Window Problem: CLAUDE-lite Solves It

**What happened:** Session 62 - system was hitting context limits because CLAUDE.md was too heavy for auto-load. Solution: split into CLAUDE.md (lite, auto-loaded) and CLAUDE-full.md (on demand).

**Pattern:**
- Auto-loaded file = checklist + rules + structure (what you need every time)
- On-demand file = detailed processes + examples (what you need sometimes)
- current-session.md also trimmed - archive old sessions, keep only last 2-3

**Rule:** When a config file grows past effective size, split it into layers. Don't just keep adding.

---

## 2026-02-20 - Hebrew CSS: Don't Apply Latin Typography Rules

**What happened:** Session 63 - website QA found Hebrew text with `text-transform: uppercase` and `letter-spacing: 2px`. Both are Latin typography conventions that break Hebrew readability.

**Rules for Hebrew web typography:**
1. Never `text-transform: uppercase` on Hebrew - Hebrew has no case
2. Never positive `letter-spacing` on Hebrew - breaks connected reading flow
3. `font-weight: 300` on textured backgrounds (washi) = hard to read. Use 400 minimum
4. These rules apply to ALL Hebrew text, including labels and UI elements

---

## 2026-02-20 - Video Lazy-Load Pattern (IntersectionObserver)

**What happened:** Session 63 - website had a 69MB hero video loading eagerly. Fixed with IntersectionObserver lazy-load + poster image for immediate visual feedback.

**Pattern:**
```html
<video poster="poster.webp" data-src="video.mp4" preload="none">
```
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      video.src = video.dataset.src;
      video.load();
      observer.unobserve(video);
    }
  });
});
```

**Key:** poster image gives instant visual. Video loads only when scrolled into view. No quality compression needed - just delayed loading.

---

## 2026-02-20 - Learning Engine: Autonomous Daily Learning

**What happened:** Built the Learning Engine - automated Morning Scout that runs daily, finds visual/technical inspiration, and writes reports.

**Architecture:**
- Config: `T-tools/learning/scout-config.md`
- Reports: `T-tools/learning/morning-reports/`
- Trigger: daily scheduled prompt
- Focus areas: Illustrator (visual inspiration) + CTO (technical patterns)

**Key insight:** The scout needs mandatory "Trigger Experiments" - without them, reports are just bookmarks. Experiments force actionable output ("try applying X technique to our Y").

---

## 2026-02-19 - Gemini Image Generation: Click "Create image" First

**What happened:** Tried to generate image by typing prompt in Gemini's regular text box. Wrong approach.

**Correct flow:** Click the "Create image" button FIRST, then write the prompt. The button activates Gemini's image generation model (Nano Banana Pro) automatically - no need to select it from the model dropdown.

**Saved as skill:** `T-tools/skills/gemini-image-skill/gemini-image-skill.md`

---

## 2026-02-19 - Blog #3: Science Meets Buddhism - Writing Learnings

**What happened:** Third blog post, Mode C (analytical-journalistic). Source document was Yaron's Hebrew research paper on meditation neuroscience. Full workflow: fact-check -> copywriter -> gatekeeper -> 6 fixes -> smoothing pass.

**Key learnings:**

1. **Academic references kill the magazine feel.** "בשנת 2007 פרסם X ב-Y" repeated 5 times reads like a term paper. Fix: name the finding, not the paper. "ממצא אחר חשף ש..." instead of "ב-2011 פרסם ברוואר ב-PNAS...". Full citations go in the sources list at the bottom.

2. **Smoothing pass is a separate step.** First draft gets the facts and structure right. Second pass (after Gatekeeper) removes the academic scaffolding. Don't try to do both at once.

3. **Gatekeeper surgical fixes work well.** 6 factual corrections applied without touching structure or voice. Key: "fix only X, Y, Z - change nothing else." This kept the Copywriter's voice intact.

4. **Fact-checking without a separate agent works.** When API limits hit, doing WebSearch directly was faster than waiting. All 11 claims verified. Consider this as default for Mode C posts with academic sources.

5. **Hook structure:** Opening with a specific dramatic moment (Dalai Lama at SfN 2005, scientists petitioning against him) then zooming out works for Mode C. Tension first, context second.

6. **50/50 balance matters.** Yaron's source was ~70% science. The blog needed equal weight for the Buddhist methodology side. Added Kalama Sutta, Abhidharma, McMindfulness critique to balance.

**Template for Mode C blog posts:**
- Hook: specific dramatic moment with tension
- Context: historical background that explains the hook
- Evidence: findings presented as narrative, not citations
- Counterweight: honest limitations and criticism
- Synthesis: both sides meeting
- Open ending: question, not answer

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
