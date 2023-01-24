from app.knights.knights_config import KNIGHTS
from app.knights.generate_knight import generate_list_of_knights
from app.knights.generate_props_for_knight import knight_ready_for_fight
from app.knights.battle.battle_fight import fighting_function


def battle(knights_config_dict: dict[KNIGHTS]) -> dict:
    fighters = generate_list_of_knights(knights_config_dict)
    knight_ready_for_fight(fighters)
    fighting_function(fighters)

    result_dictionary = dict()
    for item in fighters:
        result_dictionary[fighters[item].name] = KNIGHTS[item]["hp"]
    return result_dictionary
