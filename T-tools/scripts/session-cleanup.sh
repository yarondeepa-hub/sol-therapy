#!/bin/bash
# =============================================================
# session-cleanup.sh - Kill zombie Claude Code sessions
# =============================================================
# Called by SessionStart hook when a new chat opens.
# Only kills sessions idle for more than IDLE_THRESHOLD minutes.
# Never kills the session that invoked this script.
# =============================================================

IDLE_THRESHOLD_MIN=${1:-120}  # default: 2 hours
MY_PID=$$
LOG_PREFIX="[session-cleanup]"

# Find all Claude Code processes (the main binary, not helpers)
get_claude_pids() {
    pgrep -f "claude-code/.*/claude " 2>/dev/null
}

# Get the transcript path for a Claude session (from its cmdline)
get_resume_id() {
    local pid=$1
    ps -p "$pid" -o command= 2>/dev/null | grep -o '\-\-resume [a-f0-9-]*' | awk '{print $2}'
}

# Check if a process has been idle (low CPU) for a while
# Uses elapsed time minus CPU time as a proxy for idle time
is_zombie() {
    local pid=$1
    local threshold_sec=$(( IDLE_THRESHOLD_MIN * 60 ))

    # Get elapsed time and CPU time in seconds
    local etime_raw cputime_raw
    etime_raw=$(ps -p "$pid" -o etime= 2>/dev/null | xargs)
    cputime_raw=$(ps -p "$pid" -o cputime= 2>/dev/null | xargs)

    [ -z "$etime_raw" ] && return 1  # process gone

    # Parse time format: [[dd-]hh:]mm:ss
    parse_time() {
        local t="$1"
        local days=0 hours=0 mins=0 secs=0

        # Handle dd- prefix
        if [[ "$t" == *-* ]]; then
            days="${t%%-*}"
            t="${t#*-}"
        fi

        # Split by colon
        IFS=':' read -ra parts <<< "$t"
        local n=${#parts[@]}
        if [ "$n" -eq 3 ]; then
            hours="${parts[0]}"
            mins="${parts[1]}"
            secs="${parts[2]}"
        elif [ "$n" -eq 2 ]; then
            mins="${parts[0]}"
            secs="${parts[1]}"
        else
            secs="${parts[0]}"
        fi

        echo $(( days*86400 + hours*3600 + mins*60 + secs ))
    }

    local elapsed=$(parse_time "$etime_raw")
    local cputime=$(parse_time "$cputime_raw")

    # If process has been alive for less than threshold, it's not a zombie
    [ "$elapsed" -lt "$threshold_sec" ] && return 1

    # If CPU time is tiny relative to elapsed time AND elapsed > threshold, it's a zombie
    # A zombie uses almost no CPU after initial startup
    local cpu_ratio=0
    if [ "$elapsed" -gt 0 ]; then
        # Check if CPU was used in roughly the last IDLE_THRESHOLD period
        # If total CPU < 60 seconds and process has been alive > threshold, likely zombie
        [ "$cputime" -lt 60 ] && return 0
    fi

    return 1
}

# Kill a Claude session and all its children
kill_session() {
    local pid=$1
    local resume_id=$(get_resume_id "$pid")
    local label="${resume_id:-unknown}"

    # Kill child processes (MCP servers) first
    local children
    children=$(pgrep -P "$pid" 2>/dev/null)
    if [ -n "$children" ]; then
        echo "$children" | xargs kill 2>/dev/null
    fi

    # Kill the disclaimer helper
    local disc_pid=$(( pid - 1 ))
    kill "$disc_pid" 2>/dev/null

    # Kill the main process
    kill "$pid" 2>/dev/null

    # Wait briefly, then force-kill if needed
    sleep 1
    kill -0 "$pid" 2>/dev/null && kill -9 "$pid" 2>/dev/null

    echo "$LOG_PREFIX Killed zombie session PID=$pid (resume=$label)"
}

# Kill orphaned crashpad handlers older than 1 day
kill_old_crashpads() {
    local count=0
    for pid in $(pgrep -f "chrome_crashpad_handler" 2>/dev/null); do
        local etime_raw=$(ps -p "$pid" -o etime= 2>/dev/null | xargs)
        # If elapsed time contains a day marker (dd-), kill it
        if [[ "$etime_raw" == *-* ]]; then
            kill "$pid" 2>/dev/null
            count=$((count + 1))
        fi
    done
    [ "$count" -gt 0 ] && echo "$LOG_PREFIX Killed $count old crashpad handler(s)"
}

# --- Main ---

# Get current session's parent Claude Code PID
# The hook is called BY the Claude Code process, so we need to find it
CALLER_PID=""
if [ -n "$CLAUDE_SESSION_ID" ]; then
    # If env var is set, find matching process
    CALLER_PID=$(pgrep -f "resume.*$CLAUDE_SESSION_ID" 2>/dev/null | head -1)
fi
if [ -z "$CALLER_PID" ]; then
    # Fallback: the newest Claude Code process is likely the caller
    CALLER_PID=$(get_claude_pids | sort -rn | head -1)
fi

killed=0
checked=0

for pid in $(get_claude_pids); do
    # Never kill the calling session
    [ "$pid" = "$CALLER_PID" ] && continue

    checked=$((checked + 1))

    if is_zombie "$pid"; then
        kill_session "$pid"
        killed=$((killed + 1))
    fi
done

kill_old_crashpads

if [ "$killed" -gt 0 ]; then
    echo "$LOG_PREFIX Cleaned $killed zombie session(s) out of $checked checked"
else
    echo "$LOG_PREFIX All $checked other session(s) are active - no cleanup needed"
fi
