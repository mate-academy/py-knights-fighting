from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Armour:
    part: str
    protection: int

    @classmethod
    def from_dict(cls, data: dict) -> Armour:
        return cls(
            data["part"],
            data["protection"]
        )

    @classmethod
    def list_from_dicts(cls, data_list: Optional[List[dict]]) -> List[Armour]:
        return [cls.from_dict(item) for item in data_list] if data_list else []
