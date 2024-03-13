from .knights.knight_stats import Knight
from .battles.battle import perform_battle


def battle(knights_config):
    results = {}
    for knight_name, knight_stats in knights_config.items():
        knight = Knight(**knight_stats)
        results[knight_name] = knight.stats["hp"]
    return results
