from ingestor.domain.renamer import Renamer


def test_normalize_removes_special_chars(tmp_path):
    r = Renamer()
    f = tmp_path / "my file @2024!!.jpg"
    f.write_bytes(b"data")

    new = r.normalize(f)
    assert new.name == "my_file_2024_.jpg"


def test_normalize_empty_name(tmp_path):
    r = Renamer()
    f = tmp_path / ".jpg"
    f.write_bytes(b"data")

    new = r.normalize(f)
    assert new.name.startswith("file")


def test_avoid_collision(tmp_path):
    r = Renamer()

    f1 = tmp_path / "photo.jpg"
    f1.write_bytes(b"data")

    f2 = tmp_path / "photo.jpg"
    f2.write_bytes(b"data")

    new = r.avoid_collision(f2)
    assert new.name != "photo.jpg"
