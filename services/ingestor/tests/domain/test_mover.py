# tests/domain/test_mover.py
from ingestor.domain.mover import compute_destination, compute_unique_name


def test_compute_destination_special_folder(tmp_path):
    file = tmp_path / "photo.jpg"
    file.write_text("x")

    dest = compute_destination(file, tmp_path, "collage")
    assert dest == tmp_path / "collage"


def test_compute_unique_name_no_collision(tmp_path):
    dest = tmp_path
    file = tmp_path / "photo.jpg"
    file.write_text("x")

    new_path = compute_unique_name(dest, file)
    assert new_path == dest / "photo_1.jpg"


def test_compute_unique_name_with_collision(tmp_path):
    dest = tmp_path
    (dest / "photo.jpg").write_text("x")

    file = tmp_path / "photo.jpg"
    file.write_text("x")

    new_path = compute_unique_name(dest, file)
    assert new_path.name.startswith("photo_")
