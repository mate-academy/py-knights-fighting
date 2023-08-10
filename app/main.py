from app.knights import KNIGHTS
from app.preparation import preparations


def battle(knights: dict) -> dict:

    knights_dict = {}
    for name, knight in knights.items():
        knight_for_battle = preparations(knight)
        knights_dict[name] = knight_for_battle

    knights_dict["lancelot"]["hp"] -= \
        knights_dict["mordred"]["power"] -\
        knights_dict["lancelot"]["protection"]
    knights_dict["mordred"]["hp"] -= \
        knights_dict["lancelot"]["power"] -\
        knights_dict["mordred"]["protection"]
    knights_dict["arthur"]["hp"] -= \
        knights_dict["red_knight"]["power"] -\
        knights_dict["arthur"]["protection"]
    knights_dict["red_knight"]["hp"] -= \
        knights_dict["arthur"]["power"] -\
        knights_dict["red_knight"]["protection"]

    for knight in knights_dict.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        knights_dict["lancelot"]["name"]: knights_dict["lancelot"]["hp"],
        knights_dict["arthur"]["name"]: knights_dict["arthur"]["hp"],
        knights_dict["mordred"]["name"]: knights_dict["mordred"]["hp"],
        knights_dict["red_knight"]["name"]: knights_dict["red_knight"]["hp"]
    }


print(battle(KNIGHTS))
