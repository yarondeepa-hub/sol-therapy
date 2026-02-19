# Replicate AI - Master Skill File
## "הכלי המרכזי ליצירת איורים, עריכה, אנימציה ועיבוד תמונה"

> **עודכן: 13.02.2026 - מבוסס על מחקר מעמיק של כל הקולקציות והמודלים**

---

## IRON RULES

1. **ברירת מחדל: google/nano-banana-pro** - לכל ייצור תמונות
2. **אף פעם flux-schnell לאיורים** - רק לטסטים מהירים
3. **קרא taste profile לפני כל ייצור** - `M-memory/illustrator-taste-profile.md`
4. **קרא prompt guide לפני כתיבת prompt** - `T-tools/skills/prompt-engineering-guide.md`
5. **עצור אחרי 2 כשלונות** - החלף מודל או כלי

---

## חיבור טכני

**MCP Server:** `replicate-mcp` via stdio
**Token:** Claude-Sol-Therapy
**חשבון:** yaron.deepa@gmail.com
**חשוב:** כל הרצה עולה כסף. תבונה > כמות.

---

## A. ייצור תמונות (Text-to-Image)

### Tier 1 - ברירות מחדל

| מודל | איכות | מהירות | עלות | שימוש | API Call |
|------|-------|--------|------|-------|---------|
| **google/nano-banana-pro** | מצוינת | ~90s | בינונית | **ברירת מחדל ראשונה** | `create_models_predictions` |
| **black-forest-labs/flux-1.1-pro** | מצוינת | ~6s | ~$0.04 | Fallback 1 - שליטה בסגנון ותאורה | `create_models_predictions` |
| **black-forest-labs/flux-1.1-pro-ultra** | הגבוהה ביותר | ~10s | ~$0.06 | Fallback 2 - איכות מקסימלית | `create_models_predictions` |
| **recraft-ai/recraft-v3** | מצוינת | ~5s | ~$0.04 | **הטוב ביותר לאיורים עם style control** | `create_models_predictions` |

### Tier 2 - מיוחדים

| מודל | שימוש | מתי |
|------|-------|-----|
| **recraft-ai/recraft-v3-svg** | ייצור SVG/וקטור - לוגואים, אייקונים, line art | כשצריך וקטור |
| **black-forest-labs/flux-dev** | בסיס ל-LoRA fine-tunes | כשיש LoRA מותאם |
| **ideogram-ai/ideogram-v3-turbo** | טקסט בתוך תמונות | כשצריך טיפוגרפיה בתמונה |
| **bytedance/seedream-4.5** | תקציב נמוך | כשצריך הרבה וריאציות בזול |

### Tier 3 - אסור

| מודל | סטטוס |
|------|-------|
| **flux-schnell** | **אסור לאיורים.** רק לטסטים מהירים. |

### Recraft V3 - Style Parameters

מודל ייחודי עם שליטה מובנית בסגנון:

```
style options:
- "digital_illustration" - איור דיגיטלי (מומלץ ל-Sol Therapy)
- "vector_illustration" - וקטורי נקי
- "realistic_image" - פוטוריאליסטי
```

**API Call:**
```
mcp__replicate__create_models_predictions:
  model_owner: "recraft-ai"
  model_name: "recraft-v3"
  input: { prompt: "...", style: "digital_illustration", size: "1820x1024" }
```

---

## B. עריכת תמונות (Image Editing)

### Inpainting & Outpainting

| מודל | שימוש | איך |
|------|-------|-----|
| **black-forest-labs/flux-fill-pro** | מילוי/הרחבה של תמונה | image + mask + prompt. לבן = איפה לשנות |
| **stability-ai/stable-diffusion-inpainting** | inpainting בסיסי | image + mask + prompt + strength |

### עריכה טקסטואלית (ללא מסכה)

| מודל | שימוש | איך |
|------|-------|-----|
| **black-forest-labs/flux-kontext-pro** | עריכת תמונה עם טקסט טבעי | image_url + prompt שמתאר את השינוי. ללא מסכה. |
| **black-forest-labs/flux-kontext-max** | גרסה פרימיום - טיפוגרפיה משופרת | כנ"ל, איכות גבוהה יותר |

**דוגמה Kontext:**
```
input: {
  image_url: "https://...",
  prompt: "Change the mountains to be covered in snow, add thick fog between layers"
}
```

---

## C. Style Transfer - העברת סגנון

| מודל | שימוש | מהירות | איך |
|------|-------|--------|-----|
| **fofr/style-transfer** | העברת סגנון ישירה | ~7s | style_image + content_image |
| **black-forest-labs/flux-redux-dev** | IP-Adapter - יצירה בסגנון תמונת רפרנס | ~10s | image (רפרנס) + prompt אופציונלי |

### flux-redux-dev - מפתח קריטי

זה ה-IP-Adapter של Flux. מה שהוא עושה:
- מקבל תמונת רפרנס
- לומד ממנה סגנון, פלטה, מוד, קומפוזיציה
- מייצר תמונות חדשות באותו סגנון

**זה הכלי ליצירת סדרת איורים עקבית.**

```
input: {
  image: "https://[url-of-reference-illustration]",
  prompt: "mountain landscape with mist and layered depth"
}
```

---

## D. ControlNet - שמירת מבנה

