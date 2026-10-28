"""Regression checks for diagram exports and reverse-proxy URLs."""
from app import app


def test_diagram_exports_are_available():
    client = app.test_client()
    view = client.get("/view/master_system.mmd")
    assert view.status_code == 200
    html = view.get_data(as_text=True)
    assert 'id="download-svg"' in html
    assert 'id="download-png"' in html
    assert 'export-pptx/master_system.mmd' in html
    assert 'static/diagram_export.js' in html
    asset = client.get("/static/diagram_export.js")
    assert asset.status_code == 200
    assert b"prepareSvg" in asset.data


def test_export_asset_uses_forwarded_prefix():
    client = app.test_client()
    response = client.get("/view/master_system.mmd", headers={
        "X-Forwarded-Prefix": "/apps/mermaid-display-app",
        "X-Forwarded-Host": "example.test",
        "X-Forwarded-Proto": "https",
    })
    assert response.status_code == 200
    assert '/apps/mermaid-display-app/static/diagram_export.js' in response.get_data(as_text=True)
