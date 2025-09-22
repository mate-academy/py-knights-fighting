from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


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
    effect: Dict[str, int]


@dataclass(frozen=True)
class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Weapon = field(default=None)
    potion: Optional[Potion] = None


@dataclass
class Stats:
    name: str
    hp: int
    power: int
    protection: int
