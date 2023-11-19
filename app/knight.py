from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = Armour(config["armour"])
        self.weapon = Weapon(config["weapon"])
        self.potion = Potion(config["potion"])
