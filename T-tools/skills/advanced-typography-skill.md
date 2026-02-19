# Advanced Web Typography Skill

> CTO Skill: Typography as the design, not decoration on design.
> For Sol Therapy - sound healing, Japanese Washi/Sumi-e aesthetic, RTL Hebrew.
> Fonts: Frank Ruhl Libre (Hebrew display), Heebo (Hebrew body), Inter (English).
> Reference: migdalor.org.il where massive type IS the hero.

---

## 1. Fluid Type Scale System

### What is a Fluid Type Scale?

A fluid type scale eliminates media query breakpoints for font sizes. Instead, every size fluidly interpolates between a minimum value (at the smallest viewport) and a maximum value (at the largest viewport). The CSS `clamp()` function handles this in a single declaration.

The formula:

```
font-size: clamp(MIN, PREFERRED, MAX);
```

Where PREFERRED is a `vw`-based value that creates the linear interpolation.

### The Math Behind clamp()

Given:
- `minWidth` = smallest viewport (e.g. 320px)
- `maxWidth` = largest viewport (e.g. 1440px)
- `minSize` = font size at minWidth
- `maxSize` = font size at maxWidth

The preferred value formula:

```
slope = (maxSize - minSize) / (maxWidth - minWidth)
yAxisIntersection = minSize - slope * minWidth
preferred = yAxisIntersection(rem) + slope(vw)
```

Example for a step with min 18px (1.125rem) and max 24px (1.5rem):

```
slope = (24 - 16) / (1440 - 320) = 8 / 1120 = 0.00714
yAxisIntersection = 18 - (0.00714 * 320) = 18 - 2.286 = 15.714px = 0.982rem
preferred = 0.982rem + 0.714vw

font-size: clamp(1.125rem, 0.982rem + 0.714vw, 1.5rem);
```

### Modular Scale Ratios

A modular scale multiplies or divides a base size by a consistent ratio at each step. Common ratios:

| Ratio | Name | Feel |
|-------|------|------|
| 1.125 | Major Second | Tight, conservative |
| 1.200 | Minor Third | Compact, professional |
| 1.250 | Major Third | Balanced, versatile |
| 1.333 | Perfect Fourth | Generous, editorial |
| 1.414 | Augmented Fourth | Dramatic, display-heavy |
| 1.500 | Perfect Fifth | Very dramatic, poster-like |
| 1.618 | Golden Ratio | Maximum drama, fine art |

For Sol Therapy: use **1.333 (Perfect Fourth)** at min viewport and **1.414 (Augmented Fourth)** at max viewport. This creates a scale that tightens on mobile but becomes dramatically expressive on desktop. Type-as-design demands a wider ratio on large screens.

### Step Calculation Method

Base size: 16px at 320px viewport, 18px at 1440px viewport.

For each step, multiply/divide by the ratio:

```
step(n) = base * ratio^n

At min viewport (ratio 1.333):
  step--2 = 16 / 1.333^2 = 9.00px
  step--1 = 16 / 1.333   = 12.00px
  step-0  = 16.00px (base)
  step-1  = 16 * 1.333   = 21.33px
  step-2  = 16 * 1.333^2 = 28.43px
  step-3  = 16 * 1.333^3 = 37.90px
  step-4  = 16 * 1.333^4 = 50.52px
  step-5  = 16 * 1.333^5 = 67.34px

At max viewport (ratio 1.414):
  step--2 = 18 / 1.414^2 = 9.00px
  step--1 = 18 / 1.414   = 12.73px
  step-0  = 18.00px (base)
  step-1  = 18 * 1.414   = 25.45px
  step-2  = 18 * 1.414^2 = 35.99px
  step-3  = 18 * 1.414^3 = 50.89px
  step-4  = 18 * 1.414^4 = 71.96px
  step-5  = 18 * 1.414^5 = 101.75px
```

### Complete Sol Therapy Type Scale

```css
:root {
  /* Fluid Type Scale