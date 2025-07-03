from __future__ import annotations

from app.knights.knight import Knight


def single_battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= (knight2.power - knight1.get_total_protection())
    knight2.hp -= (knight1.power - knight2.get_total_protection())
    check_knight_hp(knight1)
    check_knight_hp(knight2)
    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }


def check_knight_hp(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
