from __future__ import annotations
from app.Knight import Knight
from app.Knight_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    return lancelot.duel(mordred) | arthur.duel(red_knight)


print(battle(KNIGHTS))
