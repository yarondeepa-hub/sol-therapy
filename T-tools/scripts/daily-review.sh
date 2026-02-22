#!/bin/bash
# Daily Review - Sol Therapy Agent System
# Runs at 21:00 daily via launchd
# TCC-safe: bash logs to /tmp/, Claude CLI handles ~/Documents/ access

DATE=$(date +%Y-%m-%d)
DAY_OF_MONTH=$(date +%d)
LOG_FILE="/tmp/sol-daily-review.log"
SOL_DIR="/Users/yaronamor/Documents/yaronamor-vault/sol"

# Monthly review flag
MONTHLY_NOTE=""
if [ "$DAY_OF_MONTH" = "01" ]; then
    MONTHLY_NOTE="TODAY IS THE 1ST OF THE MONTH - perform monthly parking lot review (see section 5b)."
fi

echo "[$DATE $(date +%H:%M:%S)] Starting daily review..." >> "$LOG_FILE"

# Try to set working directory for Claude CLI
cd "$SOL_DIR" 2>/dev/null || {
    echo "[$DATE $(date +%H:%M:%S)] Warning: Cannot cd to $SOL_DIR (TCC). Claude will use absolute paths." >> "$LOG_FILE"
}

PROMPT='יוסי - סקירה יומית אוטומטית.
Base directory: /Users/yaronamor/Documents/yaronamor-vault/sol/
If relative paths do not work, prefix them with the base directory above.

זו הרצה אוטומטית של סקירה יומית. אין צורך לחכות להוראות מירון.

## FIRST - Before Anything Else:
Check if today'\''s report already exists: M-memory/daily-reports/'"$DATE"'-daily-review.md
If it exists, say "Report already exists" and STOP immediately.

## חוק שפה (חובה מוחלטת)
כל הדוח בעברית בלבד. אפס מילים באנגלית.
שמות כלים וטכנולוגיות - תאר מה הם עושים בעברית במקום לזרוק שם באנגלית.
שפה לא טכנית - כאילו מסביר לחבר חכם, לא למתכנת.
אבל מנומקת - כל טענה עם סיבה, כל המלצה עם הסבר.
מספרים - כן. ז׳רגון - לא.

## מה לעשות (בסדר הזה):

### 1. קרא את מצב המערכת
- קרא CLAUDE.md
- קרא M-memory/active-task.md
- קרא M-memory/current-session.md
- קרא M-memory/learning-log.md (100 שורות אחרונות)

### 2. סכם את היום
- מה נעשה היום (מתוך current-session.md)
- כמה משימות הושלמו
- מה נשאר פתוח
- אם היו protocol violations - תעד

### 3. בדוק עדכוני Claude Code
- בצע WebFetch ל-https://claude.com/product/overview
- בדוק אם יש features חדשים, עדכוני מודל, שינויי API
- תעד כל דבר רלוונטי למערכת שלנו

### 4. סקירת סוכנים
- עבור על כל קבצי הסוכנים ב-A-agents/
- בדוק אם יש חוסר עקביות בין ההנחיות
- בדוק אם learning-log מכיל לקחים שלא הוטמעו בסוכנים
- בדוק אם connected-tools.md מעודכן

### 5. Learning Integration (Evening Sync)
- קרא את דוח הבוקר: T-tools/learning/morning-reports/'"$DATE"'-scout.md (אם קיים)
- סקור: האם משהו מהדוח רלוונטי למשימות של היום?
- בדוק: האם היו Tool Cards חדשים שנוצרו? האם נוצלו במשימות?
- בדוק: האם היו Trigger Experiments? מה התוצאות?
- רשום: אילו תגליות צריכות להיכנס לתכנון של מחר
- הצע: שיפור אחד לתהליך הלמידה עצמו (meta-learning)

### 5a. אימות שילוב (Integration Verification)
בדוק שסיור הבוקר שילב ממצאים ב-5 קבצי היעד:
1. M-memory/illustrator-taste-profile.md - חפש טבלת "Scout Discoveries" - האם יש שורות מהיום?
2. T-tools/skills/connected-tools.md - חפש טבלת "Learning Engine Discoveries" - האם יש שורות מהיום?
3. T-tools/learning/parking-lot.md - בדוק Lab Queue ו-Active Items - האם יש פריטים מהיום?
4. A-agents/illustrator-agent.md - חפש "Learning Engine Feed" -> "Latest Discovery" - האם מעודכן?
5. A-agents/cto-agent.md - חפש "Learning Engine Feed" -> "Latest Discovery" - האם מעודכן?
דווח: "בריאות שילוב: X/5 יעדים עודכנו"
אם פחות מ-3/5: סמן כבעיה דחופה בדוח.

