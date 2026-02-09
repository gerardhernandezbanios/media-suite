# tests/domain/test_classifier.py
from pathlib import Path

from ingestor.domain.classifier import classify


def test_classify_image():
    assert classify(Path("photo.jpg")) == "image"

def test_classify_video():
    assert classify(Path("movie.mp4")) == "video"

def test_classify_animation():
    assert classify(Path("anim.gif")) == "animation"

def test_classify_zip():
    assert classify(Path("archive.zip")) == "zip"

def test_classify_unsupported():
    assert classify(Path("file.xyz")) == "unsupported"
