from pathlib import Path
from PIL import Image
import imagehash

class Hasher:
    """
    Cálculo de hash perceptual (dHash).
    """
    def compute(self, path: Path) -> str | None:
        try:
            with Image.open(path) as img:
                return str(imagehash.dhash(img))
        except Exception:
            return None

    def compute_raw(self, path: Path):
        try:
            with Image.open(path) as img:
                return imagehash.dhash(img)
        except Exception:
            return None
