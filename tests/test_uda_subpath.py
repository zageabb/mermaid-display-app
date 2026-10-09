"""Smoke checks for Mermaid Display App through UDA and LAN."""
from app import app

def test_uda_and_lan():
    client = app.test_client()
    local = client.get("/")
    assert local.status_code == 200
    assert '<base href="/">' in local.get_data(as_text=True)
    headers = {
        "X-Forwarded-Prefix": "/apps/mermaid-display-app",
        "X-Forwarded-Host": "tanyaanne.ddns.net",
        "X-Forwarded-Proto": "https",
    }
    remote = client.get("/", headers=headers)
    assert remote.status_code == 200
    assert '<base href="/apps/mermaid-display-app/">' in remote.get_data(as_text=True)
