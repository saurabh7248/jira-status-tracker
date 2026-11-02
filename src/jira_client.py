from atlassian import Jira

def fetch_assigned(jql: str = "assignee = currentUser()", server: str = "http://localhost:8080", username: str = "user", password: str = "pass") -> list:
    jira = Jira(url=server, username=username, password=password)
    issues_data = jira.jql(jql=jql)
    if not issues_data or 'issues' not in issues_data:
        return []
    return [{"key": i['key'], "summary": i['fields']['summary']} for i in issues_data['issues']]
