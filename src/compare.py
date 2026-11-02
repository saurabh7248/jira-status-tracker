import difflib
from src.snapshot import load

def compare(date1: str, date2: str) -> str:
    today = load(date1)
    yesterday = load(date2)
    today_str = str(today)
    yesterday_str = str(yesterday)
    diff = difflib.unified_diff(
        yesterday_str.splitlines(keepends=True),
        today_str.splitlines(keepends=True),
        fromfile=date2,
        tofile=date1,
    )
    return "".join(diff)
