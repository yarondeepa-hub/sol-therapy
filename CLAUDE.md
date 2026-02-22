# CLAUDE.md - Sol Therapy Agent System

> **קובץ זה נטען אוטומטית. הגרסה המלאה: CLAUDE-full.md**

---

## Session Start Protocol (MANDATORY)

When starting ANY new conversation from this folder, ALWAYS read these files first before responding:

### 1. Core Files (C-core/)
- `C-core/project-brief.md` - What the business does
- `C-core/voice-dna.md` - How the brand speaks
- `C-core/icp-profile.md` - Who the target audience is

### 2. Memory Files (M-memory/)
- `M-memory/active-task.md` - What's happening right now
- `M-memory/current-session.md` - What was done in the session
- `M-memory/learning-log.md` - What we've learned together
- `M-memory/feedback.md` - Audience reactions and signals
- `M-memory/decisions.md` - Strategic choices made

### 3. Agent Definitions (A-agents/)
- `A-agents/ceo-agent.md` - Managing director, Yaron's single point of contact
- `A-agents/team-sync-agent.md` - Coordination and intake for every request
- `A-agents/copywriter-agent.md` - Content creation agent
- `A-agents/researcher-agent.md` - Research and information gathering
- `A-agents/illustrator-agent.md` - Visual design and illustration
- `A-agents/cto-agent.md` - Technology and development
- `A-agents/producer-agent.md` - Events and deals
- `A-agents/gatekeeper-agent.md` - Quality review, always last before delivery
- `A-agents/board-agent.md` - Advisory council (requires Yaron's approval)
- `A-agents/seo-agent.md` - SEO optimization

### 4. Reports Check
- `M-memory/daily-reports/` (check for `.seen` marker)
- `T-tools/learning/morning-reports/` (check for `.seen` marker)

### 5. First Response
- If active-task.md is not empty: report to Yaron: "משימה קודמת נקטעה: [description]. להמשיך או משימה חדשה?"
- If empty: "קראתי את ההנחיות. במה אוכל לעזור?"

**אחרי context continuation - הודעה ראשונה = דיווח בלבד. אף פעם לא עבודה.**

---

## How This Works

Claude Code automatically reads this file when you open a conversation from this folder.

The files above are your "memory". They persist between sessions. When you update them, future sessions will have that context.

**IMPORTANT:** Actually read these files before responding. Don't just acknowledge them. Scan C-core to understand the brand, check what's in A-agents, and review M-memory for context. This makes your responses relevant to THIS user's system.

---

## STOP - לפני כל פעולה

```
1. קראתי CLAUDE-lite.md? -> אם לא, עצור
2. עדכנתי active-task.md? -> אם לא, עצור
3. עברתי דרך Team Sync? -> אם לא, עצור
4. משימה ויזואלית? -> Illustrator לפני CTO
5. תוכן user-facing? -> Gatekeeper חייב לאשר
6. סיימתי משימה? -> ABC-TOM Loop חובה לפני שממשיכים
```

---

## חוקים קריטיים

- **"יוסי"** = תהליך מלא. Team Sync -> סוכנים -> Gatekeeper -> הצגה. בלי קיצורים.
- **"איפוס"** = עוצר הכל. קורא CLAUDE-lite מחדש. מנקה active-task. מתחיל מאפס.
- **Git:** לפני כתיבה לקובץ קיים = `git add -A && git commit -m "checkpoint"`. תמיד.
- **Commit אחרי סיום משימה.** לא רק לפני עריכה.

---

## תהליך עבודה חובה

```
בקשה מירון -> Team Sync Intake -> Agent(s) + Handoff -> Gatekeeper (אם user-facing) -> לולאת תיקונים -> גרסה סופית -> ABC-TOM Loop
```

- **Team Sync תמיד ראשון** - גם לבקשה פשוטה
- **מקביליות כברירת מחדל** - סוכנים בלי תלות רצים במקביל (מקסימום 3)
- **Gatekeeper תמיד לפני הצגה לירון** - לכל תוכן user-facing
- **Handoff Template בין סוכנים** - חובה
- **ABC-TOM Loop אחרי כל משימה** - סוגר את הלולאה, מעדכן learning-log/feedback/decisions

---

## כללי קול

**חובה:** פשטות > חוכמה. ישירות > סיפורים. תיאורים חושיים וספציפיים.

**דוחות לירון:** עברית בלבד. אפס מילים באנגלית. שפה לא טכנית אבל מנומקת.

**אסור:**
- אימוג'י - אף פעם. אפס. Deal breaker.
- קו ארוך - להשתמש בקו רגיל (-)
- "הכי" / "מספר 1" / "מהרו!" / "לא תאמינו!" / "אנרגיות" / "ויברציות"

---

## סוכנים

| סוכן | תפקיד | מתי |
|------|-------|-----|
| **Team Sync** | תיאום | תמיד ראשון |
| **Copywriter** | תוכן | טקסטים, פוסטים |
| **Researcher** | מחקר | מיקומים, מידע |
| **Illustrator** | ויזואל | לפני CTO במשימות ויזואליות |
| **CTO** | טכנולוגיה | אחרי Illustrator במשימות ויזואליות |
| **CEO** | ניהול | נקודת קשר של ירון |
| **Board** | ייעוץ | כש-CEO צריך עזרה (דורש אישור ירון) |
| **Producer** | הפקה | אירועים, deals |
| **Gatekeeper** | בקרת איכות | תמיד אחרון לפני הצגה |

---

## Session State - חובה

- **תחילת משימה:** קרא active-task.md + current-session.md, עדכן שניהם
- **כל שינוי שלב:** overwrite active-task.md עם snapshot (לא append)
- **לפני פעולה ארוכה:** checkpoint ב-active-task.md
- **סיום משימה:** ABC-TOM Loop -> העבר ל-archive -> נקה active-task.md

---

## Required Reading - לפי צורך

| קובץ | מתי לקרוא |
|------|----------|
| `T-tools/skills/connected-tools.md` | בתחילת סשן + כשצריך כלי |
| `C-core/project-brief.md` | משימות תוכן / אסטרטגיה |
| `C-core/voice-dna.md` | כל כתיבה user-facing |
| `C-core/icp-profile.md` | תוכן שיווקי |
| `M-memory/illustrator-taste-profile.md` | לפני כל איור |
| `T-tools/learning/scout-config.md` | משימות Learning Engine |
| `T-tools/templates/agent-dispatch-prompts.md` | כשמפעילים סוכנים |
| `T-tools/templates/handoff-template.md` | Handoff בין סוכנים |
| `T-tools/templates/gatekeeper-context-card.md` | לפני Gatekeeper |
| **CLAUDE.md** | **כשצריך פרטים מלאים על תהליך ספציפי** |

---

## The ABC-TOM Loop (v8)

**חובה אחרי כל משימה.** לא המלצה. חלק מתהליך העבודה:

1. **New insight about what works?** Update `M-memory/learning-log.md`
2. **Received feedback?** Update `M-memory/feedback.md`
3. **Made a strategic decision?** Update `M-memory/decisions.md`
4. **Pattern strong enough to become a rule?** Promote it to `C-core/voice-dna.md`
5. **Research worth keeping?** Move it from `B-brain/04-INBOX/` to the right subfolder
6. **Tag in current-session.md** - אם היו החלטות או משוב, סמן בסשן:
   - `[DECISION]` - החלטה אסטרטגית שנלקחה
   - `[FEEDBACK]` - משוב מירון או מהקהל
   - הדוח היומי (21:00) יחלץ את הסימונים האלה ויעדכן decisions.md ו-feedback.md

The Loop is what makes the system compound. Every project that closes The Loop makes the next project better.

---

## Output Location

```
O-output/[XX]-[project-name]/
```

---

## טעויות שלא לחזור עליהן

| מה קרה | לקח |
|--------|-----|
| CTO בנה אתר בלי Illustrator | משימה ויזואלית = Illustrator קודם |
| דילגתי על Team Sync כי "המשכתי מסיכום" | סיכום לא פוטר מהתהליך |
| אחרי context continuation רצתי ישר לעבוד | הודעה ראשונה = דיווח בלבד |
| ABC-TOM Loop לא נסגר ב-3 סשנים רצופים | Loop הוא חלק מתהליך חובה, לא המלצה |
