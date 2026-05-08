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
    args = sys.argv[1:]

    if len(args) == 0:
        print("Uso: python -m deduper <año> [mes]")
        print("Ejemplos:")
        print("  python -m deduper 2020 12")
        print("  python -m deduper 2020")
        return

    # Año obligatorio
    year_str = args[0]
    if not year_str.isdigit():
        print("❌ El año debe ser un número.")
        return

    year = int(year_str)

    # Caso 1: año + mes
    if len(args) == 2:
        month_str = args[1]
        if not month_str.isdigit():
            print("❌ El mes debe ser un número.")
            return

        month = int(month_str)
        folder = Config.IMAGES_ROOT / f"{year}" / f"{month:02d}"

        if not folder.exists():
            print(f"❌ La carpeta no existe: {folder}")
            return

        service = build_service()
        service.run(folder, year, month)
        return

    # Caso 2: solo año → procesar 12 meses
    service = build_service()

    for month in range(1, 13):
        folder = Config.IMAGES_ROOT / f"{year}" / f"{month:02d}"

        if not folder.exists():
            print(f"⚠ Carpeta no encontrada, se omite: {folder}")
            continue

        print(f"▶ Procesando {folder}")
        service.run(folder, year, month)


if __name__ == "__main__":
    run()
