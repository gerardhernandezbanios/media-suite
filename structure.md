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

