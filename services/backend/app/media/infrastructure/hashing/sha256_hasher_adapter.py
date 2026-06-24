# services/backend/app/media/infrastructure/hashing/sha256_hasher_adapter.py

import hashlib
from pathlib import Path
from media.domain.services.hasher import HasherPort

class SHA256HasherAdapter(HasherPort):

    def compute(self, file: Path) -> str:
        h = hashlib.sha256()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
