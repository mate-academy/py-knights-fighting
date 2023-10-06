from app.Knight_class import creation_of_knight_instances
from app.action import all_battles, battle_final_result


def battle(knights_config: dict) -> dict:

    knights = creation_of_knight_instances(knights_config)

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_potion()
        knight.apply_weapon()

    knights_pairs = {
        "lancelot": "mordred",
        "arthur": "red_knight"
    }

    all_battles(knights_pairs, knights)

    return battle_final_result(knights)
