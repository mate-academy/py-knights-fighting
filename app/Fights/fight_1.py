from __future__ import annotations

from app.Knights.knights import KnightBasic

# knight_1 = KnightBasic
# knight_2 = KnightBasic


def fight_1(knight_1: KnightBasic, knight_2: KnightBasic) -> None:

    # prepare before battle
    knight_1.battle_preparing()
    knight_2.battle_preparing()

    # battle itself
    knight_1.hp -= (knight_2.power - knight_1.protection)
    knight_2.hp -= (knight_1.power - knight_2.protection)

    # check if someone fell in battle
    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0
