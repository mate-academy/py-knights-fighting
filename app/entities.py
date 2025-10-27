# app/entities.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ArmorPiece:
    part: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class Potion:
    name: str
    effect: Dict[str, int]  # например {"hp": +10, "power": -5}


@dataclass
class Knight:

    name: str
    base_hp: int
    base_power: int
    armour: List[ArmorPiece] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None

    def final_stats(self) -> Dict[str, int]:

        hp = self.base_hp
        power = self.base_power
        protection = 0

        for piece in self.armour:
            protection += piece.protection

        if self.weapon:
            power += self.weapon.power

        if self.potion:
            for stat, delta in self.potion.effect.items():
                if stat == "hp":
                    hp += delta
                elif stat == "power":
                    power += delta
                elif stat == "protection":
                    protection += delta

        return {
            "hp": hp,
            "power": power,
            "protection": protection,
        }
