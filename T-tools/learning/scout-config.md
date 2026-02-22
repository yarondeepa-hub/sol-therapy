# Scout Config - Learning Engine Brain

> **This file controls what the Morning Scout looks for, how it scores findings, and what questions it asks.**
> Updated by CEO. Read by morning-scout.sh.

---

## Adoption Score (0-25)

Every tool, technique, or discovery gets scored on 5 parameters (0-5 each).
**Only 16+ enters learning pipeline. 19+ triggers immediate micro-experiment.**

| # | Parameter | Question | 0 | 5 |
|---|-----------|----------|---|---|
| 1 | **Brand Fit** | Does this feel like Soul Therapy / ROVR? | Generic trend, no connection | Perfect aesthetic/philosophical match |
| 2 | **Leverage** | How much time does it save or quality does it add? | Marginal improvement | 10x faster or dramatic quality jump |
| 3 | **Repeatability** | Can we get consistent results? | Random/unpredictable | Reliable recipe every time |
| 4 | **Workflow Export** | Does the output plug into our production? | Manual work needed | Direct file/code into pipeline |
| 5 | **Risk/License** | Legal, platform dependency, privacy concerns? | Locked platform, unclear license | Open, stable, no dependencies |

### Score Thresholds

| Score | Action |
|-------|--------|
| 19-25 | **Trigger Experiment** - micro-experiment today (3 variations, 10 min, document) |
| 16-18 | **Weekly Lab Queue** - enters next Weekly Lab session |
| 10-15 | **Parking Lot** - saved in parking-lot.md, revisited monthly |
| 0-9 | **Skip** - noted in report, no further action |

---

## Sources - Where to Look

### Illustrator Sources

| Source | URL / Method | What to find |
|--------|-------------|-------------|
| Replicate Trending | `mcp__replicate__list_models` + filter new | New image/video models |
| HuggingFace Papers | WebSearch "huggingface papers image generation" | Research breakthroughs |
| Civitai trending | WebSearch "civitai trending models this week" | Community-driven models, LoRAs |
| AI Art Twitter/X | WebSearch "AI art technique site:x.com" | Artist workflows, prompting tricks |
| r/StableDiffusion | WebSearch "reddit r/StableDiffusion top week" | Community techniques |
| Non-AI Art | WebSearch "[rotating topic] art technique" | Cross-pollination (see below) |
| Google AI Blog | WebSearch "google ai blog image video" | Gemini/Imagen updates |
| Midjourney changelog | WebSearch "midjourney changelog 2026" | Feature updates |

### CTO Sources

| Source | URL / Method | What to find |
|--------|-------------|-------------|
| MCP Server Registry | WebSearch "model context protocol servers new 2026" | New MCP integrations |
| GitHub Trending | WebSearch "github trending javascript typescript" | Libraries, tools |
| Claude Code Updates | WebFetch "https://docs.anthropic.com/en/docs/claude-code" | New capabilities |
| Astro Blog | WebSearch "astro framework blog 2026" | SSG/SSR improvements |
| Web.dev | WebSearch "web.dev new 2026" | Web standards, performance |
| CSS New Features | WebSearch "new CSS features 2026 shipping" | Container queries, scroll-driven, etc |
| Netlify Blog | WebSearch "netlify blog new features" | Deploy/hosting improvements |
| GSAP Updates | WebSearch "gsap greensock new plugins 2026" | Animation capabilities |
| Claude Plugins | WebFetch "https://claude.com/plugins" | New skills, integrations |

---

## Rotating Questions - The Surprise Engine

> **Each day, the scout gets ONE question from this list (cycling through).**
> These questions force lateral thinking. They prevent "AI news roundup" syndrome.

### Illustrator Questions (30-day rotation)

1. What would Saul Bass do with AI image generation?
2. How would a Japanese calligrapher use Gemini to extend their practice?
3. What risograph printing technique could translate into a prompt modifier?
4. Find an architectural photographer whose composition rules apply to sumi-e
5. What textile pattern from a non-Western culture could become a Soul Therapy texture?
6. How would Bauhaus grid principles change our illustration composition?
7. Find a ceramics artist whose glaze textures look like our ink washes
8. What would our illustrations look like if we thought in layers of sound, not light?
9. Find a book cover designer who balances emptiness like we do
10. What Korean or Chinese ink painting technique is NOT common in AI art?
11. How would a printmaker approach negative space differently than a painter?
12. Find a motion designer whose stillness-in-movement matches aroke01
13. What photography lighting technique could inform our AI prompt atmosphere?
14. How would a perfumer describe our visual palette? What scent = our aesthetic?
15. Find a paper artist (origami/kirigami) whose folds suggest new composition
16. What generative art algorithm produces organic forms like our mountain washes?
17. How would a Zen garden designer arrange elements on our canvas?
18. Find a tattoo artist whose line quality matches our ink brush aesthetic
19. What analog photography process (cyanotype/palladium/gum) maps to our palette?
20. How would a film colorist grade our illustrations? What LUT?
21. Find a weaver whose thread patterns suggest new topographic textures
22. What theater set design principle applies to our "layers of depth"?
23. How would our art look if made entirely by erosion and weathering?
24. Find a stamp carver (hanko/intaglio) whose cuts inform our line quality
25. What musical notation system looks most like our visual language?
26. How would a marine biologist's specimen drawings translate to our style?
27. Find a mapmaker whose cartographic style matches our topographic token
28. What brutalist architecture has the same "raw material honesty" as wabi-sabi?
29. How would a tea ceremony master critique our visual compositions?
30. Find a contemporary artist who combines traditional Asian + digital in a way we haven't tried

