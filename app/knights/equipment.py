from dataclasses import dataclass


@dataclass
class Armour:
    name: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class Potion:
    name: str
    effect: dict
