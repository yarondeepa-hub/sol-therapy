# Sol Therapy - Agent System Architecture
## Full System Map for External Review

---

## 1. What Is This

A multi-agent AI system managing the digital operations of Sol Therapy - a brand that produces sound meditation events and retreats in Israel. The system runs inside Claude Code (Anthropic's CLI tool) and orchestrates 10 specialized agents, persistent memory, connected external tools, and strict workflow protocols.

The owner (Yaron) interacts with one point of contact (CEO Agent, nicknamed "Yossi"). Everything flows through structured processes - no shortcuts.

---

## 2. The Business

**Sol Therapy** creates transformative sound meditation events and retreats. Think: world-class musicians performing in exceptional venues (museums, galleries, nature retreats), with 50-200 participants lying down in darkness, experiencing deep sound immersion.

- **Target audience:** Professionals 30+, thoughtful, educated, seeking meaningful experiences (not wellness cliches)
- **Brand voice:** Sophisticated, poetic-journalistic, direct. Inspired by Japanese minimalism ("Neo-Japonism")
- **Key tension:** Audience searches in plain language ("sound meditation Tel Aviv"), brand speaks in poetic language ("transformative journey into consciousness"). The system must bridge this without dumbing down.

---

## 3. Agent Architecture

```
                    YARON (Owner)
                        |
                   CEO ("Yossi")
                        |
                   TEAM SYNC
                   /    |    \
          --------  --------  --------
         /        |          |        \
   COPYWRITER  ILLUSTRATOR  CTO  RESEARCHER  PRODUCER
         \        |          |        /
          --------  --------  --------
                   \    |    /
                  GATEKEEPER
                        |
                   CEO ("Yossi")
                        |
                    YARON (Owner)


   [BOARD] --- advisory ---> CEO (only when convened)
   (GPT-5.2 + Gemini 3 Pro + Claude Opus)
```

### 3.1 Agent Roster

| # | Agent | Role | When Active |
|---|-------|------|-------------|
| 1 | **CEO ("Yossi")** | Managing director, Yaron's single point of contact. Owns all agents and project success. | Always |
| 2 | **Team Sync** | Work orchestrator. Breaks requests into workstreams, builds dependency graphs, assigns agents, tracks progress. | Always first on every request |
| 3 | **Copywriter** | All content creation. Deep analysis of owner's writing style (5 modes identified). Hebrew voice specialist. | Text, posts, descriptions |
| 4 | **Illustrator** | All visual assets. Neo-Japonism style with strict quality gates. Generates via Gemini in Chrome. | Visual tasks (always before CTO) |
| 5 | **CTO** | All technology. Websites, automation, integrations. Implements design faithfully from Illustrator handoffs. | Tech tasks |
| 6 | **Researcher** | Knowledge engine. Venues, artists, academic sources, market data. Supervised by Gatekeeper for depth. | Research tasks |
| 7 | **Producer** | Event lifecycle owner. Deals, planning, execution, debrief. Financial models, logistics. | Events, retreats |
| 8 | **Gatekeeper** | Final quality reviewer. Fact-checker, visual taste-keeper, brand guardian. Dynamic quality bar. | Always last before delivery |
| 9 | **SEO** | Search optimization strategy. Bridges poetic brand voice with search-friendly terms. | Content + tech SEO |
| 10 | **Board** | External advisory council. 3 real AI models deliberating in parallel. Requires owner approval to convene. | Strategic decisions only |

### 3.2 The Board (Advisory Council)

Three real AI models serving as advisory board members:

| Member | Model | Access Method |
|--------|-------|--------------|
| Member 1 | GPT-5.2 (OpenAI) | Direct API curl (MCP server outdated) |
| Member 2 | Gemini 3 Pro Preview | Gemini MCP, model:"pro", thinkingLevel:"high" |
| Member 3 | Claude Opus | Task tool, subagent_type: "opus" |

- All 3 dispatched in parallel
- CEO synthesizes their perspectives into actionable recommendation
- Board advises, CEO decides
- Board never communicates directly with other agents
- 5 advisory perspectives: Strategist, Brand Guardian, Devil's Advocate, Audience Voice, Culture Critic

---

## 4. Workflow Protocol

### 4.1 Mandatory Flow (No Exceptions)

```
Yaron's Request
    |
    v
Team Sync Intake
    - Understand request
    - Identify deliverables
    - Break into workstreams
    - Build dependency graph
    - Identify parallelism (max 3 concurrent agents)
    - Assign owners
    |
    v
Agents Execute (parallel where possible)
    - Each agent reads required files
    - Uses Handoff Template for agent-to-agent transfers
    - Visual tasks: Illustrator BEFORE CTO (always)
    |
    v
Gatekeeper Review (all user-facing content)
    - Brand voice check
    - Fact verification (WebSearch for every claim)
    - Visual quality gate (browser screenshots at 3 breakpoints)
    - Dynamic quality bar (rises with every "ok" or negative feedback)
    |
    v
Revision Loop (if needed, max 3 rounds)
    - Specific feedback to agent
    - Agent fixes, resubmits
    - After v3: escalate to human
    |
    v
CEO Quality Gate
    |
    v
Present to Yaron
    |
    v
ABC-TOM Loop (mandatory closure)
    - Update learning-log.md
    - Update feedback.md
    - Update decisions.md
    - Promote patterns to voice-dna.md if strong enough
```

### 4.2 Iron Rules

1. **Team Sync is ALWAYS first** - even for "simple" requests
2. **Illustrator before CTO** on any visual task
3. **Gatekeeper before Yaron** on any user-facing content
4. **ABC-TOM Loop after every task** - not optional
5. **Max 3 concurrent agents** for quality
6. **Board requires Yaron's approval** before convening
7. **Git commit before editing** existing files
8. **NO emoji** - ever. Zero. Deal breaker.
9. **NO em dash** - regular hyphen only
10. **Partners label stays English** - never translate
11. **Illustrations via Gemini Nano Banana Pro ONLY** (in Chrome browser)
12. **Context continuation = report first, work second**
13. **"Yossi" = full process** - no shortcuts when owner addresses CEO by name

---

## 5. Memory System

### 5.1 Persistent Files (survive between sessions)

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `M-memory/active-task.md` | Current task snapshot (max 50 lines, overwrite not append) | Every step change |
| `M-memory/current-session.md` | Session history, what was done | Every session |
| `M-memory/learning-log.md` | What works, what failed, patterns | After every task (ABC-TOM) |
| `M-memory/feedback.md` | Audience reactions and signals | When feedback received |
| `M-memory/decisions.md` | Strategic choices with rationale | When decisions made |
| `M-memory/illustrator-taste-profile.md` | Yaron's visual preferences (DO/DON'T, benchmarks) | After every illustration feedback |

