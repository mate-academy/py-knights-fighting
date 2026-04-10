from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Stats:
    hp: int
    power: int
    protection: int = 0

    def apply_effects(self, effects: dict[str, int]) -> None:
        self.hp += effects.get("hp", 0)
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)


@dataclass
class Knight:
    name: str
    stats: Stats
    armour_protection: int
    weapon_power: int
    potion_effects: dict[str, int]

    @classmethod
    def from_config(cls, config: dict[str, Any]) -> "Knight":
        potion = config["potion"] or {}

        return cls(
            name=config["name"],
            stats=Stats(
                hp=config["hp"],
                power=config["power"],
            ),
            armour_protection=sum(
                piece["protection"] for piece in config["armour"]
            ),
            weapon_power=config["weapon"]["power"],
            potion_effects=dict(potion.get("effect", {})),
        )

    def prepare_for_battle(self) -> None:
        self.stats.protection = self.armour_protection
        self.stats.power += self.weapon_power
        self.stats.apply_effects(self.potion_effects)
