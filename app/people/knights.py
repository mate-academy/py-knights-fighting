from __future__ import annotations
from app.ammunition.armours import Armour
from app.ammunition.potions import Potion
from app.ammunition.weapons import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = 0,
            weapon: dict = None,
            potion: dict = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection: int = 0

    # apply armour
    def wear_armour(self, armour: list[Armour]) -> None:
        for item in armour:
            self.protection += item.protection

    # apply weapon
    def take_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    # apply potion
    def drink_potion(self, potion: Potion) -> None:
        if potion:
            for effect_name, value in potion.effects.items():
                if effect_name == "power":
                    self.power += value
                if effect_name == "hp":
                    self.hp += value
                if effect_name == "protection":
                    self.protection += value

    # prepare to battle
    def preparation(self) -> None:
        self.wear_armour([Armour(armour.get("part"),
                                 armour.get("protection"))
                          for armour in self.armour])

        self.take_weapon(Weapon(self.weapon.get("name"),
                                self.weapon.get("power")))

        if self.potion:
            self.drink_potion(Potion(self.potion.get("name"),
                                     self.potion.get("effect")))

    # hit other knight
    def hit(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
