# Gallery Design Brief: "Scroll Tokonoma"

## Concept Name: Scroll Tokonoma (床の間 - the Alcove Gallery)

---

## AGENT: Illustrator
## STATUS: complete
## MERGE_KEY: gallery_design_brief
## DEPENDENCIES_SATISFIED: CTO can implement

---

## Research Summary - 6 Reference Sites

### Key Patterns Discovered

| Site | Gallery Pattern | What Makes It Special |
|------|----------------|----------------------|
| **rotemcohensoaye** | Asymmetric masonry, varying sizes, dark bg | Zero UI - work IS the interface. No cards, no borders, no shadows |
| **exhibition.nli** | Full-bleed artifacts as viewport backgrounds | Image IS the space. Large typography overlaid directly on content |
| **migdalor.nli** | Color blocks + cutout portraits + LED clock | Time-as-UI. Bold color shifts between sections |
| **telavivdance** | Horizontal carousel, 3 items, dark bg | Performance photos with structured metadata |
| **docutext.nli** | Full-bleed B&W imagery, stacked headlines | Poster-like sections. Content as background |
| **epilogue-nli** | Collage cutouts on bold color fields | Dithered/pixelated portrait art. Dramatic time displays |

### Universal Patterns (shared by ALL 6 sites)

1. **Content IS the design** - artifacts, work, performers ARE the UI. Not thumbnails in boxes.
2. **Dark backgrounds** - every single site uses dark or bold color as gallery context.
3. **Zero container chrome** - no card borders, no drop shadows, no rounded corners, no divider lines.
4. **Massive typography** - text is an architectural element, not a label.
5. **Asymmetric layouts** - nothing is centered symmetrically. Museum-wall placement.
6. **Progressive disclosure** - content reveals through scroll, not through "load more" buttons.

### Critical Insight

> **What failed in previous attempts (blob grid, horizontal strip) was treating images as objects sitting ON a surface. The reference sites treat images as environments that you move THROUGH.**

---

## The Concept: Scroll Tokonoma

### What is a Tokonoma?

A **Tokonoma** (bed no ma) is the recessed alcove in a Japanese room where a single scroll painting is displayed. Only one artwork at a time. The viewer's attention is undivided. The empty space around the artwork (Ma) is sacred.

### The Gallery Mechanic

Instead of showing all 6 images simultaneously (grid) or in a conveyor belt (horizontal scroll), the **Scroll Tokonoma** presents images ONE AT A TIME as the user scrolls vertically. Each image is a full-width "moment" that the viewer passes through - like walking through rooms in a gallery, or unrolling a hand scroll (emakimono).

### How it works - step by step

```
User scrolls down through the page...

[Events section ends]
[Trust bar]

--- GALLERY SECTION BEGINS ---

1. The section title "רגעים מהמרחב" fades in as a large,
   centered, breathing typographic element on Washi cream.
   Below it, a thin Sumi-e brush line extends downward
   like ink dripping - this becomes the scroll spine.

2. As user continues scrolling, the FIRST image rises from
   below like a scroll being unfurled. It enters at roughly
   70% viewport width, positioned asymmetrically (offset to
   one side). The caption appears opposite the image, aligned
   to the scroll spine.

3. As the user scrolls past, the image SLOWLY drifts upward
   with a parallax offset (slower than scroll speed), creating
   a gentle floating feeling. Opacity softly fades from 1 to 0.

4. The SECOND image enters from the opposite side. If the first
   was right-aligned, this one is left-aligned. The alternating
   rhythm creates a snake-like descent through the gallery.

5. Between each image, the scroll spine (thin vertical ink line)
   is visible - connecting them into a single continuous scroll.

6. The LAST image transitions into the Bokashi gradient that
   leads to the dark Sound section below.

--- GALLERY SECTION ENDS ---
```

### Why This is Original

| Existing Pattern | How We Differ |
|------------------|---------------|
| Grid gallery | One image at a time. Full focus. Ma everywhere. |
| Horizontal scroll | Vertical scroll. Natural. No hijacking scroll direction. |
| Carousel/slider | No arrows, no dots, no controls. Scroll IS the control. |
| Masonry/Pinterest | Not showing all at once. Progressive revelation. |
| Lightbox gallery | No modal overlay. Images live IN the page flow. |
| Parallax hero sections | Images alternate sides and have metadata. Not just backgrounds. |

**The closest analogy:** An emakimono (hand scroll painting) being unrolled vertically. You see one scene at a time, and the transition between scenes is part of the artwork itself.

