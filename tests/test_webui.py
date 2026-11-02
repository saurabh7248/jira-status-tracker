import sys
sys.path.insert(0, '.')

def test_app_has_index_route():
    from app import app
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
