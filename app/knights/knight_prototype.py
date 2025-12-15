from __future__ import annotations
from app.buffs.armour import Armour
from app.buffs.weapon import Weapon
from app.buffs.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            protection: int = 0,
            armour: list[Armour] = None,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.protection = protection
        self.armour = armour
        self.potion = potion

    def apply_armour(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            self.power += self.potion.power
            self.protection += self.potion.protection
            self.hp += self.potion.hp
