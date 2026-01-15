from __future__ import annotations


class Knight:

    knights_for_battle = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = [],
                 weapon: dict = {},
                 potion: dict = {}) -> None:
        self.name = name.title()
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knight.knights_for_battle[self.name] = self

    def wear_armour(self) -> None:
        self.protection = 0
        if self.armour is not None:
            for item in self.armour:
                self.protection += item["protection"]

    def take_weapon(self) -> None:
        self.power += self.weapon["power"]

    def drink_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def prep_for_battle(self) -> Knight:
        self.wear_armour()
        self.take_weapon()
        self.drink_potion()
        return self
