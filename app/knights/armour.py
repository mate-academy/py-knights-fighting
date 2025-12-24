from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def create_armour(armour: dict) -> Armour:
        return Armour(armour["part"], armour["protection"])
