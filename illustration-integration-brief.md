# Illustration Integration Brief - Sol Therapy Website

> Sumi-e ink wash artwork woven into the fabric of the site - not decoration, but atmosphere.

---

## 1. Overall Vision

The Sol Therapy website already speaks the language of Washi and ink through its typography and color palette. What it lacks is the visual layer that transforms the space from a well-designed page into an immersive, breathing environment. The goal is to integrate Sumi-e / ink wash illustrations as **structural elements** - they define the transitions between sections, they create depth behind content, they replace generic stock photography with artwork that belongs to the brand. Like a scroll painting unrolled in a gallery, the illustrations should reveal themselves as the visitor moves through the page, each section a new chapter in a single continuous landscape.

---

## 2. Color Strategy

### Primary Illustration Palette

| Color | HEX | Role in Illustrations |
|-------|-----|----------------------|
| **Indigo** | `#264348` | Mountain silhouettes, deep water, night sky, primary ink tone |
| **Prussian Blue** | `#314D59` | Mid-tones, atmospheric haze, Bokashi gradients |
| **Pine Green** | `#588475` | Foliage, hills, organic elements, secondary ink tone |
| **Washi Cream** | `#F2EAD3` | Negative space, mist, light areas, "paper showing through" |
| **Beni** | `#BE5069` | Accent ONLY - hanko seals, occasional bloom, spider lily |
| **Vermilion** | `#D3381C` | Signature seal stamps exclusively |

### Color Rules for Illustrations

1. **No full-spectrum color** - Each illustration uses a maximum of 2 tones plus the cream ground
2. **Hero + Sound sections** (indigo background): Illustrations in lighter cream/white tones, very low opacity
3. **About + Events + Gallery + Footer** (cream background): Illustrations in indigo/green tones, low-to-medium opacity
4. **Beni appears sparingly** - A red accent in maybe 2 illustrations across the entire page. Like a hanko stamp pressed once.
5. **Gradients follow Bokashi technique** - Smooth, diffused transitions. Never hard edges on color fields.

---

## 3. Section-by-Section Integration Plan

---

### SECTION 1: HERO - "The Mountain Emerges"

**Current state:** Solid indigo background, a faint `hero-mountain.webp` at 15% opacity, logo centered, tagline below.

**Illustration placement:**

#### A. Hero Background - Full Viewport Sumi-e Mountain Landscape

- **Location:** Replaces `hero__bg` - full absolute positioned background covering the entire hero section
- **Subject:** Dramatic layered mountain peaks in Sumi-e style. 3-4 layers of mountains receding into distance, with luminous mist/clouds between the layers. The closest mountain silhouette is at the bottom third, nearly touching the viewer. The distant peaks dissolve into white mist. Similar to Yaron's reference images 1 and 5 (dark indigo mountains with white mist).
- **Color palette:** Monochrome indigo to cream. Darkest peaks in `#1a2f33` (darker than site indigo), mid-mountains in `#264348`, distant peaks in `#314D59`, mist/sky in cream `#F2EAD3` fading to transparent
- **Size/Position:** Full bleed, `position: absolute; inset: 0;` covering entire hero viewport. Mountains concentrated in the lower 60% of the frame.
- **Opacity/Blend:** 25-35% opacity. The mountains should be visible but atmospheric - a presence, not a poster. The existing Bokashi gradient at the bottom (`hero__bokashi`) blends the mountains into the cream of the About section.
- **Animation:** Subtle parallax on scroll - the mountain layers move at slightly different speeds (closest faster, distant slower). CSS `transform: translateY()` driven by scroll position. 3 separate layers as separate `<img>` elements for the parallax effect.
- **Generation method:** **Replicate AI (Flux)** - Generate as a wide panoramic image (2560x1440 or 3840x1080), then split into 3 layers in post-processing (front mountains, mid mountains, distant peaks + sky).

#### B. Small Beni Accent - Hanko Seal

