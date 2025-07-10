from typing import Dict, Any

from game.knight import Knight


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.prepare_for_battle()

    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
