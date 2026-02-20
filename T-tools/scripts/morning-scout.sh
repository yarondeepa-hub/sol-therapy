#!/bin/bash
# Morning Scout - Sol Therapy Learning Engine
# Runs at 08:30 daily via launchd
# Two scouts: Illustrator + CTO - parallel discovery

set -e

# Config
SOL_DIR="/Users/yaronamor/Documents/yaronamor-vault/sol"
REPORTS_DIR="$SOL_DIR/T-tools/learning/morning-reports"
CONFIG_FILE="$SOL_DIR/T-tools/learning/scout-config.md"
DATE=$(date +%Y-%m-%d)
DAY_OF_WEEK=$(date +%u)  # 1=Monday, 5=Friday, 7=Sunday
REPORT_FILE="$REPORTS_DIR/$DATE-scout.md"
LOG_FILE="$REPORTS_DIR/morning-scout.log"

# Ensure directories exist
mkdir -p "$REPORTS_DIR"

# Log start
echo "[$DATE $(date +%H:%M:%S)] Starting morning scout..." >> "$LOG_FILE"

# Check if report already exists today
if [ -f "$REPORT_FILE" ]; then
    echo "[$DATE $(date +%H:%M:%S)] Scout report already exists for today. Skipping." >> "$LOG_FILE"
    exit 0
fi

# Read current day counter from scout-config.md
DAY_COUNTER=$(grep "^Current day:" "$CONFIG_FILE" | grep -o '[0-9]*' || echo "1")
NEXT_DAY=$(( (DAY_COUNTER % 30) + 1 ))

# Determine if it's Weekly Lab day (Friday)
IS_LAB_DAY="false"
if [ "$DAY_OF_WEEK" = "5" ]; then
    IS_LAB_DAY="true"
fi

# The prompt
PROMPT='You are the Morning Scout for Sol Therapy Learning Engine.

## Your Mission
You are NOT a news aggregator. You are a curious, opinionated scout with taste.
Your job: find 3 things for Illustrator, 3 things for CTO, 1 cross-pollination, 1 surprise.
Score everything. Only the best enters the pipeline.

## MANDATORY - Read These Files First:
1. Read: T-tools/learning/scout-config.md (scoring system, sources, questions, formats)
2. Read: M-memory/illustrator-taste-profile.md (what Yaron likes visually)
3. Read: C-core/voice-dna.md (brand voice - filter for brand fit)
4. Read: C-core/project-brief.md (what Soul Therapy is)
5. Read: T-tools/skills/connected-tools.md (what tools we have)

Then check what we already know (avoid duplicates):
6. Glob: T-tools/learning/tool-cards/illustrator/*.md (existing cards)
7. Glob: T-tools/learning/tool-cards/cto/*.md (existing cards)
8. Read: T-tools/learning/parking-lot.md (if exists - avoid re-surfacing parked items)

## Today'\''s Rotating Question (Day '"$DAY_COUNTER"'/30)
Look up question #'"$DAY_COUNTER"' from the Illustrator Questions AND CTO Questions in scout-config.md.
The question for today must appear prominently in your report and influence your search.

## What To Do:

### 1. Illustrator Scout
Search the Illustrator sources listed in scout-config.md.
Find 3 discoveries. For each:
- Score with Adoption Score (5 parameters, 0-5 each)
- If 16+: sketch a recipe (how to use it)
- If 19+: flag as Trigger Experiment

Focus on: techniques that match our sumi-e/ink wash/wabi-sabi aesthetic.
Ignore: generic "top AI tools" lists, anything that feels stock-photo-ish.

### 2. CTO Scout
Search the CTO sources listed in scout-config.md.
Find 3 discoveries. For each:
- Score with Adoption Score
- Focus on: things that reduce complexity or unlock new capability
- Ignore: tools that add dependencies without clear payoff

### 3. Cross-Pollination (MANDATORY)
Find ONE thing from outside AI/tech entirely.
A different discipline: ceramics, architecture, music, biology, textiles, film, dance...
Explain concretely how it translates to our visual or technical work.
Score it with Adoption Score.

### 4. Surprise Slot (MANDATORY)
One thing that made you stop. That does not fit any category.
That you would not have found by reading "AI news".
This is the most important item in the report.

### 5. Lab Queue Update
List items currently waiting for Weekly Lab.
'"$(if [ "$IS_LAB_DAY" = "true" ]; then echo "TODAY IS FRIDAY - flag the top Lab Queue item for this week'\''s lab."; fi)"'

### 6. Trigger Experiments (MANDATORY if 19+ exists)
If ANYTHING scored 19+, you MUST run a micro-experiment IMMEDIATELY. Do NOT ask permission. Do NOT skip this step. Do NOT just "flag it for later."

Steps:
- For Illustrator items: check if model exists on Replicate (search_models). If yes, run 3 test generations. If not on Replicate, check if available via pip/GitHub and document setup steps.
- For CTO items: test the tool/feature directly in our environment.
- Try 3 variations minimum
- Document results in the report
- If successful: CREATE a Tool Card file in the appropriate directory (T-tools/learning/tool-cards/illustrator/ or T-tools/learning/tool-cards/cto/) using the template from T-tools/learning/tool-card-template.md
- If failed: document WHY it failed and move to Parking Lot

This is autonomous. You have full permission. The whole point of --dangerously-skip-permissions is that you act.

## Output
Save the full report to: T-tools/learning/morning-reports/'"$DATE"'-scout.md
Use the Morning Report Format from scout-config.md.

## After Saving Report
Update the Day Counter in scout-config.md from '"$DAY_COUNTER"' to '"$NEXT_DAY"'.

## Tone
Be opinionated. Be specific. "This is interesting because..." not "Here are some tools."
If something is mediocre, say so. If something is exciting, say why.
You have taste. Use it.'

# Run Claude Code in non-interactive mode
cd "$SOL_DIR"
/usr/local/bin/claude -p \
    --model opus \
    --allowedTools "Read Write Glob Grep WebFetch WebSearch Edit Task" \
    --dangerously-skip-permissions \
    "$PROMPT" \
    >> "$LOG_FILE" 2>&1

# Log completion
if [ -f "$REPORT_FILE" ]; then
    echo "[$DATE $(date +%H:%M:%S)] Morning scout completed. Report: $REPORT_FILE" >> "$LOG_FILE"

    # macOS notification
    osascript -e 'display notification "3 discoveries for Illustrator, 3 for CTO, 1 surprise" with title "Morning Scout Ready" sound name "Pop"' 2>/dev/null || true
else
    echo "[$DATE $(date +%H:%M:%S)] Morning scout ran but report file not created." >> "$LOG_FILE"

    osascript -e 'display notification "Scout ran but no report was created. Check log." with title "Morning Scout - Issue" sound name "Basso"' 2>/dev/null || true
fi

echo "[$DATE $(date +%H:%M:%S)] Done." >> "$LOG_FILE"
