from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def create_potion(cls, potion: dict) -> Potion | None:
        if potion:
            return cls(potion["name"], potion["effect"])
        return
