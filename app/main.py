from __future__ import annotations

from app.data.knights_config import KNIGHTS
from app.classes.class_knights import Knights


def battle(knights_config: dict) -> dict:
    knights_instances = []

    for knight in knights_config.values():
        knights_instances.append(Knights(knight))

    lancelot, arthur, mordred, red_knight = (
        fighter for fighter in knights_instances
    )

    lancelot.fight_vs(mordred)
    arthur.fight_vs(red_knight)

    return {knight.name: knight.hp for knight in knights_instances}


battle(KNIGHTS)
