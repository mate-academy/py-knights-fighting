from app.battle_preparation.knight import Knight


class Armour:
    def __init__(self, equipment: list, protection: int) -> None:
        self.equipment = equipment
        self.protection = protection

    @classmethod
    def prepare_armour(cls, parts: list) -> "Armour":
        protection = 0
        equipment = []
        for part in parts:
            equipment.append(part["part"])
            protection += part["protection"]
        return cls(equipment, protection)

    def consider_armour_effect(self, knight: Knight) -> None:
        knight.protection = self.protection
        knight.equipment = self.equipment
