from __future__ import annotations
from app.knights.knight_instances import KNIGHTS
from app.battle.battle import (
    battle_preparation,
    battle_between_knights,
    fallen
)
from app.dict_to_class import dict_to_knight


def battle(knights_dict: dict) -> dict:
    knights = [
        dict_to_knight(knights_dict["lancelot"]),
        dict_to_knight(knights_dict["arthur"]),
        dict_to_knight(knights_dict["mordred"]),
        dict_to_knight(knights_dict["red_knight"]),
    ]

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


print(battle(KNIGHTS))
