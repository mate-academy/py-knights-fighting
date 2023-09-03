from typing import Dict, Any

from app.Knights.knights_config import KNIGHTS
from app.Knights.knight_class import Knight
from app.Battle import preparation_battle
from app.Battle.great_battle import battle_action_phase, show_result_battle


def battle(knights: Dict[str, Any] = KNIGHTS) -> Dict[str, int]:

    lancelot = Knight(**knights["lancelot"])
    arthur = Knight(**knights["arthur"])
    mordred = Knight(**knights["mordred"])
    red_knight = Knight(**knights["red_knight"])

    knights_names = [lancelot, arthur, mordred, red_knight]

    for knight in knights_names:
        preparation_battle.apply_armour(knight)
        preparation_battle.apply_weapon(knight)
        preparation_battle.apply_potion(knight)

    battle_action_phase(lancelot, mordred)
    battle_action_phase(arthur, red_knight)

    for knight in knights_names:
        show_result_battle(knight)

    return {
        knight.name: knight.hp
        for knight in knights_names
    }


print(battle())
