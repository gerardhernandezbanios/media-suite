# services/backend/app/media/infrastructure/filesystem/zip_extractor_adapter.py

import zipfile
from media.domain.services.zip_extractor_port import ZipExtractorPort

class ZipExtractorAdapter(ZipExtractorPort):

    async def extract(self, zip_path: str, dest_dir: str) -> list[str]:
        extracted = []
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(dest_dir)
            extracted = z.namelist()
        return extracted