### 5.2 Core Brand Files (rarely change)

| File | Purpose |
|------|---------|
| `C-core/project-brief.md` | What the business does, mission, unique approach |
| `C-core/voice-dna.md` | Complete brand voice definition (622 lines). 5 writing modes, vocabulary, DJ syntax, forbidden words |
| `C-core/icp-profile.md` | Ideal Customer Profile. Persona "Noa", 38, designer. What motivates, what repels |

### 5.3 Knowledge Base

| Location | Content |
|----------|---------|
| `B-brain/sol-therapy-knowledge-base.md` | Venue history, artist roster, past events |
| `B-brain/research/` | Previous research reports |
| `B-brain/data/` | Source documents (activity profile, market analysis) |
| `B-brain/references/writing-samples/` | Yaron's actual writing for style analysis |

### 5.4 Session Continuity Protocol

- **Start of task:** Read active-task.md + current-session.md, update both
- **Every step change:** Overwrite active-task.md with fresh snapshot
- **Before long operations:** Checkpoint in active-task.md
- **End of task:** ABC-TOM Loop, archive, clear active-task.md
- **Context continuation (new session):** Re-read CLAUDE.md from scratch. First message = status report only, never work.

---

## 6. Connected Tools

### 6.1 MCP Servers (Always Available)

| Tool | Purpose | Key Detail |
|------|---------|-----------|
| **Canva MCP** | Design generation, editing, export | Brand Kit ID: kAFfB4xlgWc |
| **Figma MCP** | Read designs, download images | via figma-developer-mcp + PAT |
| **Replicate MCP** | AI image generation (backup only) | Flux, SDXL, recraft-v3, veo-3 |
| **Chrome MCP** | Browser automation, visual work | Primary tool for Gemini illustration |
| **OpenAI API** | GPT-5.2, Board Member 1 | Direct curl (MCP outdated, only has gpt-4o) |
| **Gemini MCP** | Gemini 3 Pro, Board Member 2 | model:"pro", thinkingLevel:"high" |

