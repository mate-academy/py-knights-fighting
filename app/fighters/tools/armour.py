from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def get_instances(cls, armours: list) -> list[Armour]:
        return [
            cls(part=armour["part"], protection=armour["protection"])
            for armour in armours
        ]
