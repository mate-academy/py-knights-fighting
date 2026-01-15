from dataclasses import dataclass


@dataclass
class Armor:
    part: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int
