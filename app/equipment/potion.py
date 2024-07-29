from typing import Any

from app.equipment.equipment import Equipment


class Potion(Equipment):
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        super().__init__(name)
        self.effect = effect

    @classmethod
    def apply(cls, knight: Any, source: dict) -> None:
        if source.get("potion"):
            potion_effect = source["potion"]["effect"]
            for characteristic_name, value in potion_effect.items():
                if characteristic_name == "power":
                    knight.power += value
                elif characteristic_name == "hp":
                    knight.hp += value
                elif characteristic_name == "protection":
                    knight.protection += value
