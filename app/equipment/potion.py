from __future__ import annotations


class Potion:
    potions: [Potion] = []

    def __init__(self, name: str, effect_power: int = 0,
                 effect_hp: int = 0, effect_protection: int = 0) -> None:
        self.part = name
        self.effect_power = effect_power
        self.effect_hp = effect_hp
        self.effect_protection = effect_protection
        Potion.potions.append(self)
