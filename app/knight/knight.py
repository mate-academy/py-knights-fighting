
from __future__ import annotations


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config.get("name")
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0

        self.apply_armour(knight_config["armour"])
        self.apply_weapon(knight_config["weapon"])

        if knight_config["potion"]:
            self.apply_potion(knight_config["potion"])

    def apply_armour(self, armour: list) -> None:
        self.protection += sum([
            armour_part["protection"]
            for armour_part in armour
        ])

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion["effect"].get("power"):
            self.power += potion["effect"]["power"]
        if potion["effect"].get("hp"):
            self.hp += potion["effect"]["hp"]
        if potion["effect"].get("protection"):
            self.protection += potion["effect"]["protection"]

    def attack(self, other: Knight) -> None:
        damage = self.power - other.protection
        other.hp -= damage
        if other.hp < 0:
            other.hp = 0
