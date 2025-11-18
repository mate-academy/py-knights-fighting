from __future__ import annotations
from accessories.armour import ArmourPiece
from accessories.potion import Potion
from accessories.weapon import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armor: list, weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion

    def battle_preparation(self):
        self.protection = 0
        for piece in self.armor:
            self.protection += piece.protection

        self.power += self.weapon.power

        if self.potion is not None:
            effects = self.potion.effects
            if "power" in effects:
                self.power += effects["power"]

            if "protection" in effects:
                self.protection += effects["protection"]

            if "hp" in effects:
                self.hp += effects["hp"]

    def attack(self, target: Knight):
        damage = self.power - target.protection
        if damage > 0:
            target.hp -= damage

        if target.hp <= 0:
            target.hp = 0
