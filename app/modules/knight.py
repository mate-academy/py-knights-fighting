from __future__ import annotations


class Knight:
    def __init__(self, name: str, hp: int, power: int, protection: int) -> None:
        self.name = name
        self.hp = hp
        self.damage = power
        self.protection = protection

    def battle(self, other: Knight):
        self.hp -= other.damage - self.protection
        other.hp -= self.damage - other.protection
        # self.hp = 0 if self.hp <= 0 else self.hp
        # other.hp = 0 if other.hp <= 0 else other.hp
        return {self.name: self.hp, other.name: other.hp}


def create_knight(knights: dict) -> list:
    list_of_knights = []
    for knight in knights.keys():
        stats = knights[knight]
        name = stats["name"]
        power = stats["power"]
        hp = stats["hp"]
        armour = 0
        if len(stats["armour"]) > 0:
            for piece in stats["armour"]:
                armour += piece["protection"]
        weapon = stats["weapon"]["power"]
        if stats["potion"]:
            potion = stats["potion"]["effect"]
            if "hp" in potion.keys():
                hp += potion["hp"]
            if "power" in potion.keys():
                power += potion["power"]
            if "protection" in potion.keys():
                armour += potion["protection"]
        kn = Knight(name, hp, power, armour)
        print(kn.name, kn.hp, kn.damage, kn.protection)
        list_of_knights.append(Knight(name, hp, power, armour))
    return list_of_knights
