📘 HOW‑TO: Configuración y ejecución de media-suite
1. Requisitos previos
Docker + Docker Compose

Un disco externo montado en tu sistema, por ejemplo:

Código
/mnt/media
Estructura recomendada:

Código
/mnt/media/
├─ incoming/      # aquí dejas los archivos nuevos
├─ photos/
├─ videos/
├─ animations/
└─ logs/
2. Clonar el repositorio
Código
git clone https://github.com/tuusuario/media-suite.git
cd media-suite
3. Configurar variables de entorno
Editar infra/.env:

Código
MEDIA_DISK=/mnt/media

SOURCE_DIR=/data/incoming
IMAGES_ROOT=/data/photos
VIDEOS_ROOT=/data/videos
ANIMATIONS_ROOT=/data/animations

LOG_FILE=/data/logs/file_movements.csv
AUDIT_FILE=/data/logs/audit_summary.csv
4. Abrir el proyecto en Devcontainer
En VS Code:

Abre la carpeta media-suite

Pulsa F1

“Dev Containers: Reopen in Container”

Esto te dará:

Python 3.12

Poetry

Ruff

Black

MyPy

Debugger

Docker tools

5. Instalar dependencias del servicio
Dentro del devcontainer:

Código
cd services/ingestor
poetry install
6. Levantar el servicio
Desde infra/:

Código
docker compose up -d
El servicio arrancará y mostrará:

Código
Starting ingestor service...
Watching for new files in: /data/incoming
7. Probar el sistema
Copia cualquier foto/vídeo/ZIP a:

Código
/mnt/media/incoming
En segundos verás:

El archivo movido a su carpeta correspondiente

Un registro en logs/file_movements.csv

Estadísticas en logs/audit_summary.csv

8. Parar el servicio
Código
docker compose down