from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def prepare(self, armour: list[dict], weapon: dict, potion: dict) -> None:
        if armour is not None:
            for item in armour:
                self.protection += item["protection"]

        self.power += weapon["power"]

        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
