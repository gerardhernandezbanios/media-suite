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
