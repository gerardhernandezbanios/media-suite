FROM python:3.11-slim

# Instalación de dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copiar archivos de proyecto
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --no-interaction --no-ansi

# Copiar el código fuente
COPY src/ /app/src/

ENV PYTHONPATH="/app/src"

# Comando por defecto
ENTRYPOINT ["poetry", "run", "deduper"]
