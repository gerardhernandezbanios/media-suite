from pathlib import Path
from collections import defaultdict

class DuplicateDetector:
    """
    Agrupa ficheros por hash perceptual.
    """
    def __init__(self, hasher):
        self.hasher = hasher

    def find_duplicates(self, files: list[Path]) -> dict[str, list[Path]]:
        groups = defaultdict(list)

        for f in files:
            if not f.is_file():
                continue

            hash_value = self.hasher.compute(f)
            if hash_value:
                groups[hash_value].append(f)

        # Solo devolvemos grupos con más de un archivo
        return {h: g for h, g in groups.items() if len(g) > 1}
