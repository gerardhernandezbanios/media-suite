import pytest
from ingestor.domain.media_type import MediaKind, MediaType


@pytest.mark.parametrize("ext", ["jpg", "JPG", "jpeg", "png"])
def test_media_type_images(ext):
    mt = MediaType.from_extension(ext)
    assert mt.is_image()
    assert mt.kind is MediaKind.IMAGE


@pytest.mark.parametrize("ext", ["mp4", "MP4", "mov", "avi"])
def test_media_type_videos(ext):
    mt = MediaType.from_extension(ext)
    assert mt.is_video()
    assert mt.kind is MediaKind.VIDEO


@pytest.mark.parametrize("ext", ["gif", "GIF", "webp"])
def test_media_type_animations(ext):
    mt = MediaType.from_extension(ext)
    assert mt.is_animation()
    assert mt.kind is MediaKind.ANIMATION


@pytest.mark.parametrize("ext", ["txt", "pdf", "exe", "unknown"])
def test_media_type_unsupported(ext):
    mt = MediaType.from_extension(ext)
    assert not mt.is_supported()
    assert mt.kind is MediaKind.UNSUPPORTED


def test_media_type_factory_methods():
    assert MediaType.image().is_image()
    assert MediaType.video().is_video()
    assert MediaType.animation().is_animation()
    assert not MediaType.unsupported().is_supported()
