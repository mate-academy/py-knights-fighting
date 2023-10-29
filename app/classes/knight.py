from __future__ import annotations

from app.classes.weapon import Weapon
from app.classes.armour import Armour
from app.classes.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list[Armour] = None,
                 potion: Potion = None) -> None:

        self.name = name

        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

        self.total_hp = 0
        self.total_power = 0
        self.total_protection = 0

    def ready_for_battle(self) -> None:
        self.total_hp = self.hp + self.potion.hp
        self.total_power = self.power + self.weapon.power + self.potion.power
        self.total_protection = self.potion.protection
        for armour in self.armour:
            self.total_protection += armour.protection

    def fight(self, opponent: Knight) -> None:
        self.total_hp = max(
            self.total_hp - opponent.total_power + self.total_protection, 0)
