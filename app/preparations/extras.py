from __future__ import annotations


class Armor:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection
    pass


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
    pass


class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect
