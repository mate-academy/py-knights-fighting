from __future__ import annotations


class Potion:
    potions = {}

    def __init__(self, potion: dict | None, owner: str) -> None:
        self.owner = owner
        self.protection = 0
        self.hp = 0
        self.power = 0

        if potion:
            for effect, value in potion["effect"].items():
                setattr(self, effect, value)

        Potion.potions[owner] = self
