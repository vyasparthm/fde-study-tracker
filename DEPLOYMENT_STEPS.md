# 🚀 Deployment Steps — FDE Study Tracker

Complete these steps before our next session. I'll handle all the code changes once you provide the credentials.

---

## Step 1: Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up (free tier works)
2. Click **"New Project"**
3. Fill in:
   - **Name:** `fde-study-tracker`
   - **Database Password:** pick something strong (save it somewhere)
   - **Region:** choose the closest to you (e.g. `East US` if you're on the East Coast)
4. Wait ~2 minutes for the project to spin up

### Get your credentials:
1. Go to **Settings** (gear icon in left sidebar) → **API**
2. Copy these two values and save them somewhere safe:

| Value | Where to find it |
|-------|-----------------|
| **Project URL** | Under "Project URL" — looks like `https://abcdefg.supabase.co` |
| **Anon public key** | Under "Project API keys" → `anon` `public` — a long string starting with `eyJ...` |

> ⚠️ **Do NOT share the `service_role` key** — we only need the `anon` key.

---

## Step 2: Create a Streamlit Cloud Account

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign up"** → **Sign in with GitHub** (easiest option)
3. Authorize Streamlit to access your GitHub repos
4. That's it — no project to create yet

---

## Step 3: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Fill in:
   - **Repository name:** `fde-study-tracker`
   - **Description:** `6-month FDE career pivot study tracker`
   - **Visibility:** Public (required for free Streamlit Cloud) or Private (if you have Streamlit Pro)
   - **Do NOT** initialize with README (we'll push our existing code)
3. Click **"Create repository"**
4. Save the repo URL (e.g. `https://github.com/YOUR_USERNAME/fde-study-tracker`)

> 💡 Don't push any code yet — I'll set up the deployment config files first.

---

## What to bring to our next session:

| Item | Example |
|------|---------|
| ✅ Supabase Project URL | `https://abcdefg.supabase.co` |
| ✅ Supabase Anon Key | `eyJhbGciOiJIUzI1NiIs...` |
| ✅ GitHub repo URL | `https://github.com/yourname/fde-study-tracker` |
| ✅ Streamlit Cloud account ready | Signed in at share.streamlit.io |

---

## What I'll do next session:

1. Create Supabase tables (notes, completed_tasks, study_hours)
2. Rewrite `database.py` to use Supabase instead of SQLite
3. Add deployment config files (`.streamlit/config.toml`, `requirements.txt`)
4. Walk you through pushing to GitHub and connecting Streamlit Cloud
5. Add secrets (Supabase URL + key) in Streamlit Cloud dashboard

---

## Time estimate: ~20 minutes for setup, ~10 minutes for deployment

All free tier. No credit card needed for any of this. 🎉

