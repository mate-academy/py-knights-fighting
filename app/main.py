from typing import Dict, Any

from app.knight import Knight
from app.fight import Battle


def battle(knights_config: Dict[str, Any]) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    Battle(lancelot, mordred).fight()
    Battle(arthur, red_knight).fight()

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
