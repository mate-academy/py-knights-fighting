from __future__ import annotations
from app.knights.knight_prototype import Knight
from app.knights.knight_instances import lancelot, arthur, mordred, red_knight
from app.battle.battle import (
    battle_preparation,
    battle_between_knights,
    fallen
)


list_of_knights = [lancelot, arthur, mordred, red_knight]


def battle(knights: list[Knight]) -> dict:

    for knight in knights:
        battle_preparation(knight)

    battle_between_knights(knights[0], knights[2])

    battle_between_knights(knights[1], knights[3])

    fallen(knights)

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp
    }


print(battle(list_of_knights))
