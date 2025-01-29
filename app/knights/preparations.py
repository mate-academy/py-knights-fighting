from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_armour(self, armour: list) -> None:
        if armour:
            for part in armour:
                self.protection += part["protection"]

    def get_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def get_potion(self, potion: None | dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
