from __future__ import annotations
from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knights:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Potion = None) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = self.base_power
        self.hp = self.base_hp

    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_potion()
        self.apply_weapon()
