"""Supabase database for persisting notes, progress, and study hours.

Replaces the original SQLite backend. All function signatures remain
identical so app.py needs zero changes.
"""
import streamlit as st
from supabase import create_client, Client


@st.cache_resource
def _get_client() -> Client:
    """Create and cache a Supabase client (survives Streamlit reruns)."""
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


def _sb() -> Client:
    """Shorthand accessor."""
    return _get_client()


# ── Init (no-op for Supabase — tables created via SQL Editor) ──────
def init_db():
    """Validate that we can reach Supabase (tables already exist)."""
    _sb()  # will raise if secrets are missing


# ── Notes ──────────────────────────────────────────────────────────
def save_note(date: str, note: str):
    _sb().table("notes").upsert({"date": date, "note": note}).execute()


def get_note(date: str) -> str:
    result = _sb().table("notes").select("note").eq("date", date).execute()
    return result.data[0]["note"] if result.data else ""


# ── Tasks ──────────────────────────────────────────────────────────
def toggle_task(date: str, task_index: int, completed: bool):
    if completed:
        _sb().table("completed_tasks").upsert(
            {"date": date, "task_index": task_index}
        ).execute()
    else:
        _sb().table("completed_tasks").delete().eq(
            "date", date
        ).eq("task_index", task_index).execute()


def get_completed_tasks(date: str) -> set:
    result = (
        _sb().table("completed_tasks")
        .select("task_index")
        .eq("date", date)
        .execute()
    )
    return {row["task_index"] for row in result.data}


# ── Hours ──────────────────────────────────────────────────────────
def save_hours(date: str, hours: float):
    _sb().table("study_hours").upsert({"date": date, "hours": hours}).execute()


def get_hours(date: str) -> float:
    result = _sb().table("study_hours").select("hours").eq("date", date).execute()
    return float(result.data[0]["hours"]) if result.data else 0.0


# ── Bulk reads (for Progress + All Notes pages) ───────────────────
def get_all_hours() -> dict:
    result = _sb().table("study_hours").select("date, hours").execute()
    return {row["date"]: float(row["hours"]) for row in result.data}


def get_all_completed_tasks() -> dict:
    result = _sb().table("completed_tasks").select("date, task_index").execute()
    out: dict = {}
    for row in result.data:
        d = row["date"]
        if d not in out:
            out[d] = set()
        out[d].add(row["task_index"])
    return out


def get_all_notes() -> dict:
    result = (
        _sb().table("notes")
        .select("date, note")
        .neq("note", "")
        .execute()
    )
    return {row["date"]: row["note"] for row in result.data}

