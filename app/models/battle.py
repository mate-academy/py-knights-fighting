from __future__ import annotations


class Battle:
    def __init__(self, knight1: "Knight", knight2: "Knight"):
        self.knight1 = knight1
        self.knight2 = knight2

    def calculate_battle_result(self) -> dict:
        self.knight1.calculate_battle_stats()
        self.knight2.calculate_battle_stats()

        self.knight1.hp -= self.knight2.power - self.knight1.protection
        self.knight2.hp -= self.knight1.power - self.knight2.protection

        if self.knight1.hp <= 0:
            self.knight1.hp = 0
        if self.knight2.hp <= 0:
            self.knight2.hp = 0

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
