# services/backend/tests/e2e/test_upload_e2e.py
from fastapi.testclient import TestClient

from app.main import app


def test_upload_e2e(tmp_path):
    client = TestClient(app)

    # aquí usarías ficheros reales de tests/data
    with open("tests/data/photo1.jpg", "rb") as f1:
        files = [
            ("files", ("photo1.jpg", f1, "image/jpeg")),
        ]
        res = client.post("/media/upload", files=files)

    assert res.status_code == 200
    items = res.json()
    assert len(items) == 1
    assert items[0]["filename"] == "photo1.jpg"
