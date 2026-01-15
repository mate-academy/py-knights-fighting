from __future__ import annotations

from app.weapon import Weapon
from app.potions import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def equip_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power
        self.weapon_power = weapon.power
        self.weapon = weapon

    def unequip_weapon(self) -> None:
        self.power -= self.weapon_power
        del self.weapon_power

    def equip_armour(self, armour: dict) -> None:
        if not armour:
            print("No armour to equip")
        else:
            self.armour_protection = 0

            for piece in armour:
                self.protection += piece["protection"]
                self.armour_protection += piece["protection"]

    def unequip_armour(self) -> None:
        if not self.armour_protection:
            print("No armour to unequip")
        else:
            self.protection -= self.armour_protection
            del self.armour_protection

    def drink_potion(self, potion: Potion) -> None:
        self.buff = potion
        for attr in ["hp", "power", "protection"]:
            if hasattr(potion, attr):
                setattr(
                    self, attr, getattr(self, attr) + getattr(potion, attr)
                )

    @classmethod
    def create_knight(cls, info: dict) -> Knight:
        knight = cls(info["name"], info["power"], info["hp"])

        if info["armour"]:
            knight.equip_armour(info["armour"])

        return knight

    @staticmethod
    def duel(first: Knight, second: Knight) -> None:
        first.hp -= second.power - first.protection
        second.hp -= first.power - second.protection

        for knight in (first, second):
            if knight.hp <= 0:
                knight.hp = 0
                print(f"{knight.name} died")
