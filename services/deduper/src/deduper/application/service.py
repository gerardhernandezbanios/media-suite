from pathlib import Path

class DeduplicationService:
    """
    Caso de uso: detectar duplicados en una carpeta y moverlos a duplicates/.
    """
    def __init__(self, detector, fs, logger, config):
        self.detector = detector
        self.fs = fs
        self.logger = logger
        self.config = config

    def run(self, root: Path, year: int, month: int):
        self.logger.info(f"🔍 Buscando duplicados en: {root}")

        files = list(root.rglob("*"))
        duplicates = self.detector.find_duplicates(files)

        if not duplicates:
            self.logger.info("✔️ No se han encontrado duplicados.")
            return

        # Crear carpeta de destino para este batch basada en año/mes
        batch_dir = self.config.DUPLICATES_ROOT / str(year) / f"{month:02d}"
        batch_dir.mkdir(parents=True, exist_ok=True)

        for hash_value, group in duplicates.items():
            original = group[0]
            dups = group[1:]

            for dup in dups:
                dest = batch_dir / dup.name
                self.fs.move(dup, dest)
                self.logger.info(f"📁 Duplicado movido: {dup} → {dest}")

        self.logger.info(f"📦 Duplicados almacenados en: {batch_dir}")
