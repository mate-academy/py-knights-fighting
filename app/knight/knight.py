from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


class Knight:
    def __init__(self, config: dict):
        self.config = config
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

    def battle_preparation(self):
        armour = Armour(self.config["armour"])
        self.protection = armour.use_armour()

        weapon = Weapon()
        self.power += weapon.use_weapon(self.config["weapon"])

        potion = Potion(self.config["potion"])
        potion.use_potion(self)
