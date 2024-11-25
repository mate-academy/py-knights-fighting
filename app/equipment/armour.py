from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def set_of_armour(armour_list: list[dict]) -> list[Armour]:
        return [
            Armour(armour_part["part"], armour_part["protection"])
            for armour_part in armour_list
        ]
