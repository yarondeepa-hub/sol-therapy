# Decisions Log

Track key decisions you've made about your brand, content, and strategy — and why.

---

## Why Track Decisions

> "A decision without context is just a rule. A decision with context is wisdom."

When you or your agents revisit old decisions, you need to know:
- What you decided
- Why you decided it
- What you considered
- Whether it's still valid

This prevents:
- Re-debating settled issues
- Forgetting why you do things a certain way
- Inconsistent choices over time

---

## How to Use This File

**When making decisions:** Log them here with rationale
**When questioning past choices:** Check here first
**Quarterly:** Review if decisions still make sense

---

## Decision Categories

### Brand Decisions
Choices about identity, positioning, voice.

### Content Decisions
Choices about what you create and how.

### Process Decisions
Choices about how you work.

### Strategic Decisions
Choices about direction and priorities.

---

## Decision Log

### Brand Decisions

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| 2026-02-20 | אפס אימוג'י - בשום מקום | Deal breaker של ירון. כלל מוחלט | Active |
| 2026-02-21 | Partners label באנגלית בלבד | ירון החזיר ידנית לאנגלית אחרי שתורגם. לא לתרגם שוב | Active |
| 2026-02-21 | ללא חותם vermilion אדום | ירון ביקש להסיר - לא מתאים לשפה הוויזואלית | Active |
| 2026-02-22 | ללא כפתור CTA צף | ירון ביקש להסיר כפתור הרשמה צף. לא להוסיף אלמנטי UI שלא ביקש | Active |
| 2026-02-22 | סמן גלילה = אייקון, לא data viz | ירון ציפה לחץ/שברון, לא progress bar. "סימן" = אייקון | Active |

---

### Content Decisions

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| 2026-02-20 | WebP + JPG fallback ב-picture tags | תמיכה בדפדפנים ישנים + חיסכון משקל | Active |
| 2026-02-20 | WOFF2 כפורמט פונט ראשי | חיסכון 44% מ-OTF/TTF, עם fallback | Active |
| 2026-02-21 | עמוד אינדקס בלוג (blog.html) | נקודת כניסה מרכזית לכל המאמרים | Active |
| 2026-02-21 | חבילת SEO מלאה (robots, sitemap, OG, JSON-LD) | תשתית לגילוי אורגני | Active |
| 2026-02-21 | Mailchimp לניוזלטר | פלטפורמה חינמית עד 500 רשומות, אינטגרציה פשוטה | Active |
| 2026-02-21 | GA4 לאנליטיקס (G-C5VRCQ9M6V) | מעקב תנועה ואירועים | Active |
| 2026-02-22 | דחיסת וידאו רקע מ-16MB ל-1.9MB | מובייל על סלולר לא יכול לטעון 16MB | Active |
| 2026-02-22 | preload לתמונת Hero בלבד | הנכס הראשון שהמשתמש רואה - חייב להיטען מהר | Active |

---

### Process Decisions

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| 2026-02-21 | SessionStart hook cleans zombie sessions (>2hrs idle) | 3 zombie sessions caused 598MB waste + text bleeding. Hook preserves active parallel work. | Active |
| 2026-02-21 | Max 2-3 concurrent Claude Code chats | 16GB RAM + 5 MCP servers per session = swap above 3 chats. Hard limit. | Active |
| 2026-02-21 | Only one chat uses Chrome MCP at a time | Chrome native host is singleton - multiple sessions = text cross-contamination | Active |
| 2026-02-21 | Daily review monitors process count and swap | Early warning system for resource bloat | Active |

---

### Strategic Decisions

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| 2026-02-21 | דומיין מותאם sol-therapy.com | מקצועיות, SEO, מיתוג. GitHub Pages + GoDaddy | Active |
| 2026-02-21 | Learning Engine - סיור בוקר אוטומטי | גילוי כלים וטכניקות חדשות בלי עבודה ידנית | Active |
| 2026-02-21 | 4 שיפורי תהליך: Fast Track, Proactive Reset, Decision Extraction, Style Token Self-Check | ירון אישר אחרי התייעצות עם מודל חיצוני | Active |
| 2026-02-22 | iCloud duplicates לתיקייה נפרדת, לא מחיקה | ירון העדיף לשמור גיבוי: "תעביר לתקיית מחסן" | Active |

---

## Decision Template

When logging a significant decision:

```markdown
## [Date] - [Decision Title]

**Decision:** [Clear statement of what was decided]

**Context:** [What prompted this decision]

**Options Considered:**
1. [Option A] — [Pros/cons]
2. [Option B] — [Pros/cons]
3. [Chosen option] — [Why this one]

**Rationale:** [The reasoning behind the choice]

**Implications:**
- [What this means for X]
- [What this means for Y]

**Review Date:** [When to revisit this decision]

**Status:** Active / Revisit / Deprecated
```

---

## Quarterly Review Template

```markdown
## Q[X] Decision Review

### Decisions Still Valid
- [Decision] — Still working because [reason]

### Decisions to Revisit
- [Decision] — Questioning because [reason]

### Decisions to Deprecate
- [Decision] — No longer relevant because [reason]

### New Decisions Needed
- [Topic] — Need to decide [what]
```

---

*Decisions age. Context helps them age well.*

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
