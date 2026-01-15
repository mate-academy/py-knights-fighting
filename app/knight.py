from __future__ import annotations
from typing import Union

from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

        self.armour = []
        self.weapon = None
        self.potion = None

        self.attack = self.power
        self.defence = 0

    def add_weapon(self, weapon_stat: dict) -> None:
        weapon = Weapon(
            weapon_stat.get("name"),
            weapon_stat.get("power"),
        )
        self.weapon = weapon
        self.power += weapon.power

    def add_armour(self, armour: Union[list[Armour], Armour]) -> None:
        for part in armour:
            self.armour.append(part.get("part"))
            self.defence += part.get("protection")

    def add_potion(self, potion: dict) -> None:
        if potion:
            name, effect = potion.values()
            self.potion = Potion(name, effect)

    def drink_potion(self) -> None:
        if self.potion:
            for effect in self.potion.effects:
                if effect.attr == "hp":
                    self.hp += effect.power
                elif effect.attr == "power":
                    self.power += effect.power
                elif effect.attr == "protection":
                    self.defence += effect.power

    def fight(self, other: Knight) -> bool:
        if self.defence < other.power:
            other.hp -= self.power - other.defence

            if other.hp <= 0:
                other.hp = 0

        if other.defence < self.power:
            self.hp -= other.power - self.defence

            if self.hp <= 0:
                self.hp = 0

        return self.hp > other.hp

    @staticmethod
    def knights_from_dict(knights: dict) -> list[Knight]:
        list_knights: list[Knight] = []

        for stats in knights.values():
            knight = Knight(
                stats.get("name"),
                stats.get("power"),
                stats.get("hp")
            )
            knight.add_armour(stats.get("armour"))
            knight.add_weapon(stats.get("weapon"))
            knight.add_potion(stats.get("potion"))
            list_knights.append(knight)

        return list_knights
