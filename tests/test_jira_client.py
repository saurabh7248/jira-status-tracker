def test_fetch_assigned_returns_list():
    from src.jira_client import fetch_assigned
    result = fetch_assigned("assignee = currentUser()", ("user", "pass"))
    assert isinstance(result, list)
