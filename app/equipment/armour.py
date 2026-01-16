from typing import Any

from app.equipment.equipment import Equipment


class Armor(Equipment):
    def __init__(self, part: str, protection: int) -> None:
        super().__init__(part)
        self.protection = protection

    @classmethod
    def apply(cls, knight: Any) -> None:
        armor_data = knight.equipment.get("armour", [])
        for armor in armor_data:
            armor_object = Armor(**armor)
            knight.protection += armor_object.protection
