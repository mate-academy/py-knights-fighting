from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class Armour:
    part: str
    protection: int


@dataclass
class Potion:
    name: str
    effect: dict


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    armour: list[Armour]
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None
    protection: int = 0

    @classmethod
    def from_config(cls, config: dict) -> Knight:
        return cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
            armour=[Armour(**a) for a in config.get("armour", [])],
            weapon=Weapon(**config["weapon"]),
            potion=Potion(**config["potion"])
            if config.get("potion") else None,
        )

    def apply_armour(self) -> None:
        self.protection = sum(armour.protection for armour in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return

        for stat, value in self.potion.effect.items():
            setattr(self, stat, getattr(self, stat) + value)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def receive_damage(self, enemy_power: int) -> None:
        damage = max(0, enemy_power - self.protection)
        self.hp = max(0, self.hp - damage)
