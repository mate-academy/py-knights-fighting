from typing import Dict, Any


class Potion:
    def __init__(self, name: str, effect: Dict[str, Any]) -> None:
        self.name = name
        self.effect = effect
