from __future__ import annotations
from typing import List, Dict


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_list(cls, armour: List[Dict[str, str | int]]) -> List[Armour]:
        return [cls(part["part"], part["protection"]) for part in armour]
