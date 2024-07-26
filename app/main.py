from app.knights import Knight
from app.battle import Battle
from typing import Dict


def create_knights(config: Dict[str, Dict]) -> Dict[str, Knight]:
    return {key: Knight(**value) for key, value in config.items()}


def battle(config: Dict[str, Dict]) -> Dict[str, int]:
    knights = create_knights(config)
    results = {}

    battle1 = Battle(knights["lancelot"], knights["mordred"])
    result1 = battle1.fight()
    results.update(result1)

    battle2 = Battle(knights["arthur"], knights["red_knight"])
    result2 = battle2.fight()
    results.update(result2)

    return results
