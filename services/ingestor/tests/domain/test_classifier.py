from pathlib import Path

from ingestor.domain.classifier import Classifier
from ingestor.domain.file_inspector import FileInfo
from ingestor.domain.media_type import MediaType


def make_info(*, is_dir=False, is_archive=False, media_type=MediaType.unsupported()):
    return FileInfo(
        path=Path("dummy"),
        extension="jpg",
        mime=None,
        media_type=media_type,
        is_archive=is_archive,
        is_directory=is_dir,
    )


def test_classifier_directories():
    c = Classifier()
    info = make_info(is_dir=True)
    assert c.classify(info) == "directories"


def test_classifier_archives():
    c = Classifier()
    info = make_info(is_archive=True)
    assert c.classify(info) == "archives"


def test_classifier_images():
    c = Classifier()
    info = make_info(media_type=MediaType.image())
    assert c.classify(info) == "images"


def test_classifier_videos():
    c = Classifier()
    info = make_info(media_type=MediaType.video())
    assert c.classify(info) == "videos"


def test_classifier_animations():
    c = Classifier()
    info = make_info(media_type=MediaType.animation())
    assert c.classify(info) == "animations"


def test_classifier_unsupported():
    c = Classifier()
    info = make_info(media_type=MediaType.unsupported())
    assert c.classify(info) == "unsupported"
