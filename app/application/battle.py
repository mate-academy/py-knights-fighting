from typing import Dict

from app.combat.duel import duel
from app.application.factory import create_knight


def battle(config: dict) -> Dict[str, int]:
    """
    Orchestrates the entire battle.
    Creates warriors, initiates duels, aggregates and returns the result.
    """

    knights = {
        key: create_knight(knight_config)
        for key, knight_config in config.items()
    }

    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
