from __future__ import annotations
from app.battle.battle import (
    battle_preparation,
    battle_between_knights,
    fallen
)
from app.dict_to_class import dict_to_knight


def battle(knights_dict: dict) -> dict:
    keys = ["lancelot", "arthur", "mordred", "red_knight"]

    knights = [dict_to_knight(knights_dict[k]) for k in keys]

    for knight in knights:
        battle_preparation(knight)

    pairs = [(0, 2), (1, 3)]
    for first, second in pairs:
        battle_between_knights(knights[first], knights[second])

    fallen(knights)

    return {knight.name: knight.hp for knight in knights}
