from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def create_armour_list(cls, armours: list) -> list[Armour]:
        return [
            cls(armour["part"], armour["protection"])
            for armour in armours
        ]
