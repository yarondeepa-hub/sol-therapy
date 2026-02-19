# CTO / Illustrator Skill: Photoshop Automation
## "עיבוד תמונות, קומפוזיציה וbatch processing דרך סקריפטים"

---

## מטרת הסקיל

שימוש ב-Photoshop המותקן על המחשב של ירון לעיבוד תמונות מקצועי - post-processing של תמונות מ-Replicate, יצירת קומפוזיציות, batch processing, ותיקון צבעים.

---

## חיבור טכני

**סטטוס:** זמין - מותקן על המחשב.

**גרסאות:**
- `/Applications/Adobe Photoshop 2025/Adobe Photoshop 2025.app`
- `/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app`

**רישיון:** מנוי מלא (חשבון Adobe של ירון)

**אין MCP** - כל האינטראקציה דרך command line, AppleScript או JSX scripts.

---

## שיטות הפעלה

### 1. AppleScript (מומלץ)

```bash
osascript -e 'tell application "Adobe Photoshop 2026" to do javascript "
  // JavaScript code here
  var doc = app.activeDocument;
  doc.saveAs(new File(\"/path/to/output.png\"));
"'
```

### 2. JSX Script File

```bash
# כתיבת סקריפט לקובץ
cat > /tmp/ps-script.jsx << 'EOF'
var doc = app.open(new File("/path/to/input.png"));
// ... operations ...
doc.saveAs(new File("/path/to/output.png"));
doc.close(SaveOptions.DONOTSAVECHANGES);
EOF

# הרצה
osascript -e 'tell application "Adobe Photoshop 2026" to do javascript of file "/tmp/ps-script.jsx"'
```

### 3. פתיחת קובץ פשוטה

```bash
open -a "Adobe Photoshop 2026" /path/to/image.png
```

---

## פעולות נפוצות - JSX Recipes

### פתיחה ושמירה

```javascript
// פתיחת קובץ
var doc = app.open(new File("/path/to/input.png"));

// שמירה כ-PNG
var pngOpts = new PNGSaveOptions();
pngOpts.compression = 6;
doc.saveAs(new File("/path/to/output.png"), pngOpts);

// שמירה כ-JPG
var jpgOpts = new JPEGSaveOptions();
jpgOpts.quality = 10; // 1-12
doc.saveAs(new File("/path/to/output.jpg"), jpgOpts);
```

### שינוי גודל

```javascript
var doc = app.activeDocument;
doc.resizeImage(UnitValue(1920, "px"), null, null, ResampleMethod.BICUBIC);
```

### Color Overlay (Sol Therapy palette)

```javascript
// Apply color overlay to match Sol Therapy palette
var doc = app.activeDocument;
var layer = doc.activeLayer;

// Create color fill layer
var colorRef = new SolidColor();
colorRef.hex = "F2EAD3"; // Washi Cream
var fillLayer = doc.artLayers.add();
doc.selection.selectAll();
doc.selection.fill(colorRef);
fillLayer.blendMode = BlendMode.MULTIPLY;
fillLayer.opacity = 20;
```

### Batch Processing Template

```javascript
var inputFolder = new Folder("/path/to/input/");
var outputFolder = new Folder("/path/to/output/");
var files = inputFolder.getFiles("*.png");

for (var i = 0; i < files.length; i++) {
    var doc = app.open(files[i]);

    // Process each file
    doc.resizeImage(UnitValue(1920, "px"), null, null, ResampleMethod.BICUBIC);

    // Save
    var pngOpts = new PNGSaveOptions();
    doc.saveAs(new File(outputFolder + "/" + files[i].name), pngOpts);
    doc.close(SaveOptions.DONOTSAVECHANGES);
}
```

---

## שימושים לסול תרפי

| משימה | מה Photoshop עושה |
|-------|-------------------|
| **Post-process Replicate output** | תיקון צבעים, חידוד, crop |
| **Washi texture overlay** | הוספת שכבת טקסטורת נייר |
| **Color grading** | התאמה לפלטת סול תרפי |
| **Composite images** | שילוב כמה תמונות לתמונה אחת |
| **Batch resize** | הכנת תמונות במידות שונות לאתר |
| **Export for web** | אופטימיזציה לגודל/איכות |

---

## תהליך עבודה

### Post-Processing Pipeline

```
1. Replicate מייצר תמונה גולמית
2. Photoshop פותח את התמונה
3. תיקון צבעים (match Sol Therapy palette)
4. הוספת Washi texture overlay אם צריך
5. Crop/resize לגודל הנדרש
6. שמירה בפורמט המתאים (PNG for web, JPG for social)
7. Asset מוכן לשימוש בCanva/אתר
```

### Batch Asset Preparation

```
1. כל ה-assets מ-Replicate נשמרים בתיקייה
2. Photoshop script רץ על כולם
3. Resize, color correct, export
4. Output folder מוכן לימפלמנטציה
```

---

## כללים

1. **Photoshop צריך לרוץ** - לוודא שהאפליקציה פתוחה לפני הרצת סקריפטים
2. **לשמור originals** - תמיד לעבוד על copy, לא על המקור
3. **paths מוחלטים** - JSX דורש paths מלאים, לא relative
4. **אין UI interaction** - הכל דרך סקריפטים, לא ללחוץ על כפתורים
5. **קבצים זמניים ב-/tmp** - סקריפטים נשמרים ב-/tmp, output ב-O-output/

---

## Troubleshooting

| בעיה | פתרון |
|------|-------|
| "Photoshop is not running" | `open -a "Adobe Photoshop 2026"` ולחכות שיטען |
| Script timeout | Photoshop scripts ארוכים - להגדיר timeout גבוה |
| File not found | לוודא paths מוחלטים עם / ולא \ |
| Permission denied | לבדוק הרשאות על תיקיית ה-output |
| Color space issues | לוודא sRGB לweb, Adobe RGB לprint |

---

*Last updated: 2026-02-12*

---

> **c Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
