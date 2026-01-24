from dataclasses import dataclass
from typing import Dict


@dataclass
class Potion:
    name: str
    effect: Dict[str, int]  # np. {"hp": +10, "power": +5}
