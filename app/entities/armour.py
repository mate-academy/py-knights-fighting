from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def init_from_dict(cls, armour_dict: dict) -> Armour:
        return cls(armour_dict["part"], armour_dict["protection"])
