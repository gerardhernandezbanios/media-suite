# src/ingestor/logging_base.py
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime


class IngestLogger(ABC):
    @abstractmethod
    def log_move(self, src: Path, dst: Path, timestamp: datetime, zip_origin: str | None):
        """Log a successful file move."""
        pass

    @abstractmethod
    def log_unsupported(self, file: Path):
        """Log a file that could not be processed."""
        pass
