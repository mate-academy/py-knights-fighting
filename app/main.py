from typing import Optional, Dict
from app.services.battle import fight
from app.data.knights_config import KNIGHTS


def battle(knights: Optional[Dict] = None) -> Dict[str, int]:
    if knights is None:
        knights = KNIGHTS

    pairs = [
        ("Lancelot", "lancelot", "Mordred", "mordred"),
        ("Arthur", "arthur", "Red Knight", "red_knight"),
    ]

    results: Dict[str, int] = {}

    for name1, key1, name2, key2 in pairs:
        outcome = fight(knights[key1], knights[key2])
        results[name1] = outcome["first"]
        results[name2] = outcome["second"]

    return results
