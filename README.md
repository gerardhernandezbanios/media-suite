# Media Suite

Suite modular para gestionar fotos y vídeos en un entorno privado, autoalojado y extensible.

## 🚀 Objetivo

Crear un ecosistema de microservicios que permita:

- Ingesta de fotos y vídeos desde un punto de entrada.
- Organización automática por fecha y tipo.
- Procesamiento incremental (EXIF, thumbnails, duplicados…).
- Indexación y futura API de consulta.
- UI web para navegación.
- Todo ejecutándose en contenedores Docker.
- Almacenamiento en disco externo.

## 📁 Estructura

- `services/` → microservicios (ingestor, analyzer, indexer…)
- `infra/` → docker-compose, .env, configuración de despliegue
- `docs/` → arquitectura, ADRs, roadmap
- `.devcontainer/` → entorno de desarrollo reproducible

## 🐳 Levantar el sistema

```bash
cd infra
docker compose up -d
