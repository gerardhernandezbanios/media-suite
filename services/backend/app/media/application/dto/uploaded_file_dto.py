# services/backend/app/media/application/dto/uploaded_file_dto.py
from fastapi import UploadFile
from dataclasses import dataclass


@dataclass
class UploadedFileDTO:
    filename: str
    content_type: str
    file: UploadFile

    @classmethod
    def from_uploadfile(cls, f: UploadFile):
        return cls(filename=f.filename, content_type=f.content_type, file=f)
