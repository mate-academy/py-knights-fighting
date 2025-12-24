from app.powerup.armour_protection import Armour
from app.powerup.weapon_power import Weapon
from app.powerup.potion_effect import Potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.potion = Potion(config["potion"]) if config["potion"] else None
        self.armour = Armour(config["armour"]) if config["armour"] else None
        self.weapon = Weapon(config["weapon"])
        self.protection = self.armour.protection if config["armour"] else 0
        self.power += self.weapon.power
