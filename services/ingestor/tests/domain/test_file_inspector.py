from ingestor.domain.file_inspector import FileInspector
from ingestor.domain.media_type import MediaKind


def test_inspector_detects_image(tmp_path):
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"fake data")

    inspector = FileInspector()
    info = inspector.inspect(f)

    assert info.extension == "jpg"
    assert info.media_type.kind is MediaKind.IMAGE
    assert not info.is_archive
    assert not info.is_directory


def test_inspector_detects_video(tmp_path):
    f = tmp_path / "video.mp4"
    f.write_bytes(b"fake data")

    inspector = FileInspector()
    info = inspector.inspect(f)

    assert info.media_type.kind is MediaKind.VIDEO


def test_inspector_detects_archive(tmp_path):
    f = tmp_path / "file.zip"
    f.write_bytes(b"fake data")

    inspector = FileInspector()
    info = inspector.inspect(f)

    assert info.is_archive


def test_inspector_detects_directory(tmp_path):
    d = tmp_path / "folder"
    d.mkdir()

    inspector = FileInspector()
    info = inspector.inspect(d)

    assert info.is_directory
