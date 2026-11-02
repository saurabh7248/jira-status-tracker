def test_fetch_assigned_uses_atlassian_api():
    from src.jira_client import fetch_assigned
    result = fetch_assigned()
    assert isinstance(result, list)
