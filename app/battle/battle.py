from __future__ import annotations

from app.heroes.knight import Knight


def battle(knights: dict) -> None:
    print(fight(knights[0], knights[2]))
    print(fight(knights[1], knights[3]))


def fight(knight_1: Knight, knight_2: Knight) -> dict:
    knight_1.hp = knight_1.get_hp() - (knight_2.get_power() - knight_1.get_protection())
    knight_2.hp = knight_2.get_hp() - (knight_1.get_power() - knight_2.get_protection())

    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0

    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp
    }
