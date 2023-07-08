from __future__ import annotations
from app.logic.belongings import Armor, Weapon, Potion, Effect


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            health_points: int,
            armour: list[Armor],
            weapon: Weapon,
            potion: list[Potion]
    ) -> None:
        self.name = name
        self.power = power
        self.health_points = health_points
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.dressed_up = []
        self.power += self.weapon.power

    def put_on_armour(self) -> None:
        if self.armour:
            for item in self.armour:
                self.put(item)

    def apply_potions(self) -> None:
        if self.potion:
            for item in self.potion:
                self.apply_effect(item.effect)

    def initialize(self) -> None:
        self.put_on_armour()
        self.apply_potions()

    def battle(
            self,
            rival: Knight
    ) -> None:
        self.health_points -= (rival.power - self.protection)
        rival.health_points -= (self.power - rival.protection)
        if self.health_points < 0:
            self.health_points = 0
        if rival.health_points < 0:
            rival.health_points = 0

    @staticmethod
    def init_armor(
            armor_list: list[dict]
    ) -> list[Armor] | []:
        if armor_list:
            armours = []
            for armour in armor_list:
                armours.append(Armor(armour["part"], armour["protection"]))
            return armours
        return armor_list

    def apply_effect(
            self,
            effect: Effect
    ) -> None:
        self.health_points += effect.health_points
        self.power += effect.power
        self.protection += effect.protection

    def put(
            self,
            armor: Armor
    ) -> None:
        self.protection += armor.protection
        self.dressed_up.append(armor)

    def __str__(self) -> str:
        first_part_ = f"name {self.name}, power {self.power}, "
        second_part = f"hp {self.health_points}, defence {self.protection}"
        return first_part_ + second_part
