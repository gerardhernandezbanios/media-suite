# services/backend/app/media/infrastructure/queue/redis_queue_adapter.py
import rq
from __future__ import annotations
from services.backend.app.media.domain.services.queue_port import QueuePort


class RedisQueueAdapter(QueuePort):
    def __init__(self, redis_conn):
        self._redis = redis_conn

    async def enqueue(self, queue_name: str, payload: dict) -> str:
        job = rq.Queue(queue_name, connection=self._redis).enqueue(payload)
        return job.id
