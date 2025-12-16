from typing import Dict, Any
from app.resourses import Knight


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    knights: Dict[str, Knight] = {
        name: Knight(data) for name, data in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare()

    knights["lancelot"].fight(knights["mordred"])
    knights["mordred"].fight(knights["lancelot"])

    knights["arthur"].fight(knights["red_knight"])
    knights["red_knight"].fight(knights["arthur"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }