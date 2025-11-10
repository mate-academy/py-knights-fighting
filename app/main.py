from __future__ import annotations
from typing import Any, Dict
from app.models import Knight


def battle(knights_data: Dict[str, Any]) -> Dict[str, int]:
    knights = {key: Knight(data) for key, data in knights_data.items()}

    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].attack(knights["mordred"])
    knights["mordred"].attack(knights["lancelot"])

    knights["arthur"].attack(knights["red_knight"])
    knights["red_knight"].attack(knights["arthur"])

    return {
        k.name: k.hp
        for k in knights.values()
    }
