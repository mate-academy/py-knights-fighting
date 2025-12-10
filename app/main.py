from typing import Dict
from .config import KNIGHTS
from .knights.knight import Knight
from .engine.battle import fight


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    first_fight = fight(lancelot, mordred)
    second_fight = fight(arthur, red_knight)

    battle_result = {
        **first_fight, **second_fight
    }
    return battle_result
