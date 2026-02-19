# Blog Post Workflow

> תהליך עבודה מלא לכתיבת כתבת בלוג מסוג מאמר-מגזין (Mode C).
> מבוסס על הלקחים מכתבת "האם מדיטציות סאונד באמת עובדות?" (02/2026).

---

## סקירת התהליך

```
[ירון] נותן נושא + כיוון
          |
[Team Sync] Intake - מזהה: blog = Researcher + Copywriter + Gatekeeper
          |
    ------+------
    |            |
[Researcher]  [Copywriter קורא voice-dna]
    |            |
    ------+------
          |
[Copywriter] כותב טיוטה v1 (משלב מחקר + קול)
          |
[Gatekeeper] fact-check + voice review
          |
[לולאת תיקונים] עד 3 סיבובים
          |
[גרסה סופית] -> מוצגת לירון
          |
[ירון] inline notes בסוגריים מרובעים
          |
[תיקון ישיר] - ללא סוכנים, עריכת קובץ
          |
[הצגה מעודכנת] -> ירון מאשר
```

---

## Phase 0: Team Sync Intake

### Checklist

```
[ ] סוג המשימה: כתיבת בלוג (Mode C - אנליטי-עיתונאי)
[ ] User-facing: כן -> Gatekeeper חובה
[ ] ויזואלי: לא (טקסט בלבד)
[ ] סוכנים: Researcher (מקביל) + Copywriter (אחרי מחקר) + Gatekeeper (אחרון)
[ ] יצירת תיקיית output
```

### יצירת תיקייה

```
O-output/[XX]-blog-[topic]/
  |- research-data.md          # מחקר
  |- handoff-researcher.md     # Handoff מ-Researcher
  |- gatekeeper-context.md     # Context Card
  |- gatekeeper-review.md      # סיכום בדיקה
  |- final-blog-post.md        # גרסה סופית
```

---

## Phase 1: Research (Researcher Agent)

### מה לחקור

כתבת בלוג של Sol Therapy דורשת שני צירי מחקר שרצים במקביל:

**ציר מדעי:**
- מחקרים אקדמיים (Nature, PubMed, Google Scholar)
- שמות חוקרים + מוסדות
- נתונים מספריים ספציפיים (אחוזים, שנים, גדלי מדגם)
- מחקרים ישראליים רלוונטיים

**ציר תרבותי/רוחני:**
- מקורות ראשוניים (טקסטים מקוריים, לא פרשנויות)
- פרקטיקות מתרבויות שונות
- דמויות היסטוריות ספציפיות
- קשרים בין-תרבותיים

### פורמט Output

```markdown
# Research: [Topic]

## Executive Summary
[3-5 משפטים]

## Key Studies
| מחקר | שנה | ממצא מרכזי | מקור |
|------|-----|-----------|------|

## Israeli Research
| חוקר | מוסד | תחום | ממצא |
|------|------|------|------|

## Cultural/Historical Sources
| מקור | תקופה | תרבות | רלוונטיות |
|------|--------|-------|-----------|

## Facts Requiring Verification
[רשימת טענות שדורשות fact-check]

## Source List (Full Citations)
[ציטוטים מלאים בפורמט אקדמי]
```

### Researcher Dispatch Prompt (Copy-Paste Ready)

```
You are the Researcher agent for Sol Therapy.

## First - Read These Files:
1. Read: A-agents/researcher-agent.md
2. Read: C-core/project-brief.md
3. Read: T-tools/workflows/blog-post-workflow.md

## Research Task:
Deep research for a Mode C blog post about: [TOPIC]

## What to Research:
1. SCIENTIFIC AXIS: Academic studies from peer-reviewed journals. Need specific numbers, dates, researcher names, institutions. Prioritize recent studies (2020+) but include foundational research.
2. CULTURAL AXIS: Primary historical/spiritual sources. Cross-cultural practices. Specific figures, texts, traditions.
3. ISRAELI ANGLE: Israeli researchers working in this field. Their institutions and recent publications.

## Research Mode: Deep (WebSearch + WebFetch)

## Quality Requirements:
- Every claim must have a verifiable source
- Prefer primary sources over summaries
- Include full citations for every study
- Flag anything that needs fact-checking

## Output Format:
Follow the Research Output format from blog-post-workflow.md

## Handoff Output:
AGENT: Researcher
STATUS: complete
MERGE_KEY: blog_research
DEPENDENCIES_SATISFIED: Copywriter can start drafting
OUTPUT: [research report]
SOURCES: [full citation list]
```

