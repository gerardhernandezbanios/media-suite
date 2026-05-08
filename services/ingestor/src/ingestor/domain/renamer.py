import re
from datetime import datetime
from pathlib import Path


class Renamer:
    def normalize(self, path: Path) -> Path:
        name = path.stem
        ext = path.suffix.lower()

        # Quitar caracteres raros
        name = re.sub(r"[^a-zA-Z0-9_-]+", "_", name)

        # Evitar nombres vacíos
        if not name:
            name = "file"

        return path.with_name(f"{name}{ext}")

    def avoid_collision(self, path: Path) -> Path:
        if not path.exists():
            return path

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{path.stem}_{timestamp}{path.suffix}"
        return path.with_name(new_name)
