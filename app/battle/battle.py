from __future__ import annotations
from app.knights.knight import Knight


class Battle:
    battles_results = {}

    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def prepare(self) -> None:
        self.first_knight.prepare_for_battle()
        self.second_knight.prepare_for_battle()

    def fight(self) -> None:
        self.first_knight.hp -= (self.second_knight.power
                                 - self.first_knight.protection)

        self.second_knight.hp -= (self.first_knight.power
                                  - self.second_knight.protection)

        if self.first_knight.hp < 0:
            self.first_knight.hp = 0

        if self.second_knight.hp < 0:
            self.second_knight.hp = 0

        Battle.battles_results[self.first_knight.name] = self.first_knight.hp
        Battle.battles_results[self.second_knight.name] = self.second_knight.hp