---

## Phase 2: Writing (Copywriter Agent)

### Blog Voice - Mode C

זה לא פוסט רגיל. זו כתבת מגזין. הכללים:

| מאפיין | הנחיה |
|--------|-------|
| **טון** | אנליטי-עיתונאי, מגזין. לא אישי ("אני"), לא מכירתי |
| **מבנה** | 5-6 סקשנים עם כותרות. פתיחה חזקה עם ממצא מדעי מפתיע |
| **איזון** | 50/50 מדע ורוחניות. לא מעדיפים צד |
| **אורך** | 1,200-1,800 מילים |
| **סיום** | פתוח - שאלה, לא תשובה. בלי CTA |
| **מקורות** | רשימת מקורות מלאה בתחתית |

### כללי כתיבה קריטיים

**חובה:**
- משפטים ארוכים שבונים שכבות, לסירוגין עם משפטים קצרים
- תיאורים חושיים וספציפיים
- רפרנסים תמיד עם שמות, שנים, מספרים
- מתח בין מדע לרוחניות - לא פותרים אותו
- הקשר תרבותי רחב (לפחות 3 תרבויות)
- חוקרים ישראליים כצד מקומי

**אסור:**
- אימוג'י - אף פעם. אפס.
- מקף ארוך - רק מקף רגיל (-)
- "הכי" / "מספר 1" / "הטוב ביותר"
- "אנרגיות" / "ויברציות"
- שפה מכירתית או הבטחות
- CTA או הפניה לאירועים
- "אני" / "אנחנו" (כתיבה עיתונאית, לא אישית)

### מילים מאוצר המילים של ירון

מהפנט, טרנספורמטיבי, אימרסיבי, תדרים, צלילה, מרקמים, נופי סאונד, רב-שכבתי, אטמוספרי, מסע פנימי, הרחבת תודעה

### מבנה מומלץ

```
1. פתיחה (ממצא מדעי מפתיע - hook)
2. מה שהמדע מודד (מחקרים, נתונים)
3. מה שהמדע עדיין לא מודד (הפער)
4. ציר תרבותי/רוחני (טקסטים, פרקטיקות, היסטוריה)
5. נקודת המפגש (איפה מדע ורוחניות מצטלבים)
6. סיום פתוח (שאלה, לא תשובה)
+ מקורות
```

### Copywriter Dispatch Prompt (Copy-Paste Ready)

```
You are the Copywriter agent for Sol Therapy.

## First - Read These Files:
1. Read: A-agents/copywriter-agent.md
2. Read: C-core/voice-dna.md (CRITICAL - especially Mode C section)
3. Read: C-core/icp-profile.md
4. Read: C-core/project-brief.md
5. Read: T-tools/workflows/blog-post-workflow.md

## Voice Rules - CRITICAL:
- Mode C: Magazine-style article. NOT personal essay. NOT sales.
- NO emoji - ever. Zero. Deal breaker.
- NO em dash. Regular hyphen only.
- NO "הכי" / "מספר 1" / "הטוב ביותר"
- NO "אנרגיות" / "ויברציות"
- NO CTA or references to Sol Therapy events
- YES: Long flowing sentences that build images, alternating with short ones
- YES: Yaron's vocabulary - מהפנט, טרנספורמטיבי, תדרים, צלילה
- YES: Specific references with names, dates, numbers
- YES: Open ending - question, not answer

## Task:
Write a Mode C blog post about: [TOPIC]
Length: 1,200-1,800 words
Language: Hebrew with English technical terms

## Research Data:
[PASTE RESEARCHER OUTPUT HERE]

## Structure:
Follow the recommended structure from blog-post-workflow.md:
1. Opening (surprising scientific finding)
2. What science measures
3. What science doesn't measure yet (the gap)
4. Cultural/spiritual axis
5. Where they meet
6. Open ending
+ Sources list

## Handoff Output:
AGENT: Copywriter
STATUS: complete
MERGE_KEY: blog_text
DEPENDENCIES_SATISFIED: Gatekeeper can review
OUTPUT: [full blog text]
NOTES: [writing decisions, what I prioritized]
```

