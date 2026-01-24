from __future__ import annotations


class Knight:
    def __init__(
            self,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.power = power
        self.hp = hp
        self.protection = 0
        if armour:
            for arm in armour:
                self.protection += arm["protection"]
        self.power += weapon["power"]
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    def battle_vs(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0
