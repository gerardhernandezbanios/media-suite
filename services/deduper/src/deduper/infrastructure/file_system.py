from pathlib import Path
import shutil

class FileSystem:
    def move(self, src: Path, dst: Path):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
