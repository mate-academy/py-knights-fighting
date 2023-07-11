from __future__ import annotations

from app.pages.knichts_stats import KNIGHTS
from app.pages.class_knight import Knight


def battle(knights_config: dict) -> dict:

    for key, value in knights_config.items():
        Knight(knights_config[key])

    Knight.res["Lancelot"].fighting(Knight.res["Mordred"])
    Knight.res["Arthur"].fighting(Knight.res["Red Knight"])

    return {
        val.name: val.hp
        for key, val in Knight.res.items()
    }


print(battle(KNIGHTS))
