# Connected Tools - Master Inventory

> **IRON RULE: קרא קובץ זה בתחילת כל סשן. אין להגיד "אי אפשר" בלי לבדוק כאן קודם.**

---

## Quick Reference - מה יש לי

| Tool | Type | Status | Primary Use |
|------|------|--------|-------------|
| **Canva** | MCP Server | Active | Design generation, mockups, export |
| **Figma** | MCP Server | Active | Read designs, download assets, specs |
| **Replicate** | MCP Server | Active | AI image generation (Flux, SDXL) |
| **Chrome** | MCP Server | Active | Browser automation, visual UI work |
| **OpenAI (GPT)** | MCP Server | Active | Board member - strategic advisory (GPT thinking model) |
| **Gemini** | MCP Server | Active | Board member - strategic advisory (Gemini thinking model) |
| **Photoshop** | Local App | Available | Image editing, compositing, scripting |
| **Illustrator** | Local App | Available | Vector graphics, typography, logo design |
| **InDesign** | Local App | Available | Layout design, typography, print/PDF |
| **After Effects** | Local App | **Installed** | Animation, compositing, motion graphics, grain/texture loops |
| **Premiere Pro** | Local App | Available (not verified) | Video editing, export |
| **Adobe CC (Full)** | Subscription | Active | Full Creative Cloud - all apps available |
| **GSAP 3.14.2** | CDN Library | Installed | Scroll animations, timelines, text effects, SVG drawing |
| **Three.js r182** | CDN Library | Installed | 3D scenes, shaders, particles, WebGL effects |
| **Netlify** | CLI (npx) | Active | Website deploy, hosting, CD |

---

## Canva MCP

**Connection:** MCP connector (auto-managed token)
**Skill file:** `T-tools/skills/canva-design-skill/canva-design-skill.md`

### Key Capabilities
- Generate designs (presentations, posts, flyers, docs, posters, logos)
- Search and browse existing designs and folders
- Read and edit design content
- Export to PDF, PNG, JPG, PPTX, GIF, MP4
- Upload assets from URLs
- Brand Kit support (ID: `kAFfB4xlgWc`)

### When to Use
- Mockups for website designs
- Social media posts (Instagram, Facebook, LinkedIn)
- Presentations for partners
- Event flyers and invitations
- Quick visual prototypes

### Key Gotchas
- Short queries work better than detailed briefs
- Token expires periodically - ask Yaron to reconnect if needed
- RTL/Hebrew sometimes renders incorrectly
- Preview URLs require auth - use `get-design-pages` for thumbnails

---

## Figma MCP

**Connection:** `figma-developer-mcp` (Framelink) via stdio
**Token:** Claude-Sol-Therapy (Personal Access Token, expires May 13 2026)
**Account:** yaron.deepa@gmail.com / Yaron Deep'a's team (Free plan)
**Skill file:** `T-tools/skills/figma-design-skill/figma-design-skill.md`

### Key Capabilities
- `get_figma_data` - Read file structure, layout, content, components
- `download_figma_images` - Export PNG/SVG from designs

### Known Files

| File | Key | Description |
|------|-----|-------------|
| SOL_THERAPY | `7VDJA54QlyQgvVjMYVygs9` | Main Sol Therapy design file |

### When to Use
- Reading design specs (spacing, colors, typography)
- Downloading assets for code implementation
- Developer handoff
- Design system reference

### Limitations
- Read-only (no write/create via API on free plan)
- PAT expires May 13 2026 - renew before then

---

## Replicate MCP

**Connection:** `replicate-mcp` via stdio
**Token:** Stored in environment / MCP config. Never expose in docs.
**Skill file:** `T-tools/skills/replicate-skill/replicate-skill.md`

### Key Capabilities
- Run any model on Replicate (hundreds of AI models)
- Image generation: Flux, SDXL, Stable Diffusion
- Image editing and manipulation
- Style transfer
- Upscaling

### When to Use
- Generate Sumi-e / ink wash illustrations for Sol Therapy
- Create custom textures (Washi paper, ink splashes)
- Generate hero images and backgrounds
- Create unique visual assets that Canva can't produce
- Style transfer to match Sol Therapy aesthetic

### IRON RULE: Image Generation Method (Updated 2026-02-16)
**כלל ברזל חדש: כל ייצור איורים עובר דרך Gemini בדפדפן Chrome בלבד (עד הודעה חדשה).**
**ירון משלם על מנוי Gemini - אין מגבלה. לא להשתמש ב-Replicate MCP לאיורים.**
**מודל: nano-banana-pro דרך Gemini web UI.**

