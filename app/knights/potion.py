from dataclasses import dataclass
from typing import Dict


@dataclass
class Potion:
    """Класс для представления зелья."""

    name: str
    effect: Dict[str, int]
