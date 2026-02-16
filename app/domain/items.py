from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

Stat = Literal["hp", "power", "protection"]


@dataclass(frozen=True, slots=True)
class Weapon:
    name: str
    power: int


@dataclass(frozen=True, slots=True)
class Armour:
    name: str
    strength: int


@dataclass(frozen=True, slots=True)
class Potion:
    name: str
    effect: dict[Stat, int]
