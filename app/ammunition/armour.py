from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def parse_armour(armour: list[dict]) -> list[Armour]:
        parsed_armour = []
        for part in armour:
            parsed_armour.append(Armour(**part))
        return parsed_armour
