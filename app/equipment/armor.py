from typing import Any

from app.equipment.equipment import Equipment


class Armor(Equipment):
    def __init__(self, part: str, protection: int) -> None:
        super().__init__(part)
        self.protection = protection

    @classmethod
    def apply(cls, knight: Any, source: dict) -> None:
        if source.get("armour"):
            knight.equip_list = []
            for armor in source.get("armour"):
                armor = Armor(armor["part"], armor["protection"])
                knight.protection += armor.protection
                knight.equip_list.append(armor)
