# test/infrastructure/test_zip_extractor.py
import zipfile

from ingestor.config import Config
from ingestor.infrastructure.zip_extractor import ZipExtractor


def test_zip_extractor(tmp_path, monkeypatch):
    # Override SOURCE_DIR for test
    monkeypatch.setattr(Config, "SOURCE_DIR", tmp_path)

    zip_file = tmp_path / "test.zip"
    extracted_file = tmp_path / "inside.txt"

    # Create ZIP
    with zipfile.ZipFile(zip_file, "w") as z:
        extracted_file.write_text("hello")
        z.write(extracted_file, "inside.txt")

    extractor = ZipExtractor()
    files = extractor.extract(zip_file)

    assert len(files) == 1
    assert files[0].name == "inside.txt"

    extractor.cleanup(zip_file)
    assert not zip_file.exists()
