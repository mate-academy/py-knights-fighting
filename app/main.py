from typing import Any

from app.models.knight import Knight
from app.services.fight import fight


BATTLE_PAIRS = (
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
)


def battle(
    knights_config: dict[str, dict[str, Any]],
) -> dict[str, int]:
    knights: dict[str, Knight] = {}

    for knight_key, knight_config in knights_config.items():
        knight = Knight.from_config(knight_config)
        knight.prepare_for_battle()
        knights[knight_key] = knight

    for first_knight_key, second_knight_key in BATTLE_PAIRS:
        fight(
            knights[first_knight_key],
            knights[second_knight_key],
        )

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }    
