from __future__ import annotations
from app.armour.armour import Armour
from app.weapon.weapon import Weapon
from app.potion.potion import Potion


class Knight:

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon
    ) -> None:
        self.name = name
        self.power = power + weapon.power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon
        self.armours = []
        self.potion = None

    def add_armour(self, armour: Armour) -> Knight:
        if armour not in self.armours:
            self.armours.append(armour)
            self.protection += armour.protection
        return self

    def set_potion(self, potion: Potion) -> Knight:
        self.power += potion.effect.power
        self.protection += potion.effect.protection
        self.hp += potion.effect.hp

        return self