### Model Selection (for Replicate - BACKUP ONLY, not default)

| מודל | שימוש | מתי |
|------|-------|-----|
| **google/nano-banana-pro** | **ברירת מחדל ראשונה** | תמיד - לכל ייצור איורים ותמונות |
| **black-forest-labs/flux-1.1-pro-ultra** | Fallback 1 | אם nano-banana-pro לא זמין |
| **black-forest-labs/flux-1.1-pro** | Fallback 2 | אם ultra גם לא זמין |
| **black-forest-labs/flux-schnell** | **אסור לאיורים** | רק לטסטים מהירים וטקסטורות פשוטות |

**API Call (official model - no version needed):**
```
mcp__replicate__create_models_predictions:
  model_owner: "google"
  model_name: "nano-banana-pro"
  input: { prompt: "...", aspect_ratio: "16:9" }
```

**Technical notes:**
- Output: JPEG format
- Generation time: ~90 seconds (cold start longer)
- Supports: prompt, aspect_ratio
- Official model = use `create_models_predictions` (not `create_predictions`)

### Fallback Chain for Illustrations
```
1. google/nano-banana-pro (Replicate) - ברירת מחדל
2. Flux 1.1 Pro Ultra (Replicate) - אם nano-banana-pro לא זמין
3. Flux 1.1 Pro (Replicate) - אם ultra גם לא זמין
4. Canva generate-design - אם Replicate לא מספק
5. אף פעם Flux Schnell לאיורים אמנותיים
```

### Additional Key Models (from research 13.02.2026)

| מודל | סוג | שימוש |
|------|------|-------|
| **recraft-ai/recraft-v3** | ייצור עם style control | `style: "digital_illustration"` - הטוב ביותר לאיורים |
| **flux-kontext-pro** | עריכת תמונה בטקסט | image_url + prompt. ללא מסכה. |
| **flux-redux-dev** | IP-Adapter/style reference | ייצור בסגנון תמונת רפרנס |
| **flux-canny-pro** | ControlNet - סקיצה לאיור | control_image + prompt |
| **fofr/style-transfer** | העברת סגנון | style_image + content_image |
| **recraft-creative-upscale** | הגדלת רזולוציה אמנותית | מוסיף פרטים תוך הגדלה |
| **replicate/fast-flux-trainer** | LoRA training | 10-20 תמונות, 2 דקות, $2 |
| **google/veo-3-fast** | Text-to-Video | עד 1080p, 5-10s clips |

**Full reference:** `T-tools/skills/replicate-skill/replicate-skill.md`

### Quality Gate
- **עצור אחרי 2 ניסיונות כושלים - החלף כלי**
- **Gatekeeper חייב להשוות ל-benchmark לפני הצגה לירון**
- benchmark נוכחי: Canva mockup DAHBFhOLhbA (הרי אינדיגו + גבעות ירוקות)

