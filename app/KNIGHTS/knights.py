from app.EQUIPMENT.armour import Armour
from app.EQUIPMENT.potion import Potion
from app.EQUIPMENT.weapon import Weapon


class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = Armour(data.get("armour", []))
        self.weapon = Weapon(data["weapon"])
        self.protection = self.armour.total_protection()

        potion_data = data.get("potion")
        if potion_data:
            potion = Potion(potion_data)
            self.hp += potion.effect.get("hp", 0)
            self.power += potion.effect.get("power", 0)
            self.protection += potion.effect.get("protection", 0)

        self.power += self.weapon.power

    def take_damage(self, incoming_power: int) -> None:
        damage = max(0, incoming_power - self.protection)
        self.hp = max(0, self.hp - damage)
