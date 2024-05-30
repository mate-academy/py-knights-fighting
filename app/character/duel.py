from __future__ import annotations
from app.character.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= max(knight2.power - knight1.protection, 0)
    knight2.hp -= max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp, 0)
    knight2.hp = max(knight2.hp, 0)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }
