from pathlib import Path
from unittest.mock import patch

from ingestor.infrastructure.file_system import FileSystem


def test_file_system_move():
    fs = FileSystem()
    src = Path("/tmp/a.jpg")
    dst = Path("/tmp/b.jpg")

    with patch("ingestor.infrastructure.file_system.shutil.move") as mock_move:
        fs.move(src, dst)
        mock_move.assert_called_once_with(str(src), str(dst))


def test_file_system_now():
    fs = FileSystem()
    with patch("ingestor.infrastructure.file_system.datetime") as mock_dt:
        fs.now()
        mock_dt.now.assert_called_once()


def test_file_system_get_date():
    fs = FileSystem()
    fake_date = "FAKE_DATE"

    with patch(
        "ingestor.infrastructure.file_system.get_exif_date", return_value=fake_date
    ) as mock_exif:
        result = fs.get_date(Path("x.jpg"))
        assert result == fake_date
        mock_exif.assert_called_once()
