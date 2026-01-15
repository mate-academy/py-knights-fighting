from dataclasses import dataclass
from typing import Dict


@dataclass
class Potion:
    name: str
    effect: Dict[str, int]