---

## Detailed Visual Specifications

### Section Container

```css
.gallery {
    /* Full width, no max-width constraint */
    width: 100%;
    background-color: var(--color-washi); /* #F2EAD3 */
    padding: clamp(6rem, 12vw, 12rem) 0;
    position: relative;
    overflow: hidden;
}
```

### Section Title

```css
.gallery__header {
    text-align: center;
    margin-bottom: clamp(4rem, 8vw, 8rem);
    position: relative;
}

.gallery__label {
    /* Small curatorial label, like exhibition signage */
    font-family: 'Heebo', sans-serif;
    font-weight: 400;
    font-size: clamp(0.75rem, 1vw, 0.875rem);
    letter-spacing: 0.15em;
    color: var(--color-sol-green); /* #588475 */
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.gallery__title {
    font-family: 'Frank Ruhl Libre', serif;
    font-weight: 300;
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    color: var(--color-indigo); /* #264348 */
    line-height: 1.1;
}
```

### The Scroll Spine

A thin vertical ink line running down the center of the gallery, connecting all images into a continuous scroll. It uses a CSS pseudo-element with a Sumi-e brush texture.

```css
.gallery__spine {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 100%;
    top: 0;
    /* Sumi-e ink effect - not a solid line, but slightly irregular */
    background: linear-gradient(
        to bottom,
        transparent 0%,
        var(--color-sol-green) 5%,
        var(--color-sol-green) 30%,
        rgba(88, 132, 117, 0.6) 50%,
        var(--color-sol-green) 70%,
        var(--color-sol-green) 95%,
        transparent 100%
    );
    opacity: 0.3;
    /* Optional: mask with a brush-stroke SVG for organic feel */
}
```

### Individual Gallery Moment (each image + caption pair)

```css
.gallery__moment {
    position: relative;
    display: grid;
    /* Asymmetric two-column grid */
    grid-template-columns: 1fr 1fr;
    gap: clamp(2rem, 4vw, 4rem);
    align-items: center;
    padding: clamp(4rem, 8vw, 8rem) clamp(2rem, 5vw, 6rem);
    min-height: 70vh;
}

/* Odd moments: image right, text left */
.gallery__moment:nth-child(odd) .gallery__image {
    grid-column: 2;
    grid-row: 1;
}
.gallery__moment:nth-child(odd) .gallery__meta {
    grid-column: 1;
    grid-row: 1;
    text-align: left; /* RTL: this means right-aligned visually */
}

/* Even moments: image left, text right */
.gallery__moment:nth-child(even) .gallery__image {
    grid-column: 1;
    grid-row: 1;
}
.gallery__moment:nth-child(even) .gallery__meta {
    grid-column: 2;
    grid-row: 1;
    text-align: right; /* RTL: left-aligned visually */
}
```

### Image Styling

```css
.gallery__image {
    width: 100%;
    max-width: clamp(400px, 55vw, 700px);
    aspect-ratio: 4 / 3; /* Default, can vary per image */
    overflow: hidden;
    position: relative;
}

.gallery__image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    /* Subtle scale for parallax */
    transform: scale(1.08);
    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    /* Slight desaturation to match Washi aesthetic */
    filter: saturate(0.85) contrast(1.05);
}

/* NO border-radius. NO box-shadow. NO card container. */
/* The image sits directly on the Washi surface, like a print laid on paper. */
```

### Caption / Metadata

```css
.gallery__meta {
    max-width: 280px;
}

.gallery__location {
    font-family: 'Frank Ruhl Libre', serif;
    font-weight: 300;
    font-size: clamp(1.5rem, 2.5vw, 2.25rem);
    color: var(--color-indigo);
    line-height: 1.2;
    margin-bottom: 0.5rem;
}

.gallery__year {
    font-family: 'Heebo', sans-serif;
    font-weight: 400;
    font-size: clamp(0.75rem, 1vw, 0.875rem);
    letter-spacing: 0.1em;
    color: var(--color-sol-green);
    opacity: 0.7;
}

/* Optional: a small Enso circle or Sumi-e dot as a decorative accent */
.gallery__meta::before {
    content: '';
    display: block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: var(--color-beni); /* #BE5069 */
    margin-bottom: 1rem;
    opacity: 0.6;
}
```

---

## Animation Behavior

### Scroll-Triggered Reveal (IntersectionObserver)

Each `.gallery__moment` starts hidden and reveals when it enters the viewport.

