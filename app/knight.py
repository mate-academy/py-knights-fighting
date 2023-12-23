from app.knights_stuff.armour import Armour
from app.knights_stuff.potion import Potion
from app.knights_stuff.weapon import Weapon


class Knight:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

    def battle_preparation(self) -> None:
        armour = Armour(self.config["armour"])
        self.protection = armour.use_armour()

        weapon = Weapon()
        self.power += weapon.weapon_power(self.config["weapon"])

        potion = Potion(self.config["potion"])
        potion.use_potion(self)
