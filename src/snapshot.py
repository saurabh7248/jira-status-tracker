import json
import os

SNAPSHOT_DIR = "snapshots"

def save(date: str, data: dict) -> None:
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    with open(os.path.join(SNAPSHOT_DIR, f"{date}.json"), "w") as f:
        json.dump(data, f)

def load(date: str) -> dict:
    path = os.path.join(SNAPSHOT_DIR, f"{date}.json")
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)

def generate_snapshot() -> str:
    from datetime import datetime
    from src.jira_client import fetch_assigned
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    data = fetch_assigned()
    save(timestamp, data)
    return timestamp
