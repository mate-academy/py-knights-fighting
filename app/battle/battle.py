from __future__ import annotations
from app.battle.knight import Knight


class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = {
            name: Knight(**knight)
            for name, knight in knights.items()
        }
        self.pairs = []
        self.pairs_list()

    def pairs_list(self) -> None:
        names = list(self.knights)
        for i in range(0, len(names), 4):
            self.pairs.append([names[i], names[i + 2]])
            self.pairs.append([names[i + 1], names[i + 3]])

    def pairs_fight(self) -> None:
        for pair in self.pairs:
            self.knights[pair[0]].fight(self.knights[pair[1]])
            self.knights[pair[1]].fight(self.knights[pair[0]])
            self.knights[pair[0]].check_hp()
            self.knights[pair[1]].check_hp()

    def result(self) -> dict:
        return {
            knight.name: knight.hp
            for knight in self.knights.values()
        }
