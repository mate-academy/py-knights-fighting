from __future__ import annotations

from app.pages.knichts_stats import KNIGHTS
from app.pages.class_knight import Knight


def battle(knights_config: dict) -> dict:

    for key, value in knights_config.items():
        Knight(knights_config[key])

    Knight.dic.get("Lancelot").fighting(Knight.dic.get("Mordred"))
    Knight.dic.get("Arthur").fighting(Knight.dic.get("Red Knight"))

    return {
        value.name: value.hp
        for key, value in Knight.dic.items()
    }


print(battle(KNIGHTS))
