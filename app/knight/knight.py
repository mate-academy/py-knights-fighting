from __future__ import annotations

from app.weapon.weapon import Weapon
from app.armour.armour import Armour
from app.potion.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int, weapon: Weapon) -> None:
        self.name = name
        self.power = power + weapon.power
        self.hp = hp
        self.armour = []
        self.weapon = weapon
        self.potion = None
        self.protection = 0

    def equip_armour(self, new_armour: Armour) -> Knight:
        if new_armour not in self.armour:
            self.armour.append(new_armour)
            self.protection += new_armour.protection

        return self

    def equip_potion(self, potion: Potion) -> Knight:
        self.hp += potion.effect.hp
        self.protection += potion.effect.protection
        self.power += potion.effect.power
        return self