- **Location:** Bottom-right of the hero, above the Bokashi gradient, positioned asymmetrically
- **Subject:** A small vermilion hanko seal stamp. Circular or square, with stylized characters inside.
- **Color:** `#D3381C` at 50-60% opacity
- **Size:** 40-60px, small and subtle
- **Animation:** Fades in after the logo animation completes (delay 1.5s)
- **Generation method:** SVG - hand-drawn feel, slightly imperfect edges. CSS filter for ink-bleed effect.

---

### TRANSITION: Hero -> About - "Mist Dissolving"

**Current state:** The `hero__bokashi` div creates a linear gradient from transparent to cream.

**Enhancement:**

- **Subject:** Replace the linear gradient with an organic ink wash edge. The mountain peaks in the hero dissolve into wisps of mist that become the cream background. Not a geometric transition - an organic, painted one.
- **Implementation:** A PNG/WebP with transparency. The top is transparent (showing the hero), the middle is ink-wash mist strokes in various densities, the bottom is solid cream. Width: 100%, height: 30-40vh.
- **Generation method:** **Replicate AI (Flux)** - Generate horizontal ink wash mist/cloud pattern on transparent background. Then overlay with CSS.

---

### SECTION 2: ABOUT - "Landscape Alongside Text"

**Current state:** Two-column grid. Left: text block ("about__text-block"). Right: `section-landscape.webp` image at 40% opacity.

**Illustration placement:**

#### A. About Visual - Replace Stock Image with Sumi-e Landscape

- **Location:** Replaces the existing `about__visual img` element
- **Subject:** A Sumi-e landscape painting in the style of reference image 3 (the website mockup). Green watercolor hills/waves flowing horizontally, with a suggestion of water and sky. Organic brushwork, calligraphic quality. A sense of depth through overlapping layers of green hills. Matches the "rolling green hills" aesthetic from reference image 2.
- **Color palette:** Pine green (`#588475`) with lighter sage tones, on cream (`#F2EAD3`) ground. A single small vermilion hanko seal in the bottom-left corner.
- **Size/Position:** `max-width: 480px;` maintaining the current positioning. The illustration should have generous negative space (Ma) - 50-60% of the canvas should be empty cream.
- **Opacity/Blend:** 70-85% opacity. This is the first piece of artwork the visitor truly sees after the hero - it should have presence, but remain quiet.
- **Animation:** Reveal on scroll. The existing `reveal` class handles this - fade up and in.
- **Generation method:** **Replicate AI (Flux)** - Generate on cream/off-white background matching `#F2EAD3`.

#### B. Decorative Brushstroke - Background Accent

- **Location:** Behind the text block, top-right corner, partially clipped by the section boundary
- **Subject:** A single large calligraphic brushstroke, like a diagonal sweep of ink. Very light, almost ghostly.
- **Color:** `#588475` at 4-6% opacity
- **Size:** Large - about 400px wide, rotated slightly
- **Animation:** None - static background element
- **Generation method:** **SVG** or CSS. A single path with variable stroke width and slight irregularity.

---

### TRANSITION: About -> Events - "Wave Divider"

**Current state:** `wave-divider` div with a `wave-divider.webp` image at 6% opacity.

**Enhancement:**

- **Location:** Same position, same dimensions
- **Subject:** Replace the current wave divider with a proper Sumi-e ink wash horizontal stroke. Not a wave - a single horizontal ink drag across the full width, with the ink pooling and thinning organically. Like a calligrapher dragging a loaded brush across the page in one confident stroke.
- **Color:** Indigo `#264348` or green `#588475`, rendered at 8-10% opacity
- **Size:** Full width, 80-120px tall
- **Generation method:** **Replicate AI (Flux)** - Generate a single horizontal ink stroke on white/transparent background. Can also be done as SVG for performance.

---

### SECTION 3: EVENTS - "Clean, Minimal - Let the Content Breathe"

**Current state:** Cream background, typographic catalog layout with event entries separated by thin lines.

**Illustration placement:**

This section should remain **primarily typographic**. The events listing is content-heavy and needs clarity. The illustration role here is atmospheric, not central.

#### A. Subtle Background Texture - Ink Mist

