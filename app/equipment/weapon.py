from typing import Any

from app.equipment.equipment import Equipment


class Weapon(Equipment):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

    @classmethod
    def apply(cls, knight: Any, source: dict) -> None:
        weapon_data = (
            source.get(
                knight.name.lower(),
                source.get(
                    knight.name.replace(" ", "_").lower(), {}
                )
            ).get("weapon", None)
        )
        if weapon_data:
            knight.weapon = (
                Weapon(
                    name=weapon_data["name"],
                    power=weapon_data["power"]
                )
            )
            knight.power += knight.weapon.power
