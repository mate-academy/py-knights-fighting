from __future__ import annotations
from app.knight_class import Knight
from app.check_battle import fight
from app.knight_stat import calculate_knight_stats


def battle(knights_config: dict) -> dict:
    knights_list = []
    for knight_dict in knights_config.values():
        knight_stats = calculate_knight_stats(knight_dict)
        knights_list.append(Knight(name=knight_stats["name"],
                                   hp=knight_stats["hp"],
                                   power=knight_stats["power"],
                                   protection=knight_stats["protection"]))

    fight(knights_list[0], knights_list[2])
    fight(knights_list[1], knights_list[3])
    battle_results = {
        knight.name: knight.hp
        for knight in knights_list
    }
    return battle_results
