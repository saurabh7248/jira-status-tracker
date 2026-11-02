# Jira Status Tracker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI utility that saves Jira assigned issue status per user and compares it with yesterday's snapshot.

**Architecture:** Three modules: `jira_client.py` (fetch via Basic Auth), `snapshot.py` (save/load JSON), `compare.py` (console diff). Manual scheduling, console output.

**Tech Stack:** Python 3.10+, `requests`, standard library only for comparison.

**Spec:** docs/superpowers/specs/jira-status-tracker-design.md

## Global Constraints
- Python 3.10+
- Basic Auth (Jira Server)
- Console output only
- Manual scheduling
- JSON snapshots in `snapshots/`

## Review Focus
- Empty snapshot directory behavior
- Jira auth failure (bad credentials)
- Missing user assigned issues (zero count)
- Same-day comparison (no previous snapshot)
- Large snapshot memory usage
---

### Task 1: Jira Client Module

**Files:**
- Create: `src/jira_client.py`
- Test: `tests/test_jira_client.py`

**Interfaces:**
- Produces: `fetch_assigned(jql: str, auth: tuple) -> list[dict]`

- [ ] **Step 1: Write failing test**
```python
def test_fetch_assigned():
    pass  # not defined yet
```
- [ ] **Step 2: Verify fail**
Run: `pytest tests/test_jira_client.py -v`
Expected: FAIL
- [ ] **Step 3: Implement `fetch_assigned` in `src/jira_client.py`**
Uses `requests` with Basic Auth.
- [ ] **Step 4: Verify pass**
- [ ] **Step 5: Commit**

### Task 2: Snapshot Module

**Files:**
- Create: `src/snapshot.py`
- Test: `tests/test_snapshot.py`

**Produces:** `save(data)`, `load()`

- [ ] Steps 1-5: Implement save/load JSON in `snapshots/`

### Task 3: Compare Module

**Files:**
- Create: `src/compare.py`
- Test: `tests/test_compare.py`

**Produces:** `compare(today, yesterday) -> str` (console diff)

- [ ] Steps 1-5: Implement diff output using `difflib`
