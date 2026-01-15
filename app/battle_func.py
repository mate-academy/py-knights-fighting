from __future__ import annotations
from app.knight_stats import Knight


def battle_action(opponent_1: Knight, opponent_2: Knight) -> None:
    opponent_1.hp -= opponent_2.power - opponent_1.protection
    opponent_2.hp -= opponent_1.power - opponent_2.protection
    if opponent_1.hp <= 0:
        opponent_1.hp = 0
    if opponent_2.hp <= 0:
        opponent_2.hp = 0
