from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def from_dict(cls, potion: dict) -> Potion | None:
        if potion is not None:
            return Potion(potion["name"], potion["effect"])
        return None
