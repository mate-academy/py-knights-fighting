# app/main.py
from app.knight import Knight
from app.battle import Battle
from typing import Dict


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    # Create knights
    red_knight = Knight(**knights_config["red_knight"])
    lancelot = Knight(**knights_config.get("lancelot", {}))
    mordred = Knight(**knights_config["mordred"])
    arthur = Knight(**knights_config["arthur"])

    # Create battles
    battle1 = Battle(lancelot, mordred)
    battle2 = Battle(arthur, red_knight)

    # Conduct battles and collect results
    results = {}
    results.update(battle1.conduct())
    results.update(battle2.conduct())

    return results
