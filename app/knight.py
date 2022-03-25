from armour import Armour
from weapon import Weapon
from potion import Potion


class Knights():

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour()
        self.weapon = Weapon()
        self.potion = Potion()
