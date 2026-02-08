import zipfile
from pathlib import Path
from ingestor.zip_processor import process_zip

def test_process_zip(tmp_path):
    zip_path = tmp_path / "test.zip"
    inner = tmp_path / "inner.jpg"
    inner.write_text("dummy")

    with zipfile.ZipFile(zip_path, "w") as z:
        z.write(inner, "inner.jpg")

    with open(tmp_path / "log.csv", "w") as log:
        process_zip(zip_path, writer=None)

    # Aquí puedes validar que se ha extraído y procesado
