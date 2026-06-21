# services/backend/app/workers/ingest_worker.py
import asyncio

from services.backend.app.core import container
from services.backend.app.media.application.use_cases.ingest_single_media_use_case import IngestSingleMediaUseCase


def ingest_worker(payload: dict):
    uc = container.resolve(IngestSingleMediaUseCase)
    return asyncio.run(uc.execute(payload["temp_path"]))
