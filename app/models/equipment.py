from dataclasses import dataclass
from typing import Dict


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
