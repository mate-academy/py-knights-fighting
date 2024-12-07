from app.adapters.arena_config import ArenaConfig
from app.battle.arena import Arena
from app.config_dicts.knights_dicts import KNIGHTS


def battle(knights_config: dict[str, dict]) -> dict[str, int]:

    # pairs of knights who will fight each other
    matchups = [("Lancelot", "Mordred"), ("Arthur", "Red Knight")]

    arena = Arena(ArenaConfig(knights_config, matchups))

    # dictionary {"knight_name": knight_hp}
    fights_results = arena.ready_and_fight_all_pairs()

    return fights_results


print(battle(KNIGHTS))
