# services/backend/app/media/domain/services/zip_extractor_port.py
from abc import ABC, abstractmethod
from pathlib import Path


class ZipExtractorPort(ABC):

    @abstractmethod
    async def extract(self, zip_path: str, dest_dir: str) -> list[str]:
        """Devuelve lista de paths extraídos"""
        ...
