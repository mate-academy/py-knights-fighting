from dataclasses import dataclass


@dataclass
class Effect:
    hp: int = 0
    power: int = 0
    protection: int = 0


@dataclass
class Potion:
    name: str
    effect: Effect
