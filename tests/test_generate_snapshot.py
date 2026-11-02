from datetime import datetime
from src.snapshot import save
from src.jira_client import fetch_assigned

def test_generate_snapshot_uses_current_time():
    now_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    # This should call fetch_assigned and save; we'll verify file exists after fix
    pass
