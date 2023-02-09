from __future__ import annotations
from app.entities.stuff import Weapon, SetArmourScope, Potion


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: SetArmourScope,
                 potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def set_hp_level(self, hp: int) -> None:
        if hp:
            self.hp += hp

    def set_power_level(self, power: int | None) -> None:
        if power:
            self.power += power

    def set_protection_level(self, protection: int | None) -> None:
        if protection:
            self.armour.protection_level += protection

    def battle_preparation(self) -> None:
        if self.potion:
            hp = self.potion.effect.get("hp")
            power = self.potion.effect.get("power")
            protection = self.potion.effect.get("protection")

            self.set_hp_level(hp)
            self.set_power_level(power)
            self.set_protection_level(protection)
        self.set_power_level(self.weapon.power)

    def is_defeated(self) -> None:
        if self.hp < 0:
            self.hp = 0

    def __sub__(self, other: Knight) -> None:
        self.hp -= other.power - self.armour.protection_level
        other.hp -= self.power - other.armour.protection_level
