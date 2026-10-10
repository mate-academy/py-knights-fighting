from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ArmourPart:
    part: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class Potion:
    name: str
    effect: Dict[str, int] = field(default_factory=dict)
