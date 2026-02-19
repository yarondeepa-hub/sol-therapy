# CTO Skill: Advanced CSS Layout Systems

> **From "looks like WordPress" to "this feels like an exhibition."**
> Copy-paste-ready patterns for editorial, asymmetric, magazine-style layouts.
> Every section includes working CSS. No theory without code.

---

## Table of Contents

1. [CSS Grid Advanced Patterns](#1-css-grid-advanced-patterns)
2. [CSS Subgrid](#2-css-subgrid)
3. [Container Queries](#3-container-queries)
4. [Advanced Positioning Techniques](#4-advanced-positioning-techniques)
5. [Fluid Everything](#5-fluid-everything)
6. [Magazine / Editorial Layouts](#6-magazine--editorial-layouts)
7. [RTL-Specific Layout Considerations](#7-rtl-specific-layout-considerations)
8. [Ready-to-Use Patterns for Sol Therapy](#8-ready-to-use-patterns-for-sol-therapy)

---

## 1. CSS Grid Advanced Patterns

### 1.1 Asymmetric Grid Layouts

The default `1fr 1fr` grid is the enemy. Symmetric grids scream "template." These ratios create visual tension and hierarchy.

**Golden Ratio (1.618:1 = ~62/38):**

```css
.grid-golden {
  display: grid;
  grid-template-columns: 1.618fr 1fr;
  gap: clamp(1.5rem, 3vw, 4rem);
}
```

**60/40 Split:**

```css
.grid-60-40 {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: clamp(2rem, 4vw, 6rem);
}
```

**70/30 Split (dominant image + sidebar text):**

```css
.grid-70-30 {
  display: grid;
  grid-template-columns: 7fr 3fr;
  gap: clamp(1.5rem, 3vw, 4rem);
  align-items: start; /* prevents stretching */
}
```

**Flipped asymmetry - alternate rows:**

```css
.grid-alternating > *:nth-child(even) {
  direction: rtl; /* flip child order visually */
}
.grid-alternating > *:nth-child(even) > * {
  direction: ltr; /* restore text direction */
}
```

A cleaner approach for alternating without direction hacks:

```css
.grid-alternating {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: clamp(2rem, 4vw, 6rem);
}

.grid-alternating > *:nth-child(even) {
  grid-column: 1; /* push to first column */
}

.grid-alternating > *:nth-child(even) + * {
  grid-column: 2;
  grid-row: auto; /* same row */
}
```

Or explicitly with `order`:

```css
.grid-alternating > section:nth-child(4n+3) { order: 1; } /* image */
.grid-alternating > section:nth-child(4n+4) { order: 0; } /* text first */
```

---

### 1.2 Grid Template Areas for Magazine Layouts

Named grid areas make complex layouts readable and maintainable. This is the single most powerful tool for editorial layouts.