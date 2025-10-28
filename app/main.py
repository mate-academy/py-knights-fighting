import copy

from app.knights.all_knights import KNIGHTS
from app.knights.create_knight import CreateKnight
from app.battle.battle import Battle


def result_battle(knights_obj: dict) -> dict:
    copy_dict_knight = copy.deepcopy(knights_obj)
    updated_knights = CreateKnight(copy_dict_knight)
    updated_knights.stats_knight()
    updated_knights.aply_potion()
    battle = Battle(updated_knights.knights)
    result = battle.start_battle()
    return result


knight = result_battle(KNIGHTS)

battle = result_battle
