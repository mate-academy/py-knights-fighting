from __future__ import annotations


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    @classmethod
    def create_armours(cls, armours: list) -> list[Armour] | []:
        return [
            cls(armour["part"], armour["protection"])
            for armour in armours
        ] if armours else []
