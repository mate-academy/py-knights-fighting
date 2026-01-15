from typing import List


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def total_protection(armours: List["Armour"]) -> int:
        return sum(armour.protection for armour in armours)
