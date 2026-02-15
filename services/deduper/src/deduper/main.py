import sys
from pathlib import Path

from deduper.domain.hashing import Hasher
from deduper.domain.duplicate_detector import DuplicateDetector
from deduper.infrastructure.file_system import FileSystem
from deduper.infrastructure.logging.logger import get_logger
from deduper.infrastructure.config import Config
from deduper.application.service import DeduplicationService


def build_service():
    Config.validate()

    return DeduplicationService(
        detector=DuplicateDetector(Hasher()),
        fs=FileSystem(),
        logger=get_logger("deduper"),
        config=Config,
    )


def run():
    if len(sys.argv) < 3:
        print("Uso: python -m deduper <año> <mes>")
        print("Ejemplo: python -m deduper 2020 12")
        return

    year = sys.argv[1]
    month = sys.argv[2]

    # Validación básica
    if not year.isdigit() or not month.isdigit():
        print("❌ Año y mes deben ser números.")
        return

    year = int(year)
    month = int(month)

    # Construimos la ruta: IMAGES_ROOT / año / mes
    folder = Config.IMAGES_ROOT / f"{year}" / f"{month:02d}"

    if not folder.exists():
        print(f"❌ La carpeta no existe: {folder}")
        return

    service = build_service()
    service.run(folder, year, month)


if __name__ == "__main__":
    run()