```javascript
// Each moment observes when it enters the viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
        }
    });
}, {
    threshold: 0.15,       // Triggers when 15% visible
    rootMargin: '0px 0px -10% 0px'  // Slightly before fully visible
});

document.querySelectorAll('.gallery__moment').forEach(moment => {
    observer.observe(moment);
});
```

### CSS Reveal Animation

```css
.gallery__moment {
    opacity: 0;
    transform: translateY(60px);
    transition:
        opacity 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94),
        transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.gallery__moment.is-visible {
    opacity: 1;
    transform: translateY(0);
}

/* Stagger: image and meta appear with slight delay */
.gallery__moment .gallery__image {
    opacity: 0;
    transform: translateY(40px);
    transition:
        opacity 0.6s 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94),
        transform 0.6s 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.gallery__moment .gallery__meta {
    opacity: 0;
    transform: translateY(30px);
    transition:
        opacity 0.6s 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94),
        transform 0.6s 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.gallery__moment.is-visible .gallery__image,
.gallery__moment.is-visible .gallery__meta {
    opacity: 1;
    transform: translateY(0);
}
```

### Subtle Parallax on Scroll

The inner image moves at a slightly different speed than the container, creating a gentle floating/breathing effect. This is the "zen" quality - nothing is static.

```javascript
// Lightweight parallax - CSS transform only, requestAnimationFrame
function initParallax() {
    const images = document.querySelectorAll('.gallery__image img');

    function updateParallax() {
        images.forEach(img => {
            const rect = img.getBoundingClientRect();
            const viewportCenter = window.innerHeight / 2;
            const imageCenter = rect.top + rect.height / 2;
            const offset = (imageCenter - viewportCenter) * 0.04; // Very subtle
            img.style.transform = `scale(1.08) translateY(${offset}px)`;
        });
        requestAnimationFrame(updateParallax);
    }

    requestAnimationFrame(updateParallax);
}
```

**CRITICAL:** The parallax multiplier is `0.04` - extremely subtle. This is NOT a dramatic parallax effect. It's a gentle breathing, like the image is floating on water. If it feels "parallax-y," it's too strong. Reduce.

### Image Hover

On desktop, hovering an image removes the desaturation filter, revealing the original colors. Like wiping mist off a window.

```css
.gallery__image:hover img {
    filter: saturate(1) contrast(1.05);
    transform: scale(1.05);
    transition: all 0.4s ease;
}
```

---

## Responsive Behavior

### Desktop (> 1024px)
- Two-column grid, alternating sides
- Images at 55vw max
- Full spine visible
- Parallax active

### Tablet (768px - 1024px)
- Still two-column but tighter gap
- Images at 60vw max
- Parallax reduced (multiplier 0.02)

### Mobile (< 768px)

```css
@media (max-width: 768px) {
    .gallery__moment {
        /* Stack to single column */
        grid-template-columns: 1fr;
        gap: 1.5rem;
        padding: clamp(3rem, 6vw, 5rem) clamp(1.5rem, 4vw, 2rem);
        min-height: auto;
    }

    /* All images full width, always same column */
    .gallery__moment:nth-child(odd) .gallery__image,
    .gallery__moment:nth-child(even) .gallery__image {
        grid-column: 1;
        grid-row: 1;
    }

    .gallery__moment:nth-child(odd) .gallery__meta,
    .gallery__moment:nth-child(even) .gallery__meta {
        grid-column: 1;
        grid-row: 2;
        text-align: right; /* RTL default */
    }

    .gallery__image {
        max-width: 100%;
    }

    /* Hide spine on mobile */
    .gallery__spine {
        display: none;
    }

    /* Disable parallax on mobile */
    .gallery__image img {
        transform: none !important;
    }
}
```

---

## HTML Structure

```html
<section class="gallery" id="gallery">
    <!-- Scroll spine -->
    <div class="gallery__spine" aria-hidden="true"></div>

    <!-- Header -->
    <div class="gallery__header reveal">
        <div class="gallery__label">archive visuel</div>
        <h2 class="gallery__title">moments from the space</h2>
    </div>

    <!-- Moment 1 -->
    <div class="gallery__moment">
        <div class="gallery__image">
            <img src="[image-url]" alt="sound meditation at Tel Aviv Museum" loading="lazy">
        </div>
        <div class="gallery__meta">
            <div class="gallery__location">Tel Aviv Museum</div>
            <div class="gallery__year">2025</div>
        </div>
    </div>

    <!-- Moment 2 (alternates automatically via nth-child) -->
    <div class="gallery__moment">
        <div class="gallery__image">
            <img src="[image-url]" alt="Pastoral retreat" loading="lazy">
        </div>
        <div class="gallery__meta">
            <div class="gallery__location">Pastoral Retreat</div>
            <div class="gallery__year">2025</div>
        </div>
    </div>

    <!-- Moments 3-6 follow the same pattern -->
    <!-- nth-child handles alternation automatically -->
</section>
```

