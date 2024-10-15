from .combat import Combat
from typing import Dict
from app.models.knight import Knight


def battle(knights: Dict[str, Knight]) -> Dict[str, int]:
    # Визначення матчапів
    matchups = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    results = {}

    for k1_key, k2_key in matchups:
        knight1 = knights[k1_key]
        knight2 = knights[k2_key]
        combat = Combat(knight1, knight2)
        combat.engage()
        results.update(combat.get_result())

    return results
