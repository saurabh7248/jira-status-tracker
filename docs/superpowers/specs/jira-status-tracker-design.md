# Jira Status Tracker Design

**Goal:** A Python CLI utility that fetches Jira assigned issues per user, saves the status, and compares with yesterday's snapshot.

**Approach:** Python script using `atlassian-python-api` for Jira queries, interactive date selection for comparison, per-date JSON snapshots (`snapshots/YYYY-MM-DD.json`), console diff with `difflib`. Plus Flask web UI (`app.py`) with browser date selection and side-by-side field comparison view.

**Constraints:** Python 3.10+, no external DB, manual scheduling, console-only output.
