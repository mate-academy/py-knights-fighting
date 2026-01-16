from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def add_protection(self, armour_list: list[Armour]) -> None:
        for armour_inst in armour_list:
            self.protection += armour_inst.protection
        Armour.armour_list = []

    def add_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def add_potion(self, potion: Potion) -> None:
        for key, value in potion.effect.items():
            if key == "power":
                self.power += value
            if key == "hp":
                self.hp += value
            if key == "protection":
                self.protection += value


class Armour:
    armour_list = []

    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection
        Armour.armour_list.append(self)


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict | None) -> None:
        self.name = name
        self.effect = effect
