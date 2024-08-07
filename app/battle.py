from typing import Dict, Any
from app.knight import Knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    # Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
