from datetime import date, timedelta
from typing import List, Dict, Optional

# Start Date: Monday, Aug 10, 2026
START_DATE = date(2026, 8, 10)

WEEKLY_PLANS: List[Dict] = [
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 0 – Python Fundamentals Gap-Fill (Weeks 1-6)
    # ═══════════════════════════════════════════════════════════════════
    {   # Week 1: CS50P Foundations (Lectures 0-2)
        "week": 1,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "CS50P Foundations (Lectures 0-2)",
        "days": [
            {"topic": "CS50P Lecture 0: Functions, Variables",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 0", "🌆 Evening (2h): Complete Problem Set 0"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 1: Conditionals",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 1", "🌆 Evening (2h): Complete Problem Set 1"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 2: Loops",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 2", "🌆 Evening (2h): Complete Problem Set 2"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "Review: Functions, Conditionals, Loops",
             "tasks": ["🌅 Morning (1.5h): Review functions/conditionals/loops via quick drills",
                        "🌆 Evening (2h): Solve 2 warm-up problems (FizzBuzz variant, palindrome check) using only what's covered so far"],
             "resources": []},
            {"topic": "Python Practice – List Basics",
             "tasks": ["🌅 Morning (1.5h): List basics deep dive (indexing, slicing, comprehensions)",
                        "🌆 Evening (2h): Practice: 5 list-manipulation snippets from scratch"],
             "resources": []},
            {"topic": "Weekend: Dictionaries & Sets",
             "tasks": ["Dict & set fundamentals (methods, set operations)",
                        "Build a word-frequency counter script",
                        "LeetCode Easy: Two Sum (#1)",
                        "LeetCode Easy: Contains Duplicate (#217)"],
             "resources": ["https://leetcode.com/problems/two-sum/", "https://leetcode.com/problems/contains-duplicate/"]},
            {"topic": "Weekend: Review & GitHub Push",
             "tasks": ["Review week 1 code",
                        "Push all code to GitHub 'fde-journey' repo",
                        "Write a short recap note: what clicked, what's still fuzzy"],
             "resources": []},
        ],
    },
    {   # Week 2: Exceptions, Libraries, NeetCode Easy begins
        "week": 2,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "Exceptions, Libraries, NeetCode Easy Begins",
        "days": [
            {"topic": "CS50P Lecture 3: Exceptions",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 3", "🌆 Evening (2h): Complete Problem Set 3"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 4: Libraries",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 4", "🌆 Evening (2h): Complete Problem Set 4"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "NeetCode Easy: Two Sum & Valid Anagram",
             "tasks": ["🌅 Morning (1.5h): NeetCode Easy: Two Sum, redo with hashmap + explain approach in comments",
                        "🌆 Evening (2h): NeetCode Easy: Valid Anagram (#242)"],
             "resources": ["https://leetcode.com/problems/valid-anagram/"]},
            {"topic": "Requests & JSON Basics",
             "tasks": ["🌅 Morning (1.5h): requests basics — fetch data from a public API (jsonplaceholder.typicode.com)",
                        "🌆 Evening (2h): Parse a nested JSON response into a flat dict"],
             "resources": ["https://jsonplaceholder.typicode.com/"]},
            {"topic": "NeetCode Easy: Contains Duplicate & Stock",
             "tasks": ["🌅 Morning (1.5h): NeetCode Easy: Contains Duplicate, clean redo",
                        "🌆 Evening (2h): NeetCode Easy: Best Time to Buy/Sell Stock (#121)"],
             "resources": ["https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"]},
            {"topic": "Weekend: API Caching Script",
             "tasks": ["Build a script that fetches + caches API data to a local JSON file and reloads it on next run",
                        "Review try/except patterns used"],
             "resources": []},
            {"topic": "Weekend: NeetCode Sweep & Review",
             "tasks": ["NeetCode Easy sweep (2-3 more, e.g. Valid Palindrome, Missing Number)",
                        "Weekly review",
                        "Push code to GitHub"],
             "resources": []},
        ],
    },
    {   # Week 3: File I/O, Unit Testing
        "week": 3,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "File I/O, Unit Testing",
        "days": [
            {"topic": "CS50P Lecture 5: Unit Tests",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 5", "🌆 Evening (2h): Complete Problem Set 5, learn pytest basics"],
             "resources": ["https://cs50.harvard.edu/python/", "https://docs.pytest.org/"]},
            {"topic": "CS50P Lecture 6: File I/O",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 6", "🌆 Evening (2h): Complete Problem Set 6"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CSV Handling & Testing",
             "tasks": ["🌅 Morning (1.5h): Practice CSV read/write with error handling (missing files, malformed rows)",
                        "🌆 Evening (2h): Write pytest tests for Problem Set 6 solutions"],
             "resources": []},
            {"topic": "NeetCode Easy: Arrays",
             "tasks": ["🌅 Morning (1.5h): NeetCode Easy: Concatenation of Array (#1929)",
                        "🌆 Evening (2h): NeetCode Easy: Missing Number (#268)"],
             "resources": ["https://leetcode.com/problems/missing-number/"]},
            {"topic": "JSON Deep Dive & Mini-Project",
             "tasks": ["🌅 Morning (1.5h): JSON deep dive: json.load/dump, nested structures",
                        "🌆 Evening (2h): Mini-project: read a JSON API response, write matching rows to CSV (mirrors your BigQuery pipeline at work, standalone)"],
             "resources": []},
            {"topic": "Weekend: Finish Mini-Project",
             "tasks": ["Finish the mini file-I/O + API + CSV project",
                        "Add pytest coverage"],
             "resources": []},
            {"topic": "Weekend: Review & GitHub Push",
             "tasks": ["Weekly review",
                        "Push code to GitHub",
                        "2 NeetCode Easy problems",
                        "Update recap note"],
             "resources": []},
        ],
    },
    {   # Week 4: Regex, OOP
        "week": 4,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "Regex, OOP",
        "days": [
            {"topic": "CS50P Lecture 7: Regular Expressions",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 7", "🌆 Evening (2h): Complete Problem Set 7"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 8: OOP (Part 1)",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 8 Part 1 (classes, __init__, attributes/methods)",
                        "🌆 Evening (2h): Build a DataRecord class with validation"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "CS50P Lecture 8: OOP (Part 2)",
             "tasks": ["🌅 Morning (1.5h): OOP Part 2 (inheritance, composition)", "🌆 Evening (2h): Complete Problem Set 8"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "NeetCode Easy: Stacks",
             "tasks": ["🌅 Morning (1.5h): NeetCode Easy: Valid Parentheses (#20)",
                        "🌆 Evening (2h): One more NeetCode Easy of your choice"],
             "resources": ["https://leetcode.com/problems/valid-parentheses/"]},
            {"topic": "Class Hierarchy Practice",
             "tasks": ["🌅 Morning (1.5h): Build a small class hierarchy: base Pipeline class + subclasses per data source (toy version of the Phase 2 agentic pipeline)",
                        "🌆 Evening (2h): Write pytest tests for the class hierarchy"],
             "resources": []},
            {"topic": "Weekend: Regex + OOP Consolidation",
             "tasks": ["Extend the week-3 mini project into a class-based pipeline (source → transform → sink)"],
             "resources": []},
            {"topic": "Weekend: Review & GitHub Push",
             "tasks": ["Weekly review",
                        "Push code to GitHub",
                        "2 NeetCode Easy problems"],
             "resources": []},
        ],
    },
    {   # Week 5: Et Cetera, Pandas, Integration
        "week": 5,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "Et Cetera, Pandas, Integration",
        "days": [
            {"topic": "CS50P Lecture 9: Et Cetera",
             "tasks": ["🌅 Morning (1.5h): Watch CS50P Lecture 9 (dataclasses, enums)",
                        "🌆 Evening (2h): Refactor week 4's classes to use @dataclass"],
             "resources": ["https://cs50.harvard.edu/python/"]},
            {"topic": "Pandas Fundamentals (Part 1)",
             "tasks": ["🌅 Morning (1.5h): Pandas fundamentals: Series/DataFrame basics, reading CSV/JSON",
                        "🌆 Evening (2h): Pandas fundamentals: filtering, grouping, aggregation"],
             "resources": ["https://pandas.pydata.org/docs/getting_started/"]},
            {"topic": "NeetCode Easy & Pandas Practice",
             "tasks": ["🌅 Morning (1.5h): 2 NeetCode Easy problems",
                        "🌆 Evening (2h): Reproduce an earlier file-I/O script using pandas instead of raw csv/json; compare tradeoffs"],
             "resources": []},
            {"topic": "Error Handling Deep Dive",
             "tasks": ["🌅 Morning (1.5h): Custom exception classes, logging module basics",
                        "🌆 Evening (2h): Add logging + custom exceptions to the pipeline project"],
             "resources": []},
            {"topic": "Review & Documentation",
             "tasks": ["🌅 Morning (1.5h): Self-quiz review of CS50P concepts (Lectures 0-9)",
                        "🌆 Evening (2h): Push a clean, documented version of the pipeline project to GitHub with a README"],
             "resources": []},
            {"topic": "Weekend: Integration Project",
             "tasks": ["Connect the pipeline to a second toy data source, exercising file I/O + JSON + OOP + pandas together"],
             "resources": []},
            {"topic": "Weekend: Review & Reflection",
             "tasks": ["Weekly review",
                        "Write a note on how this connects to the real BigQuery pipeline at work",
                        "2 NeetCode Easy problems"],
             "resources": []},
        ],
    },
    {   # Week 6: Buffer, Review & Transition into Phase 1
        "week": 6,
        "phase": "Phase 0: Python Fundamentals",
        "theme": "Buffer, Review & Transition into Phase 1",
        "days": [
            {"topic": "NeetCode Sweep",
             "tasks": ["🌅 Morning (1.5h): NeetCode Easy sweep on lowest-confidence topics",
                        "🌆 Evening (2h): Review weak spots from this phase"],
             "resources": []},
            {"topic": "NeetCode 150 Roadmap",
             "tasks": ["🌅 Morning (1.5h): Skim the NeetCode 150 roadmap, pick your Phase 1 pattern order (Arrays/Hashing first)",
                        "🌆 Evening (2h): Solve first 2 problems from that pattern group"],
             "resources": ["https://neetcode.io/practice"]},
            {"topic": "LLM API Fundamentals",
             "tasks": ["🌅 Morning (1.5h): Read the Claude/OpenAI API quickstart docs",
                        "🌆 Evening (2h): Make your first API call to an LLM from a Python script"],
             "resources": []},
            {"topic": "Project Review",
             "tasks": ["🌅 Morning (1.5h): Review the Phase 0 pipeline project end-to-end",
                        "🌆 Evening (2h): Update its README and push the final version to GitHub"],
             "resources": []},
            {"topic": "Resume Draft & Catch-up",
             "tasks": ["🌅 Morning (1.5h): Draft a resume bullet for 'Python fundamentals + mini data pipeline project' (rough, polish in Phase 3)",
                        "🌆 Evening (2h): Buffer/catch-up for anything unfinished"],
             "resources": []},
            {"topic": "Weekend: Phase 0 Checkpoint",
             "tasks": ["Self-assess against the CLAUDE.md 'not yet fluent' list (data structures, OOP, file I/O, exceptions, JSON, APIs)"],
             "resources": []},
            {"topic": "Weekend: Phase 0 Complete 🎉",
             "tasks": ["Phase 0 wrap-up",
                        "Rest before Phase 1",
                        "Add a reflection note in the app"],
             "resources": []},
        ],
    },
]


def _placeholder_week(week_num: int, phase: str, theme: str) -> Dict:
    """A lightweight 7-day placeholder for weeks not yet planned in detail."""
    placeholder_task = f"Detailed plan to be added closer to this week — see CLAUDE.md {phase.split(':')[0]} notes"
    return {
        "week": week_num,
        "phase": phase,
        "theme": theme,
        "days": [
            {"topic": f"Week {week_num}: {theme} (not yet planned)",
             "tasks": [placeholder_task],
             "resources": []}
            for _ in range(7)
        ],
    }


# ═══════════════════════════════════════════════════════════════════
# PHASE 1-4 – Placeholders (weeks 7-29), to be fleshed out later
# ═══════════════════════════════════════════════════════════════════
_PLACEHOLDER_PHASES = [
    ("Phase 1: NeetCode 150 & LLM API Fundamentals", 8),   # weeks 7-14
    ("Phase 2: Portfolio Projects (RAG + Agentic Pipeline)", 8),  # weeks 15-22
    ("Phase 3: Resume Polish & Applications", 3),          # weeks 23-25
    ("Phase 4: Interviews & Iteration", 4),                # weeks 26-29
]

_next_week = len(WEEKLY_PLANS) + 1
for _phase_name, _num_weeks in _PLACEHOLDER_PHASES:
    for _ in range(_num_weeks):
        WEEKLY_PLANS.append(_placeholder_week(_next_week, _phase_name, _phase_name.split(": ", 1)[1]))
        _next_week += 1

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def generate_schedule(shifts: Optional[List[Dict]] = None) -> List[Dict]:
    """Generate the full day-by-day schedule.

    `shifts` is an optional list of {"content_index": i, "shift_days": n} dicts.
    Each entry delays content_index i (and everything after it, since dates are
    assigned by walking forward sequentially) by n additional calendar days.
    """
    shift_map: Dict[int, int] = {}
    for s in shifts or []:
        shift_map[s["content_index"]] = shift_map.get(s["content_index"], 0) + s["shift_days"]

    schedule = []
    content_index = 0
    current_date = START_DATE

    for week_plan in WEEKLY_PLANS:
        week_num = week_plan["week"]
        phase = week_plan["phase"]
        theme = week_plan["theme"]

        for day_plan in week_plan["days"]:
            if content_index in shift_map:
                current_date += timedelta(days=shift_map[content_index])

            day_date = current_date
            weekday = day_date.weekday()
            is_weekend = weekday >= 5
            hours = 5.0 if is_weekend else 3.5

            schedule.append({
                "content_index": content_index,
                "date": day_date,  # date object for comparison
                "date_str": day_date.strftime("%Y-%m-%d"),  # string for database keys
                "day": DAY_NAMES[weekday],
                "day_name": DAY_NAMES[weekday],  # alias used in weekly view
                "week": week_num,
                "phase": phase,
                "theme": theme,
                "topic": day_plan["topic"],
                "tasks": day_plan.get("tasks", []),
                "resources": day_plan.get("resources", []),  # resources list
                "target_hours": hours,
            })

            current_date += timedelta(days=1)
            content_index += 1

    return schedule


# Generate the schedule (used by app.py as SCHEDULE)
SCHEDULE = generate_schedule()
