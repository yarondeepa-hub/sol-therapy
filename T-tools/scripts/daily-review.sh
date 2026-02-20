#!/bin/bash
# Daily Review - Sol Therapy Agent System
# Runs at 21:00 daily via launchd
# Activates CEO (Yossi) for autonomous daily review

set -e

# Config
SOL_DIR="/Users/yaronamor/Documents/yaronamor-vault/sol"
REPORTS_DIR="$SOL_DIR/M-memory/daily-reports"
DATE=$(date +%Y-%m-%d)
REPORT_FILE="$REPORTS_DIR/$DATE-daily-review.md"
LOG_FILE="$REPORTS_DIR/daily-review.log"

# Ensure reports directory exists
mkdir -p "$REPORTS_DIR"

# Log start
echo "[$DATE $(date +%H:%M:%S)] Starting daily review..." >> "$LOG_FILE"

# Check if report already exists today (avoid double runs)
if [ -f "$REPORT_FILE" ]; then
    echo "[$DATE $(date +%H:%M:%S)] Report already exists for today. Skipping." >> "$LOG_FILE"
    exit 0
fi

# The prompt - injected directly into Claude Code
PROMPT='יוסי - סקירה יומית אוטומטית.

זו הרצה אוטומטית של סקירה יומית. אין צורך לחכות להוראות מירון.

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

### 5. הצעות לשיפור
- מה עובד טוב ולמה
- מה לא עובד ומה לשנות
- האם יש כלים/תהליכים חדשים שכדאי לשקול

### 6. שמור את הדוח
שמור את הדוח כקובץ: M-memory/daily-reports/'"$DATE"'-daily-review.md

הפורמט:
# Daily Review - '"$DATE"'

## Day Summary
[2-5 bullet points]

## Open Items
[Pending items]

## Claude Code Updates
[New features or "No updates"]

## Agent System Health
[Issues found]

## Recommendations
[3-5 suggestions]

## Protocol Compliance
[Violations noted]

חשוב: אתה מורשה לחפש ברשת, לקרוא קבצים, ולכתוב את הדוח. לא צריך אישור מירון.'

# Run Claude Code in non-interactive mode
cd "$SOL_DIR"
/usr/local/bin/claude -p \
    --model opus \
    --allowedTools "Read Write Glob Grep WebFetch WebSearch Edit" \
    --dangerously-skip-permissions \
    "$PROMPT" \
    >> "$LOG_FILE" 2>&1

# Log completion
if [ -f "$REPORT_FILE" ]; then
    echo "[$DATE $(date +%H:%M:%S)] Daily review completed. Report: $REPORT_FILE" >> "$LOG_FILE"
else
    echo "[$DATE $(date +%H:%M:%S)] Daily review ran but report file not created." >> "$LOG_FILE"
fi

# macOS notification to Yaron
osascript -e 'display notification "הדוח היומי מוכן ב-daily-reports/" with title "יוסי - סקירה יומית" sound name "Glass"' 2>/dev/null || true

echo "[$DATE $(date +%H:%M:%S)] Done." >> "$LOG_FILE"