- **Location:** Fixed background, covering the top-right quadrant of the section
- **Subject:** Very light ink mist/cloud. Not a landscape - just atmospheric haze. A few wisps of diluted ink floating.
- **Color:** `#264348` at 3-4% opacity
- **Size:** About 40% of the section width, 50% of its height, positioned top-right (top-left in the visual flow since RTL)
- **Animation:** None - static
- **Generation method:** **Replicate AI (Flux)** - Minimal ink cloud on white background.

#### B. Ink Wash Border Accent on Event Entries

- **Location:** Replace the `border-bottom: 1px solid` lines between event entries
- **Subject:** Instead of CSS borders, use a very thin ink wash line - slightly irregular, slightly organic. Not a ruled line but a brushed one.
- **Implementation:** CSS `border-image` using a horizontal ink stroke SVG, or a repeating background image on a pseudo-element
- **Generation method:** **SVG** - Create 3-4 variations of a thin horizontal brushstroke and rotate between them for visual variety.

---

### SECTION 4: GALLERY - "Sumi-e Gallery Wall"

**Current state:** 3x2 grid of Unsplash stock photos with captions. This is the weakest section visually - generic images that don't represent the brand.

**Complete Redesign - Two Options:**

#### Option A (Recommended): Mixed Gallery - Event Photos + Sumi-e Art

Replace the stock photos with a mix of:
- 3 slots: **Real event photography** (from Sol Therapy events - Yaron would need to provide these)
- 3 slots: **Sumi-e artwork** that represents the Sol Therapy aesthetic

The Sumi-e pieces serve as the "art direction" of the gallery - they set the tone while real photos provide authenticity.

**Sumi-e pieces for the gallery:**

1. **"Mountain Mist"** - Indigo mountain peaks dissolving into mist. Horizontal format. References image 4 (blue ink mountains on cream).
2. **"Sound Waves"** - Abstract concentric water ripples in ink wash. Square format. The vibration of a singing bowl visualized.
3. **"Bamboo & Silence"** - A single bamboo stalk with 2-3 leaves, vast empty space. Vertical energy in a horizontal frame.

- **Color:** Each piece uses a different primary tone from the palette - one indigo, one green, one mixed with a beni accent
- **Size:** Match the current grid item heights. Generate at 1600x1200 for horizontal, 1200x1600 for vertical.
- **Filter:** Apply `filter: saturate(0.82) contrast(1.05)` via CSS to match real photos

#### Option B: Full Sumi-e Gallery

Replace ALL 6 images with Sumi-e artwork. The gallery becomes a curated art collection that represents Sol Therapy's visual identity. Each piece is a different subject from the brand motif library (mountains, water, bamboo, spider lily, enso circle, mist landscape).

**Risk:** Without real event photos, the section loses social proof. But it gains a powerful artistic statement.

**Gallery Frame Treatment (applies to both options):**

- **Subject:** Each gallery item gets a subtle inner shadow/frame effect that resembles aged paper edges
- **Implementation:** CSS `box-shadow: inset 0 0 30px rgba(38,67,72,0.08)` on each `.gallery__item`
- **No additional border/frame images needed** - the existing clip-path reveal animation is strong enough

---

### TRANSITION: Gallery -> Trust -> Sound - "Descent into Deep Water"

**Current state:** The `bokashi-to-dark` div creates a cream-to-indigo gradient before the Sound section.

**Enhancement:**

- **Location:** Replace `bokashi-to-dark` with a taller transition element (30vh instead of 20vh)
- **Subject:** An ink wash that begins as cream at the top and descends into deep indigo water. The feeling of sinking beneath the surface. Organic, not geometric. The ink should flow downward in tendrils and pools, getting denser toward the bottom.
- **Color:** Cream `#F2EAD3` to indigo `#264348` with organic ink-wash intermediary
- **Generation method:** **Replicate AI (Flux)** - Generate vertical ink wash gradient on cream background

---

### SECTION 6: SOUND - "Deep Water"

**Current state:** Indigo background with `water-ripples.webp` at 6% opacity, centered. Audio player and text.

**Illustration placement:**

