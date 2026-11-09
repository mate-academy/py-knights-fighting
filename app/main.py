"""Application entry points for the knights fighting simulation."""

from typing import Dict, Mapping

from .config import KNIGHTS
from .domain.battle import resolve_duel
from .domain.knight import Knight, KnightConfig

BATTLE_PAIRS = (
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
)


def battle(knights_config: Mapping[str, KnightConfig]) -> Dict[str, int]:
    """Run the configured duels and return each knight's remaining HP."""
    knights = {
        knight_id: Knight.from_config(config)
        for knight_id, config in knights_config.items()
    }

    for first_id, second_id in BATTLE_PAIRS:
        resolve_duel(knights[first_id], knights[second_id])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
