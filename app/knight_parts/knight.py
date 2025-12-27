from __future__ import annotations

from app.knight_parts.armour import Armour
from app.arsenal.weapon import Weapon
from app.arsenal.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def convert_to_knight(knight: dict) -> Knight:
        return Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=Armour.convert_to_armour(knight["armour"]),
            weapon=Weapon(knight["weapon"]["name"], knight["weapon"]["power"]),
            potion=Potion.convert_to_potion(knight["potion"])
        )

    def prepare_for_battle(self) -> None:
        self.protection = Armour.calculate_protection(self.armour)
        self.power += self.weapon.power
        if self.potion is not None:
            self.hp += self.potion.effect.hp
            self.power += self.potion.effect.power
            self.protection += self.potion.effect.protection

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
