from __future__ import annotations
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.aplay_armour()
        self.aplay_weapon()
        self.aplay_potion()

    def aplay_armour(self) -> None:
        self.protection = sum(part.protection for part in self.armour)

    def aplay_weapon(self) -> None:
        self.power += self.weapon.power

    def aplay_potion(self) -> None:
        if self.potion:
            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect["hp"]
            if self.potion.effect.get("power"):
                self.power += self.potion.effect["power"]
            if self.potion.effect.get("protection"):
                self.protection += self.potion.effect["protection"]

    def __sub__(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0
        other.hp -= self.power - other.protection
        if other.hp < 0:
            other.hp = 0
