from dataclasses import dataclass
from pathlib import Path

import filetype
from ingestor.config import Config
from ingestor.domain.media_type import MediaType


@dataclass(frozen=True)
class FileInfo:
    path: Path
    extension: str | None
    mime: str | None
    media_type: MediaType
    is_archive: bool
    is_directory: bool


class FileInspector:
    def inspect(self, path: Path) -> FileInfo:
        ext = path.suffix.lower().lstrip(".") if path.suffix else None

        # MIME detection
        kind = filetype.guess(str(path))
        mime = kind.mime if kind else None

        # MediaType (ext + mime)
        media_type = self._detect_media_type(ext, mime)

        return FileInfo(
            path=path,
            extension=ext,
            mime=mime,
            media_type=media_type,
            is_archive=self._is_archive(ext),
            is_directory=path.is_dir(),
        )

    def _detect_media_type(self, ext: str | None, mime: str | None) -> MediaType:
        # MIME tiene prioridad
        if mime:
            if mime.startswith("image/"):
                if mime == "image/gif":
                    return MediaType.animation()
                return MediaType.image()

            if mime.startswith("video/"):
                return MediaType.video()

        # Si MIME no ayuda, usar extensión
        if ext:
            return MediaType.from_extension(ext)

        return MediaType.unsupported()

    def _is_archive(self, ext: str | None) -> bool:
        return ext in Config.ARCHIVE_EXTENSIONS
