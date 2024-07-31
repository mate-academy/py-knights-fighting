from __future__ import annotations

from app.knights.inventory.weapon import Weapon
from app.knights.inventory.armour import Armour
from app.knights.inventory.consumables import Potion


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.weapon = Weapon(knight["weapon"])
        self.armour = [
            Armour(part["part"], part["protection"])
            for part in knight["armour"]
        ]
        self.potion = Potion.add(knight["potion"])

    def __str__(self) -> None:
        return self.name

    def get_ready(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        if self.potion:
            self.use_potion()

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_armour(self) -> None:
        for item in self.armour:
            self.protection += item.protection

    def use_potion(self) -> None:
        for effect, value in vars(self.potion.effect).items():
            new_value = self.__getattribute__(effect) + value
            self.__setattr__(effect, new_value)

    def strike(self, other: Knight) -> None:
        other.hp -= self.power - other.protection
