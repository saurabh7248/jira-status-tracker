# Jira Status Tracker Design

**Goal:** A Python CLI utility that fetches Jira assigned issues per user, saves the status, and compares with yesterday's snapshot.

**Approach:** Python script using `requests` for Jira Basic Auth (Server), stores JSON snapshots in `snapshots/`, outputs console diff with `difflib`.

**Constraints:** Python 3.10+, no external DB, manual scheduling, console-only output.
