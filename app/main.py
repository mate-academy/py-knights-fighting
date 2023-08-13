from app.action import fight
from app.knights import KNIGHTS
from app.preparation import preparations
from app.final_health import final_health


def battle(knights: dict) -> dict:

    knights_dict = {}
    for name, knight in knights.items():
        # Here we prepare all the knights for battle
        knight_for_battle = preparations(knight)
        knights_dict[name] = knight_for_battle

    # knights are fighting here
    fight(knights_dict["lancelot"], knights_dict["mordred"])
    fight(knights_dict["arthur"], knights_dict["red_knight"])

    # if life < 0, bring to the correct value
    final_health(knights_dict)

    return {
        knights_dict["lancelot"]["name"]: knights_dict["lancelot"]["hp"],
        knights_dict["arthur"]["name"]: knights_dict["arthur"]["hp"],
        knights_dict["mordred"]["name"]: knights_dict["mordred"]["hp"],
        knights_dict["red_knight"]["name"]: knights_dict["red_knight"]["hp"]
    }


print(battle(KNIGHTS))
