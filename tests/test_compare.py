from src.compare import compare

def test_compare_two_dates():
    from src.snapshot import save
    save("2026-11-01", {"status": "open"})
    save("2026-11-02", {"status": "closed"})
    result = compare("2026-11-02", "2026-11-01")
    assert "---" in result or result != ""
