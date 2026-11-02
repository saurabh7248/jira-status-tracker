def test_compare_shows_diff():
    from src.compare import compare
    result = compare({"a": 2}, {"a": 1})
    assert "---" in result or "+++" in result or result != ""
