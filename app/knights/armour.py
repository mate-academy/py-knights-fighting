from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def total_armour(armour_list: list[Armour]) -> int:
        total_protection = 0
        for arm in armour_list:
            total_protection += arm.protection
        return total_protection
