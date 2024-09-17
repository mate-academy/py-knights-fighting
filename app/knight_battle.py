from __future__ import annotations


class KnightBattle:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def knights_protection(self, armours: list[dict]) -> None:
        if not armours:
            self.protection = 0
        for armour in armours:
            self.protection += armour["protection"]

    def knights_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def potion_effects(self, potion: dict) -> None:
        if potion:
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    def battle(
            self,
            opponent_knight: KnightBattle
    ) -> None:
        self.hp -= (opponent_knight.power - self.protection)
        opponent_knight.hp -= (self.power - opponent_knight.protection)
        KnightBattle.is_defeated(self)
        KnightBattle.is_defeated(opponent_knight)

    @staticmethod
    def is_defeated(knight: KnightBattle) -> None:
        if knight.hp <= 0:
            knight.hp = 0
