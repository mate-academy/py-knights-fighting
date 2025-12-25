from __future__ import annotations
from app.inventory.armour import Armour
from app.inventory.weapon import Weapon
from app.inventory.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list[Armour], weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.protection = 0
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection += sum([armor.protection for armor in self.armour])

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if "power" in self.potion.effects:
                self.power += self.potion.effects["power"]
            if "protection" in self.potion.effects:
                self.protection += self.potion.effects["protection"]

            if "hp" in self.potion.effects:
                self.hp += self.potion.effects["hp"]

    def equip(self) -> Knight:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.hp = max(self.hp, 0)
        other.hp = max(other.hp, 0)
