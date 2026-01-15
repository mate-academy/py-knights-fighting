from __future__ import annotations
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


class Knight:
    knights_dict: dict = {}

    def __init__(self, name: str, power: int = 0, hp: int = 1,
                 armour: [Armour] = None,
                 weapon: Weapon = None,
                 potion: Potion = None
                 ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.hp_total = hp
        self.power_total = power
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        if name and name not in Knight.knights_dict:
            Knight.knights_dict.update({name: self})

    def set_equipment(self) -> None:
        self.protection = 0
        for armour in self.armour:
            if isinstance(armour, Armour):
                self.protection += armour.protection

        self.power_total = self.power
        if self.weapon and isinstance(self.weapon, Weapon):
            self.power_total += self.weapon.power

        self.hp_total = self.hp
        if self.potion and isinstance(self.potion, Potion):
            self.power_total += self.potion.effect_power
            self.hp_total += self.potion.effect_hp
            self.protection += self.potion.effect_protection
