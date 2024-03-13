from .knights.knight_stats import Knight
from .battles.battle import perform_battle

def battle(knights_config):
    knights = {}
    for knight_name, knight_data in knights_config.items():
        knights[knight_name] = Knight(**knight_data)

    battle_result = perform_battle(knights["lancelot"], knights["mordred"])
    battle_result.update(perform_battle(knights["arthur"], knights["red_knight"]))

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
