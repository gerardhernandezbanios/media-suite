FROM python:3.12-slim

WORKDIR /app

# System dependencies for Pillow, watchdog, etc.
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Configure Poetry to create venv inside the project
RUN poetry config virtualenvs.in-project true

# Copy dependency definitions
COPY pyproject.toml poetry.lock ./

# Copy application source code BEFORE installing
COPY src/ src/

# Install dependencies AND your package
RUN poetry install --no-interaction --no-ansi

# Run the service
CMD ["poetry", "run", "python", "-m", "ingestor.main"]
