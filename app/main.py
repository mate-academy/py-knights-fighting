from typing import Dict
from .knights.knight import Knight
from .engine.battle import fight


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    knights = {name: Knight(data) for name, data in knights_config.items()}

    battle_result = {}
    battle_result.update(fight(knights["lancelot"], knights["mordred"]))
    battle_result.update(fight(knights["arthur"], knights["red_knight"]))

    return battle_result
