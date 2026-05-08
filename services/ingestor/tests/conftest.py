import pytest


@pytest.fixture
def fake_file(tmp_path):
    file = tmp_path / "file.jpg"
    file.write_text("data")
    return file
