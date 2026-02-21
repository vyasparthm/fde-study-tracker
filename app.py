"""
FDE Career Pivot – Study Tracker
A Streamlit app to track your 6-month learning journey.
"""
import streamlit as st
from datetime import date, timedelta, datetime
import pandas as pd
from zoneinfo import ZoneInfo

from schedule_data import SCHEDULE, WEEKLY_PLANS, START_DATE
from database import (
    init_db, save_note, get_note, toggle_task,
    get_completed_tasks, save_hours, get_hours,
    get_all_hours, get_all_completed_tasks, get_all_notes,
)

# ── Init ──────────────────────────────────────────────────────────────
init_db()
st.set_page_config(
    page_title="FDE Study Tracker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Password Gate ────────────────────────────────────────────────────
def check_password() -> bool:
    """Block access until the correct password is entered."""
    if st.session_state.get("authenticated"):
        return True
    st.title("🔒 FDE Study Tracker")
    st.caption("Enter the password to access your study tracker.")
    pwd = st.text_input("Password", type="password", key="login_pwd")
    if pwd:
        if pwd == st.secrets["app"]["password"]:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("❌ Incorrect password. Try again.")
    return False

if not check_password():
    st.stop()

# ── Helpers ───────────────────────────────────────────────────────────
# Set your local timezone (change this to your timezone)
LOCAL_TZ = ZoneInfo("America/Chicago")  # Adjust to your timezone

def get_local_today() -> date:
    """Get today's date in the local timezone, not UTC."""
    return datetime.now(LOCAL_TZ).date()

PHASE_COLORS = {
    "Phase 1: Python & DSA": "🟦",
    "Phase 2: Agentic AI & Modern Data Stack": "🟩",
    "Phase 3: Security, Evals & Production": "🟧",
    "Job Search & Interview Prep": "🟥",
}

def get_day_entry(d: date):
    for entry in SCHEDULE:
        if entry["date"] == d:
            return entry
    return None

def days_until_end():
    end = START_DATE + timedelta(weeks=26)
    return (end - get_local_today()).days

def current_week():
    delta = (get_local_today() - START_DATE).days
    if delta < 0:
        return 0
    return min(delta // 7 + 1, 26)

# ── Sidebar ───────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🚀 FDE Study Tracker")
    st.caption("6-Month Career Pivot Roadmap")
    st.divider()
    page = st.radio("Navigate", [
        "📅 Today",
        "📆 Weekly View",
        "🗓️ Full Schedule",
        "📊 Progress",
        "📝 All Notes",
    ], label_visibility="collapsed")
    st.divider()
    cw = current_week()
    st.metric("Current Week", f"{cw} / 26")
    st.metric("Days Remaining", days_until_end())
    st.progress(min(cw / 26, 1.0))

# ══════════════════════════════════════════════════════════════════════
# PAGE: TODAY
# ══════════════════════════════════════════════════════════════════════
if page == "📅 Today":
    st.header("📅 Today's Study Plan")
    selected_date = st.date_input("Date", value=get_local_today())
    entry = get_day_entry(selected_date)

    if entry is None:
        if selected_date < START_DATE:
            st.info(f"Your journey starts on **{START_DATE.strftime('%A, %B %d, %Y')}**. "
                    f"That's in **{(START_DATE - selected_date).days}** days!")
        else:
            st.warning("No schedule entry for this date.")
    else:
        phase_icon = PHASE_COLORS.get(entry["phase"], "⬜")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(f"{phase_icon} {entry['topic']}")
            st.caption(f"Week {entry['week']} · {entry['phase']} · {entry['theme']}")
        with col2:
            st.metric("Target Hours", f"{entry['target_hours']}h")

        st.divider()

        # Tasks with checkboxes
        st.subheader("✅ Tasks")
        completed = get_completed_tasks(entry["date_str"])
        for i, task in enumerate(entry["tasks"]):
            checked = st.checkbox(
                task, value=(i in completed),
                key=f"task_{entry['date_str']}_{i}"
            )
            toggle_task(entry["date_str"], i, checked)

        # Progress for this day
        total = len(entry["tasks"])
        done = sum(1 for i in range(total)
                   if st.session_state.get(f"task_{entry['date_str']}_{i}", False))
        if total > 0:
            st.progress(done / total, text=f"{done}/{total} tasks completed")

        # Resources
        if entry["resources"]:
            st.subheader("🔗 Resources")
            for url in entry["resources"]:
                st.markdown(f"- [{url}]({url})")

        # Hours tracking
        st.divider()
        st.subheader("⏱️ Hours Studied")
        saved_hours = get_hours(entry["date_str"])
        hours = st.number_input(
            "Hours studied today", min_value=0.0, max_value=12.0,
            value=saved_hours, step=0.5,
            key=f"hours_{entry['date_str']}"
        )
        if hours != saved_hours:
            save_hours(entry["date_str"], hours)

        # Notes
        st.divider()
        st.subheader("📝 Notes")
        saved_note = get_note(entry["date_str"])
        note = st.text_area(
            "Your notes for today", value=saved_note,
            height=150, key=f"note_{entry['date_str']}"
        )
        if note != saved_note:
            save_note(entry["date_str"], note)

# ══════════════════════════════════════════════════════════════════════
# PAGE: WEEKLY VIEW
# ══════════════════════════════════════════════════════════════════════
elif page == "📆 Weekly View":
    st.header("📆 Weekly View")
    week_num = st.selectbox(
        "Select Week",
        range(1, 27),
        index=max(0, current_week() - 1),
        format_func=lambda w: f"Week {w}: {WEEKLY_PLANS[w-1]['theme']}"
    )
    wp = WEEKLY_PLANS[week_num - 1]
    phase_icon = PHASE_COLORS.get(wp["phase"], "⬜")
    st.subheader(f"{phase_icon} {wp['theme']}")
    st.caption(f"{wp['phase']}")
    st.divider()

    # Get all days for this week
    week_entries = [e for e in SCHEDULE if e["week"] == week_num]
    all_completed = get_all_completed_tasks()

    for entry in week_entries:
        completed = all_completed.get(entry["date_str"], set())
        total = len(entry["tasks"])
        done = len(completed)
        pct = done / total if total > 0 else 0
        status = "✅" if pct == 1 else "🔶" if pct > 0 else "⬜"

        with st.expander(
            f"{status} **{entry['day_name']}** {entry['date'].strftime('%b %d')} — "
            f"{entry['topic']} ({done}/{total})",
            expanded=(entry["date"] == get_local_today()),
        ):
            for i, task in enumerate(entry["tasks"]):
                checked = st.checkbox(
                    task, value=(i in completed),
                    key=f"wk_task_{entry['date_str']}_{i}"
                )
                toggle_task(entry["date_str"], i, checked)
            if entry["resources"]:
                st.markdown("**Resources:** " + " · ".join(
                    f"[Link]({u})" for u in entry["resources"]
                ))

# ══════════════════════════════════════════════════════════════════════
# PAGE: FULL SCHEDULE
# ══════════════════════════════════════════════════════════════════════
elif page == "🗓️ Full Schedule":
    st.header("🗓️ Full 26-Week Schedule")
    all_completed = get_all_completed_tasks()

    # Phase filter
    phases = list(dict.fromkeys(e["phase"] for e in SCHEDULE))
    selected_phase = st.selectbox("Filter by Phase", ["All"] + phases)

    entries = SCHEDULE if selected_phase == "All" else [
        e for e in SCHEDULE if e["phase"] == selected_phase
    ]

    # Build summary table
    rows = []
    for e in entries:
        completed = all_completed.get(e["date_str"], set())
        total = len(e["tasks"])
        done = len(completed)
        rows.append({
            "Date": e["date"].strftime("%b %d (%a)"),
            "Week": e["week"],
            "Phase": PHASE_COLORS.get(e["phase"], "") + " " + e["phase"],
            "Topic": e["topic"],
            "Tasks": f"{done}/{total}",
            "Hours": f"{e['target_hours']}h",
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True, height=600)

# ══════════════════════════════════════════════════════════════════════
# PAGE: PROGRESS
# ══════════════════════════════════════════════════════════════════════
elif page == "📊 Progress":
    st.header("📊 Progress Dashboard")
    all_completed = get_all_completed_tasks()
    all_hours = get_all_hours()

    # Overall stats
    total_tasks = sum(len(e["tasks"]) for e in SCHEDULE)
    done_tasks = sum(len(v) for v in all_completed.values())
    total_hours_studied = sum(all_hours.values())
    total_target_hours = sum(e["target_hours"] for e in SCHEDULE)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tasks Completed", f"{done_tasks}/{total_tasks}")
    with col2:
        pct = done_tasks / total_tasks * 100 if total_tasks > 0 else 0
        st.metric("Completion %", f"{pct:.1f}%")
    with col3:
        st.metric("Hours Studied", f"{total_hours_studied:.1f}h")
    with col4:
        st.metric("Target Hours", f"{total_target_hours}h")

    st.divider()

    # Phase breakdown
    st.subheader("Phase Progress")
    for phase_name in dict.fromkeys(e["phase"] for e in SCHEDULE):
        phase_entries = [e for e in SCHEDULE if e["phase"] == phase_name]
        phase_total = sum(len(e["tasks"]) for e in phase_entries)
        phase_done = sum(
            len(all_completed.get(e["date_str"], set()))
            for e in phase_entries
        )
        phase_pct = phase_done / phase_total if phase_total > 0 else 0
        icon = PHASE_COLORS.get(phase_name, "⬜")
        st.markdown(f"**{icon} {phase_name}**")
        st.progress(phase_pct, text=f"{phase_done}/{phase_total} tasks")

    st.divider()

    # Weekly hours chart
    st.subheader("📈 Weekly Study Hours")
    weekly_hours = {}
    for e in SCHEDULE:
        w = e["week"]
        h = all_hours.get(e["date_str"], 0)
        weekly_hours[w] = weekly_hours.get(w, 0) + h

    weekly_targets = {}
    for e in SCHEDULE:
        w = e["week"]
        weekly_targets[w] = weekly_targets.get(w, 0) + e["target_hours"]

    chart_data = pd.DataFrame({
        "Week": list(range(1, 27)),
        "Studied": [weekly_hours.get(w, 0) for w in range(1, 27)],
        "Target": [weekly_targets.get(w, 0) for w in range(1, 27)],
    }).set_index("Week")
    st.bar_chart(chart_data)

    # LeetCode tracker
    st.divider()
    st.subheader("💻 LeetCode Progress")
    lc_tasks = sum(
        1 for e in SCHEDULE
        for t in e["tasks"]
        if "leetcode" in t.lower()
    )
    lc_done = sum(
        1 for e in SCHEDULE
        for i, t in enumerate(e["tasks"])
        if "leetcode" in t.lower()
        and i in all_completed.get(e["date_str"], set())
    )
    st.metric("LeetCode Tasks", f"{lc_done}/{lc_tasks}")
    if lc_tasks > 0:
        st.progress(lc_done / lc_tasks)

# ══════════════════════════════════════════════════════════════════════
# PAGE: ALL NOTES
# ══════════════════════════════════════════════════════════════════════
elif page == "📝 All Notes":
    st.header("📝 All Notes")
    all_notes = get_all_notes()

    if not all_notes:
        st.info("No notes yet. Start adding notes on the Today page!")
    else:
        # Sort by date descending
        sorted_notes = sorted(all_notes.items(), key=lambda x: x[0], reverse=True)
        for date_str, note in sorted_notes:
            entry = get_day_entry(datetime.strptime(date_str, "%Y-%m-%d").date())
            topic = entry["topic"] if entry else "Unknown"
            with st.expander(f"📅 **{date_str}** — {topic}"):
                st.markdown(note)

