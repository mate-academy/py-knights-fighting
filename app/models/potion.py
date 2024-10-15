from dataclasses import dataclass
from typing import Dict
import random


@dataclass
class Potion:
    name: str
    base_effect: Dict[str, int]

    def get_effect(self) -> Dict[str, int]:
        """
        Генерує новий ефект напою,
        додаючи випадкову варіацію ±5 до кожного параметра.
        """
        effect = {}
        for key, value in self.base_effect.items():
            variation = random.randint(-5, 5)
            effect[key] = value + variation
        return effect
