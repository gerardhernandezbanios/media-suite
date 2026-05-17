import io
from zipfile import ZipFile

from fastapi.testclient import TestClient

from app.main import app


def create_zip_bytes() -> bytes:
    buf = io.BytesIO()
    with ZipFile(buf, "w") as z:
        z.writestr("a.jpg", b"fake-image-a")
        z.writestr("nested/b.png", b"fake-image-b")
    buf.seek(0)
    return buf.read()


def test_ingest_zip_pipeline(tmp_path, monkeypatch):
    client = TestClient(app)

    zip_bytes = create_zip_bytes()

    files = [
        ("files", ("batch.zip", zip_bytes, "application/zip")),
    ]

    response = client.post("/media/upload", files=files)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2  # a.jpg + nested/b.png
