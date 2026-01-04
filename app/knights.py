from __future__ import annotations


class KNIGHT:

    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            armor: list = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = 0
        if potion:
            self.power += potion["effect"].get("power", 0)
            self.hp += potion["effect"].get("hp", 0)
            self.protection += potion["effect"].get("protection", 0)
        if armor:
            for part in armor:
                self.protection += part["protection"]

    def fight(self, other: KNIGHT) -> None:
        if other.power > self.protection:
            self.hp -= other.power - self.protection
            if self.hp < 0:
                self.hp = 0
