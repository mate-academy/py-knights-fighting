from typing import Any

from app.equipment.equipment import Equipment


class Weapon(Equipment):
    def __init__(self, weapon_dict: dict) -> None:
        super().__init__(weapon_dict.get("name"))
        self.power = weapon_dict.get("power")

    @classmethod
    def apply(cls, knight: Any) -> None:
        knight.weapon = Weapon(knight.equipment.get("weapon"))
        knight.power += knight.weapon.power
