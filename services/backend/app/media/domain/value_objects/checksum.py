#  services/backend/app/media/domain/value_objects/checksum.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Checksum:
    value: str

    def __post_init__(self):
        if not self.value or len(self.value) < 16:
            raise ValueError("Checksum inválido")