### 6.2 Local Applications

| App | Use |
|-----|-----|
| Photoshop | Post-processing, compositing, color correction |
| Illustrator | Vector graphics, logos |
| InDesign | Automated print layouts (via AppleScript + JSX) |
| After Effects | Animation, grain/texture loops |
| Premiere Pro | Video editing/export |

### 6.3 Web Libraries (Sol Therapy Website)

| Library | Version | Purpose |
|---------|---------|---------|
| GSAP | 3.14.2 | ScrollTrigger, ScrollSmoother, SplitText, DrawSVG |
| Three.js | r182 | 3D engine for WebGL effects |

### 6.4 Illustration Pipeline

```
PRIMARY: Gemini Nano Banana Pro (Chrome browser)
    |
    v (if Gemini unavailable)
FALLBACK 1: nano-banana-pro (Replicate)
    |
    v
FALLBACK 2: Flux 1.1 Pro Ultra (Replicate)
    |
    v
FALLBACK 3: Flux 1.1 Pro (Replicate)
```

---

## 7. Brand Voice (Condensed)

### 7.1 Five Writing Modes

| Mode | Name | When | Key Feature |
|------|------|------|-------------|
| A | Communique/Event | Announcements, invitations | Formal, rich, restrained enthusiasm |
| B | Personal-Journalistic | Blog, personal posts | Associative, dual stance (participant + observer) |
| C | Opinion/Tech-Cultural | Articles, analysis | Academic-lite, rhetorical questions, open endings |
| D | Personal-Intimate | Eulogies, personal | First person, specific details, quiet grief |
| E | Scene/Party | Event announcements | Cultural critique, visceral language |

### 7.2 Signature Vocabulary (Must-Use)

Hebrew terms that define the brand: "mehapnet" (enchanting), "transformativi", "immersivi", "virtuozi", "tzlila" (diving), "merkamim" (textures), "tdarim" (frequencies), "nofei sound" (soundscapes), "rav-shichvati" (multi-layered), "atmosferi", "tamhil meduyak" (precise blend), "ginat zen" (zen garden)

### 7.3 Forbidden

- Emoji (deal breaker)
- Em dash (use regular hyphen)
- "The best" / "number 1" / superlatives
- "Hurry!" / "You won't believe!" / sales pressure
- "Energies" / "vibrations" / wellness cliches
- "Sound healing" (explicitly rejected by owner)
- Apologetic language

### 7.4 DJ Syntax

Writing follows a DJ set structure:
- **Build:** Layered sentences, tension accumulates
- **Breakdown:** Dash/parenthesis, intimate whisper
- **Drop:** Main claim lands

Required paragraph rhythm: long + long + short, OR short + medium + long. Never all same length.

---

## 8. Visual Identity ("Neo-Japonism")

### 8.1 Style

Fusion of traditional East Asian art (Ukiyo-e, Shin-hanga, Sumi-e) and modern editorial design.

### 8.2 Style Tokens (5+ of 10 required per illustration)

1. Warm paper texture (not sterile white) - CRITICAL
2. Ink monochrome brushwork - CRITICAL
3. 60-75% negative space - CRITICAL
4. Vertical scroll format
5. Mountains/water/mist nature elements - CRITICAL
6. Bamboo rhythm (organic repetition)
7. Topographic indigo textures
8. Editorial micro-typography
9. Wabi-sabi restraint - HIGH

### 8.3 Color Palette

| Role | HEX | Usage |
|------|-----|-------|
| Paper base | #e0ddd3 | 60-80% surface |
| Ink charcoal | #283335 | Soft black line |
| Cool ink grey | #7b817d | Background |
| Indigo cool | #4d615d | Deep blue-green |
| Teal water | #257167 | Water motif only |

### 8.4 Quality Gate (4/6 = pass)

1. Layer depth (3+ visible layers)
2. Tone variation (3+ shades same color)
3. Texture (brush/paper visible)
4. Atmosphere (sense of space/mood)
5. Human feel (not AI-generated look)
6. Negative space (60%+)

