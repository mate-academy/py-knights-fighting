from __future__ import annotations


class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, armour_dict: dict) -> Armour:
        return cls(
            armour_dict["part"],
            armour_dict["protection"]
        )

    @staticmethod
    def from_list_to_list(armour_list: list) -> list:
        new_list = [Armour.from_dict(item) for item in armour_list]
        return new_list
