media-suite/
└── service/
    └── backend/
        ├── app/
        │   ├── core/
        │   │   ├── config.py
        │   │   ├── container.py
        │   │   ├── logging.py  (pendiente de implementar)
        │   │   └── events.py
        │   │
        │   ├── shared/
        │   │   ├── domain/ (pendiente de implementar)
        │   │   │   ├── value_objects.py
        │   │   │   └── exceptions.py
        │   │   ├── dto/
        |   |   |   |__ media.py
        │   │   └── utils/ (pendiente de implementar)
        │   │
        │   ├── media/
        │   │   ├── domain/
        │   │   │   ├── entities.py
        │   │   │   ├── events.py (pendiente de implementar)
        │   │   │   └── repositories.py (pendiente de implementar)
        │   │   │
        │   │   ├── application/
        │   │   │   ├── commands.py
        │   │   │   ├── queries.py (pendiente de implementar)
        │   │   │   └── services.py (pendiente de implementar)
        │   │   │
        │   │   ├── infrastructure/
        │   │   │   ├── db/
        |   |   |   |   |__ mappers.py
        │   │   │   │   ├── models.py
        │   │   │   │   ├── repositories.py
        │   │   │   │   └── migrations/ (pendiente de implementar)
        |   |   |   |__ exif
        |   |   |   |   |__ extractor.py
        │   │   │   ├── filesystem/
        │   │   │   │   ├── storage.py
        │   │   │   ├── hashing/
        │   │   │   │   ├── perceptual.py
        │   │   │   │   └── sha256.py
        │   │   │   └── ingestor/
        │   │   │       ├── watcher.py (pendiente de implementar)
        │   │   │       └── processor.py
        │   │   │
        │   │   └── api/
        │   │       ├── upload.py
        │   │       ├── media.py
        │   │       └── albums.py
        |   |       |__ mappers.py
        │   │
        │   ├── auth/ (pendiente de implementar)
        │   │   ├── domain/
        │   │   ├── application/
        │   │   ├── infrastructure/
        │   │   └── api/
        │   │
        │   └── recognition/ (pendiente de implementar)
        │       ├── domain/
        │       ├── application/
        │       ├── infrastructure/
        │       └── api/
        │
        ├── tests/ (pendiente de implementar)
        │   ├── unit/
        │   ├── integration/
        │   └── e2e/
        │
        ├── main.py
        ├── pyproject.toml
        └── README.md
