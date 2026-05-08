media-suite-backend/
│
├── app/
│   ├── core/                     # Config, logging, DI, eventos, startup
│   │   ├── config.py
│   │   ├── container.py          # Dependency Injection
│   │   ├── logging.py
│   │   └── events.py             # startup/shutdown
│   │
│   ├── shared/                   # Shared Kernel (solo lo común)
│   │   ├── domain/
│   │   │   ├── value_objects.py
│   │   │   └── exceptions.py
│   │   ├── dto/
│   │   └── utils/
│   │
│   ├── media/                    # Bounded context principal
│   │   ├── domain/
│   │   │   ├── entities.py       # Photo, Video, Album, Tag...
│   │   │   ├── events.py         # Domain events (PhotoCreated, HashComputed…)
│   │   │   └── repositories.py   # Interfaces
│   │   │
│   │   ├── application/
│   │   │   ├── commands.py       # Use cases: ingest, hash, register, update
│   │   │   ├── queries.py        # Use cases: list, search, get
│   │   │   └── services.py       # Orquestación del pipeline
│   │   │
│   │   ├── infrastructure/
│   │   │   ├── db/
│   │   │   │   ├── models.py     # SQLAlchemy
│   │   │   │   ├── repositories.py
│   │   │   │   └── migrations/
│   │   │   ├── filesystem/
│   │   │   │   ├── storage.py    # Guardar ficheros
│   │   │   ├── hashing/
│   │   │   │   ├── perceptual.py
│   │   │   │   └── sha256.py
│   │   │   └── ingestor/
│   │   │       ├── watcher.py
│   │   │       └── processor.py
│   │   │
│   │   └── api/
│   │       ├── upload.py         # POST /media/upload
│   │       ├── media.py          # GET /media, GET /media/{id}
│   │       └── albums.py
│   │
│   ├── auth/                     # Opcional: usuarios, tokens, permisos
│   │   ├── domain/
│   │   ├── application/
│   │   ├── infrastructure/
│   │   └── api/
│   │
│   └── recognition/              # Futuro: IA, tags automáticos
│       ├── domain/
│       ├── application/
│       ├── infrastructure/
│       └── api/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── main.py                       # FastAPI app + DI + routers
├── pyproject.toml
└── README.md
