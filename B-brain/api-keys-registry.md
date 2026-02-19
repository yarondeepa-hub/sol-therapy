# API Keys Registry

Track all external services connected to your AI team.

> **IMPORTANT:** Never store actual API keys in this file. Keep your keys secure in Claude Code settings or environment variables only. This file is for documentation and tracking purposes.

---

## Connected Services

| Service | Purpose | Connected | Status |
|---------|---------|-----------|--------|
| Google Gemini | יצירת תמונות מטקסט | 2026-01-30 | ✅ Active |
| Canva MCP | יצירת ועריכת עיצובים בחשבון Canva | 2026-02-01 | ✅ Active |

---

## Service Details

---

## Google Gemini (Nano Banana Pro)

**Connected:** 2026-01-30
**Purpose:** יצירת תמונות מטקסט (Text-to-Image Generation)
**Used by:** Illustrator Agent
**Billing:** ✅ מחובר לתשלום

### Capabilities
- **Imagen 4** — יצירת תמונות באיכות גבוהה מפרומפט טקסט
- **Image understanding** — ניתוח והבנת תמונות
- **Multi-modal** — עבודה עם טקסט + תמונה יחד

### Limitations
- דורש חשבון עם billing מופעל
- יש הגבלות תוכן (ללא פנים של אנשים אמיתיים וכו')

### Script Location

**סקריפט יצירת תמונות:**
```
T-tools/scripts/gemini-image-gen.py
```

### Usage (Quick Reference)

```bash
# יצירת לוגו Sol Therapy
python3 T-tools/scripts/gemini-image-gen.py --logo

# יצירת תמונה מותאמת אישית
python3 T-tools/scripts/gemini-image-gen.py "your prompt here"
```

**תמונות נשמרות ב:** `C-content/images/`

### Prompt Guidelines for Sol Therapy Style

כשכותבים פרומפט ל-Gemini, לכלול:

```
Style: Minimalist Japanese Hanko seal + Swiss design
Colors: Cream background (#F5F0E8), Seal red (#B74C4C) as accent
Elements: Clean lines, negative space, meditative figures
Mood: Zen, quiet, contemplative
Avoid: Psychedelic, neon colors, visual clutter, wellness clichés
```

### Status
✅ **Active:** API Key configured + Billing enabled (2026-01-30)

---

## Canva MCP (Creative Server)

**Connected:** 2026-02-01
**Purpose:** יצירת ועריכת עיצובים ישירות מ-Claude לחשבון Canva שלך
**Used by:** Illustrator Agent, CTO Agent
**Billing:** לפי תוכנית Canva שלך (יש לך מנוי בתשלום ✅)

### Capabilities

**מה אפשר לעשות:**
- ✅ **יצירת עיצובים חדשים** — מתיאור טקסט
- ✅ **חיפוש עיצובים** — בחשבון Canva שלך
- ✅ **ייצוא** — PNG, PDF
- ✅ **שינוי גודל** — התאמה לפלטפורמות שונות
- ✅ **Autofill templates** — מילוי אוטומטי של תבניות
- ✅ **סיכום מצגות** — קריאה וסיכום תוכן

### Limitations
- ⚠️ עריכת טקסט בתוך עיצוב קיים — דורשת פתיחה בממשק Canva
- ⚠️ עריכה דקה — עדיף לעשות ידנית

### Setup Command Used

```bash
claude mcp add canva -- npx -y mcp-remote@latest https://mcp.canva.com/mcp
```

### Prerequisites
- Node.js v20 ומעלה (✅ מותקן: v24.13.0)
- חשבון Canva (✅ מנוי בתשלום)

### Status
✅ **Active:** Connected successfully (2026-02-01)

### Documentation
- [Canva AI Connector](https://www.canva.com/ai-connector/)
- [Canva MCP Actions](https://www.canva.com/help/mcp-canva-usage/)

---

<!--
Add a new section for each service you connect:

## [Service Name]

**Connected:** [Date]
**Purpose:** [What it does for your agents]
**Used by:** [Which agents use it]

### Capabilities
- [What you can do with it]

### Limitations
- [Usage limits, pricing notes]

### Setup Notes
- [Any special configuration notes]

-->

---

## How to Add a New Service

1. Use the prompt in `T-tools/prompts/BONUS/08-connect-api-keys.md`
2. Follow the setup process
3. Add documentation here (but NOT your actual API key)
4. Update the table above

---

## Example Entry

## Google Gemini (Example)

**Connected:** 2024-01-15
**Purpose:** Generate images from text prompts
**Used by:** Copywriter Agent (for social media visuals)

### Capabilities
- Text-to-image generation
- Image understanding/vision
- Multi-modal content creation

### Limitations
- Free tier: 60 requests/minute
- Images may have watermarks on free tier
- Some content restrictions apply

### Setup Notes
- API key stored in Claude Code settings
- MCP server: `@anthropic/mcp-gemini` (example)

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
