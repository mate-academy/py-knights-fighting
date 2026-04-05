from app.knights.knight import Knight
from app.battlefield.battle import fight
from app.armor.ammunition import ammunition


def battle(knightsconfig: dict) -> dict:
    knights_list = []
    for knight_dict in knightsconfig.values():
        knight_stats = ammunition(knight_dict)
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
