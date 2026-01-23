from app.artifacts.armour import Armour
from app.artifacts.weapon import Weapon
from app.artifacts.potion import Potion


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
