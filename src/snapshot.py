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