### Key Gotchas
- Runs cost money per prediction (Yaron's account)
- Pro/Ultra models cost more than schnell - but quality justifies it
- Generation takes 5-30 seconds depending on model
- Results need quality review - not always usable on first try
- **14 ניסיונות עם schnell נכשלו (13.02.2026) - לא לחזור על הטעות**

---

## OpenAI API - GPT-5.2 (Board Member 1)

**Model:** `gpt-5.2` (GPT-5.2-2025-12-11)
**Connection:** Direct API via curl (NOT via MCP - the MCP is outdated)
**Config:** API key in `~/.claude.json` under `mcpServers.openai.env.OPENAI_API_KEY`
**Billing:** Separate from ChatGPT Plus - uses OpenAI API credits (platform.openai.com)

### Available Models (on this API key)
- **gpt-5.2** - Board default. Most advanced.
- **gpt-5.2-pro** - Even stronger, but more expensive
- **o3** - Thinking/reasoning model (like o1 but better)
- gpt-5.1, gpt-5, gpt-4.1, gpt-4o - older, cheaper options

### How to Call (direct API via Bash)
```bash
curl -s https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.2", "messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]}'
```
Parse: `.choices[0].message.content`

### Skill File
`T-tools/skills/board-activation-skill/board-activation-skill.md` - Full dispatch pattern for all 3 Board members

### Why NOT via MCP
The installed `@mzxrai/mcp-openai` MCP server only supports `gpt-4o`, `gpt-4o-mini`, `o1-preview`, `o1-mini` - all outdated. Direct curl gives access to GPT-5.2.

### Key Gotchas
- API billing is separate from ChatGPT Plus subscription
- Monitor usage at platform.openai.com to avoid unexpected charges
- GPT-5.2 is more expensive than 4o - use wisely for Board sessions only
- No access to web browsing or tools - pure reasoning only

---

## Gemini MCP - Gemini 3 Pro Deep Think (Board Member 2)

**Model:** `gemini-3-pro-preview` (Gemini 3 Pro Preview, thinking=True)
**Connection:** `@rlabs-inc/gemini-mcp` via stdio
**Config:** User-level (`~/.claude.json`), env: `GEMINI_API_KEY` + `GEMINI_MODEL=gemini-2.5-flash` (for initial connection)
**Billing:** Free tier from Google AI Studio (aistudio.google.com)

### How to Call (via Gemini MCP)
```
mcp__gemini__gemini-query:
  prompt: "[Advisory brief]"
  model: "pro"              # Routes to gemini-3-pro-preview
  thinkingLevel: "high"     # Deep thinking mode = "Deep Think"
```

### Available Models (via MCP)
- **pro** -> `gemini-3-pro-preview` (Board default, deep thinking)
- **flash** -> `gemini-3-flash-preview` (faster, cheaper)

### Additional MCP Tools (37 total)
- `gemini-search` - Google Search grounded answers
- `gemini-analyze-image` - Image analysis
- `gemini-analyze-document` - PDF/document analysis
- `gemini-deep-research` - Multi-step research
- `gemini-generate-image` - Image generation
- `gemini-brainstorm` - Multi-round brainstorming
- And more: structured output, YouTube analysis, code execution

### Key Gotchas
- Free tier has rate limits - sufficient for advisory sessions
- API key from aistudio.google.com (NOT from Gemini Pro subscription)
- Config uses `GEMINI_MODEL=gemini-2.5-flash` for initial handshake, but Pro calls route to `gemini-3-pro-preview` automatically
- `thinkingLevel: "high"` is critical for Board-quality analysis

---

## Chrome MCP (Browser)

**Connection:** Claude in Chrome extension
**Status:** Available when Chrome extension is active

### Key Capabilities
- Navigate to any URL
- Read page content (accessibility tree, text extraction)
- Interact with UI (click, type, scroll, screenshot)
- Fill forms
- Execute JavaScript
- Record GIFs

### When to Use
- Visual inspection of designs in Canva/Figma browser UI
- Web research requiring interaction
- Testing website implementations
- Any task requiring browser automation

### Key Gotchas
- Needs Chrome extension to be active and connected
- Cannot access cross-origin restricted content
- Cannot handle CAPTCHAs
- Sensitive actions require user confirmation

---

## Photoshop (Local)

**Location:** `/Applications/Adobe Photoshop 2025/` and `/Applications/Adobe Photoshop 2026/`
**License:** Full subscription (Yaron's Adobe account)
**Skill file:** `T-tools/skills/photoshop-skill/photoshop-skill.md`

### Key Capabilities
- Professional image editing and compositing
- Scriptable via JSX (ExtendScript) or UXP
- Batch processing
- Advanced filters and effects
- Layer compositing

### When to Use
- Post-processing AI-generated images
- Creating complex composites (multiple layers)
- Precise color correction
- Creating textures and patterns
- Batch processing multiple assets
- Anything requiring pixel-level control

### How to Script
- **JSX:** `osascript -e 'tell application "Adobe Photoshop 2026" to do javascript "..."'`
- **Command line:** `/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026`
- Can open files, apply operations, save/export

### Key Gotchas
- App needs to be running for scripts to work
- No MCP server - all interaction via command line or AppleScript
- Heavy operations take time
- Need to handle file paths carefully

---

## Adobe Illustrator (Local)

**Location:** `/Applications/Adobe Illustrator 2026/`
**License:** Full subscription (Yaron's Adobe account)

### Key Capabilities
- Vector graphics creation and editing
- Advanced typography and text on path
- Logo and icon design
- SVG export for web
- Scriptable via JSX (ExtendScript)
- Integration with Photoshop (smart objects)

### When to Use
- Creating vector assets (icons, logos, SVG elements)
- Advanced typography layouts (text + illustration composites)
- Designing elements that need to scale without quality loss
- Creating SVG animations source files
- Any vector-based design work

### How to Script
- **JSX:** `osascript -e 'tell application "Adobe Illustrator" to do javascript "..."'`
- Can create documents, draw paths, manipulate text, export SVG/PNG/PDF

### Key Gotchas
- App needs to be running for scripts to work
- No MCP server - all interaction via command line or AppleScript
- JSX API is different from Photoshop's JSX API

---

## Adobe InDesign (Local)

**Location:** `/Applications/Adobe InDesign 2026/`
**License:** Full subscription (Yaron's Adobe account)

### Key Capabilities
- Professional page layout and typography
- Multi-page document design
- Advanced text formatting (OpenType features, paragraph styles)
- PDF export with precise control
- Scriptable via JSX (ExtendScript) or UXP

### When to Use
- Creating professional print layouts (brochures, programs, menus)
- Advanced typographic compositions (text + image integration)
- Multi-page documents with consistent design
- Event programs, festival guides
- Anything requiring professional print-ready output

### How to Script
- **JSX:** `osascript -e 'tell application "Adobe InDesign 2026" to do javascript "..."'`
- Can create documents, place images, format text, export PDF

### Key Gotchas
- App needs to be running for scripts to work
- No MCP server - all interaction via command line or AppleScript
- Overkill for web-only assets - use for print/PDF work

---

## Adobe After Effects (Local)

**Location:** `/Applications/Adobe After Effects 2026/`
**Status:** Installed and verified (2026-02-20)
**License:** Full subscription (Yaron's Adobe CC account)

### Key Capabilities
- Motion graphics and animation (keyframe-based)
- Compositing layers (2D and 2.5D)
- Effects: grain, noise, blur, glow, particle systems
- Frame-by-frame animation
- Expressions (JavaScript-like scripting for automated animation)
- Integration with Illustrator (import vector layers), Photoshop (import PSD layers), Cinema 4D (Cineware)
- Export: MP4, WebM, GIF (via Media Encoder), image sequences
- Scriptable via JSX (ExtendScript) and CEP panels

### When to Use
- Creating animated loops from static illustrations (grain pulse, breathing, subtle movement)
- Compositing risograph/analog textures onto motion
- Kinetic typography
- Video content for Instagram/social
- Creating animation assets that CTO embeds as video loops on website
- Any task requiring frame-level animation control

### How to Script
- **JSX:** `osascript -e 'tell application "Adobe After Effects 2026" to DoScriptFile "path/to/script.jsx"'`
- **Render from CLI:** `aerender -project "path/to/project.aep" -comp "comp_name" -output "path/to/output"`
- Can create compositions, add layers, apply effects, render

### aroke01-relevant techniques
- **Grain overlay loop:** Fractal Noise effect -> animate evolution -> loop 4 seconds -> export WebM
- **Layer parallax:** Multiple Pre-comp layers at different speeds
- **Turntable from stills:** Import 3D object renders as image sequence, or use Cineware for live C4D link
- **Risograph texture mapping:** Import scanned textures, set blend mode to Multiply/Overlay

### Key Gotchas
- App needs to be running for scripts to work
- No MCP server - all interaction via command line, AppleScript, or JSX
- Rendering is CPU/GPU intensive - heavy compositions take time
- Media Encoder needed for some export formats
- aerender CLI can render without the UI open (headless)

---

## Adobe Premiere Pro (Local)

**Location:** `/Applications/Adobe Premiere Pro 2026/` (verify exact path)
**License:** Full subscription (Yaron's Adobe CC account)

### Key Capabilities
- Video editing and timeline assembly
- Color grading
- Audio mixing
- Export to all standard video formats
- Integration with After Effects (Dynamic Link)

### When to Use
- Editing longer video content (event recaps, promotional videos)
- Assembling multiple After Effects compositions into final video
- Quick video trimming and export
- Audio sync with video

### Key Gotchas
- For motion graphics, After Effects is the right tool, not Premiere
- Use Premiere for editing/assembly, AE for creation/animation

---

## Netlify

**Connection:** CLI via `npx netlify-cli` (no global install needed, auth token saved locally)
**Skill file:** `T-tools/skills/netlify-deploy-skill/netlify-deploy-skill.md`

### Account
- User: yaron amor (yaron.deepa@gmail.com)
- Team: Sol Therapy
- Site: sol-therapy (ID: `285d7e3c-21a8-4804-92bf-e7c152a4f8e8`)
- URL: https://sol-therapy.netlify.app

### Key Capabilities
- Deploy static sites to production
- Deploy previews for testing before publish
- Rollback to previous deploys
- Custom domain management
- Automatic SSL (Let's Encrypt)

### Quick Deploy Command
```bash
# 1. Prepare clean deploy folder
mkdir -p /tmp/sol-therapy-deploy
SRC="/Users/yaronamor/Documents/yaronamor-vault/sol/O-output/website-sol-therapy"
cp "$SRC/index.html" /tmp/sol-therapy-deploy/
cp -r "$SRC/assets" "$SRC/fonts" "$SRC/css" "$SRC/js" "$SRC/images" /tmp/sol-therapy-deploy/

# 2. Deploy to production
cd /tmp/sol-therapy-deploy && npx netlify-cli deploy --prod --dir=. --site=285d7e3c-21a8-4804-92bf-e7c152a4f8e8
```

### When to Use
- Publishing new website versions
- Testing changes before going live (deploy preview without --prod)
- Rolling back if something breaks

### Key Gotchas
- Use Site ID, not site name, in --site flag
- Don't upload markdown files, backups, or briefs - only site files
- npx downloads CLI fresh each time (~10s), this is normal
- Large files (video) upload fine but take longer

---

## Decision Matrix - Which Tool When

| Need | Primary Tool | Fallback |
|------|-------------|----------|
| Quick mockup | **Canva** | Figma |
| Social media post | **Canva** | - |
| Design system / specs | **Figma** | - |
| AI image generation | **Replicate (nano-banana-pro default)** | Flux Pro Ultra |
| Custom illustration | **Replicate (nano-banana-pro)** | Canva generate-design |
| Image post-processing | **Photoshop** | - |
| Vector graphics / SVG | **Illustrator** | Figma |
| Typography + illustration composites | **Illustrator** / **Photoshop** | InDesign |
| Print layouts / multi-page docs | **InDesign** | Canva |
| Batch asset export | **Photoshop** | Figma |
| Browser interaction | **Chrome** | - |
| Strategic advisory (Board) | **All 3: GPT + Gemini + Claude** | - |
| Developer handoff | **Figma** | - |
| Presentation | **Canva** | - |
| Scroll animations | **GSAP** | CSS transitions |
| Text animations | **GSAP SplitText** | CSS |
| SVG drawing effects | **GSAP DrawSVG** | CSS stroke-dasharray |
| 3D scenes / particles | **Three.js** | - |
| Shader effects (fog, water) | **Three.js** | CSS filters |
| Website deploy / hosting | **Netlify** | - |
| Video processing | **ffmpeg** (needs install) | - |
| Image batch processing (CLI) | **ImageMagick** (needs install) | Photoshop |

---

## Pipeline for Sol Therapy Visual Work

```
[Illustrator defines visual direction]
        |
        v
[Replicate (nano-banana-pro default) generates Sumi-e illustrations]
        |
        v
[Photoshop post-processes if needed]
        |
        v
[Canva creates mockup/layout with assets]
   or
[CTO builds in code with assets from Figma]
        |
        v
[Gatekeeper reviews]
```

---

## GSAP 3.14.2 (Website Animation)

**Location:** CDN script tags in `O-output/website-sol-therapy/index.html`
**CDN:** jsDelivr
**License:** Free (all plugins) - Webflow acquisition
**Research:** `O-output/gsap-research/gsap-comprehensive-report.md`

### Installed Plugins

| Plugin | CDN Path | Use |
|--------|----------|-----|
| **Core** | `gsap@3.14.2/dist/gsap.min.js` | to(), from(), fromTo(), timeline() |
| **ScrollTrigger** | `gsap@3.14.2/dist/ScrollTrigger.min.js` | Scroll-based animations, pinning, scrub |
| **ScrollSmoother** | `gsap@3.14.2/dist/ScrollSmoother.min.js` | Smooth scrolling, data-speed, data-lag |
| **SplitText** | `gsap@3.14.2/dist/SplitText.min.js` | Character/word/line text animations |
| **DrawSVGPlugin** | `gsap@3.14.2/dist/DrawSVGPlugin.min.js` | SVG stroke drawing animations |

### When to Use
- Scroll reveal animations (replaces IntersectionObserver)
- Timeline-based sequences (hero entrance, section reveals)
- Text animations per character/word
- SVG line drawing effects
- Parallax scroll effects (scrub)
- Section pinning (pin + scrub for storytelling)
- Smooth page scrolling

### Current Usage in Sol Therapy
- All `.reveal` elements use ScrollTrigger
- Event entries slide-in with stagger
- Gallery ink reveal via ScrollTrigger + gsap.delayedCall
- Nav/CTA toggle via ScrollTrigger.create()

---

## Three.js r182 (3D / WebGL)

**Location:** Import map in `<head>` of `O-output/website-sol-therapy/index.html`
**CDN:** jsDelivr
**License:** MIT (free)
**Research:** `O-output/threejs-research/threejs-comprehensive-report.md`

### Setup

```html
<!-- Already in <head> -->
<script type="importmap">
{
    "imports": {
        "three": "https://cdn.jsdelivr.net/npm/three@0.182.0/build/three.module.min.js",
        "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.182.0/examples/jsm/"
    }
}
</script>

<!-- Usage: add type="module" scripts -->
<script type="module">
    import * as THREE from 'three';
    // Create scenes here
</script>
```

### Key Capabilities
- Full 3D scenes (Scene, Camera, Renderer, Mesh)
- Custom shaders (water ripples, fog, dissolve, noise)
- Particle systems (floating particles, dust, fireflies)
- Post-processing (bloom, depth of field, film grain)
- WebGPU support with WebGL fallback

### When to Use
- Background shader effects (water, fog, organic textures)
- 3D hero elements
- Particle systems for atmospheric effects
- Interactive scroll-driven 3D animations
- Any visual effect that requires GPU shaders

### Status
**Installed but not yet active** - import map is loaded, ready for `<script type="module">` blocks when a visual concept requires it.

---

## CTO Website Development Skills (7 Skill Files)

> **19,584 שורות של ידע מתקדם - קרא לפי הצורך של המשימה.**

| Skill File | Lines | When to Read |
|-----------|-------|-------------|
| `css-advanced-layout-skill/css-advanced-layout-skill.md` | 2,192 | Layout work - CSS Grid, subgrid, container queries, magazine layouts, RTL |
| `advanced-typography-skill.md` | 2,109 | Font/text work - fluid type, variable fonts, Hebrew typography, SplitText |
| `webgl-shader-skill/webgl-shader-skill.md` | 2,874 | Visual effects - Three.js shaders, washi/ink/fog, post-processing |
| `micro-interactions-skill/micro-interactions-skill.md` | 2,999 | Interaction work - GSAP advanced, cursor, hover, scroll, page transitions |
| `image-art-direction-skill/image-art-direction-skill.md` | 3,113 | Image work - clip-path, mask-image, SVG filters, blend modes, Canvas |
| `performance-production-skill/performance-production-skill.md` | 3,290 | Build/deploy - Vite, Astro, Core Web Vitals, image opt, fonts, SEO |
| `cms-integration-skill/cms-integration-skill.md` | 3,007 | CMS work - Sanity v3, GROQ, Portable Text, Astro integration |

**Location:** All in `T-tools/skills/[name]/[name].md`

---

## Maintenance

| What | When | Action |
|------|------|--------|
| Canva token | When expired | Ask Yaron to reconnect connector |
| Figma PAT | Before May 13 2026 | Create new token in Figma settings |
| Replicate token | If revoked | Ask Yaron for new token |
| Chrome extension | Each session | Verify connection with `tabs_context_mcp` |
| Photoshop | Before use | Verify app is running |
| Illustrator | Before use | Verify app is running |
| InDesign | Before use | Verify app is running |
| OpenAI API | If billing runs out | Check platform.openai.com, ask Yaron for top-up |
| Gemini API | If rate limited | Free tier - check aistudio.google.com |

---

## NOT YET INSTALLED (Needs Homebrew)

These tools require Homebrew first. Yaron needs to run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then:
```bash
brew install ffmpeg imagemagick
```

| Tool | Purpose | Status |
|------|---------|--------|
| **Homebrew** | Package manager (base for all below) | NOT INSTALLED - needs sudo |
| **ffmpeg** | Video processing, format conversion, audio extraction | NOT INSTALLED - needs Homebrew |
| **ImageMagick** | CLI image processing, batch resize, format convert | NOT INSTALLED - needs Homebrew |

---

*Last updated: 2026-02-20 (After Effects + Media Encoder installed and verified, Hadassah font system-installed)*

---

> **c Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
