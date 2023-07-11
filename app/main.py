from __future__ import annotations

from app.pages.knichts_stats import KNIGHTS
from app.pages.class_knight import Knight


def battle(knights_config: dict) -> dict:

    res = dict()

    for key, value in knights_config.items():
        res.update({key: Knight(knights_config[key])})

    res["lancelot"].fighting(res["mordred"])
    res["arthur"].fighting(res["red_knight"])

    return {
        val.name: val.hp
        for key, val in res.items()
    }


print(battle(KNIGHTS))
