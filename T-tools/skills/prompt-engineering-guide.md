# The Definitive Guide to AI Image Prompt Engineering

> For high-quality artistic illustrations. Research-based, model-tested, continuously updated.
> Written for the Illustrator agent and anyone generating visual assets for Sol Therapy.

---

## Table of Contents

1. [A. Prompt Anatomy](#a-prompt-anatomy)
2. [B. Style Modifiers Library](#b-style-modifiers-library)
3. [C. Quality Boosters](#c-quality-boosters)
4. [D. Anti-Patterns](#d-anti-patterns)
5. [E. Model-Specific Tips](#e-model-specific-tips)
6. [F. Example Prompts](#f-example-prompts)

---

## A. Prompt Anatomy

Every effective AI image prompt is built from layers. Think of it as a blueprint - each layer adds specificity and steers the model toward your vision.

### The 7-Layer Structure

```
[1. Subject] + [2. Style/Medium] + [3. Composition] + [4. Lighting/Mood] + [5. Color Palette] + [6. Technical Quality] + [7. Exclusions]
```

### Layer 1: Subject

The main focus. What the image depicts. Place this FIRST - all models give highest weight to early tokens.

**Rules:**
- One clear subject. Multi-subject scenes need explicit spatial relationships.
- Be concrete, not abstract: "towering mountain peaks with snow" beats "mountains."
- Describe relationships: "emerging from," "obscured by," "reflected in."

**Examples:**
- Weak: "mountains"
- Strong: "towering indigo mountain peaks with snow on their crests, emerging from a thick bank of atmospheric clouds"

---

### Layer 2: Style / Medium

The artistic approach. This single layer has the most dramatic impact on the final look.

**Key principle:** Name the specific technique, not just the genre. "Traditional East Asian ink wash painting on rice paper" works much harder than "Asian art."

**Format options:**
- Named technique: "Sumi-e ink wash painting"
- Named medium: "watercolor on cold-pressed cotton paper"
- Named movement: "Shin-hanga woodblock print style"
- Named reference: "in the style of Hasui Kawase landscape prints"
- Combined: "traditional Japanese Sumi-e ink wash on handmade Washi paper"

**Critical:** Style/medium should come immediately after the subject. Models parse prompts left-to-right. What comes first carries the most weight.

---

### Layer 3: Composition

How the scene is arranged spatially. This layer controls what the viewer sees and from where.

**Spatial depth keywords:**
- "multiple receding layers creating extreme depth"
- "foreground, middle ground, and distant background"
- "atmospheric perspective with objects fading into distance"

**Framing keywords:**
- Wide / panoramic / landscape orientation
- Close-up / macro / detail view
- Bird's eye / aerial / overhead
- Low angle / looking up

**Arrangement keywords:**
- "asymmetric composition with visual weight on the left"
- "centered subject with negative space surrounding"
- "rule of thirds placement"
- "full-bleed edge-to-edge composition"

---

### Layer 4: Lighting / Mood

Lighting defines the emotional tone. It is the single most impactful "invisible" element.

**Lighting types that work well:**
| Keyword | Effect |
|---------|--------|
| "soft diffused light" | Gentle, even illumination, no harsh shadows |
| "golden hour warm light" | Warm yellow-orange, long shadows, romantic |
| "dramatic side lighting" | High contrast, strong shadows, tension |
| "backlit / rim light" | Silhouette edges, halo effect, ethereal |
| "volumetric light through fog" | Visible light beams, 3D atmosphere |
| "overcast ambient light" | Flat, even, melancholic, grey |
| "low-key dramatic shadows" | Mostly dark with selective illumination |
| "moonlight / nocturnal" | Cool blue, soft silver, mysterious |

**Mood keywords:**
- Serene, contemplative, meditative
- Dramatic, brooding, intense
- Ethereal, dreamlike, mystical
- Melancholic, wistful, nostalgic
- Majestic, awe-inspiring, grand

---

### Layer 5: Color Palette

Specific color direction steers the model away from generic palettes.

**How to specify color:**

For Flux models, you can use hex codes directly:
```
"color #264348 deep indigo tones"
"gradient starting with color #264348 and finishing with color #FAF6F0"
```

For all models, descriptive color works reliably:
```
"deep indigo and navy blue tones transitioning to soft cream"
"monochromatic palette of varied green tones from forest to sage"
"warm cream and cool indigo contrast"
```

**Principles:**
- Specify tonal variation within a color family: "rich tonal variation from near-black indigo to pale blue-grey"
- Name 2-3 dominant colors maximum, plus one accent
- Describe color relationships: "warm against cool," "muted earth tones with a single pop of vermillion red"

---

### Layer 6: Technical Quality Modifiers

Keywords that push the model toward higher detail and resolution.

**Proven effective (all models):**
```
"8k ultra detailed"
"fine art museum quality"
"extremely detailed"
"sharp focus"
"high resolution"
```

**Proven effective (artistic styles):**
```
"masterwork quality"
"gallery exhibition quality"
"visible brushstroke texture"
"rich tonal gradation"
"paper grain visible"
```

**Use sparingly - diminishing returns:**
```
"4k" / "8k" - one resolution tag is enough
"best quality" - vague, but mildly helpful
"trending on artstation" - biases toward digital art, not traditional
```

See Section C for the full breakdown of what works vs. myth.

---

### Layer 7: Exclusions / Negative Direction

**For Flux models:** Negative prompts are NOT supported. You must describe what you WANT, not what you don't want. Use positive phrasing:
- Instead of "no blur" -> "sharp focus"
- Instead of "no text" -> ... actually, "no text" is the exception - include this phrase anyway as it helps prevent text artifacts

**For SDXL / Stable Diffusion (negative prompt field):**

Core negative prompt for artistic illustrations:
```
text, watermark, signature, letters, numbers, words, logo, blurry, low quality, low resolution, ugly, deformed, disfigured, extra fingers, bad anatomy, jpeg artifacts, out of frame, cropped, duplicate
```

For Sumi-e / ink wash specifically, add:
```
photorealistic, 3d render, CGI, digital art, plastic texture, neon colors, oversaturated, cartoon, anime
```

**Negative prompt principles:**
1. Be specific - "blurry face" beats "bad quality"
2. Start small, add only what you need
3. Don't overload - too many negatives confuse the model
4. Weight problem areas: "(extra fingers:1.4)" for persistent issues
5. Test iteratively - remove negatives one at a time to see their actual effect

---

### Putting It All Together: The Assembly Formula

**Short prompt (exploration - 20-40 words):**
```
[Subject + key detail], [style/medium], [mood + lighting], [1-2 quality tags], no text
```

**Medium prompt (production - 40-80 words):**
```
[Subject with spatial relationships], [specific technique + medium], [composition and depth],
[lighting type + mood], [color palette with 2-3 named tones], [texture and material details],
[2-3 quality tags], no text
```

**Long prompt (maximum control - 80-150 words):**
```
[Detailed subject with multiple elements and spatial positioning], [named technique + historical
reference + medium], [specific composition with foreground/midground/background described],
[lighting type + direction + quality], [full color specification with gradients and tonal range],
[surface texture + material + tool marks], [atmospheric effects - fog, mist, particles],
[3-4 quality tags], no text
```

**Important for Flux:** Keep prompts under 200 tokens for optimal quality. The T5 encoder handles up to 512 tokens but quality degrades beyond 256. The CLIP encoder hard-truncates at 77 tokens. For best results, frontload the most critical information.

---

## B. Style Modifiers Library

### Japanese Art Styles

#### Sumi-e (ink wash painting)
| Modifier | What it does |
|----------|-------------|
| "traditional Sumi-e ink wash painting" | Core style - black ink on paper, tonal gradation |
| "wet-on-wet Sumi-e technique" | Soft bleeding edges, diffused forms |
| "wet-on-dry Sumi-e brushstrokes" | Crisp, defined strokes with texture |
| "Sumi-e with visible brushstroke texture" | Emphasizes the hand-painted quality |
| "Sumi-e hatsuboku technique" | Splashed/broken ink, spontaneous |
| "Sumi-e tarashikomi pooling ink" | Layered wet washes that pool and blend |
| "monochrome ink wash, Sumi-e" | Strictly black ink, no color |
| "Sumi-e with subtle indigo tones" | Extends beyond pure black into blue-black |

**Best subject pairings:** Mountains, bamboo, cranes, water, pine trees, landscapes, bridges in mist.

#### Ukiyo-e (woodblock prints)
| Modifier | What it does |
|----------|-------------|
| "Ukiyo-e woodblock print style" | Core style - flat color areas, bold outlines |
| "Ukiyo-e with visible woodgrain texture" | Adds the print medium's signature texture |
| "Ukiyo-e in the style of Hokusai" | Dynamic compositions, Prussian blue dominant |
| "Ukiyo-e in the style of Hiroshige" | Serene landscapes, atmospheric perspective |
| "Ukiyo-e kacho-e bird-and-flower" | Nature study sub-genre |
| "Ukiyo-e bokashi gradient technique" | Gradated color printing, smooth tonal shifts |

**Best subject pairings:** Waves, Mt. Fuji, bridges, seasons, birds, cherry blossoms, travelers.

#### Shin-hanga (new prints, early 20th century revival)
| Modifier | What it does |
|----------|-------------|
| "Shin-hanga woodblock print style" | More atmospheric and detailed than Ukiyo-e |
| "Shin-hanga in the style of Hasui Kawase" | Rain, snow, twilight landscapes, soft atmosphere |
| "Shin-hanga in the style of Ohara Koson" | Birds and flowers with exquisite detail |
| "Shin-hanga night scene with soft lantern glow" | Characteristic nocturnal atmosphere |
| "Shin-hanga rain scene with visible droplets" | Signature weather effects |

**Best subject pairings:** Temples at night, rain on water, snow scenes, birds on branches, moonlit landscapes.

#### Nihonga (Japanese-style painting, mineral pigments)
| Modifier | What it does |
|----------|-------------|
| "Nihonga painting technique" | Mineral pigments on silk or paper, luminous |
| "Nihonga with gold leaf accents" | Traditional kinpaku gold leaf application |
| "Nihonga on silk with iwa-enogu mineral pigments" | Maximum authenticity cue |
| "Nihonga rinpa decorative style" | Bold, decorative, gold backgrounds |

**Best subject pairings:** Flowers, birds, landscapes, seasons, screens, scrolls.

---

### Watercolor Techniques

| Modifier | What it does |
|----------|-------------|
| "watercolor painting" | Basic watercolor look |
| "wet-on-wet watercolor technique" | Soft bleeding, diffused edges, organic flow |
| "dry brush watercolor" | Textured, scratchy, paper grain shows through |
| "watercolor wash with granulation" | Pigment settling into paper texture |
| "transparent watercolor layers" | Light passing through pigment, luminous |
| "watercolor on cold-pressed cotton paper" | Specific texture - bumpy, organic |
| "watercolor on hot-pressed smooth paper" | Clean, precise, smooth gradients |
| "watercolor with soft bleeding edges" | Pigment feathering at boundaries |
| "watercolor with visible paper white showing" | Reserves, highlights from the paper itself |
| "plein air watercolor sketch" | Loose, observational, outdoor feel |
| "botanical watercolor illustration" | Precise, scientific, detailed naturalism |

---

### Ink Wash Techniques

| Modifier | What it does |
|----------|-------------|
| "East Asian ink wash painting" | Broad category, covers Chinese and Japanese |
| "Chinese Shan-shui mountain-water painting" | Classical Chinese landscape tradition |
| "ink wash with layered tonal gradation" | Key to depth - light to dark in same hue |
| "spontaneous ink splatter and controlled strokes" | Contrast of control and chaos |
| "ink wash on xuan rice paper" | Specific absorbent paper texture |
| "running ink technique, broken edges" | Ink flowing beyond the stroke |
| "dry ink with flying white texture" | Fast stroke leaving gaps, paper shows through |
| "layered ink washes creating atmospheric depth" | Multiple transparent layers building form |
| "ink and light color wash (qianjiang)" | Ink base with pale color washes on top |

---

### Fine Art References

| Reference | What it evokes |
|-----------|---------------|
| "in the tradition of Sesshu Toyo" | Bold Sumi-e, dramatic landscapes |
| "reminiscent of Hasui Kawase prints" | Atmospheric, moody, rain/snow/twilight |
| "in the spirit of Ma Yuan landscapes" | Chinese Southern Song, one-corner composition |
| "echoing Tohaku Hasegawa pine screens" | Misty, minimal, pine trees in fog |
| "influenced by Yokoyama Taikan" | Modern Nihonga, atmospheric haze |
| "Turner-esque atmospheric light" | Western - dramatic light, fog, water |
| "Rothko-like color field depth" | Abstract color meditation, blurred edges |
| "Monet's water lily palette" | Impressionist, reflective, pastel depth |

---

### Texture Modifiers

| Modifier | What it adds |
|----------|-------------|
| "on handmade Washi paper" | Fibrous, warm, organic Japanese paper |
| "on aged rice paper with foxing" | Antique feel, brown spots, aged |
| "on rough cotton rag paper" | Heavy texture, artisanal |
| "on smooth silk scroll" | Luminous, smooth, traditional mounting |
| "visible canvas weave texture" | Oil painting substrate feel |
| "visible paper grain and fiber" | Shows the support material |
| "crackled aged surface" | Antique, weathered, historical |
| "gold leaf texture with patina" | Metallic, aged luxury |
| "raw linen canvas texture" | Natural, unfinished, contemporary |

---

### Atmospheric Modifiers

| Modifier | What it creates |
|----------|----------------|
| "thick atmospheric mist between mountain layers" | Depth, mystery, distance |
| "morning fog obscuring the lower valleys" | Soft, diffused, peaceful |
| "rain falling as visible fine lines" | Weather, movement, mood |
| "snow settling on branches and peaks" | Quiet, still, cold beauty |
| "clouds swirling around mountain peaks" | Dramatic, scale, movement |
| "haze creating atmospheric perspective" | Objects fade with distance |
| "dust particles visible in light beams" | Volumetric, tangible atmosphere |
| "steam rising from hot springs" | Organic, warm, living landscape |
| "twilight sky with gradient from deep blue to amber" | Time of day, warmth-cool contrast |

---

## C. Quality Boosters

### What Actually Works (Evidence-Based)

**Tier 1 - Consistently effective across models:**

| Keyword | Why it works |
|---------|-------------|
| "8k" or "8k ultra detailed" | Signals high-resolution training data. One resolution tag is enough. |
| "extremely detailed" | Pushes the model toward its highest-detail outputs |
| "sharp focus" | Counteracts the model's tendency toward soft-focus |
| "fine art museum quality" | Associates with curated, exhibition-grade work |
| "masterwork" / "masterpiece" | In SD/SDXL training data, correlates with high-quality images |

**Tier 2 - Effective for artistic styles specifically:**

| Keyword | Why it works |
|---------|-------------|
| "visible brushstroke texture" | Forces the model to render paint texture, not smooth digital |
| "rich tonal gradation" | Prevents flat single-tone areas |
| "paper grain visible" | Adds materiality, breaks the digital look |
| "hand-painted quality" | Steers away from AI-generated smoothness |
| "gallery exhibition quality" | Higher tier than generic "high quality" |

**Tier 3 - Helpful but with caveats:**

| Keyword | Caveat |
|---------|--------|
| "4k" | Redundant if you already used "8k" |
| "high quality" | Too vague on its own, combine with specific details |
| "best quality" | Mildly helpful in SDXL, nearly meaningless in Flux |
| "trending on artstation" | Biases toward digital concept art, NOT for traditional styles |
| "professional" | Helpful for photography, less so for fine art |

### What Doesn't Work (Myths)

| Claim | Reality |
|-------|---------|
| "Stacking 5+ quality tags improves quality" | Diminishing returns after 2-3 tags. Wastes tokens. |
| "beautiful" alone improves output | Too subjective. Combine with specific descriptors instead. |
| "award-winning" adds quality | Inconsistent effect, model-dependent |
| "photorealistic" for paintings | Actively fights against painterly styles. Avoid for traditional art. |
| "HDR" for paintings | Introduces photography-specific processing, wrong for art |
| "trending on artstation" for Sumi-e | Biases toward Western digital art, counterproductive for Eastern traditional |
| "detailed" repeated 3 times | Once is enough. Repetition does NOT increase weight in Flux. |

### The Real Quality Formula

Quality in AI art comes from **specificity of description**, not from stacking magic keywords. A well-described scene with zero quality tags will outperform a vague scene with ten quality tags.

```
GOOD: "dramatic indigo mountain landscape painting, traditional East Asian ink wash
technique, towering peaks with snow emerging from thick atmospheric clouds, multiple
receding mountain layers creating extreme depth, rich tonal gradation from near-black
foreground to misty pale background, visible wet brushstroke texture, paper grain
visible, fine art museum masterwork quality, no text"

BAD: "mountains, ink painting, beautiful, masterpiece, best quality, 8k, ultra HD,
detailed, extremely detailed, sharp focus, high resolution, award-winning"
```

The good example works because every phrase adds visual information. The bad example burns tokens on empty qualifiers.

---

## D. Anti-Patterns - What Ruins Prompts

### 1. Conflicting Instructions

The model cannot resolve contradictions. It will attempt both and produce neither.

| Conflict | Why it fails |
|----------|-------------|
| "photorealistic" + "watercolor painting" | Opposite rendering philosophies |
| "minimal" + "extremely detailed" | Contradictory levels of complexity |
| "bright, vibrant" + "muted, subdued" | Opposing color directions |
| "close-up portrait" + "wide landscape" | Incompatible framing |
| "ancient traditional" + "futuristic neon" | Clashing time periods (unless intentional) |

### 2. Over-Specification

More detail is NOT always better. Beyond ~150 words, prompts often degrade.

**Symptoms of over-specification:**
- Model ignores parts of the prompt entirely
- Image becomes incoherent or "confused"
- Competing elements cancel each other out
- Style becomes muddled - neither one thing nor another

**The fix:** Prioritize. Decide what matters most and describe THAT in detail. Leave secondary elements less specified.

### 3. Keyword Soup

Listing disconnected keywords without grammatical structure or spatial relationships.

```
BAD: "mountain, fog, ink, Japanese, detailed, blue, mist, paper, traditional, dark,
beautiful, 8k, masterpiece"

GOOD: "A dramatic mountain landscape in traditional Japanese ink wash style, with thick
fog weaving between multiple receding peaks, painted on textured Washi paper with
visible brushstrokes and rich indigo tonal gradation"
```

Flux especially punishes keyword soup. Its T5 encoder is a language model - it understands sentences, not word lists.

### 4. Vague Style Direction

"Asian art" or "Japanese style" is too broad. The model has thousands of reference points and will average them into something generic.

**Fix:** Name the specific technique, era, or master:
- "Sumi-e ink wash" not "Japanese art"
- "Shin-hanga woodblock print" not "Japanese print"
- "Nihonga mineral pigment painting" not "traditional Japanese"

### 5. Wrong Quality Tags for the Style

Using photographic quality tags for paintings:
- "bokeh" on a watercolor (meaningless)
- "HDR" on an ink wash (introduces wrong processing)
- "ray tracing" on a Sumi-e (3D rendering term)
- "DSLR" on a traditional painting (camera reference)

Use quality tags that match your medium:
- For paintings: "museum quality," "gallery exhibition," "masterwork"
- For photography: "DSLR," "bokeh," "f/1.4," "Kodak Portra 400"

### 6. Including Text/Numbers in Prompts

AI models frequently render text as garbled artifacts. Including words you want "written" in the image is risky.

**For Flux:** Put desired text in double quotation marks and specify placement. It handles short text reasonably well.

**For all models:** Always add "no text" or "no words, no letters, no numbers" unless you specifically want text rendered.

### 7. Hex Codes as Plain Text (Non-Flux Models)

Writing "#264348" in a prompt for Stable Diffusion or Recraft will render those characters as text in the image. Only Flux supports hex code color specification natively.

### 8. Negative Prompts on Models That Don't Support Them

Flux does NOT support negative prompts. Writing "negative prompt: blurry" will be interpreted as part of the positive prompt, potentially making the output blurry.

---

## E. Model-Specific Tips

### Flux Pro / Flux 1.1 Pro Ultra (Primary Model for Sol Therapy)

**Architecture:** Dual text encoder - T5-XXL (language model, up to 512 tokens) + CLIP (visual embeddings, 77 token hard limit).

**What makes Flux different:**
- Natural language, not keywords. Write complete sentences.
- Word order matters heavily. First things = strongest influence.
- NO negative prompt support. Describe what you want.
- NO weight syntax support. "(keyword:1.5)" does NOT work and may damage output.
- Hex color codes ARE supported: "color #264348"
- Text rendering via quotation marks: "the text 'SOL' in red"

**Optimal prompt length:** 40-80 words (medium). Under 200 tokens. Going longer shows minimal improvement and can degrade quality.

**What works uniquely well in Flux:**
- Camera/lens specifications for photorealism ("Shot on Fujifilm X-T5, 35mm f/1.4")
- Spatial language ("In the foreground... Behind it... In the distance...")
- Natural emphasis phrases ("with emphasis on," "with a focus on," "the dominant feature is")
- Hex color codes tied to specific objects
- Native language prompting for culturally authentic scenes

**What to avoid in Flux:**
- Parenthetical weighting syntax: (keyword:1.5) - broken, may damage output
- Square bracket de-weighting: [keyword] - not supported
- Negative prompts - not supported at all
- Keyword repetition for emphasis - does not increase weight
- "white background" in Flux dev specifically - causes fuzzy outputs

**Flux-specific prompt template for Sol Therapy Sumi-e:**
```
A [subject description with spatial relationships], painted in traditional
East Asian Sumi-e ink wash technique on handmade Washi paper, [composition
details with foreground/middle/background], [lighting/mood], [color palette
using descriptive names], visible brushstroke texture and paper grain,
atmospheric mist creating depth between layers, fine art museum masterwork
quality, 8k ultra detailed, no text
```

---

### SDXL / Stable Diffusion XL

**Architecture:** CLIP text encoder only (77 token limit for base, extended via some frontends).

**What makes SDXL different:**
- Keyword-friendly. Comma-separated descriptors work well.
- Supports negative prompts (separate field).
- Supports prompt weighting: (keyword:1.2) for emphasis, (keyword:0.7) for reduction.
- Responds strongly to artist name references.
- Benefits from quality tags like "masterpiece, best quality."

**Prompt weighting syntax:**
```
(important element:1.3)    - increases weight by 30%
(less important:0.8)       - decreases weight by 20%
((very important))         - roughly equivalent to :1.21
[de-emphasized element]    - reduces weight slightly
```

**Caution:** Use weighting sparingly. Weights above 1.5 or below 0.5 cause artifacts. Stick to the 0.8-1.3 range.

**SDXL negative prompt template for traditional art:**
```
photorealistic, 3d render, CGI, digital art, plastic texture, neon colors,
oversaturated, cartoon, anime, text, watermark, signature, blurry, low quality,
low resolution, jpeg artifacts, cropped, duplicate, extra fingers, bad anatomy,
ugly, deformed
```

**SDXL prompt template for Sol Therapy Sumi-e:**
```
(traditional Sumi-e ink wash painting:1.2), dramatic mountain landscape,
(multiple overlapping layers creating depth:1.1), towering peaks with snow,
thick atmospheric fog between layers, rich tonal gradation from near-black
to pale grey, visible brushstroke texture, (paper grain:1.1), warm cream
background, fine art museum quality, masterpiece, 8k ultra detailed
```

---

### Recraft V3

**What makes Recraft different:**
- Designed for graphic design, not photorealism.
- Style parameter system - set style separately from prompt.
- Excellent at clean illustrations, consistent design motifs.
- Supports text rendering with size and position control.
- "Artistic level" parameter controls creative variation vs. prompt adherence.

**Key tips:**
- Lower "Artistic level" = closer to prompt specification
- Use reference-based styling for consistent series
- Enable "Avoid text" in negative prompt settings for designs without text
- Break complex descriptions into focused parts
- Use "Creative Upscale" post-generation if faces/hands are distorted

**Style parameter recommendations:**

For traditional Japanese styles, use the "Illustration" base style with detailed prompts specifying the technique. Recraft's strength is clean graphic output, so combine it with specific traditional art descriptors.

---

### Google Imagen / Nano-Banana-Pro (Default for Sol Therapy)

**Access:** Via Replicate as `google/nano-banana-pro`

**What we know:**
- Takes `prompt` and `aspect_ratio` as inputs
- Outputs JPEG
- Generally strong at following detailed prompts
- Responds well to the same natural language approach as Flux

**Tips based on Sol Therapy experience:**
- Use the same prompt templates as Flux (natural language, not keywords)
- Include "no text" explicitly
- The detailed Sumi-e templates from the taste profile work well here
- Always specify aspect_ratio ("16:9" for hero/landscape, "1:1" for square)

---

### Comparison: How Models Interpret the Same Prompt

Given: "Japanese ink wash mountain landscape with mist and depth"

| Model | Likely Output |
|-------|--------------|
| **Flux Pro** | Photographic-quality rendering with realistic atmospheric depth, may lean photorealistic unless "painting" is explicit |
| **SDXL** | More stylized, responds to keyword emphasis, may need "(ink wash:1.2)" to prevent photorealistic drift |
| **Recraft V3** | Clean, graphic interpretation, excellent edges and composition, may simplify texture |
| **Nano-Banana-Pro** | Strong at following the artistic direction, good tonal gradation |

**Lesson:** Always specify "painting" or "painted" for traditional art styles. Without it, models default toward photorealism.

---

## F. Example Prompts

### 1. Dark Dramatic Mountain Landscape (Sumi-e / Shan-shui)

**For Flux Pro / Nano-Banana-Pro:**
```
Dramatic mountain landscape painting in traditional East Asian Sumi-e ink wash
technique, towering indigo peaks with snow on their crests emerging from thick
banks of atmospheric clouds, multiple receding mountain layers creating extreme
depth from near-black foreground cliffs to misty pale distant peaks, rich tonal
gradation through deep navy, indigo, and soft grey-blue, visible wet brushstroke
texture on every surface, handmade Washi paper grain showing through the paint,
heavy atmospheric mist weaving between the mountain layers, fine art museum
masterwork quality, 8k ultra detailed, no text
```

**For SDXL (with negative prompt):**
```
Positive:
(traditional Sumi-e ink wash painting:1.2), dramatic mountain landscape,
towering (indigo peaks with snow:1.1), emerging from thick atmospheric clouds,
(multiple receding mountain layers:1.2) creating extreme depth, rich tonal
gradation from near-black to pale grey-blue, visible wet brushstroke texture,
Washi paper grain, heavy mist between layers, fine art museum masterwork,
masterpiece, 8k ultra detailed

Negative:
photorealistic, 3d render, digital art, neon, oversaturated, text, watermark,
signature, blurry, low quality, anime, cartoon, plastic texture
```

---

### 2. Green Watercolor Rolling Hills

**For Flux Pro / Nano-Banana-Pro:**
```
Lush green rolling hills painted in watercolor technique, multiple overlapping
organic hill shapes in varied shades of green from deep forest emerald to light
sage and celadon, each hill layer has slightly different saturation creating
rich visual depth, soft watercolor bleeding edges where colors meet, Japanese
Nihonga painting influence in the layering, warm cream paper background showing
through between brush marks, subtle cold-pressed paper grain texture visible
throughout, gentle morning light creating soft shadows in the valleys between
hills, fine art gallery exhibition quality, 8k detail, no text
```

**For SDXL:**
```
Positive:
(watercolor painting:1.2), lush green rolling hills, (multiple overlapping
organic hill shapes:1.1) in varied greens from deep forest to light sage,
Nihonga painting technique, each layer different saturation, soft bleeding
watercolor edges, warm cream paper background showing through, visible paper
grain texture, gentle morning light, masterpiece, gallery quality, 8k

Negative:
photorealistic, digital art, flat colors, text, watermark, blurry, low quality,
oversaturated, neon, 3d render
```

---

### 3. Abstract Ink Wash

**For Flux Pro / Nano-Banana-Pro:**
```
Abstract ink wash composition with flowing organic forms, traditional East Asian
ink painting technique using varied concentrations of black ink creating rich
tonal range from intense black pools to barely-there pale grey washes,
spontaneous ink splatter contrasting with controlled calligraphic brushstrokes,
wet ink bleeding and pooling on absorbent rice paper creating organic tarashikomi
effects, negative white space as a compositional element occupying roughly half
the image, visible paper fiber texture where ink is thinnest, contemplative and
meditative mood, fine art museum quality, 8k ultra detailed, no text
```

---

### 4. Washi Paper Texture (Background/Texture Asset)

**For Flux Pro / Nano-Banana-Pro:**
```
Close-up texture of handmade Japanese Washi paper, warm cream color with subtle
variations in tone from ivory to pale honey, visible long plant fibers embedded
in the paper surface, slightly rough tactile texture with tiny irregularities,
soft warm ambient light revealing the paper's surface topology, organic natural
material quality, the paper fills the entire frame edge to edge with no objects
on it, 8k ultra detailed macro photography of paper texture, no text
```

**For SDXL:**
```
Positive:
(macro photograph of handmade Washi paper:1.3), warm cream color, visible plant
fibers, (tactile rough texture:1.1), subtle tonal variations, soft ambient
light, fills entire frame, (paper texture detail:1.2), 8k ultra detailed

Negative:
text, watermark, objects, illustration, digital, blurry, low quality, drawing,
painting, flat
```

---

### 5. Atmospheric Fog/Mist Scene

**For Flux Pro / Nano-Banana-Pro:**
```
Mountainous landscape shrouded in thick morning mist, painted in traditional
Sumi-e ink wash technique, only the faintest silhouettes of distant peaks
visible through layers of atmospheric fog, one dark pine tree in the near
foreground partially obscured by swirling mist, the fog itself rendered with
masterful wet-on-wet ink wash gradations from dense near-white to translucent
grey, vast empty space filled with mist creating a sense of infinite depth and
solitude, monochrome palette of ink blacks and paper whites with the subtlest
warm cream undertone from the Washi paper, contemplative Zen meditation
atmosphere, fine art museum masterwork, 8k ultra detailed, no text
```

---

### 6. Traditional Japanese Hanko Stamp Composition

**For Flux Pro / Nano-Banana-Pro:**
```
A traditional Japanese Hanko seal stamp impression on cream Washi paper,
square format red vermillion ink stamp with slightly uneven edges showing the
hand-carved quality, the seal contains an abstract kanji-like mark, the red
ink has subtle variations in density with heavier ink at the edges and lighter
center showing the stamp pressure, tiny ink bleeds where the vermillion meets
the absorbent paper fibers, the stamp is positioned in the lower right corner
of the composition with vast empty cream paper space above and to the left,
traditional East Asian aesthetic with masterful use of negative space, fine art
quality, 8k detail, no text except the stamp mark
```

---

### 7. Combined Scene: Sol Therapy Hero (Sumi-e Mountains on Dark Background)

**For Flux Pro / Nano-Banana-Pro:**
```
Dramatic Sumi-e ink wash mountain landscape on a near-black background,
towering peaks painted in indigo and navy blue ink with white snow on their
crests, thick atmospheric clouds and mist swirling between multiple receding
mountain layers, the mountains emerge from darkness with rich tonal gradation
from deep shadow to luminous peak highlights, traditional East Asian brushwork
with visible wet brush texture and controlled ink bleeding, atmospheric depth
extending far into misty distance, the overall mood is contemplative and
majestic, painted on dark-toned handmade paper with subtle grain, fine art
museum masterwork quality, 8k ultra detailed, no text
```

---

### 8. Combined Scene: Sol Therapy About Section (Green Hills with Hanko)

**For Flux Pro / Nano-Banana-Pro:**
```
Lush green rolling hills watercolor painting with a small red Hanko stamp seal
in the lower right corner, multiple overlapping organic hill shapes in varied
shades of green from deep forest to light sage, Japanese Nihonga painting
technique with each hill layer showing different saturation for rich visual
depth, soft watercolor bleeding edges between the hill shapes, warm cream Washi
paper background visible between painted areas, the red Hanko stamp is a small
square vermillion seal adding a single point of warm color contrast against the
cool greens, gentle atmospheric haze in the valleys, fine art gallery quality,
8k ultra detailed, no text except the stamp mark
```

---

## Quick Reference Card

### Before Every Generation

```
1. Check illustrator-taste-profile.md for current DO/DON'T
2. Choose model: Nano-Banana-Pro -> Flux Pro Ultra -> Flux Pro (fallback chain)
3. Build prompt using 7-layer structure
4. Verify: no conflicting instructions, no keyword soup, no wrong quality tags
5. Include "no text" at the end
6. Set aspect_ratio to match intended use (16:9 hero, 1:1 square, 3:4 portrait)
7. Generate and compare to benchmark before showing to Yaron
```

### The 5-Point Quality Check (from taste-profile.md)

Before presenting ANY illustration:

1. Layer depth - at least 3 visible layers
2. Tonal variation - at least 3 shades of the dominant color
3. Texture - visible brushstroke or paper grain
4. Atmosphere - sense of space and depth
5. Human feel - does NOT look computer-generated

**Pass threshold: 3 out of 5 minimum.**

---

## Sources

Research compiled from:
- [Black Forest Labs - FLUX.2 Prompting Guide](https://docs.bfl.ml/guides/prompting_guide_flux2)
- [getimg.ai - FLUX.1 Prompt Guide: Pro Tips and Common Mistakes](https://getimg.ai/blog/flux-1-prompt-guide-pro-tips-and-common-mistakes-to-avoid)
- [Skywork - 14 Essential FLUX.1 Prompts](https://skywork.ai/blog/flux1-prompts-tested-templates-tips-2025/)
- [Skywork - Flux Prompting Ultimate Guide](https://skywork.ai/blog/flux-prompting-ultimate-guide-flux1-dev-schnell/)
- [Ambience AI - FLUX Prompting Guide](https://www.ambienceai.com/tutorials/flux-prompting-guide)
- [Recraft - Prompting and Image Generation Best Practices](https://www.recraft.ai/docs/best-practices/prompting-and-image-generation)
- [Recraft Blog - How to Craft Prompts for AI-Generated Images](https://www.recraft.ai/blog/how-to-craft-prompts-for-accurate-ai-generated-images)
- [Stable Diffusion Art - Prompt Guide](https://stable-diffusion-art.com/prompt-guide/)
- [Learn Prompting - Quality Boosters](https://learnprompting.org/docs/image_prompting/quality_boosters)
- [letsenhance.io - How to Write AI Image Prompts](https://letsenhance.io/blog/article/ai-text-prompt-guide/)
- [Civitai Education - Prompt Crafting Guide Part 2](https://education.civitai.com/civitais-prompt-crafting-guide-part-2-intermediate/)
- [Medium/Dira - Simulating Sumi-e and Chinese Brush Painting with AI](https://bydira.medium.com/simulating-sumi-e-and-chinese-brush-painting-with-ai-b722225b109d)
- [Apatero - Flux 2 Klein Prompting Techniques 2026](https://apatero.com/blog/flux-2-klein-prompting-techniques)
- [Apatero - How to Prompt Flux 2 Complete Guide](https://apatero.com/blog/how-to-prompt-flux-2-complete-prompting-guide-2025)
- [Leonardo.ai - AI Art Styles Guide](https://leonardo.ai/news/ai-art-styles/)
- [Zapier - 70+ AI Art Styles](https://zapier.com/blog/ai-art-styles/)
- [OpenArt - Stable Diffusion Prompts for Watercolor](https://openart.ai/blog/post/stable-diffusion-prompts-for-watercolor)
- [ClickUp - 120+ Stable Diffusion Negative Prompts](https://clickup.com/blog/stable-diffusion-negative-prompts/)
- [Hugging Face - Weighted Prompts in Diffusers](https://huggingface.co/docs/diffusers/en/using-diffusers/weighted_prompts)
- [Tensor.Art - Emphasis, Weighting, and Down-Weighting](https://tensor.art/articles/816872603533949146)
- [NightCafe - Sumi-e Ink Painting Generator](https://creator.nightcafe.studio/tools/japanese-sumi-e-ink-painting-generator)
- [ImagineArt - Japanese Art Generator](https://www.imagine.art/features/japanese-art-generator)
- [Segmind - Flux 1.1 Pro Ultra](https://blog.segmind.com/flux-1-1-pro-ultra-the-best-ai-text-to-image-tool/)

---

*Created: 2026-02-13*
*Based on: 10 web searches + 6 deep page analyses + Sol Therapy production experience*
*For: Illustrator Agent, Gatekeeper Agent, anyone generating Sol Therapy visual assets*
