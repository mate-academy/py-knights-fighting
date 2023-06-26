from __future__ import annotations
from app.knight import Knight
from app.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    return lancelot.skirmish(mordred) | arthur.skirmish(red_knight)


print(battle(KNIGHTS))
