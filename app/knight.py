from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def knight_statistic(
            name: str,
            hp: int,
            power: int,
            armours: list,
            weapon: dict,
            potion: dict | None = None
    ) -> Knight:
        knight_power = power
        knight_power += weapon["power"]
        knight_protection = 0
        if armours:
            for armour in armours:
                knight_protection += armour["protection"]
        knight_hp = hp
        if potion:
            if potion["effect"].get("power"):
                knight_power += potion["effect"]["power"]
            if potion["effect"].get("hp"):
                knight_hp += potion["effect"]["hp"]
            if potion["effect"].get("protection"):
                knight_protection += potion["effect"]["protection"]
        return Knight(name, knight_power, knight_hp, knight_protection)

    @staticmethod
    def new_knight(dictionary: dict) -> Knight:
        knight = Knight.knight_statistic(
            dictionary["name"],
            dictionary["hp"],
            dictionary["power"],
            dictionary["armour"],
            dictionary["weapon"],
            dictionary["potion"])
        return knight

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
