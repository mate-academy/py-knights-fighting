from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @staticmethod
    def parse_weapon(weapon_dict: dict) -> Weapon:
        return Weapon(weapon_dict.get("name"), weapon_dict.get("power"))
