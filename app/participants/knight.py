from __future__ import annotations
from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = []

    def wear_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.protection += armour.protection

    def drink_potion(self, potion: Potion) -> None:
        self.potion.append(potion)
        for prop in potion.effect:
            current_value = getattr(self, prop, 0)
            setattr(self, prop, current_value + potion.effect[prop])

    def get_armed(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def attack(self, enemy: Knight) -> None:
        enemy.hp -= (self.power - enemy.protection)
        if enemy.hp <= 0:
            enemy.hp = 0
