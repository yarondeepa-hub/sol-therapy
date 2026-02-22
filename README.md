# Sol Therapy Website

אתר אינטרנט לסול תרפיה - חוויות צליל טרנספורמטיביות

## מבנה הפרויקט

```
website-sol-therapy/
├── index.html              # עמוד הבית
├── css/
│   ├── tokens.css          # Design System - משתנים
│   ├── base.css            # סגנונות בסיס ורסט
│   ├── components.css      # רכיבים (כפתורים, כרטיסים, טפסים)
│   ├── sections.css        # סגנונות לפי סקשנים
│   └── responsive.css      # התאמה למובייל וטאבלט
├── js/
│   └── main.js             # אינטראקציות ופונקציונליות
├── assets/
│   ├── images/             # תמונות
│   ├── audio/              # קבצי אודיו
│   └── video/              # קבצי וידאו
└── README.md               # המסמך הזה
```

## Design System

האתר בנוי על בסיס עקרונות העיצוב של Rotem Cohen-Soaye:

### טיפוגרפיה
- **עברית:** Frank Ruhl Libre (כותרות), Heebo (טקסט)
- **אנגלית:** Inter

### צבעים - Zen Gallery Palette
- **כהה (דיו סומי):** #1A1918
- **בהיר (נייר וואשי):** #F5F3EE
- **מבטא (זהב מקדש):** #B8956B
- **ורמיליון (שימוש מינימלי):** #D3381C

### מרחבים - Ma (間)
- מינימום 60% שטח לבן
- נשימה בין אלמנטים

## התקנה והפעלה

1. פתח את `index.html` בדפדפן
2. או השתמש ב-Live Server:
   ```bash
   npx live-server
   ```

## נכסים נדרשים

לפני העלאה לאוויר, יש להוסיף:

### תמונות
- `assets/images/hero-placeholder.jpg` - תמונת רקע להירו
- `assets/images/about-yaron.jpg` - תמונת ירון
- `assets/images/event-1.jpg` עד `event-3.jpg` - תמונות אירועים
- `assets/images/gallery-1.jpg` עד `gallery-6.jpg` - גלריה

### וידאו (אופציונלי)
- `assets/video/hero-bg.mp4` - וידאו רקע להירו

### אודיו
- `assets/audio/sample.mp3` - דוגמת צליל

## פונקציונליות

- [x] ניווט responsive עם תפריט מובייל
- [x] הירו עם אנימציית נשימה
- [x] מודלים (אודות, בטיחות)
- [x] פילטרים לגלריה
- [x] נגן אודיו
- [x] טופס ניוזלטר
- [x] אנימציות כניסה לאלמנטים
- [x] תמיכה ב-RTL מלאה
- [x] נגישות בסיסית

## דגשים טכניים

- **RTL:** האתר בנוי RTL מלא עם `dir="rtl"` ו-`lang="he"`
- **Responsive:** Mobile-first עם breakpoints ב-640px ו-1024px
- **Performance:** CSS ו-JS מינימליים, ללא frameworks
- **Accessibility:** תמיכה בקורא מסך, מצב reduced motion

## שלבים הבאים

1. להוסיף את התמונות והמדיה
2. לחבר את טופס הניוזלטר לשירות (Mailchimp/ConvertKit)
3. לחבר את כרטיסי האירועים למערכת הרשמה
4. להוסיף Google Analytics
5. להעלות ל-hosting (Vercel/Netlify מומלץ)

---

נבנה על בסיס אפיון האתר של סול תרפיה
Design System: Rotem Cohen-Soaye principles
