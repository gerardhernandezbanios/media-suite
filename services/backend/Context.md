📦 CONTEXTO COMPLETO DEL BACKEND MEDIA‑SUITE
(para reutilizar en futuras sesiones)

1. Arquitectura general (DDD + FastAPI + Postgres + Filesystem)
Código
media-suite/service/backend/
│
├── app/
│   ├── core/                     # Config, logging, DI, eventos, startup
│   ├── shared/                   # Shared Kernel
│   ├── media/                    # Bounded context principal
│   │   ├── domain/               # Entidades, repos, eventos
│   │   ├── application/          # Commands, queries, services
│   │   ├── infrastructure/       # DB, FS, hashing, ingestor, exif
│   │   └── api/                  # Routers FastAPI
│   ├── auth/
│   └── recognition/
│
├── tests/
├── main.py
└── pyproject.toml
2. Entidades de dominio
2.1 MediaItem
python
@dataclass
class MediaItem:
    id: Optional[int]
    type: MediaType
    filename: str
    filepath: str
    sha256: str
    phash: Optional[str]
    size_bytes: int
    width: Optional[int]
    height: Optional[int]
    duration: Optional[float]
    created_at: datetime
    ingested_at: datetime
2.2 MediaMetadata (modelo completo)
python
@dataclass
class MediaMetadata:
    id: Optional[int]
    media_id: int

    width: Optional[int]
    height: Optional[int]
    orientation: Optional[int]

    camera_make: Optional[str]
    camera_model: Optional[str]
    lens_model: Optional[str]
    iso: Optional[int]
    aperture: Optional[float]
    shutter_speed: Optional[str]
    focal_length: Optional[float]
    created_at: Optional[datetime]

    duration: Optional[float]
    video_codec: Optional[str]
    audio_codec: Optional[str]
    frame_rate: Optional[float]
    bit_rate: Optional[int]
3. Modelos SQLAlchemy
3.1 MediaItemModel
python
class MediaItemModel(Base):
    __tablename__ = "media_items"

    id = mapped_column(Integer, primary_key=True)
    type = mapped_column(Enum(MediaType), nullable=False)
    filename = mapped_column(String(255), nullable=False)
    filepath = mapped_column(String(500), nullable=False)

    sha256 = mapped_column(String(64), nullable=False, index=True)
    phash = mapped_column(String(32))

    size_bytes = mapped_column(Integer, nullable=False)
    width = mapped_column(Integer)
    height = mapped_column(Integer)
    duration = mapped_column(Float)

    created_at = mapped_column(DateTime, nullable=False)
    ingested_at = mapped_column(DateTime, nullable=False)

    metadata = relationship("MediaMetadataModel", back_populates="media_item", uselist=False)
3.2 MediaMetadataModel
python
class MediaMetadataModel(Base):
    __tablename__ = "media_metadata"

    id = mapped_column(Integer, primary_key=True)
    media_id = mapped_column(ForeignKey("media_items.id", ondelete="CASCADE"), unique=True)

    width = mapped_column(Integer)
    height = mapped_column(Integer)
    orientation = mapped_column(Integer)

    camera_make = mapped_column(String(255))
    camera_model = mapped_column(String(255))
    lens_model = mapped_column(String(255))
    iso = mapped_column(Integer)
    aperture = mapped_column(Float)
    shutter_speed = mapped_column(String(50))
    focal_length = mapped_column(Float)
    created_at = mapped_column(DateTime)

    duration = mapped_column(Float)
    video_codec = mapped_column(String(50))
    audio_codec = mapped_column(String(50))
    frame_rate = mapped_column(Float)
    bit_rate = mapped_column(Integer)

    media_item = relationship("MediaItemModel", back_populates="metadata")
4. DTOs
4.1 MediaItemDTO
python
class MediaItemDTO(BaseModel):
    id: int
    type: MediaTypeDTO
    filename: str
    filepath: str
    sha256: str
    phash: str | None
    size_bytes: int
    width: int | None
    height: int | None
    duration: float | None
    created_at: datetime
    ingested_at: datetime
    metadata: MediaMetadataDTO | None
4.2 MediaMetadataDTO
python
class MediaMetadataDTO(BaseModel):
    width: int | None
    height: int | None
    orientation: int | None

    camera_make: str | None
    camera_model: str | None
    lens_model: str | None
    iso: int | None
    aperture: float | None
    shutter_speed: str | None
    focal_length: float | None
    created_at: datetime | None

    duration: float | None
    video_codec: str | None
    audio_codec: str | None
    frame_rate: float | None
    bit_rate: int | None
5. Mappers
5.1 Dominio ↔ SQLAlchemy
python
def model_to_domain(model: MediaItemModel) -> MediaItem: ...
def domain_to_model(entity: MediaItem) -> MediaItemModel: ...

def metadata_model_to_domain(model: MediaMetadataModel) -> MediaMetadata: ...
def metadata_domain_to_model(entity: MediaMetadata) -> MediaMetadataModel: ...
5.2 Dominio ↔ DTO
python
def domain_to_dto(entity: MediaItem) -> MediaItemDTO: ...
def metadata_domain_to_dto(entity: MediaMetadata) -> MediaMetadataDTO: ...
6. Pipeline completo
(upload → ingestor → EXIF → hashing → metadata → DB)

6.1 Flujo
Guardar archivo temporal

Ingestor (ZIP o archivo normal)

Extraer EXIF (si es imagen)

Determinar fecha de creación

Mover a /media/{image|video}/{año}/{mes}/

Calcular SHA256

Calcular pHash (solo imágenes)

Crear MediaItemModel

Crear MediaMetadataModel

Persistir en DB

Devolver DTO

6.2 EXIF extractor
python
class ExifExtractor:
    def extract(self, path: Path) -> ExifData:
        ...
7. pyproject.toml (Poetry + Ruff + Black + Pytest)
toml
[tool.poetry]
name = "media-suite-backend"
version = "0.1.0"
packages = [{ include = "app" }]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.110.0"
uvicorn = { extras = ["standard"], version = "^0.29.0" }
sqlalchemy = "^2.0.29"
asyncpg = "^0.29.0"
pydantic = "^2.7.0"
python-multipart = "^0.0.9"
pillow = "^10.3.0"
imagehash = "^4.3.1"
dependency-injector = "^4.41.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.1.0"
pytest-asyncio = "^0.23.6"
black = "^24.3.0"
ruff = "^0.3.5"
mypy = "^1.9.0"
✔️ Este es tu contexto maestro
Guárdalo donde quieras.
Cuando quieras continuar, solo dime:

“Usa el contexto”  
y pégalo.

¿Qué quieres construir ahora?
Opciones naturales:

procesamiento de vídeo

API de búsqueda avanzada

tests del pipeline

migraciones Alembic

¿Cuál seguimos?