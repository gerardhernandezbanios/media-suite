from ingestor.watcher import IngestEventHandler
from watchdog.events import FileCreatedEvent
from pathlib import Path

def test_watcher_event(tmp_path, monkeypatch):
    handler = IngestEventHandler()

    fake_file = tmp_path / "photo.jpg"
    fake_file.write_text("dummy")

    event = FileCreatedEvent(str(fake_file))

    handler.on_created(event)

    # Aquí puedes validar que se ha movido, logueado, etc.