**NOTE:** The actual Hebrew content should be:
- Label: "archive visuel" (Hebrew: "ארכיון ויזואלי")
- Title: "moments from the space" (Hebrew: "רגעים מהמרחב")
- Location names in Hebrew as they currently are

---

## What Makes This ORIGINAL

1. **The "one at a time" reveal** - No site in the reference set does a vertical scroll-through gallery with alternating sides. Exhibition does full-bleed backgrounds but shows them all as hero sections. We show them as intimate moments with breathing room.

2. **The Scroll Spine** - A continuous ink line connecting all moments into a single scroll. This is a direct reference to emakimono (Japanese hand scroll) and connects to the Sumi-e aesthetic of the broader site. No reference site has this.

3. **Alternating asymmetry** - The snake-like left-right-left-right rhythm creates visual interest without complexity. It feels like a walk through a gallery where you turn your head to see each piece on alternating walls.

4. **The breathing parallax** - Not dramatic. Not "look at me" parallax. A subtle floating that makes each image feel alive, like it's resting on water. This is the zen quality Yaron wants.

5. **Zero chrome** - No borders, no rounded corners, no shadows, no cards. Following every single reference site: the image sits directly on the Washi surface. Like a print laid on Japanese paper.

6. **Progressive desaturation** - Images are slightly muted until hovered, matching the Washi aesthetic. Hover reveals true color. This is the "mist clearing" metaphor.

---

## What This is NOT

- NOT a grid (too static, too Pinterest-like)
- NOT a horizontal scroll (rejected by Yaron, scroll hijacking is annoying)
- NOT a carousel with arrows (too e-commerce, too generic)
- NOT full-bleed hero sections (too heavy for a gallery of 6 images, feels like a separate landing page)
- NOT a masonry layout (too Tumblr, too busy)
- NOT a lightbox gallery (disrupts flow, modal patterns are outdated for this context)

---

## Inspiration Sources

| Source | What We Take |
|--------|-------------|
| Japanese emakimono (hand scrolls) | One scene at a time, revealed through unrolling |
| Museum gallery walk | Alternating walls, breathing room between pieces |
| exhibition.nli.org.il | Images as environments, bold typography on images |
| rotemcohensoaye.com | Zero UI chrome, work IS the interface |
| Tokonoma alcove | Single artwork focus, sacred empty space |
| Sumi-e scroll painting | The vertical ink spine connecting moments |

---

## Performance Notes for CTO

- **No external libraries needed** - Pure CSS Grid + IntersectionObserver + requestAnimationFrame
- **Lazy loading** - All images use `loading="lazy"`
- **No scroll hijacking** - Natural vertical scroll. No `scroll-snap`. No wheel event listeners.
- **No heavy transforms** - Only `translateY` and `scale` (GPU-accelerated)
- **Reduced motion** - Wrap parallax and animations in `prefers-reduced-motion` check
- **Image sizes** - Serve images at 2x for retina. Recommended: 1400px wide at 2x = 700px display. WebP format.

```css
@media (prefers-reduced-motion: reduce) {
    .gallery__moment,
    .gallery__moment .gallery__image,
    .gallery__moment .gallery__meta {
        opacity: 1;
        transform: none;
        transition: none;
    }

    .gallery__image img {
        transform: none !important;
        filter: saturate(0.85) contrast(1.05);
    }
}
```

---

## NOTES

- This concept was designed after visual analysis of all 6 reference sites that Yaron provided
- The key learning: every top-tier cultural site treats images as spatial experiences, not thumbnails
- The Tokonoma metaphor aligns perfectly with Sol Therapy's Zen/Japanese aesthetic
- This is achievable with zero external dependencies - pure CSS/JS
- The spine element can be enhanced later with an actual Sumi-e brush stroke SVG when real images are available
- When real event photography replaces the Unsplash placeholders, the slight desaturation filter will help maintain visual cohesion across images of varying quality and color temperature

---

*Illustrator Agent - Sol Therapy*
*Brief created: 2026-02-12*
*For CTO implementation*
