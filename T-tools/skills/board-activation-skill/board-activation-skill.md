---
name: board-activation-skill
description: Dispatch the Board's 3 AI advisors (GPT-5.2, Gemini 3.1 Deep Think, Claude Opus) through a structured deliberation protocol to reach actionable recommendations.
---

# Board Activation Skill

Three AI minds deliberate a problem. Not just opinions - a structured discussion that builds toward a solution.

---

## Quick Reference

| Member | Model | How to Call |
|--------|-------|------------|
| **GPT** | `gpt-5.2` | Bash curl to OpenAI API |
| **Gemini** | `gemini-3.1-pro` | `mcp__gemini__gemini-query` (model: pro, thinkingLevel: high) |
| **Claude** | Opus | Task tool (model: opus) |

---

## The Protocol: 3 Rounds

```
Round 1 - Independent Positions (parallel)
  3 members get the same brief, respond independently
  No member sees another's answer
      |
      v
Round 2 - Challenge & Build (parallel)
  Each member sees the OTHER TWO positions
  Must respond to disagreements, strengthen weak spots, or change their mind
      |
      v
Round 3 - CEO Synthesis (single)
  CEO finds the signal: what converged, what stayed contested, what emerged
  Produces final recommendation for Yaron
```

**Why 3 rounds?**
- Round 1 = raw independent thinking. No groupthink.
- Round 2 = the magic. Models challenge each other. Weak ideas die. Strong ideas get stronger. New ideas emerge from the collision.
- Round 3 = human judgment. The CEO reads the deliberation and decides what matters.

---

## Round 1: Independent Positions

### The Brief (goes to all three)

CEO builds this from the problem Yaron raised. Must include brand context for GPT and Gemini:

```
## Board Deliberation Brief

**Problem:** [The problem or question Yaron raised - in his words]

**Context:** [Background - what led here, what's been tried, what's at stake]

**About Sol Therapy:** We produce sound meditation events and retreats with leading artists - musicians, researchers, Buddhist practitioners, and visual artists. Our audience: independent professionals 30+, thoughtful, body-mind aware, appreciate art and quality. Based in Israel.

**Constraints:** [Timeline, budget, non-negotiables - if any]

---

You are one of three independent strategic advisors. The other two will NOT see your answer in this round.

Respond with:
1. **Your take** - What do you think about this problem? (2-3 sentences)
2. **Your proposed direction** - What would you recommend? (3-5 sentences)
3. **The risk you see** - What could go wrong with your recommendation?
4. **What you'd want to know** - What information would change your recommendation?
```

### Dispatch (3 parallel Task calls in one message)

**Task 1 - GPT-5.2:**
```
Tool: Task
  subagent_type: "general-purpose"
  description: "Board R1 - GPT position"
  prompt: |
    Get GPT-5.2's independent position on a strategic question.

    Use Bash to call:
    curl -s https://api.openai.com/v1/chat/completions \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '<JSON with system prompt + brief>'

    System prompt: "You are a strategic advisor for Sol Therapy. Be direct and honest. No marketing speak."
    User message: <THE BRIEF>

    Return ONLY GPT's response text.
```

**Task 2 - Gemini 3.1:**
```
Tool: Task
  subagent_type: "general-purpose"