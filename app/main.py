from app.action import fight
from app.knights import KNIGHTS
from app.preparation import preparations


def battle(knights: dict) -> dict:
    # prepare all knights
    knights_dict = preparations(knights)
    # knights are fighting here
    fight(knights_dict["lancelot"], knights_dict["mordred"])
    fight(knights_dict["arthur"], knights_dict["red_knight"])
    fight(knights_dict["mordred2"], knights_dict["red_knight2"])

    result_dict = {}
    for knight_prop in knights_dict.values():
        result_dict.update({knight_prop["name"]: knight_prop["hp"]})

    return result_dict


print(battle(KNIGHTS))
