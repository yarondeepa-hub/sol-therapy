# Gemini Image Generation Skill

> כל האיורים נוצרים דרך Gemini בכרום. זה הכלל. אין חריגים.

---

## How To Generate Images in Gemini (Chrome)

### Step-by-step:

1. **פתח טאב חדש בכרום** (`tabs_create_mcp`)
2. **נווט ל-** `https://gemini.google.com`
3. **לחץ על כפתור "Create image"** - לא לכתוב פרומפט טקסטואלי בתיבת הטקסט הרגילה!
4. **כתוב את הפרומפט** בתיבת הטקסט שנפתחת אחרי "Create image"
5. **חכה ליצירת התמונות** - Gemini ייצר 2-4 תמונות
6. **צלם מסך** (`screenshot`) כדי לראות את התוצאות
7. **בחר את התמונה הטובה** - לחץ עליה
8. **הורד** - לחץ על כפתור ההורדה (שלוש נקודות או אייקון הורדה)
9. **שמור לתיקיית הפרויקט**

### Critical Rules:

- **תמיד לחץ "Create image" קודם** - לא לכתוב "generate an image" בתיבת הטקסט הרגילה
- **המודל נבחר אוטומטית** - אין צורך לבחור "Nano Banana Pro" ידנית, זה מה שג'מיני משתמש ליצירת תמונות
- **אין צורך לשנות מודל בדרופדאון** - "Create image" מפעיל את המודל הנכון
- **לא להשתמש ב-Replicate/Flux** - רק Gemini בכרום
- **לא להשתמש ב-Gemini MCP** ליצירת איורים - רק דרך הכרום

### Prompt Best Practices:

- פרומפטים באנגלית עובדים טוב יותר
- תיאור ספציפי של סגנון (sumi-e, ink wash, watercolor)
- ציין aspect ratio (16:9, 3:2, 1:1)
- "No text" בסוף - למנוע טקסט בתמונה
- תיאור של מה שרוצים, לא מה שלא רוצים

### After Generation:

- הצג לירון לפני שממשיכים
- אם לא טוב - נסה פרומפט מתוקן
- עצור אחרי 2 ניסיונות כושלים - שנה גישה
- Gatekeeper משווה ל-benchmark לפני אישור סופי

---

## Model Info

- **Model:** Gemini uses its native image generation (Imagen/Nano Banana Pro) when "Create image" is clicked
- **Platform:** gemini.google.com in Chrome browser
- **Access:** Via Chrome MCP browser automation
- **Account:** Yaron's Google account (Plus subscription)
