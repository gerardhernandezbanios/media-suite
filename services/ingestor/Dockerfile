FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY src/ src/

CMD ["poetry", "run", "python", "-m", "ingestor.main"]
