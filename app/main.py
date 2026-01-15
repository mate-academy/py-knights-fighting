from __future__ import annotations
from app.knight.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_dict(knights_config["lancelot"])
    mordred = Knight.from_dict(knights_config["mordred"])
    arthur = Knight.from_dict(knights_config["arthur"])
    red_knight = Knight.from_dict(knights_config["red_knight"])

    return lancelot.fight(mordred) | arthur.fight(red_knight)
