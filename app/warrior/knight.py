from app.equipment.weapon import Weapon
from app.warrior.stats import Stats
from app.equipment.armour import Armour
from app.equipment.potion import Potion


class Knight:
    def __init__(self, info_dict: dict) -> None:
        self.name = info_dict["name"]
        self.armour = Armour(info_dict["armour"])
        self.weapon = Weapon(info_dict["weapon"])
        self.potion = Potion(info_dict["potion"])
        self.stats = (Stats(power=info_dict["power"], hp=info_dict["hp"])
                      + self.armour.stats
                      + self.potion.stats
                      + self.weapon.stats)
