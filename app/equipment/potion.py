from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @staticmethod
    def from_dict(potion: dict) -> Potion:
        if potion:
            return Potion(potion["name"], potion["effect"])
