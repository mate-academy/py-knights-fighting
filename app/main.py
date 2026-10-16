from typing import Dict, Any
from app.knight import Knight
from app.battle import simulate_single_battle


def battle(
    knights_config: Dict[str, Dict[str, Any]]
) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    simulate_single_battle(lancelot, mordred)
    simulate_single_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
