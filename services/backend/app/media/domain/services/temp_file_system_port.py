# services/backend/app/media/domain/services/temp_file_system_port.py
from abc import ABC, abstractmethod


class TempFileSystemPort(ABC):
    @abstractmethod
    async def save_upload(self, upload: UploadedFileDTO) -> str:
        ...

    @abstractmethod
    async def create_temp_dir(self) -> str:
        ...
