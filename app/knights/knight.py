from app.knights.equipment.armour import Armour
from app.knights.equipment.potion import Potion
from app.knights.equipment.weapon import Weapon


class Knight:
    def __init__(self, description: dict) -> None:
        self.name = description["name"]
        self.protection = 0
        self.power = description["power"]
        self.hp = description["hp"]
        self.armour = {
            armour["part"]: Armour(armour) for armour in description["armour"]
        }
        self.weapon = Weapon(description["weapon"])
        if description["potion"] is None:
            self.potion = None
        else:
            self.potion = Potion(description["potion"])

    def apply_equipment(self) -> None:
        for part in self.armour.values():
            self.protection += part.protection
        self.power += self.weapon.power
        if self.potion is not None:
            self.protection += self.potion.protection
            self.power += self.potion.power
            self.hp += self.potion.hp