---

## Phase 3: Gatekeeper Review

### Blog-Specific Checks

מעבר לבדיקות הרגילות, ב-blog יש שכבה נוספת:

**Fact-Check Protocol:**
1. כל טענה עובדתית -> אמת מול WebSearch
2. שמות חוקרים -> בדיקה שקיימים ועובדים במוסד הנכון
3. שנות פרסום -> בדיקה מול מקור
4. נתונים מספריים -> בדיקה מול מחקר מקורי
5. טענות היסטוריות -> בדיקת דיוק כרונולוגי

**Voice Check:**
1. מוד C - אנליטי, לא אישי?
2. אין אימוג'י?
3. אין מקף ארוך?
4. איזון 50/50 מדע/רוחניות?
5. סיום פתוח?
6. אוצר מילים של ירון?
7. אין שפה מכירתית?

### Gatekeeper Context Card (Template)

```markdown
## Gatekeeper Context Card

### Original Request
כתבת בלוג: [TOPIC]

### Type
Mode C blog post (magazine-style)

### Agents Who Worked
1. Researcher - [brief summary]
2. Copywriter - [brief summary]

### What to Check
1. FACT-CHECK: כל טענה עובדתית (שמות, שנים, מוסדות, נתונים)
2. VOICE: Mode C compliance (see blog-post-workflow.md)
3. STRUCTURE: 5-6 sections, sources list
4. BALANCE: 50/50 science/spirituality
5. LENGTH: 1,200-1,800 words

### Content to Review
[FULL BLOG TEXT]
```

### Gatekeeper Dispatch Prompt (Copy-Paste Ready)

```
You are the Gatekeeper agent for Sol Therapy.

## First - Read These Files:
1. Read: A-agents/gatekeeper-agent.md
2. Read: C-core/voice-dna.md (especially Mode C)
3. Read: T-tools/workflows/blog-post-workflow.md

## Critical Checks:
- NO emoji - instant fail
- NO em dash - use regular hyphen
- NO sales language or wellness cliches
- Mode C voice - magazine, not personal
- FACT-CHECK every claim via WebSearch

## Review Task:
Review this Mode C blog post for:
1. Factual accuracy (every claim, name, date, number)
2. Voice alignment (Mode C - analytical, magazine-style)
3. Structure (5-6 sections, open ending, sources)
4. Balance (50/50 science vs spirituality)
5. Length (1,200-1,800 words)

## Gatekeeper Context Card:
[PASTE CONTEXT CARD]

## Content to Review:
[FULL BLOG TEXT]

## Output Format:
AGENT: Gatekeeper
STATUS: [APPROVED / REVISIONS_NEEDED]
REVIEW_ROUND: [1/2/3]

FACT_CHECK_RESULTS:
| Claim | Verified? | Issue | Fix |
|-------|----------|-------|-----|

VOICE_CHECK:
[pass/fail per criterion]

WHAT_WORKS:
[list]

WHAT_NEEDS_FIXING:
[specific issues with specific fixes]

VERDICT:
[APPROVED / REVISIONS_NEEDED with details]
```

---

## Phase 4: Yaron's Inline Notes

### איך זה עובד

אחרי שהגרסה הסופית מוצגת לירון:

1. ירון מחזיר את הטקסט עם הערות בסוגריים מרובעים: `[הערה]`
2. כל הערה היא הנחיה ישירה - ביצוע מיידי, בלי סוכנים
3. סוגי הערות:
   - `[עוד הסבר על X]` = הוסף תוכן
   - `[למחוק: ...]` = מחק את הקטע
   - `[מילה אחרת במקום מילה]` = החלף
   - `[מעולה]` = אל תשנה
4. עריכה ישירה על הקובץ (Edit tool)
5. הצגה מחדש לירון בצ'אט

### חוק: תמיד להציג בצ'אט

> "תמיד תציג לי פה טקסט אל תשלח אותי לקבצים"

כל גרסה מוצגת inline בצ'אט, לא רק קישור לקובץ.

