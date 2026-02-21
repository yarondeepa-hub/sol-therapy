# Morning Scout Skill

> **הרצה ידנית של סייר הבוקר - כשהאוטומציה לא רצה או כשרוצים סיור מיידי.**
> Slash command: `/morning-scout`

---

## When to Use

- The automated 08:30 scout didn't run (computer was asleep, launchd error)
- Yaron asks for immediate research/inspiration
- Starting a creative session and need fresh discoveries

## What It Does

Runs the full Morning Scout process:
1. Reads scout-config.md for day counter, sources, scoring system
2. Reads context files (illustrator-taste-profile, voice-dna, project-brief, connected-tools)
3. Checks existing tool cards and parking lot to avoid duplicates
4. Dispatches 3 parallel research agents:
   - **Illustrator Scout** - 3 visual/illustration discoveries + cross-pollination
   - **CTO Scout** - 3 technology discoveries
   - **Surprise Scout** - 1 unexpected find outside AI/tech
5. Scores everything with Adoption Score (0-25)
6. Routes by score: 19+ Trigger Experiment, 16-18 Lab Queue, 10-15 Parking Lot, 0-9 Skip
7. Writes report to `T-tools/learning/morning-reports/YYYY-MM-DD-scout.md`
8. Updates day counter in scout-config.md

## How to Invoke

Say any of:
- "סייר בוקר" / "morning scout"
- "תמצא לי השראות" / "find inspirations"
- "הרץ סיור" / "run scout"
- `/morning-scout`

## Prerequisites

- scout-config.md must exist with day counter
- Internet access for web searches
- No manual approvals needed - runs autonomously

## Output

Report saved to: `T-tools/learning/morning-reports/YYYY-MM-DD-scout.md`

### Report Structure
```
# Morning Scout - YYYY-MM-DD
## שאלת היום (יום X מתוך 30)
## תגליות אילוסטרייטור (3)
## תגליות טכנולוגיה (3)
## הצלבה: [תחום]
## תא ההפתעה
## עדכון תור מעבדה
## ניסויים מיידיים (ציון 19+)
## טבלת סיכום
## 1. מה למדתי היום          <-- חובה: סיכום בעברית פשוטה
## 2. המלצות                  <-- חובה: טבלת פעולות (מי, מה, כמה זמן)
## 3. בדיקת בטיחות            <-- חובה: לכל פריט - האם פוגע בקיים?
```

### Three Closing Sections (MANDATORY)

Every report MUST end with these three sections:

**1. מה למדתי היום** - בעברית פשוטה, נקודה לכל תגלית. מה השורה התחתונה? לא מה מצאתי - מה למדתי.

**2. המלצות** - טבלה עם עמודות: עדיפות, מה לעשות, מי עושה, כמה זמן. ממיינים מגבוהה לנמוכה.

**3. בדיקת בטיחות** - לכל פריט חדש: האם הוא דורס מידע קיים? מוחק קבצים? משנה תהליכים? מחליף כלי שעובד? טבלה עם תוצאה: בטוח / בטוח-הפיך / נדחה לבדיקה.

## Agent Dispatch Pattern

Three Task agents run in parallel:

### Illustrator Scout Agent
```
subagent_type: "general-purpose"
Research focus: HuggingFace papers, Civitai trending, AI art techniques,
               Replicate new models, rotating question of the day
Must include: 3 discoveries + 1 cross-pollination (non-AI/tech discipline)
Score each with Adoption Score (5 parameters x 0-5)
```

### CTO Scout Agent
```
subagent_type: "general-purpose"
Research focus: MCP servers, GitHub trending, CSS new features,
               web performance, rotating question of the day
Must include: 3 discoveries
Score each with Adoption Score
```

### Surprise Scout Agent
```
subagent_type: "general-purpose"
Research focus: unexpected connections to sound/meditation/art/consciousness
Must include: 1 genuinely surprising find
No scoring - pure editorial judgment
```

## Scoring System (Adoption Score 0-25)

| Parameter | Question | 0 | 5 |
|-----------|----------|---|---|
| Brand Fit | Matches sumi-e/wabi-sabi? | Generic | Perfect match |
| Leverage | Time saved / quality added? | Marginal | 10x improvement |
| Repeatability | Consistent results? | Random | Reliable recipe |
| Workflow Export | Plugs into pipeline? | Manual work | Direct integration |
| Risk/License | Dependencies? | Locked platform | Open, stable |

### Thresholds
- **19-25:** Trigger Experiment (micro-experiment today)
- **16-18:** Weekly Lab Queue
- **10-15:** Parking Lot (revisit monthly)
- **0-9:** Skip

## Language Rule

The entire report must be in Hebrew. Tool names described functionally in Hebrew.
Numbers and scores in digits. No jargon.

## Post-Scout Actions

After report is saved:
1. Day counter incremented in scout-config.md
2. If items scored 19+: trigger experiments documented in report
3. Illustrator experiments that need Chrome/Gemini: flagged for Yaron
4. CTO experiments that can run in terminal: executed immediately
5. New parking lot items: added to parking-lot.md

---

## Automation Status

- **Automated run:** 08:30 daily via launchd (`com.sol.morning-scout.plist`)
- **Script:** `T-tools/scripts/morning-scout.sh` (base64 embedded in plist)
- **Model:** opus
- **This skill:** Manual fallback when automation doesn't fire

---

*Created: 2026-02-21*
*Version: 1.0*
