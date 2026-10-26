from collections.abc import Mapping
from typing import Any

from app.battle import fight
from app.knight import prepare_knight


def battle(knights_config: Mapping[str, Any]) -> dict[str, int]:
    prepared_knights = {
        knight_id: prepare_knight(knight_config)
        for knight_id, knight_config in knights_config.items()
    }

    scheduled_fights = (("lancelot", "mordred"), ("arthur", "red_knight"))
    for first_id, second_id in scheduled_fights:
        fight(prepared_knights[first_id], prepared_knights[second_id])

    return {
        knight["name"]: knight["hp"]
        for knight in prepared_knights.values()
    }
