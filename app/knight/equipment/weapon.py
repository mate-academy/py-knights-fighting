from typing import Any


class Weapon:
    @staticmethod
    def add_weapon(weapon: dict, knight: Any) -> object:
        knight.power += weapon["power"]
        return knight
