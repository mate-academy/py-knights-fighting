from typing import Dict


class Potion:
    name: str
    effect: Dict[str, int]  # keys: "hp", "power", "protection"

    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect
