from app.knight_class import Knight
from app.check_battle import fight
from app.knight_stat import calculate_knight_stat


def battle(knightsconfig: dict) -> dict:
    knights_list = []
    for knight_dict in knightsconfig.values():
        knight_stats = calculate_knight_stat(knight_dict)
        knights_list.append(
            Knight(
                name=knight_stats["name"],
                power=knight_stats["power"],
                hp=knight_stats["hp"],
                protection=knight_stats["protection"]
            )
        )
    fight(knights_list[0], knights_list[2])
    fight(knights_list[1], knights_list[3])
    battle_result = {
        knight.name: knight.hp
        for knight in knights_list
    }
    return battle_result
