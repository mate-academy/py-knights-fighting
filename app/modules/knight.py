from __future__ import annotations


class Knight:
    def __init__(
            self, name: str, hp: int, power: int, protection: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.damage = power
        self.protection = protection

    def battle(self, other: Knight) -> dict:
        self.hp -= other.damage - self.protection
        other.hp -= self.damage - other.protection
        self.hp = 0 if self.hp <= 0 else self.hp
        other.hp = 0 if other.hp <= 0 else other.hp
        return {self.name: self.hp, other.name: other.hp}


def create_knight(knights: dict) -> list:
    list_of_knights = []
    for knight_data in knights.keys():
        knight = Knight(
            name=knights[knight_data]["name"],
            hp=knights[knight_data]["hp"],
            power=knights[knight_data]["power"],
            protection=0
        )
        stats = knights[knight_data]
        if len(stats["armour"]) > 0:
            for piece in stats["armour"]:
                knight.protection += piece["protection"]
        knight.damage += stats["weapon"]["power"]
        if stats["potion"]:
            potion = stats["potion"]["effect"]
            if "hp" in potion.keys():
                knight.hp += potion["hp"]
            if "power" in potion.keys():
                knight.damage += potion["power"]
            if "protection" in potion.keys():
                knight.protection += potion["protection"]
        list_of_knights.append(knight)
    return list_of_knights