### CTO Questions (30-day rotation)

1. What boring technology could replace our most complex current solution?
2. Find an MCP server that connects to something we use daily but haven't automated
3. What would our site architecture look like with zero JavaScript?
4. Find a CSS-only technique that could replace one of our GSAP animations
5. What deployment workflow could make our publish cycle 2 minutes instead of 10?
6. How would a database designer optimize our file-based content structure?
7. Find a testing approach that works for visual regression in our illustrations
8. What accessibility feature are we missing that would also improve aesthetics?
9. Find a performance monitoring tool that works without adding weight
10. What would our site look like on a 2G connection? What breaks first?
11. How would a game developer optimize our scroll performance?
12. Find a tool that auto-generates social media meta tags from our content
13. What edge computing feature could pre-render our most expensive visuals?
14. How would a mobile-first redesign change our current grid?
15. Find an animation library that's lighter than GSAP but handles our needs
16. What observability tool gives us real user metrics without GDPR headaches?
17. How would we architect for multi-language if Soul Therapy goes international?
18. Find a form/CRM integration that's simpler than what we currently don't have
19. What would our build pipeline look like if we adopted Astro or equivalent?
20. How would a security auditor rate our current deployment?
21. Find a way to serve our illustrations in AVIF with graceful fallback
22. What WebGPU feature is shipping that could enhance our Three.js effects?
23. How would we implement an offline-capable version of our site?
24. Find a content workflow that lets Yaron edit without touching code
25. What micro-frontend approach could let us update sections independently?
26. How would a CDN engineer optimize our asset delivery?
27. Find a headless CMS that costs zero and fits our file-based approach
28. What native browser API replaced a library we're still loading?
29. How would we implement real-time collaboration on our site content?
30. Find a monitoring solution that alerts us before users notice problems

---

## Cross-Pollination Protocol (Illustrator Only)

> **Every morning report MUST include one Cross-Pollination item.**
> This is the mechanism that prevents "AI news roundup" and creates genuine surprise.

### Rules:
1. The source must NOT be AI art or digital art
2. It must come from a different discipline entirely (ceramics, architecture, music, biology, textiles...)
3. It must include a concrete translation: "How this becomes a prompt/technique/composition for us"
4. It gets scored with the regular Adoption Score
5. If it scores 16+, it enters the pipeline just like any tool

### Format:
```
## Cross-Pollination: [Source Discipline]

**Artist/Technique:** [Name]
**What caught attention:** [1 sentence]
**Translation to our work:** [Specific prompt modifier / composition rule / technique]
**Adoption Score:** [X/25]
```

---

## Morning Report Format

```markdown
# Morning Scout - [YYYY-MM-DD]

## Today's Question
[The rotating question for this day]

## Illustrator Discoveries (top 3)

### 1. [Name/Tool/Technique]
- What: [1 sentence]
- Why it matters: [1 sentence]
- Adoption Score: [X/25] -> [Action: Skip/Parking/Lab/Trigger]
- Recipe sketch: [If 16+, outline the recipe]

### 2. [Name/Tool/Technique]
...

### 3. [Name/Tool/Technique]
...

## CTO Discoveries (top 3)

### 1. [Name/Tool/Technique]
...

## Cross-Pollination: [Discipline]
[See format above]

## Surprise Slot
[One thing that doesn't fit any category but made the scout stop and think]

## Plugin Catalog Scan
- New plugins found: [count]
- Recommended: [names + scores]
- Already installed: [confirmation that nothing was missed]

## Lab Queue Update
- In queue: [items waiting for Weekly Lab]
- This week's lab topic: [if Friday]

## Trigger Experiments (if any scored 19+)
- [What was tested]
- [3 variations tried]
- [Result: Tool Card created? Recipe created?]
```

---

## Weekly Lab Protocol

> **Runs every Friday (or when Yaron says "Lab").**
> The scout report that day flags it.

### What happens in Weekly Lab:
1. Pick the highest-scored item from the Lab Queue
2. Full experiment: 5+ variations, real outputs, real measurements
3. If successful: create Tool Card + Recipe
4. If failed: document why in weekly-lab report, move to Parking Lot
5. Duration: 30-45 minutes max
6. Output: `T-tools/learning/weekly-lab/YYYY-MM-DD-lab.md`

### Lab Report Format:
```markdown
# Weekly Lab - [YYYY-MM-DD]

## Subject: [What was tested]
## Adoption Score: [X/25]
## Hypothesis: [What we expected]

## Experiment
- Variations tried: [list with parameters]
- Tools used: [Gemini/Replicate/Photoshop/etc]
- Time spent: [X minutes]

## Results
- [What worked]
- [What didn't]
- [Unexpected findings]

## Outputs
- Tool Card created: [Yes/No -> path]
- Recipe created: [Yes/No -> path]
- Files generated: [paths]

## Verdict
[Adopt / Shelve / Revisit in [timeframe]]
```

---

## Parking Lot

> Items that scored 10-15. Revisited on the 1st of each month.

File: `T-tools/learning/parking-lot.md`

---

## Day Counter

> Used to cycle through rotating questions.

Current day: 4
(Morning scout increments this. Resets at 30.)

---

*Created: 2026-02-20*
*Version: 1.0*
