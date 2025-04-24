from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def armour_prot(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def weapon_apply(self) -> None:
        self.power += self.weapon["power"]

    def potion_exist(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def battle(self, other: Knight) -> None:
        damage = max(0, other.power - self.protection)
        if damage > 0:
            self.hp -= damage

    def check_feel(self) -> None:
        if self.hp <= 0:
            self.hp = 0
