from __future__ import annotations

from app.knight_staff.armour import Armour
from app.knight_staff.potion import Potion
from app.knight_staff.weapon import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[dict] = None,
                 weapon: Weapon = None,
                 potion: Potion = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(part=arm["part"],
                              protection=arm["protection"]) for arm in armour]
        self.weapon = Weapon(name=weapon["name"], power=weapon["power"])
        if potion is not None:
            self.potion = Potion(name=potion["name"], effect=potion["effect"])
        else:
            self.potion = None
        self.protection = 0

        self.apply_weapon()
        self.apply_armor()
        self.apply_potion()

    def apply_armor(self) -> None:
        for arm in self.armour:
            self.protection += arm.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if self.potion.effect.power:
                self.power += self.potion.effect.power
            if self.potion.effect.protection:
                self.protection += self.potion.effect.protection
            if self.potion.effect.hp:
                self.hp += self.potion.effect.hp

    def battle_result(self) -> None:
        if self.hp <= 0:
            self.hp = 0
