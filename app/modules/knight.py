from __future__ import annotations

from app.modules.armour import Armour
from app.modules.potion import Potion
from app.modules.weapon import Weapon


class Knight:
    knights = {}    # stores all instances of class

    def __init__(self, name: str, power: int, health: int) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.armour = []    # stores all instances of armour after applying
        self.protection = 0     # updates after applying armours and potions
        self.weapon = None
        self.potion = None
        Knight.knights[self.name] = self  # new instance appends to class dict

    def apply_armour(self, features: list) -> None:
        for item in features:
            self.armour.append(Armour(item["part"], item["protection"]))

    def apply_weapon(self, weapon_item: dict) -> None:
        self.weapon = Weapon(weapon_item)

    def apply_potion(self, potion: dict) -> None:
        if not potion:
            return None
        self.potion = Potion(potion["name"], potion["effect"])

    # apply all features if a knight before fight
    @staticmethod
    def apply_features(other: Knight) -> None:
        other.power += other.weapon.damage_power + sum(
            [0 if not other.potion else other.potion.effect["power"]]
        )
        other.health += sum(
            [0 if not other.potion else other.potion.effect["hp"]]
        )
        other.protection = sum(other.armour) + sum(
            [0 if not other.potion else other.potion.effect["protection"]]
        )

    # make battle and update health power
    @staticmethod
    def battle(first: Knight, other: Knight) -> None:
        first.apply_features(first)
        other.apply_features(other)

        first.health = max(0, first.health - other.power + first.protection)
        other.health = max(0, other.health - first.power + other.protection)

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "power": self.power,
            "hp": self.health,
            "armour": self.armour,
            "weapon": self.weapon,
            "potion": self.potion
        }

    def __repr__(self) -> str:
        return str(self.__dict__())
