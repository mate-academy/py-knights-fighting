from typing import Dict
import copy

from .knights.battle import prepare_knights, duel


def base_knights_config() -> Dict[str, Dict]:
    return copy.deepcopy(base_knights_config())


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """Run battles and return final hp of all knights."""
    knights = prepare_knights(knights_config)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    # DRY – zamiast ręcznie składać słownik, robimy dict comprehension
    return {knight.name: knight.hp for knight in knights.values()}
