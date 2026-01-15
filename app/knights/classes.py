from dataclasses import dataclass


@dataclass
class Armour:
    part: str = "Unknown"
    protection: int = 0


@dataclass
class Potion:
    name: str = "Unknown"
    effect_power: int = 0
    effect_hp: int = 0
    effect_protection: int = 0


@dataclass
class Weapon:
    name: str = "Unknown"
    weapon_power: int = 0
