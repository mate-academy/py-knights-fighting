from app.equipment.equipments import get_ready
from app.battles.battle import duel, battle_result
from app.knights_change.knights import Knights
from app.knights_change.change import from_dict


def battle(knights_config: dict) -> dict:
    from_dict(knights_config)
    for knight in Knights.all_knights:
        get_ready(Knights.all_knights[knight])
    duel(Knights.all_knights["Lancelot"], Knights.all_knights["Mordred"])
    duel(Knights.all_knights["Arthur"], Knights.all_knights["Red Knight"])
    return battle_result()
