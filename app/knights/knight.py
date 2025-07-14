from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.protection = 0
        self.armour = [Armour(**a) for a in data["armour"]]
        self.weapon = Weapon(**data["weapon"])
        self.potion = Potion(**data["potion"]) if data["potion"] else None

    def apply_equipment_and_potion(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

        if self.weapon:
            self.power += self.weapon.power

        if self.potion:
            effects = self.potion.effect
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

        if self.hp < 0:
            self.hp = 0
