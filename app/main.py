from typing import Dict
from app.knights import Knight
from app.battle import duel

def battle(config: Dict[str, Dict]) -> Dict[str, int]:
    """Runs predefined battles and returns final HP of all involved knights."""

    knights: Dict[str, Knight] = {
        name: Knight(data) for name, data in config.items()
    }

    matchups = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    results: Dict[str, int] = {}
    for k1, k2 in matchups:
        results.update(duel(knights[k1], knights[k2]))

    return results
