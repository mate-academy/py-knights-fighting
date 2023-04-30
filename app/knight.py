from __future__ import annotations


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"].get("power")
        self.hp = knight["hp"]
        self.protection = sum(armour["protection"]
                              for armour in knight["armour"])
        if knight["potion"] is not None:
            self.power += knight["potion"].get("effect").get("power", 0)
            self.hp += knight["potion"].get("effect").get("hp", 0)
            self.protection += knight["potion"].get("effect").\
                get("protection", 0)

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> dict:
        print(f"{knight1.name} has:"
              f" {knight1.hp}HP,"
              f" {knight1.protection} protection,"
              f" {knight1.power} power")
        print(f"{knight2.name} has:"
              f" {knight2.hp}HP,"
              f" {knight2.protection} protection,"
              f" {knight2.power} power")
        knight1_hit = knight1.power - knight2.protection
        knight2_hit = knight2.power - knight1.protection
        knight2.hp -= knight1_hit
        knight1.hp -= knight2_hit
        print(f"{knight1.name} hit {knight2.name} HP by {knight1_hit} damage")
        print(f"{knight2.name} hit {knight1.name} HP by {knight2_hit} damage")
        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
        return {knight1.name: knight1.hp, knight2.name: knight2.hp}
