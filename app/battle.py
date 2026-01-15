from __future__ import annotations

from app.knight import Knight


class KnightBattle:
    @staticmethod
    def battle(knight_1: Knight, knight_2: Knight) -> None:
        # knight_1 vs knight_2:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

        # check if someone fell in battle
        if knight_1.hp <= 0:
            knight_1.hp = 0

        if knight_2.hp <= 0:
            knight_2.hp = 0
