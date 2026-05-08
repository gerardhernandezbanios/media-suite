from pathlib import Path

from ingestor.domain.mover import compute_destination, compute_unique_name


def test_compute_destination(tmp_path, monkeypatch):
    # Fake EXIF date
    class FakeDate:
        year = 2024
        month = 3

    monkeypatch.setattr("ingestor.domain.mover.get_exif_date", lambda f: FakeDate())

    file = tmp_path / "photo.jpg"
    dest = compute_destination(file, Path("/root"), "images")

    assert dest == Path("/root/images/2024/03")


def test_compute_unique_name(tmp_path):
    dest = tmp_path
    f1 = dest / "photo.jpg"
    f1.write_bytes(b"data")

    f2 = dest / "photo.jpg"
    f2.write_bytes(b"data")

    new = compute_unique_name(dest, f2)
    assert new.name != "photo.jpg"