#### A. Water Ripples - Enhanced Background

- **Location:** Replace `sound__bg` element
- **Subject:** Concentric water ripples emanating from the center, in Sumi-e ink wash style. Not photographic ripples - painted ones. The rings should be slightly irregular, as if drawn by hand. Some rings thicker, some thinner. The outermost rings dissolve into nothing.
- **Color:** Cream/light tones on the indigo background. `#F2EAD3` at 5-8% opacity
- **Size:** 80vw circle, centered
- **Animation:** Very slow rotation - `animation: spin 120s linear infinite;` - barely perceptible, creates a living quality
- **Generation method:** **Replicate AI (Flux)** or **SVG**. SVG preferred for the clean circular geometry with hand-drawn line quality.

#### B. Ink Splash Accent

- **Location:** Top-left corner (top-right in RTL visual), partially outside the viewport
- **Subject:** A splash of ink - a single drip or splash mark, as if someone accidentally flicked their brush. Raw, organic, unplanned.
- **Color:** Cream `#F2EAD3` at 3-4% opacity on the indigo background
- **Size:** 200-300px
- **Animation:** None
- **Generation method:** **SVG** - randomized splash path

---

### TRANSITION: Sound -> Footer - "Rising to the Surface"

**Current state:** `bokashi-to-light` div, indigo-to-cream gradient.

**Enhancement:** Same approach as the Hero-to-About transition but inverted. An organic ink wash edge where the deep indigo dissolves upward into cream through wisps of mist. Mirror/flip the hero transition asset.

---

### SECTION 7: FOOTER - "Quiet Ending"

**Current state:** Cream background, two-column grid (newsletter + contact), bottom bar with social links and hanko stamp.

**Illustration placement:**

#### A. Subtle Mountain Echo

- **Location:** Background, bottom-right corner of the footer (bottom-left in RTL visual)
- **Subject:** A very faint echo of the hero mountain silhouette. Just one or two distant peaks, as if the landscape from the hero reappears far away in the mist. A callback, a closing of the circle.
- **Color:** `#588475` at 3-5% opacity
- **Size:** About 30% of footer width, positioned in the corner
- **Animation:** None - static
- **Generation method:** Can reuse the hero mountain distant layer at reduced opacity

#### B. Hanko Stamp Enhancement

- **Location:** Replace the CSS `.hanko` element with an actual illustration
- **Subject:** A proper vermilion hanko seal stamp. Slightly imperfect - ink pooling in corners, thin spots where the stamp didn't press evenly. Contains "ST" or a stylized Sol character.
- **Color:** `#D3381C` at 70% opacity
- **Size:** 48-56px square
- **Generation method:** **SVG** - hand-crafted seal design with imperfect edges and ink-bleed texture

---

## 4. Generation Prompts (Replicate Flux Model)

### Prompt 1: Hero Mountain Landscape (3 layers)

**Layer 1 - Distant peaks + sky:**
```
Minimalist Sumi-e ink wash painting of distant mountain peaks dissolving into white mist. Japanese ink painting style. Very light, ethereal, barely visible mountain silhouettes in pale indigo gray. Vast negative space. Washi paper texture. Horizontal panoramic composition. Monochrome indigo and cream palette. Atmospheric, meditative. No detail - just suggestion of form through diluted ink washes. Shin-hanga influence. Colors: pale gray-blue (#6a8a96) fading to warm cream (#F2EAD3).
```
**Negative prompt:** photorealistic, 3D, busy, detailed, colorful, sunset, trees, buildings, people, text, watermark, frame, border

**Layer 2 - Mid mountains:**
```
Sumi-e ink wash painting of mountain range, medium tonal value. Japanese ink painting brushwork. Three overlapping mountain silhouettes with soft edges dissolving into mist at the peaks. Visible brushstrokes with varying ink density. Horizontal panoramic. Monochrome in medium indigo tone (#314D59) on transparent/white background. Bokashi gradient technique - ink concentration varies naturally. Washi paper texture. Ma negative space principle - 40% of composition is empty.
```
**Negative prompt:** photorealistic, colorful, detailed trees, sunset, people, animals, text, watermark

