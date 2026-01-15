from typing import Dict
from app.knight import Knight
from app.battle import fight


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    knights: Dict[str, Knight] = {
        key: Knight(**config) for key, config in knights_config.items()
    }

    results: Dict[str, int] = {}
    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for k1, k2 in pairs:
        outcome = fight(knights[k1], knights[k2])
        results.update(outcome)

    return results
