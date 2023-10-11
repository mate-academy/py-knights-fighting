from app.creating.weapon import Weapon
from app.creating.armour import Armour
from app.creating.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = None
        self.armor = []
        self.potion = []

    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def equip_armor(self, armour: Armour) -> None:
        self.armor.append(armour)
        self.protection += armour.protection

    def use_potion(self, potion: Potion) -> None:
        self.potion.append(potion)
        for effect, value in potion.effect.items():
            if effect == "hp":
                self.hp += value
            elif effect == "power":
                self.power += value
            elif effect == "protection":
                self.protection += value
