from __future__ import annotations
from app.config import KNIGHTS
from app.knight.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    return lancelot.fight(mordred) | arthur.fight(red_knight)


print(battle(KNIGHTS))
