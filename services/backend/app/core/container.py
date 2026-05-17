#services/backend/app/core/container.py
from pathlib import Path

from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.media.application.services import (
    FileUploadService,
    IngestMediaHandler,
    UploadMediaService,
)
from app.media.infrastructure.exif.extractor import PillowExifReader
from app.media.infrastructure.hashing.sha256 import DefaultHashCalculator
from app.media.infrastructure.filesystem.storage import LibraryMediaStorage
from app.media.infrastructure.db.repositories import SqlAlchemyMediaItemRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_session = providers.Dependency(instance_of=AsyncSession)

    tmp_dir = providers.Factory(
        Path,
        "/tmp/media-suite",
    )

    library_dir = providers.Factory(
        Path,
        "/media",
    )

    exif_reader = providers.Factory(
        PillowExifReader,
    )

    hash_calculator = providers.Factory(
        DefaultHashCalculator,
    )

    media_storage = providers.Factory(
        LibraryMediaStorage,
        base_dir=library_dir,
    )

    media_item_repository = providers.Factory(
        SqlAlchemyMediaItemRepository,
        session=db_session,
    )

    file_upload_service = providers.Factory(
        FileUploadService,
        tmp_dir=tmp_dir,
    )

    ingest_media_handler = providers.Factory(
        IngestMediaHandler,
        exif_reader=exif_reader,
        hash_calculator=hash_calculator,
        storage=media_storage,
        repo=media_item_repository,
    )

    upload_media_service = providers.Factory(
        UploadMediaService,
        uploader=file_upload_service,
        ingestor=ingest_media_handler,
    )


container = Container()

