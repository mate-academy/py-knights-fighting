from __future__ import annotations
from app.ammunition.armours import Armour
from app.ammunition.potions import Potion
from app.ammunition.weapons import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour] = 0,
            weapon: Weapon = None,
            potion: Potion = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    # apply armour
    def add_armour(self, armour: list[Armour]) -> None:
        for item in armour:
            self.armour += item.protection

    # apply weapon
    def add_weapon(self, weapon: Weapon) -> None | Weapon:
        if self.weapon:
            return self.weapon
        else:
            self.weapon = weapon
            self.power += weapon.power

    # apply potion
    def add_potion(self, potion: Potion) -> None:
        for effect_name, value in potion.effects.items():
            if effect_name == "power":
                self.power += value
            if effect_name == "hp":
                self.hp += value
            if effect_name == "protection":
                self.armour += value
