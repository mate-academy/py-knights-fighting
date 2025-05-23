from typing import Any
from app.knight import Knight


def battle(knights_config: dict[str, dict[str, Any]]) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
