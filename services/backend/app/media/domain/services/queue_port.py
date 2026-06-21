# services/backend/app/media/domain/services/queue_port.py
from abc import ABC, abstractmethod
from typing import Any

class QueuePort(ABC):
    @abstractmethod
    async def enqueue(self, queue_name: str, payload: dict[str, Any]) -> None:
        ...