---

## 9. Website Architecture

- **Live:** https://sol-therapy.com (GitHub Pages, custom domain)
- **Repo:** yarondeepa-hub/sol-therapy
- **Stack:** Single-file HTML with inline CSS/JS, Heebo + Inter + DM Mono fonts, Masada display font
- **Pages:** index.html, blog.html, blog-sound-meditation.html, blog-science-buddhism.html, blog-collective-sync.html, 404.html
- **SEO:** robots.txt, sitemap.xml, canonical URLs, OG tags, Twitter Cards, JSON-LD (Organization + Event)
- **Deploy:** Manual git push to GitHub Pages (deploy script has known bug)

---

## 10. Automation

### 10.1 Daily Review (21:00)

- macOS launchd job runs at 21:00
- Script: `T-tools/scripts/daily-review.sh`
- Uses `claude -p --model opus`
- Checks: day summary, open items, Claude updates, agent health
- Reports saved to `M-memory/daily-reports/`
- macOS notification when done
- Unseen reports auto-displayed at session start (.seen marker)

### 10.2 Session Cleanup (SessionStart hook)

- Runs on every new Claude Code chat
- Kills zombie sessions (>2hrs idle)
- Prevents resource exhaustion (was causing 1.8GB swap)

---

## 11. Templates

| Template | Purpose | Location |
|----------|---------|----------|
| Handoff Template | Agent-to-agent work transfer | `T-tools/templates/handoff-template.md` |
| Gatekeeper Context Card | Pre-review briefing | `T-tools/templates/gatekeeper-context-card.md` |
| Agent Dispatch Prompts | How to brief each agent | `T-tools/templates/agent-dispatch-prompts.md` |

---

## 12. Known Issues / Open Items

1. **Video compression needed:** Hero video 16MB, gallery 14MB
2. **Font conversion to WOFF2:** Currently loading OTF
3. **Responsive images (srcset):** Not implemented yet
4. **Google Fonts non-blocking:** Applied to index.html only, not blog pages
5. **Newsletter form:** Needs Mailchimp/ConvertKit decision
6. **Testimonials/social proof:** Needs participant quotes
7. **Deploy script bug:** find command issue, deploying manually via git push
8. **decisions.md and feedback.md:** Mostly empty, not consistently used
9. **Producer agent:** Not yet tested in real event scenario

---

## 13. What's Working Well

1. **Parallel agent execution** - 3 agents running simultaneously, dependency-aware
2. **Gatekeeper's dynamic quality bar** - rises with feedback, prevents rubber-stamping
3. **Illustrator taste profile** - persistent visual preferences that improve over time
4. **ABC-TOM Loop** - compounding learning system (when followed)
5. **Session continuity** - active-task.md + current-session.md survive context loss
6. **Voice DNA depth** - 5 writing modes, DJ syntax, signature vocabulary
7. **Board advisory** - 3 real models providing diverse strategic perspectives

---

## 14. Questions for Review

When reviewing this system, consider:

1. **Agent overlap:** SEO Agent mirrors CEO Agent in many responsibilities. Should it be merged or differentiated?
2. **Memory utilization:** decisions.md and feedback.md are underused. How to make them more actionable?
3. **Gatekeeper bottleneck:** Every user-facing item goes through Gatekeeper. Is this sustainable as output grows?
4. **Board activation:** Currently requires owner approval each time. Too much friction? Or appropriate safeguard?
5. **Workflow rigidity:** Team Sync on EVERY request, even trivial ones. Right balance of process vs. speed?
6. **Learning compounding:** ABC-TOM Loop is mandatory but sometimes skipped under time pressure. How to enforce?
7. **Tool sprawl:** 6 MCP servers + 5 local apps + 2 JS libraries. Is the tool surface too wide?
8. **Single point of failure:** Everything runs through Claude Code. What happens when context window fills?
9. **Producer agent untested:** No real event has gone through the full lifecycle. Risk?
10. **Visual pipeline:** Gemini-only for illustrations with Replicate as fallback. Robust enough?

---

*Generated 2026-02-21. Based on full scan of all system files: 10 agent definitions, 3 core brand files, 6 memory files, 4 tool/template files, master instruction file (CLAUDE-full.md, 686 lines).*
