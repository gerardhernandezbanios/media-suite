from pathlib import Path
from typing import Dict, List
import imagehash


class DuplicateDetector:
    """
    Agrupa ficheros por hash perceptual.
    """
    def __init__(self, hasher):
        self.hasher = hasher

    def find_duplicates(self, files: list[Path]) -> dict[str, list[Path]]:
        hashes: Dict[imagehash.ImageHash, List[Path]] = {}  # hash -> list of files
        for f in files:
            if not f.is_file():
                continue

            h = self.hasher.compute_raw(f)  # devuelve ImageHash, no string
            if h is None:
                continue

            # Buscar si ya existe un hash idéntico
            found = False
            for existing_hash in hashes:
                if h - existing_hash == 0:  # distancia Hamming exacta
                    hashes[existing_hash].append(f)
                    found = True
                    break

            if not found:
                hashes[h] = [f]

        # Filtrar solo grupos con duplicados
        return {str(h): g for h, g in hashes.items() if len(g) > 1}
