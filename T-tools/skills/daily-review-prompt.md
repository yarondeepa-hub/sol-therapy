# Daily Review Prompt

> This prompt is injected into Claude Code via `claude -p` every day at 21:00.
> The shell script `daily-review.sh` calls this automatically.

---

## The Prompt

```
יוסי - סקירה יומית אוטומטית.

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
- האם יש עדכוני Claude Code שמשנים את הדרך שאנחנו עובדים

### 6. שמור את הדוח
שמור את הדוח כקובץ:
M-memory/daily-reports/YYYY-MM-DD-daily-review.md

הפורמט:
```markdown
# Daily Review - [DATE]

## Day Summary
[2-5 bullet points of what was done]

## Open Items
[What's still pending]

## Claude Code Updates
[New features/changes found, or "No updates"]

## Agent System Health
[Any inconsistencies or issues found]

## Recommendations
[3-5 actionable suggestions]

## Protocol Compliance
[Any violations noted today]
```

חשוב: אתה מורשה לחפש ברשת, לקרוא קבצים, ולכתוב את הדוח. לא צריך אישור מירון.
```
