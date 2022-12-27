from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def parse_armour(armour_list: list) -> list[Armour]:
        parsed_armour = []
        for item in armour_list:
            parsed_armour.append(Armour(item.get("name"),
                                        item.get("protection")))
        return parsed_armour
