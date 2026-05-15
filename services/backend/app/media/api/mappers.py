# services/backend/app/media/api/mappers.py
from app.media.domain.entities import MediaItem, MediaMetadata
from app.shared.dto.media import MediaItemDTO, MediaTypeDTO
from app.shared.dto.media import MediaMetadataDTO


def metadata_domain_to_dto(entity: MediaMetadata) -> MediaMetadataDTO:
    return MediaMetadataDTO(
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


def domain_to_dto(entity: MediaItem) -> MediaItemDTO:
    return MediaItemDTO(
        id=entity.id,
        type=MediaTypeDTO(entity.type.value),
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