**Layer 3 - Foreground mountains (closest):**
```
Bold Sumi-e ink wash painting of dramatic mountain peaks in the foreground. Strong brushwork, confident calligraphic strokes. Dark indigo ink (#1e353a) with rich tonal variation. Peaks are sharp and defined at the top, dissolving into mist at the base. Horizontal panoramic composition. The darkest, most dramatic layer. Japanese ink painting inspired by Sesshu Toyo. Washi paper texture. Ink pooling effects at the base of mountains.
```
**Negative prompt:** photorealistic, 3D render, colorful, sunset, gradient sky, people, text, watermark

### Prompt 2: About Section Landscape

```
Sumi-e ink wash landscape painting of rolling green hills and distant mountains. Japanese watercolor style. Soft sage green (#588475) and olive tones on warm cream paper (#F2EAD3). Gentle, meditative mood. Layered horizontal hills receding into distance with atmospheric perspective. A small vermilion red hanko seal stamp in the bottom left corner. Generous negative space - Ma principle - 55% empty cream space. Washi paper texture visible. Flowing organic brushwork. Inspired by Kawase Hasui landscape prints. Horizontal composition, wide format.
```
**Negative prompt:** photorealistic, busy, colorful, sunset, people, buildings, modern, text (except seal), watermark, frame

### Prompt 3: Hero-to-About Mist Transition

```
Abstract horizontal ink wash mist and clouds. Japanese Sumi-e style. Wisps of diluted ink floating and dispersing from top to bottom. Dense at the top (dark indigo #264348), gradually thinning and breaking apart into nothing toward the bottom (white/transparent). Organic, unpredictable ink behavior - pooling, bleeding, thinning. Very wide horizontal format (5:1 ratio). No subject - pure atmospheric ink wash texture. Washi paper visible through the thin areas.
```
**Negative prompt:** mountains, landscape, objects, people, text, frame, geometric, sharp edges

### Prompt 4: Wave Divider Brushstroke

```
Single horizontal calligraphic brushstroke drawn across the full width. Japanese Sumi-e ink. The brush was loaded with ink on the left, dragged across to the right - ink thins and breaks up naturally. Variable line weight. Ink pooling on one end, dry brush texture on the other. Minimal - just one confident stroke on white paper. Washi paper texture. High contrast black ink on cream. Very wide format.
```
**Negative prompt:** multiple strokes, complex, detailed, colorful, text, geometric

### Prompt 5: Gallery Art - Mountain Mist (Indigo)

```
Horizontal Sumi-e ink wash landscape. Layered mountain peaks in indigo blue (#264348) tones on warm cream background (#F2EAD3). Three layers of mountains with luminous white mist between them. Japanese ink painting style. Small vermilion red hanko seal in bottom right. Atmospheric perspective through ink density variation. Peaceful, contemplative. Bokashi gradient technique. Washi paper texture. Inspired by Hiroshi Yoshida mountain prints.
```
**Negative prompt:** photorealistic, colorful, sunset, people, text (except seal), modern, digital

### Prompt 6: Gallery Art - Sound Waves (Green)

```
Abstract Sumi-e ink wash painting of concentric water ripples. Japanese ink painting style. Circles emanating from a central point, painted with a single loaded brush in sage green (#588475) ink on warm cream paper (#F2EAD3). The circles are slightly imperfect - hand-drawn, not geometric. Outer rings fade and break apart. Massive negative space - the ripples occupy only the center-lower portion. Meditative, zen aesthetic. Square composition.
```
**Negative prompt:** photorealistic, colorful, pond, water drops, 3D, realistic water, fish, lotus

### Prompt 7: Gallery Art - Bamboo & Silence

```
Minimalist Sumi-e ink painting of a single bamboo stalk with two or three leaves. Japanese ink wash style. Bold vertical brushstroke for the stalk, delicate lighter strokes for leaves. Monochrome - dark ink (#264348) with varied wash tones. Enormous negative space - Ma principle - the bamboo occupies less than 20% of the composition, placed asymmetrically to the right. Warm cream washi paper background (#F2EAD3). Calligraphic quality. Inspired by traditional Zen ink paintings. A single small beni-colored (#BE5069) accent - perhaps a tiny insect or a subtle color wash at the leaf tip.
```
**Negative prompt:** photorealistic, colorful, garden, forest, many plants, busy, symmetrical, centered

