from app.battle.fight import Battle
from app.battle.prepare import preparing


def battle(knights_config: dict) -> dict:

    prepared = preparing(knights_config)

    results = {}

    battle1 = Battle(prepared["lancelot"], prepared["mordred"])
    results.update(battle1.fight())

    battle2 = Battle(prepared["arthur"], prepared["red_knight"])
    results.update(battle2.fight())

    return results
