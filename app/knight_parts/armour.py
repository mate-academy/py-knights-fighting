from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def convert_to_armour(armours: list) -> list[Armour]:
        if not armours:
            return []
        return [
            Armour(armour["part"], armour["protection"])
            for armour in armours
        ]

    @staticmethod
    def calculate_protection(armours: list[Armour]) -> int:
        return sum(
            armour.protection
            for armour in armours
        )
