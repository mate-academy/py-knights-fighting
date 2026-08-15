from typing import Any

from app.battle import fight
from app.knight import Knight


def battle(
    knights_config: dict[str, dict[str, Any]],
) -> dict[str, int]:
    knights = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
