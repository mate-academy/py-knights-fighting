from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def equip_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def equip_armour(self, armour: Armour) -> None:
        self.protection += armour.protection

    def drink_potion(self, potion: Potion) -> None:
        for stat, value in potion.effect.items():
            if stat == "power":
                self.power += value
            elif stat == "hp":
                self.hp += value
            elif stat == "protection":
                self.protection += value
