from unittest.mock import Mock

import pytest
from ingestor.application.service import IngestService


@pytest.fixture
def fs():
    return Mock()


@pytest.fixture
def config(tmp_path):
    class DummyConfig:
        IMAGES_ROOT = tmp_path / "images"
        VIDEOS_ROOT = tmp_path / "videos"
        ANIMATIONS_ROOT = tmp_path / "animations"
        UNSUPPORTED_ROOT = tmp_path / "unsupported"
        WATCH_ROOT = tmp_path / "watch"

    cfg = DummyConfig()
    for p in [
        cfg.IMAGES_ROOT,
        cfg.VIDEOS_ROOT,
        cfg.ANIMATIONS_ROOT,
        cfg.UNSUPPORTED_ROOT,
        cfg.WATCH_ROOT,
    ]:
        p.mkdir(parents=True, exist_ok=True)

    return cfg


@pytest.fixture
def service(fs, config):
    return IngestService(fs, config)


def test_ingest_image(service, fs, config, tmp_path):
    src = tmp_path / "photo.JPG"
    src.touch()

    service.ingest_file(src)

    dst = config.IMAGES_ROOT / src.name
    fs.move.assert_called_once_with(src, dst)


def test_ingest_video(service, fs, config, tmp_path):
    src = tmp_path / "clip.mp4"
    src.touch()

    service.ingest_file(src)

    dst = config.VIDEOS_ROOT / src.name
    fs.move.assert_called_once_with(src, dst)


def test_ingest_animation(service, fs, config, tmp_path):
    src = tmp_path / "anim.webp"
    src.touch()

    service.ingest_file(src)

    dst = config.ANIMATIONS_ROOT / src.name
    fs.move.assert_called_once_with(src, dst)


def test_ingest_unsupported(service, fs, config, tmp_path):
    src = tmp_path / "readme.txt"
    src.touch()

    service.ingest_file(src)

    dst = config.UNSUPPORTED_ROOT / src.name
    fs.move.assert_called_once_with(src, dst)


def test_initial_processing(service, fs, config):
    # Creamos ficheros ya existentes en WATCH_ROOT
    f1 = config.WATCH_ROOT / "a.jpg"
    f2 = config.WATCH_ROOT / "b.mp4"
    f1.touch()
    f2.touch()

    service.process_existing_files()

    assert fs.move.call_count == 2
