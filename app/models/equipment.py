from dataclasses import dataclass


@dataclass(frozen=True)
class Armour:
    protection: int


@dataclass(frozen=True)
class Weapon:
    power: int


@dataclass(frozen=True)
class Potion:
    effect: dict[str, int]
