from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list[Armour] = None, weapon: Weapon = None,
                 potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potion = potion


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Effect:
    def __init__(self, hp: int, power: int, protection: int = None) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect
