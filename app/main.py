from __future__ import annotations
from typing import Dict
from app.knights.knight import Knight
from app.knights.battle import duel


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    """Return HP of all four knights after two duels.

    Duel order required by the tests:
      1) Arthur vs Red Knight
      2) Lancelot vs Mordred
    """
    keys = ["arthur", "red_knight", "lancelot", "mordred"]
    knights = {key: Knight.from_config(knights_config[key]) for key in keys}

    duels = [("arthur", "red_knight"), ("lancelot", "mordred")]

    result: Dict[str, int] = {}
    for left, right in duels:
        result.update(duel(knights[left], knights[right]))

    return result
