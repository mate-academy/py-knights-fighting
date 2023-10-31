from __future__ import annotations


class Knight:
    dict_knights = {}

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armor: list,
                 weapon: dict,
                 potion: dict | None
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.put_armor(armor)
        self.take_weapon(weapon)
        self.apply_potion(potion)
        Knight.dict_knights[name] = self

    def __sub__(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        self.hp = 0 if self.hp < 0 else self.hp

    def put_armor(self, armour: list) -> None:
        for part in armour:
            self.protection += part["protection"]

    def take_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return
        for perk in potion["effect"]:
            if perk == "power":
                self.power += potion["effect"][perk]
            if perk == "hp":
                self.hp += potion["effect"][perk]
            if perk == "protection":
                self.protection += potion["effect"][perk]