### Prompt 8: Water Ripples for Sound Section

```
Concentric water ripples drawn in Sumi-e ink wash style. Light cream (#F2EAD3) ink on dark indigo background (#264348). Circles emanating outward from center. Hand-painted quality - not geometric circles but organic, slightly irregular rings. Some rings thicker, some barely there. The outermost rings dissolve into nothing. Very subtle, ethereal. Japanese ink painting aesthetic. Square format. The feeling of a stone dropped into still dark water.
```
**Negative prompt:** colorful, bright, 3D, realistic water, splash, photorealistic, text

### Prompt 9: Descent Transition (Gallery -> Sound)

```
Vertical ink wash transition. Top is clean warm cream (#F2EAD3), bottom is dense dark indigo (#264348). Between them: organic ink flowing downward in tendrils and pools, getting denser and darker toward the bottom. Like ink dropped into water, seen from the side. Sumi-e ink wash style. The ink descends in natural, unpredictable patterns - some areas dense, some thin, creating an organic transition from light to dark. Very wide horizontal format (5:1 ratio). Japanese ink painting technique.
```
**Negative prompt:** landscape, mountains, objects, geometric, sharp edges, text, frame

---

## 5. CSS Integration Notes (for CTO)

### General Implementation Approach

1. **Use `<picture>` elements** with WebP format for all illustrations. Provide fallback PNG.
2. **Lazy load** all illustrations below the fold using `loading="lazy"`.
3. **Separate parallax layers** in the hero as individual absolutely-positioned images with different `data-speed` attributes for the scroll parallax JS.
4. **Illustrations as background images** where they serve as decoration (events section mist, footer mountain echo). Use CSS `background-image` with `background-size: contain` or `cover` as appropriate.
5. **SVG inline** for small accent elements (brushstroke dividers, hanko stamps, ink splashes) for performance and scalability.

### Specific CSS Patterns

**Hero Parallax Layers:**
```css
.hero__mountain-layer {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center bottom;
    will-change: transform;
}
.hero__mountain-far { opacity: 0.12; z-index: 1; }
.hero__mountain-mid { opacity: 0.18; z-index: 2; }
.hero__mountain-near { opacity: 0.25; z-index: 3; }
```

**Organic Transitions (replacing linear gradients):**
```css
.transition-mist {
    width: 100%;
    height: 35vh;
    background-image: url('assets/illustrations/mist-transition.webp');
    background-size: 100% 100%;
    background-repeat: no-repeat;
}
```

**Ink Wash Section Dividers:**
```css
.ink-divider {
    width: 100%;
    height: 2px;
    background-image: url('assets/illustrations/brushstroke-divider.svg');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    opacity: 0.12;
}
```

**Gallery Inner Frame Effect:**
```css
.gallery__item::after {
    content: '';
    position: absolute;
    inset: 0;
    box-shadow: inset 0 0 40px rgba(38, 67, 72, 0.1);
    pointer-events: none;
}
```

**Sound Section Slow Rotation:**
```css
.sound__ripples {
    animation: slow-spin 120s linear infinite;
}
@keyframes slow-spin {
    from { transform: translate(-50%, -50%) rotate(0deg); }
    to { transform: translate(-50%, -50%) rotate(360deg); }
}
```

### Performance Considerations

- Hero mountain layers: Load immediately (above the fold). Use `fetchpriority="high"` on the nearest layer.
- All other illustrations: `loading="lazy"`.
- SVG elements should be inlined, not loaded as images, for elements under 5KB.
- Consider using CSS `content-visibility: auto` on sections below the fold.
- Total illustration weight target: Under 500KB compressed for all assets combined.

### File Naming Convention

