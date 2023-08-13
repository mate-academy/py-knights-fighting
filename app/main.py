from app.action import fight
from app.knights import KNIGHTS
from app.preparation import preparations


def battle(knights: dict) -> dict:
    # prepare all knights
    knights_dict = preparations(knights)
    # knights are fighting here
    fight(knights_dict["lancelot"], knights_dict["mordred"])
    fight(knights_dict["arthur"], knights_dict["red_knight"])

    return {
        knights_dict["lancelot"]["name"]: knights_dict["lancelot"]["hp"],
        knights_dict["arthur"]["name"]: knights_dict["arthur"]["hp"],
        knights_dict["mordred"]["name"]: knights_dict["mordred"]["hp"],
        knights_dict["red_knight"]["name"]: knights_dict["red_knight"]["hp"]
    }


print(battle(KNIGHTS))
