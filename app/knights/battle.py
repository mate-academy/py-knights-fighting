from __future__ import annotations
from app.knights.battle_preparation import Knight


def fight(knight1: Knight, knight2: Knight) -> tuple[Knight, Knight]:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0
    return knight1, knight2
