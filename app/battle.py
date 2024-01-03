from __future__ import annotations
from app.create_knights import Knight


class Battle:
    @staticmethod
    def calculate_battle_result(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        if knight_1.hp < 0:
            knight_1.hp = 0
        if knight_2.hp < 0:
            knight_2.hp = 0
