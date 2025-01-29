from __future__ import annotations
from app.knights.preparations import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def damages(self) -> None:
        self.first_knight.hp -= \
            self.second_knight.power - self.first_knight.protection
        self.second_knight.hp -= \
            self.first_knight.power - self.second_knight.protection

    def winner(self) -> None:
        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0
            print("The first knight was defeated")
        if self.second_knight.hp <= 0:
            self.second_knight.hp = 0
            print("The second knight was defeated")
        if self.first_knight == 0 and self.second_knight == 0:
            print("It is a draw")

    def fight(self) -> None:
        self.damages()
        self.winner()
