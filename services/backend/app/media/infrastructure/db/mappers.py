from app.media.domain.entities import MediaItem, MediaType
from app.media.infrastructure.db.models import MediaItemModel
from app.media.domain.entities import MediaMetadata
from app.media.infrastructure.db.models import MediaMetadataModel


def metadata_model_to_domain(model: MediaMetadataModel) -> MediaMetadata:
    return MediaMetadata(
        id=model.id,
        media_id=model.media_id,
        width=model.width,
        height=model.height,
        orientation=model.orientation,
        camera_make=model.camera_make,
        camera_model=model.camera_model,
        lens_model=model.lens_model,
        iso=model.iso,
        aperture=model.aperture,
        shutter_speed=model.shutter_speed,
        focal_length=model.focal_length,
        created_at=model.created_at,
        duration=model.duration,
        video_codec=model.video_codec,
        audio_codec=model.audio_codec,
        frame_rate=model.frame_rate,
        bit_rate=model.bit_rate,
    )


def metadata_domain_to_model(entity: MediaMetadata) -> MediaMetadataModel:
    return MediaMetadataModel(
        id=entity.id,
        media_id=entity.media_id,
        width=entity.width,
        height=entity.height,
        orientation=entity.orientation,
        camera_make=entity.camera_make,
        camera_model=entity.camera_model,
        lens_model=entity.lens_model,
        iso=entity.iso,
        aperture=entity.aperture,
        shutter_speed=entity.shutter_speed,
        focal_length=entity.focal_length,
        created_at=entity.created_at,
        duration=entity.duration,
        video_codec=entity.video_codec,
        audio_codec=entity.audio_codec,
        frame_rate=entity.frame_rate,
        bit_rate=entity.bit_rate,
    )


def model_to_domain(model: MediaItemModel) -> MediaItem:
    return MediaItem(
        id=model.id,
        type=MediaType(model.type.value),
        filename=model.filename,
        filepath=model.filepath,
        sha256=model.sha256,
        phash=model.phash,
        size_bytes=model.size_bytes,
        width=model.width,
        height=model.height,
        duration=model.duration,
        created_at=model.created_at,
        ingested_at=model.ingested_at,
    )


def domain_to_model(entity: MediaItem) -> MediaItemModel:
    return MediaItemModel(
        id=entity.id,
        type=entity.type,
        filename=entity.filename,
        filepath=entity.filepath,
        sha256=entity.sha256,
        phash=entity.phash,
        size_bytes=entity.size_bytes,
        width=entity.width,
        height=entity.height,
        duration=entity.duration,
        created_at=entity.created_at,
        ingested_at=entity.ingested_at,
    )
