# Tool Card: Recraft V4

> Discovered: 2026-02-22 | Score: 22/25 | Agent: Illustrator

---

## What is it
מודל ייצור תמונות עם "טעם עיצובי" - מקבל החלטות קומפוזיציה, תאורה וצבע שמרגישות מכוונות ולא גנריות. יוצר גם וקטורים אמיתיים (SVG).

## When to use
- כשצריך איורי דיו ושטיפות מים באיכות גבוהה
- כשחשוב שהקומפוזיציה תהיה מעוצבת ולא אקראית
- כשצריך יחס גובה-רוחב ספציפי (תומך ב-14 אפשרויות)
- כשרוצים פלט SVG אמיתי שנפתח ב-Illustrator/Figma

## When NOT to use
- לסגנון פוטוריאליסטי - Flux 2 עדיף
- לטקסט בתוך תמונה - GPT Image או Ideogram עדיפים
- לתמונות עם הרבה פרטים קטנים - המודל נוטה לפשט

## Recipe

### Prerequisites
- Replicate API token
- חשבון עם קרדיט (כ-$0.02 לתמונה ברזולוציה סטנדרטית)

### Steps
1. הכן prompt בשפה טבעית עם תיאורים ספציפיים
2. בחר aspect_ratio מתוך הרשימה (4:3 לנופים רחבים, 3:4 לאנכי, 16:9 לפנורמי)
3. שלח בקשה ל-API וחכה כ-15-20 שניות
4. הורד את התמונה מה-URL שחוזר

### Prompt Skeleton
```
[subject] [technique] painting, [color palette], [composition details],
[texture description], [atmosphere], [paper/background], no text
```

### Code Skeleton
```bash
curl -s -X POST 'https://api.replicate.com/v1/models/recraft-ai/recraft-v4/predictions' \
  -H 'Authorization: Bearer $REPLICATE_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "input": {
      "prompt": "[PROMPT]",
      "aspect_ratio": "[RATIO]"
    }
  }'
```

### Available Aspect Ratios
`1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `16:9`, `9:16`, `1:2`, `2:1`, `14:10`, `10:14`, `4:5`, `5:4`, `6:10`

## Pitfalls (3 common mistakes)
1. **prompts קצרים מדי** - המודל עובד הכי טוב עם תיאורים עשירים. לפחות 50 מילים.
2. **ציפייה לריאליזם** - זה מודל עיצובי. הוא מפרש, לא מעתיק.
3. **Rate limit** - עם פחות מ-$5 קרדיט, מוגבל ל-6 בקשות בדקה עם burst של 1.

## Example
שלושה ניסויים מ-2026-02-22:
- `variation-1-mountains.webp` - הרי דיו דרמטיים עם טפטופים
- `variation-2-bamboo.webp` - במבוק יחיד על נייר קרם, 80% חלל ריק
- `variation-3-hills.webp` - גבעות ירוקות מתגלגלות בווריאציות גוון

Location: `T-tools/learning/trigger-experiments/2026-02-22-recraft-v4/`

## How we use it at Soul Therapy
**מיקום בשרשרת הייצור:** אלטרנטיבה ל-nano-banana-pro ב-Gemini.

**יתרון ספציפי לנו:**
- המודל "מבין" קומפוזיציה - הוא לא ממלא את כל הקנבס אלא משאיר חלל ריק באופן מכוון
- תומך ב-aspect ratios שאנחנו משתמשים בהם (4:3 לנופים, 3:4 לאנכי, 16:9 לפנורמי)
- הטקסטורות שהוא מייצר מרגישות "יד אנושית" יותר מ-Flux

**Prompt modifiers שעובדים:**
- "sumi-e brushwork texture visible" - מכריח טקסטורת מכחול
- "warm off-white aged paper" - מייצר את הרקע הנכון
- "X percent negative space" - עובד! המודל מכבד את זה
- "no text" - חיוני למניעת artifacts

---

## Adoption Score Breakdown

| Parameter | Score | Notes |
|-----------|-------|-------|
| Brand Fit | 4/5 | מצוין לסגנון ink wash. לא מושלם לכל מוטיב. |
| Leverage | 5/5 | 15-20 שניות לתמונה ברמת איכות גבוהה מאוד |
| Repeatability | 4/5 | תוצאות עקביות עם prompts טובים |
| Workflow Export | 5/5 | WebP ישירות, או SVG אמיתי עם גרסת וקטור |
| Risk/License | 4/5 | שימוש מסחרי מותר. תלוי ב-Replicate (פלטפורמה יציבה) |
| **Total** | **22/25** | |

---

*Source: Replicate blog, Morning Scout 2026-02-22*
*Lab tested: Yes - 2026-02-22 (3 variations, all succeeded)*
