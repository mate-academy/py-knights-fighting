from dataclasses import dataclass


@dataclass
class Potion:
    name: str
    effect: dict


@dataclass
class Armour:
    part: str
    effect: dict


@dataclass
class Weapon:
    name: str
    effect: dict
