from typing import Any

from app.equipment.equipment import Equipment


class Armor(Equipment):
    def __init__(self, part: str, power: int) -> None:
        super().__init__(part)
        self.power = power

    @classmethod
    def apply(cls, knight: Any, source: dict) -> None:
        armor_data = (
            source.get(knight.name.lower(),
                       source.get(knight.name.replace(" ", "_").lower(), {})
                       ).get("armour", [])
        )

        if armor_data:
            knight.equip_list = []
            for armor in armor_data:
                armor = Armor(part=armor["part"], power=armor["protection"])
                knight.armor += armor.power
                knight.equip_list.append(armor)