| מודל | סוג | שימוש |
|------|------|-------|
| **flux-canny-pro** | קווי מתאר | הפיכת סקיצה לאיור מוגמר |
| **flux-depth-pro** | מפת עומק | שמירת מרחב תלת-ממדי, שינוי סגנון |
| **xlabs-ai/flux-dev-controlnet** | מולטי-סוג | canny + depth + soft edge באחד |

**פרמטר מפתח:** `control_strength` (0.0-1.0) - גבוה = קרוב יותר למבנה המקורי

---

## E. Upscaling - הגדלת רזולוציה

| מודל | שימוש | מתי |
|------|-------|-----|
| **recraft-ai/recraft-creative-upscale** | **מומלץ לאיורים** - מוסיף פרטים אמנותיים תוך הגדלה | לאיורים |
| **batouresearch/magic-image-refiner** | הגדלה + שיפור + inpainting בכלי אחד | לשימוש כללי |
| **nightmareai/real-esrgan** | מהיר וזול, 2x/4x | ל-batch processing |
| **tencentarc/gfpgan** | שחזור פנים | לפני upscaling כשיש פנים |

### Pipeline Upscaling:
```
1. אם יש פנים -> gfpgan קודם
2. לאיורים -> recraft-creative-upscale
3. לכללי -> magic-image-refiner
```

---

## F. אנימציה ווידאו

### Text-to-Video

| מודל | איכות | משך | רזולוציה |
|------|-------|------|----------|
| **google/veo-3-fast** | מצוינת | 5-10s | עד 1080p | ברירת מחדל |
| **google/veo-3.1** | פרימיום | 5-10s | עד 1080p | איכות מקסימלית |

### Image-to-Video (הנפשת תמונה)

| מודל | איכות | שימוש |
|------|-------|-------|
| **Kling v2.6 Pro** | מצוינת | סינמטי, תנועה חלקה |
| **Wan-AI** | טובה מאוד | קוד פתוח, תומך LoRA |

---

## G. טכניקות מתקדמות

### 1. Custom Style Training (LoRA)

**הכלי החזק ביותר לעקביות סגנונית.**

**מודל:** `replicate/fast-flux-trainer`
```
1. אסוף 10-20 תמונות בסגנון הרצוי
2. אימון: ~2 דקות, פחות מ-$2
3. בחר trigger word (למשל "SOLSTYLE")
4. הרץ עם: black-forest-labs/flux-dev-lora + LoRA weights
5. כלול trigger word בprompt
```

**זה הפתרון לבעיית העקביות.**

### 2. Pipeline מומלץ לסול תרפי

```
Option A: Single Illustration
  nano-banana-pro -> [אם צריך עריכה] flux-kontext-pro -> recraft-creative-upscale

Option B: From Reference Style
  flux-redux-dev (+ reference image) -> [עריכה] flux-kontext-pro -> upscale

Option C: From Sketch
  flux-canny-pro (+ סקיצה) -> [עריכה] flux-kontext-pro -> upscale

Option D: Consistent Series (הכי חזק)
  fast-flux-trainer (אימון חד-פעמי) -> flux-dev-lora (כל תמונה) -> upscale

Option E: Animation
  [ייצור תמונה] -> Kling v2.6 Pro (image-to-video) -> export
```

### 3. Fallback Chain

```
1. google/nano-banana-pro (ברירת מחדל)
2. recraft-ai/recraft-v3 (style: digital_illustration)
3. black-forest-labs/flux-1.1-pro-ultra
4. black-forest-labs/flux-1.1-pro
5. Canva generate-design
6. אף פעם flux-schnell לאיורים
```

---

## H. Decision Matrix - מה להשתמש מתי

| אני רוצה... | מודל |
|-------------|------|
| איור מטקסט | nano-banana-pro / recraft-v3 |
| וקטור/SVG | recraft-v3-svg |
| לערוך תמונה קיימת במילים | flux-kontext-pro |
| למלא/להרחיב תמונה | flux-fill-pro |
| להפוך סקיצה לאיור | flux-canny-pro |
| להעביר סגנון מתמונה לתמונה | fofr/style-transfer / flux-redux-dev |
| סדרת איורים עקבית | Train LoRA -> flux-dev-lora |
| להגדיל רזולוציה (איור) | recraft-creative-upscale |
| להגדיל רזולוציה (כללי) | magic-image-refiner |
| להנפיש תמונה | Kling v2.6 Pro |
| לייצר וידאו מטקסט | google/veo-3-fast |
| draft מהיר וזול | flux-schnell (רק לzה!) |

---

## I. אינטגרציה

| מ-Replicate ל... | איך |
|------------------|-----|
| **Canva** | `upload-asset-from-url` עם URL של output |
| **Photoshop** | curl לדיסק, פתיחה |
| **אתר** | curl לassets folder |
| **Figma** | upload דרך דפדפן |

---

## J. Troubleshooting

| בעיה | פתרון |
|------|-------|
| "Invalid API token" | טוקן חדש מ-replicate.com/account/api-tokens |
| תוצאה שטוחה/גנרית | החלף מודל. בדוק taste profile. שפר prompt. |
| טקסט/מספרים בתמונה | הוסף "no text no words no numbers" לprompt |
| צבעים לא נכונים | Flux: השתמש ב-hex. אחרים: תאר במילים. |
| cold start ארוך | nano-banana-pro: ~90s נורמלי. Flux Pro: ~6s. |
| 2 ניסיונות נכשלו | **עצור. החלף מודל או כלי.** |

---

*Last updated: 2026-02-13*
