from typing import Dict
from app.models.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    lancelot = Knight.from_dict(knights_config["lancelot"])
    arthur = Knight.from_dict(knights_config["arthur"])
    mordred = Knight.from_dict(knights_config["mordred"])
    red_knight = Knight.from_dict(knights_config["red_knight"])

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
