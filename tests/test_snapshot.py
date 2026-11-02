import os

def test_snapshot_save_and_load():
    from src.snapshot import save, load
    save({"user": {"status": "open"}})
    result = load()
    assert result == {"user": {"status": "open"}}
