# services/backend/app/media/infrastructure/hashing/perceptual.py
from __future__ import annotations

from pathlib import Path
from typing import Optional

import imagehash
from PIL import Image


def compute_phash(path: Path) -> Optional[str]:
    try:
        with Image.open(path) as img:
            return str(imagehash.phash(img))
    except Exception:
        return None
