from __future__ import annotations

from typing import Optional


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def create_potion(cls, potion: dict) -> Optional[Potion]:
        if potion is None:
            return None
        return cls(potion["name"], potion["effect"])
