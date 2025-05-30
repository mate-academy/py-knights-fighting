from __future__ import annotations

from app.knights.knight import Knight


class Battle:
    results = {}

    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.k1 = knight1
        self.k2 = knight2

    def fight(self) -> None:
        self.k1.hp -= max(0, self.k2.power - self.k1.protection)
        self.k2.hp -= max(0, self.k1.power - self.k2.protection)

        if self.k1.hp <= 0:
            self.k1.hp = 0

        if self.k2.hp <= 0:
            self.k2.hp = 0

        Battle.results[self.k1.name] = self.k1.hp
        Battle.results[self.k2.name] = self.k2.hp
