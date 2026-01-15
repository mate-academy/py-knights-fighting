from __future__ import annotations


class Armour:
    def __init__(self, armour: dict) -> None:
        self.part = armour["part"]
        self.protection = armour["protection"]

    @staticmethod
    def get_total_protection(armour_items: list[Armour]) -> int:
        total_protection = 0

        for item in armour_items:
            total_protection += item.protection

        return total_protection
