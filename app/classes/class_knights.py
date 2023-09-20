from __future__ import annotations


class Knights:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        # preparations for battle
        self.protection_calc(knight["armour"])
        self.weapon_power(knight["weapon"])
        self.drink_potion(knight["potion"])

    def protection_calc(self, armour: list) -> None:
        for part in armour:
            self.protection += part["protection"]

    def weapon_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def drink_potion(self, potion: dict | None) -> None:
        if potion:
            for key, value in potion["effect"].items():
                self.__dict__[key] += value

    def fight_vs(self, other: Knights) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.hp = 0 if self.hp < 0 else self.hp
        other.hp = 0 if other.hp < 0 else other.hp
