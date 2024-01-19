from __future__ import annotations
from app.knights.knight import Knight


class Battle:
    battles_results = {}

    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.knights = [first_knight, second_knight]

    def prepare(self) -> None:
        for knight in self.knights:
            knight.prepare_for_battle()

    def fight(self) -> None:
        self.knights[0].hp -= (self.knights[1].power
                               - self.knights[0].protection)

        self.knights[1].hp -= (self.knights[0].power
                               - self.knights[1].protection)

        for knight in self.knights:
            if knight.hp < 0:
                knight.hp = 0

            Battle.battles_results[knight.name] = knight.hp
