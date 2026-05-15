# services/backend/app/media/infrastructure/hashing/perceptual.py
from pathlib import Path
from PIL import Image
import imagehash

def compute_phash(path: Path) -> str | None:
    try:
        img = Image.open(path)
        return str(imagehash.phash(img))
    except Exception:
        return None
