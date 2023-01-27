from __future__ import annotations


class Knight:

    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        for item in armour:
            self.protection += item["protection"]

        self.power += weapon["power"]

        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

    def duel(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
