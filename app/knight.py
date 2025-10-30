from .weapon import Weapon
from .armour import Armour
from .potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list,
            potion: dict) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = Weapon(weapon["name"], weapon["power"])

        self.armour = []
        self.total_protection = 0
        for item in armour:
            armour_piece = Armour(item["part"], item["protection"])
            self.armour.append(armour_piece)
            self.total_protection += item["protection"]

        if potion:
            self.potion = Potion(potion["name"], potion["effect"])
            self.potion.apply_effect(self)
        else:
            self.potion = None

        self.power += self.weapon.weapon_power
