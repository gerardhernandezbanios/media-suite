import zipfile

from ingestor.infrastructure.zip_extractor import ZipExtractor


def test_zip_extractor(tmp_path):
    zip_path = tmp_path / "test.zip"

    # Create a zip
    with zipfile.ZipFile(zip_path, "w") as z:
        z.writestr("file1.txt", "hello")
        z.writestr("file2.txt", "world")

    dest = tmp_path / "out"
    dest.mkdir()

    extractor = ZipExtractor()
    extracted = extractor.extract(zip_path, dest)

    assert len(extracted) == 2
    assert (dest / "file1.txt").exists()
    assert (dest / "file2.txt").exists()
