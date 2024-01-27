from __future__ import annotations
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.power = power + self.weapon.power
        self.potion = potion
        self.protection = sum(part.protection for part in self.armour)
        self.aplay_potion()

    def aplay_potion(self) -> None:
        if self.potion:
            for potion_stat, potion_effect in self.potion.effect.items():
                setattr(self, potion_stat,
                        getattr(self, potion_stat) + potion_effect)

    def __sub__(self, other: Knight) -> None:
        self.hp = 0 if self.hp - (other.power - self.protection) < 0 \
            else self.hp - (other.power - self.protection)
        other.hp = 0 if other.hp - (self.power - other.protection) < 0 \
            else other.hp - (self.power - other.protection)
