from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list = [],
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.weapon = weapon
        self.protection = sum(
            element_of_armour["protection"]
            for element_of_armour
            in armour)
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        if knight1.protection < knight2.power:
            knight1.hp -= knight2.power - knight1.protection
            if knight1.hp < 0:
                knight1.hp = 0
        if knight2.protection < knight1.power:
            knight2.hp -= knight1.power - knight2.protection
            if knight2.hp < 0:
                knight2.hp = 0
