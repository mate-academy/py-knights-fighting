from app.knights.knights_config import KNIGHTS
from app.knights.generate_knight import generate_list_of_knights
from app.knights.generate_props_for_knight import knight_ready_for_fight


def battle(knights_config_dict: dict[KNIGHTS]) -> dict:
    fighters = generate_list_of_knights(knights_config_dict)
    knight_ready_for_fight(fighters)

    fighters["lancelot"].fight(fighters["mordred"])
    fighters["mordred"].fight(fighters["lancelot"])
    fighters["arthur"].fight(fighters["red_knight"])
    fighters["red_knight"].fight(fighters["arthur"])

    fight_result = dict()
    for knight in fighters:
        fight_result[fighters[knight].name] = fighters[knight].hp

    return fight_result
