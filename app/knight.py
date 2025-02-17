from __future__ import annotations
from typing import Dict

from app.potion import Potion
from app.weapon import Weapon
from app.armour import Armour


class Knight:
    knights: Dict[str, Knight] = {}

    def __init__(self, name: str, power: int, hp: int, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

        Knight.knights[name] = self

    def armour(self, armour: Armour) -> None:
        self.protection += armour.protection

    def weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def potion(self, potion: Potion) -> None:
        self.power += potion.power
        self.hp += potion.hp
        self.protection += potion.protection

    def fight(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        self.check_fell()

    def check_fell(self):
        if self.hp <= 0:
            self.hp = 0