---

## Parallel Execution Map

```
Round 1 (parallel):
  Task 1: Researcher - deep research on topic
  [Copywriter reads voice-dna while waiting]

Round 2 (sequential - after research):
  Task 2: Copywriter - write blog with research data

Round 3 (sequential):
  Task 3: Gatekeeper - fact-check + voice review

Round 4 (if needed - correction loop):
  Task 4: Copywriter - fixes
  Task 5: Gatekeeper - re-review

Round 5 (after Gatekeeper APPROVED):
  Present to Yaron in chat
```

---

## Lessons Learned (02/2026)

### Copywriter

| לקח | הסבר |
|-----|------|
| Over-revision | כש-Gatekeeper מבקש 3 תיקונים, הכותב שינה גם את הכותרת והמבנה. צריך הנחיה מפורשת: "תקן רק X, Y, Z - אל תשנה כלום אחר" |
| Mode C = לא אישי | הטיוטה הראשונה נכתבה ב"אני". מוד C הוא עיתונאי - גוף שלישי |
| Short queries > long briefs | הנחיות קצרות וממוקדות עובדות טוב יותר מ-briefs ארוכים |

### Gatekeeper

| לקח | הסבר |
|-----|------|
| Fact-check הכרחי | גילינו 3 שגיאות עובדתיות: יאמבליכוס לא היה תלמיד של פיתגורס (800 שנה הפרש), תדרי דידג'רידו לא "בטווח התטא", PET ו-fMRI עושים דברים שונים |
| כרונולוגיה | טענות היסטוריות דורשות בדיקת תאריכים מדויקת |
| הקשר מדעי | כש-Copywriter כותב "X גורם ל-Y", צריך לוודא שהמחקר באמת אומר את זה ולא רק "X קשור ל-Y" |

### Process

| לקח | הסבר |
|-----|------|
| Inline notes = עריכה ישירה | כשירון שולח הערות בסוגריים, אין צורך בסוכנים. Edit ישיר על הקובץ |
| הצגה בצ'אט | ירון רוצה לראות את הטקסט בצ'אט, לא להיכנס לקבצים |
| v5.1 pattern | גרסה ראשית (v5) -> Gatekeeper -> ירון -> inline fixes (v5.1) -> ירון מאשר |

---

## Quick Reference - Blog Types

| סוג | דוגמה | מחקר | טון |
|-----|-------|------|-----|
| Science + Spirituality | "האם מדיטציות סאונד עובדות?" | מחקרים + טקסטים עתיקים | 50/50 אנליטי + תרבותי |
| Artist Profile | "הסאונד של [אמן]" | ביוגרפיה + הקלטות | אוצרותי + פואטי |
| Cultural Analysis | "למה סאונד בלילה?" | תרבויות + מדע שינה | Mode C + E |
| Event Reflection | "מה קרה ב-[אירוע]" | תיעוד + חוויות | Mode D + C |

---

## Checklist - Copy for Every New Blog

```
## Blog: [TOPIC]

### Phase 0 - Setup
- [ ] תיקיית output נוצרה
- [ ] current-session.md עודכן
- [ ] סוג הבלוג מזוהה

### Phase 1 - Research
- [ ] Researcher dispatched
- [ ] Scientific sources collected
- [ ] Cultural sources collected
- [ ] Israeli angle found
- [ ] Full citations prepared
- [ ] Research saved to file

### Phase 2 - Writing
- [ ] Copywriter read voice-dna Mode C
- [ ] Copywriter received research data
- [ ] Draft v1 written
- [ ] 1,200-1,800 words
- [ ] Sources list included

### Phase 3 - Review
- [ ] Gatekeeper Context Card prepared
- [ ] Fact-check completed
- [ ] Voice check passed
- [ ] Corrections applied (if needed)
- [ ] APPROVED by Gatekeeper

### Phase 4 - Present
- [ ] Full text displayed in chat
- [ ] Yaron's inline notes applied
- [ ] Updated version displayed in chat
- [ ] Final version saved to file
- [ ] current-session.md updated
```

---

*Based on: Blog #1 - "האם מדיטציות סאונד באמת עובדות?" (v5.1, February 2026)*
*Workflow created: 2026-02-15*
