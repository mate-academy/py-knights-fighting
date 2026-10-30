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

    for knight_id, knight_config in knights_config.items():
        knight = Knight.from_config(knight_config)
        knight.prepare_for_battle()
        knights[knight_id] = knight

    for first_knight_id, second_knight_id in BATTLE_PAIRS:
        fight(
            knights[first_knight_id],
            knights[second_knight_id],
        )

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
