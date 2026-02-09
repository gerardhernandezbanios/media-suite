media-suite/
├─ .devcontainer/
│  ├─ devcontainer.json
│  └─ Dockerfile
├─ infra/
│  ├─ docker-compose.yml
│  ├─ .env
│  └─ README.md
├─ services/
│  ├─ ingestor/
│  │  ├─ src/
│  │  │  ├─ ingestor/
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ config.py
│  │  │  │  ├─ exif.py
│  │  │  │  ├─ file_classifier.py
│  │  │  │  ├─ mover.py
│  │  │  │  ├─ stats.py
│  │  │  │  ├─ zip_processor.py
│  │  │  │  └─ main.py
│  │  │  └─ cli.py
│  │  ├─ tests/
│  │  ├─ Dockerfile
│  │  └─ pyproject.toml
├─ docs/
│  ├─ arquitectura.md
│  ├─ roadmap.md
│  └─ adr/
├─ .gitignore
└─ README.md

## Estructura final actualizada

media-suite/
├─ .devcontainer/
│  ├─ devcontainer.json
│  └─ Dockerfile
├─ .vscode/
│  ├─ tasks.json
│  └─ launch.json
├─ infra/
│  ├─ docker-compose.yml
│  ├─ .env
│  └─ README.md
├─ services/
│  ├─ ingestor/
│  │  ├─ pyproject.toml
│  │  ├─ poetry.lock
│  │  ├─ Dockerfile
│  │  ├─ src/
│  │  │  └─ ingestor/...
│  │  └─ tests/
├─ docs/
├─ .gitignore
└─ README.md

## Estructura aplicando arquitectura limpia

src/
  ingestor/
    config.py          ← infraestructura compartida
    domain/
      classifier.py
      exif_reader.py
      mover.py
      stats.py
    application/
      service.py
    infrastructure/
      logging_base.py
      logging_csv.py
      file_system.py
      zip_extractor.py
      watcher.py
  main.py               ← nivel superior (entrypoint)
tests/
  conftest.py
  domain/
    test_classifier.py
    test_mover.py
  infrastructure/
    test_logging_csv.py
    test_zip_extractor.py
  application/
    test_service.py

