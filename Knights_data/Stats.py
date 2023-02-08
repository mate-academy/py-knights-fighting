from __future__ import annotations


class KnightStats:
    knights = {}
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = self.wearing_armour(armour)
        self.potion = potion
        KnightStats.knights[name] = self

    @staticmethod
    def wearing_armour(armours: list) -> int:
        if armours:
            block = 0
            for armour in armours:
                block += armour["protection"]
            return block
        return 0

    def potion(self) -> None:
        if self.potion:
            if self.potion["effect"]["hp"] is not None:
                self.hp += self.potion["effect"]["hp"]
            if self.potion["effect"]["power"] is not None:
                self.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("protection") is not None:
                self.protection += self.potion["effect"]["protection"]
