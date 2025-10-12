from __future__ import annotations
from typing import Dict

from app.knights.knight import Knight
from app.knights.battle import duel


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    """Return a single dict with HP of all four knights after two duels.

    Order of duels expected by tests:
      1) Arthur vs Red Knight
      2) Lancelot vs Mordred
    """
    lancelot = Knight.from_config(knights_config["lancelot"])
    mordred = Knight.from_config(knights_config["mordred"])
    arthur = Knight.from_config(knights_config["arthur"])
    red = Knight.from_config(knights_config["red_knight"])

    result: Dict[str, int] = {}
    result.update(duel(arthur, red))

    result.update(duel(lancelot, mordred))

    return result
