from __future__ import annotations

from app.classes.class_knights import Knights
from app.battle.preparation import preparation
from app.battle.fight import fight_vs


def battle(knights_config: dict) -> dict:
    knights_instances = []

    for knight in knights_config.values():
        knights_instances.append(Knights(knight))
        preparation(knights_instances[-1], knight)

    lancelot, arthur, mordred, red_knight = (
        fighter for fighter in knights_instances
    )

    fight_vs(lancelot, mordred)
    fight_vs(arthur, red_knight)

    return {knight.name: knight.hp for knight in knights_instances}
