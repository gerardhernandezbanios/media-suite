media-suite/
└── service/
    └── backend/
        ├── app/
        │   ├── core/
        │   │   ├── config.py
        │   │   ├── container.py
        │   │   ├── logging.py
        │   │   └── events.py
        │   │
        │   ├── shared/
        │   │   ├── domain/
        │   │   │   ├── value_objects.py
        │   │   │   └── exceptions.py
        │   │   ├── dto/
        │   │   └── utils/
        │   │
        │   ├── media/
        │   │   ├── domain/
        │   │   │   ├── entities.py
        │   │   │   ├── events.py
        │   │   │   └── repositories.py
        │   │   │
        │   │   ├── application/
        │   │   │   ├── commands.py
        │   │   │   ├── queries.py
        │   │   │   └── services.py
        │   │   │
        │   │   ├── infrastructure/
        │   │   │   ├── db/
        │   │   │   │   ├── models.py
        │   │   │   │   ├── repositories.py
        │   │   │   │   └── migrations/
        │   │   │   ├── filesystem/
        │   │   │   │   ├── storage.py
        │   │   │   ├── hashing/
        │   │   │   │   ├── perceptual.py
        │   │   │   │   └── sha256.py
        │   │   │   └── ingestor/
        │   │   │       ├── watcher.py
        │   │   │       └── processor.py
        │   │   │
        │   │   └── api/
        │   │       ├── upload.py
        │   │       ├── media.py
        │   │       └── albums.py
        │   │
        │   ├── auth/
        │   │   ├── domain/
        │   │   ├── application/
        │   │   ├── infrastructure/
        │   │   └── api/
        │   │
        │   └── recognition/
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
        ├── main.py
        ├── pyproject.toml
        └── README.md
