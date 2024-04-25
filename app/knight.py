from __future__ import annotations

from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def apply_armour(self, part: Armour) -> None:
        self.protection += part.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        potion_power = potion.effect.get("power")
        if potion_power:
            self.power += potion_power

        potion_hp = potion.effect.get("hp")
        if potion_hp:
            self.hp += potion_hp

        potion_protection = potion.effect.get("protection")
        if potion_protection:
            self.protection += potion_protection

    def battle(self, opponent: Knight) -> None:
        opponent.hp -= self.power - opponent.protection
        if opponent.hp < 0:
            opponent.hp = 0

        self.hp -= opponent.power - self.protection
        if self.hp < 0:
            self.hp = 0
