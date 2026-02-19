# Handoff Template

> **חובה למלא בכל העברת עבודה בין סוכנים.**
> סוכן שמסיים עבודה ומעביר לסוכן אחר חייב למלא את התבנית הזו.

---

## Agent Handoff

| Field | Value |
|-------|-------|
| **From Agent** | [Copywriter / Researcher / Illustrator / CTO / Producer / CEO] |
| **To Agent** | [Copywriter / Researcher / Illustrator / CTO / Producer / Gatekeeper / CEO] |
| **Date** | [Date] |
| **Task** | [Brief description of the task] |
| **Status** | [complete / partial / blocked] |

---

## What Was Done

[Clear description of what this agent produced. Be specific.]

---

## Output

**MERGE_KEY:** [What this output provides - e.g., "post_text", "visual_brief", "venue_options"]

**Files Created/Modified:**
- [file path 1]
- [file path 2]

**Inline Output (if short):**
```
[The actual content, if it fits here. Otherwise reference the file paths above.]
```

---

## Dependencies Satisfied

[What downstream agents can now start as a result of this work being done.]

- [ ] [Agent X] can now [do Y]
- [ ] [Agent Z] can now [do W]

---

## Context for Next Agent

[What the receiving agent needs to know to continue the work effectively.]

### Original Request from Yaron
> [Exact quote of what Yaron asked for]

### Decisions Made
- [Decision 1 - and why]
- [Decision 2 - and why]

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Open Questions
- [Anything unresolved that the next agent should be aware of]

---

## Notes

[Any additional context, warnings, or recommendations.]

---

## Checklist Before Handoff

- [ ] Output is complete (or clearly marked as partial with reason)
- [ ] MERGE_KEY is clear
- [ ] Original request is included
- [ ] Decisions and assumptions are documented
- [ ] File paths are correct
- [ ] current-session.md has been updated
- [ ] active-task.md has been updated
