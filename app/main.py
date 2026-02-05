from typing import Dict

from app.models.knight import Knight
from app.battle.engine import fight


def battle(knights_config: Dict) -> Dict[str, int]:
    knights: Dict[str, Knight] = {
        key: Knight(config)
        for key, config in knights_config.items()
    }

    # predefined battles
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
