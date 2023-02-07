from app.buttle.start import start_fight
from app.buttle.knights_data import KNIGHTS
from app.buttle.preparation_functions import list_of_knights_to_dict,\
    list_of_knight_instances_from_dict


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_instances = list_of_knight_instances_from_dict(knights_config)
    # BATTLE:
    # 1 Lancelot vs Mordred:
    start_fight([knights_instances[0], knights_instances[2]])
    # 2 Arthur vs Red Knight:
    start_fight([knights_instances[1], knights_instances[3]])
    return list_of_knights_to_dict(knights_instances)


print(battle(KNIGHTS))
