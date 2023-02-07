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

    def potion_bonus(self, potion: Potion) -> None:
        if potion.effect.power:
            self.power += self.potion.effect.power
        if potion.effect.protection:
            self.protection += self.potion.effect.protection
        if potion.effect.hp:
            self.hp += self.potion.effect.hp

    def calculate_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour.protection

    def calculate_power(self) -> None:
        self.power += self.weapon.power


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
