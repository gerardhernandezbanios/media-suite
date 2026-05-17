#services/backend/app/core/container.py
from dependency_injector import containers, providers
from app.media.application.services import FileUploadService, UploadMediaService
from app.media.infrastructure.ingestor.processor import IngestorService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.media"]
    )

container = Container()


tmp_dir = Path("/tmp/media-suite")

container.file_upload_service = providers.Factory(
    FileUploadService,
    tmp_dir=tmp_dir,
)

container.upload_media_service = providers.Factory(
    UploadMediaService,
    uploader=container.file_upload_service,
    ingestor=container.ingestor_service,
)
