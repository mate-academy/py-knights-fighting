from __future__ import annotations

from app.gears.armours import Armour
from app.gears.potions import Potion
from app.gears.weapons import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.wear_armour(armour)
        self.take_weapon(weapon)
        self.drink_potion(potion)

    def wear_armour(self, armours: list[Armour]) -> None:
        for armour in armours:
            print(f"{self.name} wore {armour.part}.")
            self.protection += armour.protection

    def take_weapon(self, weapon: Weapon) -> None:
        print(f"{self.name} took {weapon.name}.")
        self.power += weapon.power

    def drink_potion(self, potion: Potion) -> None:
        if not potion:
            return
        print(f"{self.name} drank {potion.name}.")
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]

    def fight_with(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

    def check_hp(self) -> None:
        if self.hp <= 0:
            print(f"{self.name} fell in the battle!")
            self.hp = 0
