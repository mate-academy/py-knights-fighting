from typing import Callable


def battle_vs(knight_1: Callable, knight_2: Callable) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0
