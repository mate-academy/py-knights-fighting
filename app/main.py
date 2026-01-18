from app.build_instance.knights import creation_of_knight_instances
from app.actions.fights import all_battles, battle_final_result


KNIGHTS_PAIRS = {
    "lancelot": "mordred",
    "arthur": "red_knight"
}


def battle(knights_config: dict) -> dict:

    knights = creation_of_knight_instances(knights_config)

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_potion()
        knight.apply_weapon()

    all_battles(KNIGHTS_PAIRS, knights)

    return battle_final_result(knights)
