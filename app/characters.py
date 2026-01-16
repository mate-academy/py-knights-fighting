from __future__ import annotations


class Character:

    def __init__(self, name: str, power: int, hp: int) -> Character:
        self.name = name
        self.power = power
        self.hp = hp

    def use_weapon(self, power: int) -> Character:
        self.power += power

    def use_armour(self, armour: list) -> Character:
        if armour is not None:
            for item in armour:
                self.hp += item["protection"]

    def use_potion(self, potion: dict) -> Character:
        if potion is not None:
            for key, value in potion["effect"].items():
                if key == "power":
                    self.power += value
                if key == "protection" or key == "hp":
                    self.hp += value
