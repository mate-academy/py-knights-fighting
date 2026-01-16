from typing import Dict, Any

from app.knights.knights_config import KNIGHTS
from app.knights.knight_class import Knight
from app.battle import preparation_functions
from app.battle.battle_functions import perform_fight, show_result_battle


def battle(knights_config: Dict[str, Any] = KNIGHTS) -> Dict[str, int]:

    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        preparation_functions.apply_armour(knight)
        preparation_functions.apply_weapon(knight)
        preparation_functions.apply_potion(knight)

    perform_fight(lancelot, mordred)
    perform_fight(arthur, red_knight)

    for knight in knights:
        show_result_battle(knight)

    return {
        knight.name: knight.hp
        for knight in knights
    }
