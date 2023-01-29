from __future__ import annotations


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        for item in armour:
            self.protection += item["protection"]

        self.power += weapon["power"]

        potion_item = ["power", "protection", "hp"]

        if potion is not None:
            for item in potion_item:
                if item in potion["effect"]:
                    setattr(self,
                            item,
                            getattr(self, item) + potion["effect"][item])

    def duel(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.is_fall()
        other.is_fall()

    def is_fall(self) -> None:
        if self.hp <= 0:
            self.hp = 0