```
assets/illustrations/
  hero-mountain-far.webp       (distant peaks)
  hero-mountain-mid.webp       (mid mountains)
  hero-mountain-near.webp      (foreground mountains)
  hero-hanko-seal.svg           (small vermilion seal)
  transition-mist-down.webp    (hero -> about transition)
  transition-mist-up.webp      (sound -> footer transition)
  about-landscape.webp          (green hills landscape)
  about-brushstroke.svg         (background accent)
  divider-brushstroke.svg       (section divider line)
  events-mist.webp              (subtle background texture)
  gallery-mountains.webp        (gallery art piece 1)
  gallery-ripples.webp          (gallery art piece 2)
  gallery-bamboo.webp           (gallery art piece 3)
  transition-descent.webp       (gallery -> sound transition)
  sound-ripples.svg             (water ripples background)
  sound-ink-splash.svg          (corner accent)
  footer-mountain-echo.webp     (faint callback to hero)
  footer-hanko-seal.svg         (proper stamp illustration)
```

---

## 6. Priority Order

### Phase 1 - Maximum Impact (implement first)

| # | Asset | Why First |
|---|-------|-----------|
| 1 | **Hero Mountain Layers** (3 images) | First thing every visitor sees. Transforms the hero from flat indigo to a living landscape. |
| 2 | **About Section Landscape** | Replaces the faint stock-style image with authentic Sumi-e art. Second thing visitors see. |
| 3 | **Hero-to-About Mist Transition** | Replaces the hard linear gradient with organic ink wash. Connects the two most important sections. |

### Phase 2 - Structural Improvements

| # | Asset | Why Second |
|---|-------|------------|
| 4 | **Wave Divider Brushstroke** | Quick replacement of existing asset. Small effort, noticeable improvement. |
| 5 | **Gallery Art Pieces** (3 images) | Replaces all Unsplash stock. Even if real event photos are mixed in later, the Sumi-e pieces establish the gallery's character. |
| 6 | **Gallery-to-Sound Descent Transition** | Turns the flat gradient into a dramatic ink-wash moment. |

### Phase 3 - Refinement & Atmosphere

| # | Asset | Why Third |
|---|-------|-----------|
| 7 | **Sound Section Water Ripples** | Enhancement of existing element. SVG replacement for the current bitmap. |
| 8 | **Footer Hanko Seal** | Small detail that elevates the footer from functional to branded. |
| 9 | **Events Section Mist Background** | Very subtle - adds atmosphere to a content-heavy section. |
| 10 | **Footer Mountain Echo** | Quiet callback to the hero. A detail for attentive visitors. |

### Phase 4 - Polish

| # | Asset | Why Last |
|---|-------|----------|
| 11 | **Ink Wash Divider Lines** (SVG) | Replace CSS borders between event entries. Subtle refinement. |
| 12 | **About Brushstroke Background** | Barely visible - a whisper of decoration behind text. |
| 13 | **Sound Section Ink Splash** | Corner accent. Very minor. |
| 14 | **Sound-to-Footer Mist Transition** | Mirror of the hero transition. Can reuse assets. |

---

## 7. What NOT to Do

- **Do not illustrate every section equally.** The Events section and FAQ should breathe. Not every surface needs artwork.
- **Do not use realistic gradients or Photoshop-style effects.** Every visual element should feel hand-painted, imperfect, organic.
- **Do not center illustrations symmetrically.** Follow the Sumi-e principle of asymmetry. Mountains shift to one side. Brushstrokes trail off to an edge.
- **Do not use any motifs from the "Do Not" list:** no lotus flowers, no chakras, no mandala patterns, no rainbow colors, no dreamcatchers, no third-eye symbols.
- **Do not make the illustrations compete with the text.** They serve the text. They create the world the text lives in. The content is still king.
- **Do not exceed 8-10% opacity for background illustrations.** The moment an illustration behind text becomes distracting, it has failed its purpose.
- **Do not forget Ma.** When in doubt, leave it empty.

---

*Brief prepared by Illustrator Agent. Ready for CTO implementation.*
*Illustration generation via Replicate Flux model. SVG accents handcrafted.*
