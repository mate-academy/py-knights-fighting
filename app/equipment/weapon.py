from typing import Any

from app.equipment.equipment import Equipment


class Weapon(Equipment):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

    @classmethod
    def apply(cls, knight: Any, source: dict) -> None:
        knight.weapon = (
            Weapon(source["weapon"]["name"], source["weapon"]["power"]))
        knight.power += knight.weapon.power
