from __future__ import annotations

from app.knight_package.armour import Armour
from app.knight_package.weapon import Weapon
from app.knight_package.potion import Potion


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = Armour(knight["armour"])
        self.weapon = Weapon(knight["weapon"])
        self.potion = Potion(knight["potion"])
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection += self.armour.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        self.power += self.potion.get_effect("power")
        self.hp += self.potion.get_effect("hp")
        self.protection += self.potion.get_effect("protection")

    def battle_preparation(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def attack(self, enemy: Knight) -> None:
        enemy.hp -= max(0, self.power - enemy.protection)
        enemy.fell_in_battle()

    def fell_in_battle(self) -> None:
        if self.hp < 0:
            self.hp = 0
