from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, armour: dict) -> list[Armour]:
        return [Armour(a["part"], a["protection"]) for a in armour]
