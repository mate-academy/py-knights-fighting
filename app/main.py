from typing import Dict
from app.knight import Knight


def _fight(k1: Knight, k2: Knight) -> None:
    k1.take_damage(k2.power)
    k2.take_damage(k1.power)


def battle(knights_config: Dict) -> Dict[str, int]:
    knights: dict[str, Knight] = {}

    for key, data in knights_config.items():
        knights[key] = Knight(data)

    _fight(knights["lancelot"], knights["mordred"])
    _fight(knights["arthur"], knights["red_knight"])

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }
