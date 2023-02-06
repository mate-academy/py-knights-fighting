from __future__ import annotations
from typing import List

from app.items import Weapon, Armour, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0,
            weapon: Weapon = None,
            armour: List[Armour] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.protection = protection
        self.weapon = weapon

    def armour_up(self, armour: Armour) -> None:
        if not self.armour:
            self.armour = [armour]
        else:
            self.armour.append(armour)

        self.protection += armour.protection

    def weapon_up(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def use_potion(self, potion: Potion) -> None:
        self.hp += potion.hp
        self.power += potion.power
        self.protection += potion.protection

    def strike_enemy(self, enemy: Knight) -> None:
        enemy.hp = max(0, enemy.hp + enemy.protection - self.power)
