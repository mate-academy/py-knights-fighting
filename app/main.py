from typing import Dict, Any
from classes import Knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    knights = {
        name: Knight(**config) for name, config in knights_config.items()
    }

    knights["lancelot"].receive_damage(knights["mordred"].power)
    knights["mordred"].receive_damage(knights["lancelot"].power)

    knights["arthur"].receive_damage(knights["red_knight"].power)
    knights["red_knight"].receive_damage(knights["arthur"].power)

    results = {knight.name: knight.hp for knight in knights.values()}

    return results
