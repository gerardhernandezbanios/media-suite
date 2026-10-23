# services/backend/app/core/container.py

"""
| .NET      | Python DI                 | Significado                                   |
| Transient | ``providers.Factory``     | Nueva instancia cada vez                      |
| Scoped    | ``providers.Resource``    | Instancia por contexto (ideal DB sessions)    |
| Singleton | ``providers.Singleton``   | Una instancia global                          |
"""
from pathlib import Path

from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings

from app.media.application.use_cases.upload_media_use_case import UploadMediaUseCase
from app.media.application.use_cases.process_job_use_case import ProcessJobUseCase
from app.media.domain.services.job_port import JobPort
from app.media.infrastructure.filesystem.job_filesystem_adapter import JobFilesystemAdapter

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

    wiring_config = containers.WiringConfiguration(
        modules=[
            "media.api.upload",
            "media.api.media",
            "media.api.albums",
        ]
    )

    # -------------------------
    # Ports / Adapters
    # -------------------------
    job_port: providers.Provider[JobPort] = providers.Factory(
        JobFilesystemAdapter,
        base_path=settings.WORK_BASE_PATH,
    )

    # -------------------------
    # Use Cases
    # -------------------------
    upload_media_use_case = providers.Factory(
        UploadMediaUseCase,
        job_port=job_port,
    )
    process_job_use_case = providers.Factory(
    ProcessJobUseCase,
    job_port=job_port,
    zip_extractor=zip_extractor_port,
    media_type_detector=media_type_detector_port,
    exif_reader=exif_reader_port,
    hasher=hasher_port,
    media_path_factory=media_path_factory_port,
)



container = Container()
