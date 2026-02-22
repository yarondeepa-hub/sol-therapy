# Parking Lot - Items Scored 10-15

> Revisited on the 1st of each month.
> Items that didn't make the cut but might become relevant later.

---

## Lab Queue (16-18 - Waiting for Weekly Lab)

> מנוהל אוטומטית על ידי סיור הבוקר. פריטים נכנסים כשהציון 16-18.
> פריטים יוצאים אחרי בדיקה ב-Lab השבועי (עוברים לכרטיסי כלי או לחניון).

| שם | ציון | תאריך | סוכן | סטטוס |
|----|------|-------|------|-------|
| risograph halftone dots | 17/25 | 2026-02-22 | illustrator | waiting |
| crackle glaze ceramics (kannyu) | 18/25 | 2026-02-22 | illustrator | waiting |
| CSS scroll-driven animations | 16/25 | 2026-02-22 | cto | waiting |
| Feldman graphic scores | 17/25 | 2026-02-22 | illustrator | waiting |

---

## Format

```
### [Name] (Score: X/25, Date: YYYY-MM-DD)
- What: [1 sentence]
- Why parked: [What kept the score below 16]
- Revisit trigger: [What would need to change for this to become relevant]
```

---

## Active Items

### Z-Image (Score: 14/25, Date: 2026-02-20)
- What: Efficient 6B-parameter image generation model with 8-step inference
- Why parked: Not available on Replicate, unclear licensing for commercial use, general-purpose model not tuned for our aesthetic
- Revisit trigger: When it appears on Replicate with clear license terms

### Astro 6 (Score: 15/25, Date: 2026-02-20)
- What: Web framework with Cloudflare integration, unified dev/prod runtime, component islands
- Why parked: Violates "boring technology" principle - adds complexity we don't need since our vanilla HTML/CSS/JS stack works fine
- Revisit trigger: If we need component islands, SSR, or edge computing features

### CalliffusionV2 (Score: 12/25, Date: 2026-02-21)
- What: Academic diffusion model for calligraphy generation with stroke-level control (angle, thickness, style)
- Why parked: Research model only - no API, no deployment, unclear commercial license. Concept is sound but not accessible
- Revisit trigger: When deployed on Replicate or available via API

### Mystic Sumi LoRA (Score: 14/25, Date: 2026-02-22)
- What: LoRA model trained on ancient sumi-e art and modern artists. Dynamic compositions with sharp ink lines, soft washes, atmospheric splashes
- Why parked: Only on Civitai, not on Replicate. Unclear commercial license. Perfect brand fit but not accessible
- Revisit trigger: When available on Replicate or via ComfyUI integration

### CSS Anchor Positioning + Popover API (Score: 12/25, Date: 2026-02-22)
- What: CSS-only dropdown menus and tooltips without JavaScript, using anchor positioning
- Why parked: Chrome experimental only. We have minimal interactive UI. Low payoff for current needs
- Revisit trigger: When browser support reaches 90%+ and we need more interactive components

### Zero-JS Architecture (Score: 15/25, Date: 2026-02-22)
- What: Architecture approach replacing JS with modern CSS for animations, interactions, dark mode
- Why parked: Requires significant refactor. Current GSAP stack works. Philosophically aligned but practically costly
- Revisit trigger: Next major site redesign or if GSAP dependency becomes a problem

---

## Archived (no longer relevant)

(none)

---

*Last reviewed: 2026-02-22*
*Next review: 2026-03-01*
