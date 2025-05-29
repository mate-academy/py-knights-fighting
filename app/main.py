from app.battle.fight import Battle
from app.preparation.prepare import preparation


def battle(knights_config: dict) -> dict:
    prepared = preparation(knights_config)
    battle1 = Battle(prepared["lancelot"], prepared["mordred"])
    battle1.fight()

    battle2 = Battle(prepared["arthur"], prepared["red_knight"])
    battle2.fight()

    return Battle.results
