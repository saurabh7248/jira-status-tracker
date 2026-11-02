def test_snapshot_save_and_load_by_date():
    from src.snapshot import save, load
    save("2026-11-01", {"user": {"status": "open"}})
    result = load("2026-11-01")
    assert result == {"user": {"status": "open"}}
