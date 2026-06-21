# services/backend/app/media/domain/services/file_system_port.py
from abc import ABC, abstractmethod
from .value_objects import MediaPath

class FileSystemPort(ABC):
    @abstractmethod
    async def move(self, src: str, dest: MediaPath) -> None:
        ...

    @abstractmethod
    async def exists(self, path: MediaPath) -> bool:
        ...
