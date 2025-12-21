from typing import Any

from app.services.create_knights import create_knights
from app.services.duel import duel


def battle(knights_config: dict[str, dict[str, Any]]) -> dict:
    knights = create_knights(knights_config)

    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.current_hp for knight in knights.values()}
