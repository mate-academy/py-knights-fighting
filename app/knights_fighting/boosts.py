from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        self.name = name
        self.effect = effect
