from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        self.power += knight["weapon"]["power"]

        if len(knight["armour"]) != 0:
            for one in knight["armour"]:
                self.protection += one["protection"]

        if knight.get("potion") is not None:
            self.power += knight["potion"]["effect"].get("power", 0)
            self.protection += knight["potion"]["effect"].get("protection", 0)
            self.hp += knight["potion"]["effect"].get("hp", 0)

    def battle_knight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