### 5b. סקירת חניון חודשית (1 לחודש בלבד)
'"$MONTHLY_NOTE"'
אם היום הוא ה-1 לחודש:
- קרא T-tools/learning/parking-lot.md
- לכל פריט ב-Active Items: בדוק האם "תנאי השינוי" (Revisit trigger) התקיים
- אם כן: העבר לתור Lab (שנה ציון ל-16+) או צור Tool Card
- אם לא: השאר. אם הפריט ישן מ-3 חודשים ללא שינוי: העבר ל-Archived
- עדכן "Last reviewed" ו-"Next review" בתחתית הקובץ
אם היום לא ה-1 לחודש: דלג על שלב זה.

### 6. חילוץ ABC-TOM (MANDATORY)
קרא M-memory/current-session.md
חפש סימוני [DECISION] ו-[FEEDBACK]:
- לכל [DECISION]: הוסף שורה ל-M-memory/decisions.md עם תאריך, תיאור, והקשר
- לכל [FEEDBACK]: הוסף שורה ל-M-memory/feedback.md עם תאריך, מקור, ותוכן
אם אין סימונים: רשום "אין סימוני ABC-TOM היום" בדוח.

בדוק גם: אם דפוס חוזר 3+ פעמים ב-M-memory/learning-log.md (100 שורות אחרונות):
- תעד את הדפוס
- הצע קידום ל-C-core/voice-dna.md (הצעה בלבד - לא לבצע אוטומטית, דורש אישור ירון)

### 7. הצעות לשיפור
- מה עובד טוב ולמה
- מה לא עובד ומה לשנות
- האם יש כלים/תהליכים חדשים שכדאי לשקול

### 8. שמור את הדוח
שמור את הדוח כקובץ: M-memory/daily-reports/'"$DATE"'-daily-review.md

הפורמט:
# Daily Review - '"$DATE"'

## Day Summary
[2-5 bullet points]

## Open Items
[Pending items]

## Learning Sync
- Morning Scout highlights: [top finding from morning report]
- Tool Cards created today: [count and names]
- Relevance to today work: [how morning discoveries connected to actual tasks]
- Learning process health: [is the engine producing value or noise?]

## Integration Health
- בריאות שילוב: X/5
- taste-profile: [OK/FAIL/SKIP]
- connected-tools: [OK/FAIL/SKIP]
- parking-lot: [OK/FAIL/SKIP]
- illustrator-agent: [OK/FAIL/SKIP]
- cto-agent: [OK/FAIL/SKIP]

## ABC-TOM Extraction
- Decisions extracted: [count]
- Feedback extracted: [count]
- Pattern promotion candidates: [list or "none"]

## Monthly Review (1st only)
[Parking lot changes or "Not 1st of month"]

## Claude Code Updates
[New features or "No updates"]

## Agent System Health
[Issues found]

## Recommendations
[3-5 suggestions]

## Protocol Compliance
[Violations noted]

חשוב: אתה מורשה לחפש ברשת, לקרוא קבצים, ולכתוב את הדוח. לא צריך אישור מירון.'

# Run Claude Code
echo "[$DATE $(date +%H:%M:%S)] Calling claude CLI..." >> "$LOG_FILE"
/usr/local/bin/claude -p \
    --model opus \
    --allowedTools "Read Write Glob Grep WebFetch WebSearch Edit" \
    --dangerously-skip-permissions \
    "$PROMPT" \
    >> "$LOG_FILE" 2>&1
CLAUDE_EXIT=$?
echo "[$DATE $(date +%H:%M:%S)] Claude exited with code: $CLAUDE_EXIT" >> "$LOG_FILE"

# macOS notification
osascript -e 'display notification "הדוח היומי מוכן" with title "יוסי - סקירה יומית" sound name "Glass"' 2>/dev/null || true

echo "[$DATE $(date +%H:%M:%S)] Done." >> "$LOG_FILE"
