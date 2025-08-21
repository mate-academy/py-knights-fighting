from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Armour:
    part: str
    protection: int


@dataclass(frozen=True)
class Weapon:
    name: str
    power: int


@dataclass(frozen=True)
class Potion:
    name: str
    hp: int = 0
    power: int = 0
    protection: int = 0


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Optional[Potion] = None

    hp: int = 0
    power: int = 0
    protection: int = 0

    def prepare_for_battle(self) -> None:
        if self.armour:
            self.protection = sum(a.protection for a in self.armour)
        else:
            self.protection = 0

        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp

        if self.potion is not None:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection
