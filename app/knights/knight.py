from __future__ import annotations


class Knight:
    protection = 0

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def armour_protection(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection

    def check_fell(self) -> None:
        if self.hp <= 0:
            self.hp = 0
