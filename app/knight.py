from __future__ import annotations
from app.accessories.armour import ArmourPiece
from app.accessories.potion import Potion
from app.accessories.weapon import Weapon


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armor: list[ArmourPiece],
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def battle_preparation(self) -> None:
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

    def battle(self, target: Knight) -> None:
        damage = self.power - target.protection
        if damage > 0:
            target.hp -= damage

        if target.hp <= 0:
            target.hp = 0
