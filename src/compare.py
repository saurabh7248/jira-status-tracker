import difflib

def compare(today: dict, yesterday: dict) -> str:
    today_str = str(today)
    yesterday_str = str(yesterday)
    diff = difflib.unified_diff(
        yesterday_str.splitlines(keepends=True),
        today_str.splitlines(keepends=True),
        fromfile="yesterday",
        tofile="today",
    )
    return "".join(diff)
