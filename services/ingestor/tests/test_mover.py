import shutil
from pathlib import Path
from ingestor.mover import move_file

def test_move_file(tmp_path):
    src = tmp_path / "photo.jpg"
    dst_dir = tmp_path / "images"
    dst_dir.mkdir()

    src.write_text("dummy")

    with open(tmp_path / "log.csv", "w") as log:
        move_file(src, dst_dir, writer=None)

    assert (dst_dir / "photo.jpg").exists()
    assert not src.exists()
