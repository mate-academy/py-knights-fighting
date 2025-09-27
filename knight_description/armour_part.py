from __future__ import annotations


class ArmourPart:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def get_armor(cls, armours: list[dict]) -> dict:
        armour = [
            cls(armour["part"], armour["protection"])
            for armour in armours
        ]
        protection = sum(armour_part.protection for armour_part in armour)
        return {"armour": armour, "protection": protection}
