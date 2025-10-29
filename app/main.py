import copy

from app.knights.create_knight import KnightStatCalculator
from app.battle.battle import Battle


def battle(knights_obj: dict) -> dict:
    copy_dict_knight = copy.deepcopy(knights_obj)
    updated_knights = KnightStatCalculator(copy_dict_knight)
    updated_knights.stats_knight()
    updated_knights.apply_potion()
    battle = Battle(updated_knights.knights)
    result = battle.start_battle()
    return result
