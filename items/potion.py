from __future__ import annotations


class Potion:
    potions = {}

    def __init__(self, potion: dict | None, owner: str) -> None:
        self.owner = owner
        self.protection = 0
        for key, value in potion["effect"].items():
            setattr(self, key, value)

        Potion.potions[owner] = self
