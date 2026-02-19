```

---

## Phase 3: Illustrations (Illustrator Agent)

### Style: Watercolor / Sumi-e

כל האיורים בסגנון אחיד: צבעי מים / דיו יפני על נייר חם.
מיוצרים באמצעות **Gemini MCP** (`gemini-generate-image`).

### Illustration Set per Blog Post

כל כתבה צריכה 6-8 איורים:

| # | סוג | תפקיד | דוגמה מהכתבה |
|---|-----|--------|-------------|
| 1 | Hero image | תמונה ראשית ב-hero | singing-bowl.jpg |
| 2 | Inline float (washi) | נמס לתוך טקסט בסקשן בהיר | amygdala.jpg |
| 3 | Panoramic break | מעבר בין בהיר לכהה, 21:9 | singing-bowl.jpg (reused) |
| 4 | Inline float (dark) | נמס לתוך טקסט בסקשן כהה | avalokiteshvara.jpg |
| 5-7 | Trio strip | 3 תמונות בקולאז' | yoruba-drums, didgeridoo, pythagoras |
| 8 | Optional extra | לפי צורך | - |

### Style Tokens (5+ מתוך 9 חובה)

| Token | תיאור |
|-------|-------|
| `paper_warm_offwhite` | רקע נייר חם - לא לבן סטרילי |
| `ink_monochrome_brush` | דיו שחור/אפור עם מכחול נראה |
| `negative_space_70` | לפחות 60-75% חלל ריק |
| `vertical_scroll_format` | פורמט אנכי - תחושת scroll/page |
| `shan_shui_nature` | הר/מים/ערפל כצורות מהותיות |
| `bamboo_rhythm` | מקצב של קנים/קווים |
| `topographic_indigo` | טקסטורות מפה/דלתא בכחול-אפור |
| `editorial_microtype` | טיפוגרפיה זעירה כתווית מוזיאלית |
| `wabi_sabi_restraint` | ריסון, טבעיות, חוסר-שלמות אסתטי |

### Prompt Rules

**חובה בכל prompt:**
```
- "warm paper texture" / "warm off-white paper"
- "monochrome ink wash" / "visible brushwork"
- "zen negative space" / "lots of breathing room"
- "one focal subject" / "single central element"
- "traditional [technique] painting style"
- "fine art museum quality"
- "subtle paper grain"
- "no text no letters no numbers"
```

**אסור בכל prompt:**
```
- "vermilion seal" / "red seal stamp" / "hanko"
- "minimal" / "simple" / "sparse" (ירון רוצה עשיר בטקסטורה)
- "abstract" ללא צורות מזוהות
- "flat" / "clean"
- "glossy" / "3D" / "neon" / "gradient"
- "photorealism" / "photographic"
```

### Generation Tool: Gemini MCP

```
mcp__gemini__gemini-generate-image:
  prompt: [see templates below]
  aspectRatio: "3:4" (vertical for inline) or "21:9" (panoramic)
  imageSize: "2K"
  style: "watercolor sumi-e ink wash"
```

### Prompt Templates

**Inline float (vertical 3:4):**
```
[subject] painted in traditional East Asian sumi-e ink wash technique on warm
off-white aged paper, visible wet brushstroke texture, monochrome with subtle
warm undertones, single focal subject surrounded by generous negative space
occupying 65 percent of composition, paper grain visible, fine art museum
quality, contemplative atmosphere, no text no letters no numbers
```

**Panoramic break (21:9):**
```
[subject] in wide panoramic format, traditional ink wash painting technique,
atmospheric layers creating depth, visible brushwork texture, monochrome with
warm paper tones showing through, multiple receding layers from dark foreground
to misty background, rich variation of ink darkness from near-black to
translucent grey washes, paper grain visible, no text no letters no numbers
```

**Trio images (3:4 each, varied subjects):**
```
[cultural subject] painted in sumi-e watercolor style, warm off-white paper
texture visible, single focused composition with one main element, visible
wet brush strokes, contemplative minimalist atmosphere, fine art quality,
no text no letters no numbers
```

### Image File Naming

```
assets/blog/[descriptive-name].jpg
```

Examples: `amygdala.jpg`, `singing-bowl.jpg`, `yoruba-drums.jpg`

---

## Phase 4: HTML/CSS Build (CTO Agent)

### Template Structure

כל כתבת בלוג בנויה כ-HTML עצמאי (`blog-[topic].html`) עם CSS inline ב-`<style>`.

### HTML Structure Pattern

```
<!DOCTYPE html>