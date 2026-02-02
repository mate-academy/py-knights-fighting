from __future__ import annotations

from app.weapon import Weapon
from app.armour import ArmourPart
from app.potion import Potion


class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.raw_power = power
        self.raw_protection = 0

        self.weapon = None
        self.armour = []
        self.potion = None

    @property
    def power(self) -> int:
        return self.raw_power + self.weapon.power

    @property
    def protection(self) -> int:
        return self.raw_protection + sum(
            part.protection for part in self.armour
        )

    def use_potion(self) -> None:
        if self.potion is None:
            return
        self.hp += self.potion.hp_adj
        self.raw_power += self.potion.power_adj
        self.raw_protection += self.potion.protection_adj

        self.potion = None

    def fight(self, other_knight: Knight) -> None:
        self.use_potion()
        other_knight.use_potion()

        self.hp -= other_knight.power - self.protection
        if self.hp < 0:
            self.hp = 0
        other_knight.hp -= self.power - other_knight.protection
        if other_knight.hp < 0:
            other_knight.hp = 0

    @classmethod
    def from_dict(cls, dct: dict) -> Knight:
        knight = cls(dct["name"], dct["hp"], dct["power"])
        weapon_dict = dct["weapon"]
        knight.weapon = Weapon(weapon_dict["name"], weapon_dict["power"])
        knight.armour = [
            ArmourPart(part["part"], part["protection"])
            for part in dct["armour"]
        ]
        potion_dict = dct["potion"]
        knight.potion = Potion.from_dict(potion_dict) if potion_dict else None

        return knight
