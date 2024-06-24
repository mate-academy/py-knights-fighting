from __future__ import annotations


class Knight:
    def __init__(self, knight_info: dict[list | str | int | dict]) -> None:
        # Basic characteristics
        self.name = knight_info["name"]
        self.power = knight_info["power"] + knight_info["weapon"]["power"]
        self.hp = knight_info["hp"]
        self.protection = 0

        # Applying protection
        if knight_info.get("armour"):
            self.add_protection(knight_info["armour"])

        # Applying potion effects
        if knight_info.get("potion"):
            self.add_potion_effect(knight_info.get("potion"))

    def add_protection(self, all_armor: list[dict]) -> None:
        for armor in all_armor:
            self.protection += armor["protection"]

    def add_potion_effect(self, potion: dict):
        self.hp += potion["effect"].get("hp", 0)
        self.power += potion["effect"].get("power", 0)
        self.protection += potion["effect"].get("protection", 0)

    # Realisation of fight
    def __sub__(self, other: Knight) -> None:
        self.hp = self.hp - (other.power - self.protection)
        if self.hp <= 0:
            self.hp = 0
