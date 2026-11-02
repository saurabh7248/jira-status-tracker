# Jira Status Tracker Design

**Goal:** A Python CLI utility that fetches Jira assigned issues per user, saves the status, and compares with yesterday's snapshot.

**Approach:** Python script using `atlassian-python-api` for Jira queries, interactive date selection for comparison, per-date/time JSON snapshots (`snapshots/YYYY-MM-DD-HHMM.json`), console diff with `difflib`. Plus Flask web UI (`app.py`) with browser date/time selection, side-by-side field comparison view, and "Generate Snapshot" button calling `fetch_assigned()`.

**Constraints:** Python 3.10+, no external DB, manual scheduling, console-only output.
