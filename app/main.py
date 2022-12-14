from app.pkg.fighting import fighting
from app.pkg.knight_config import KNIGHTS
from app.pkg.preparations import preparations


def battle(knights: dict) -> dict:
    preparations(knights)

    # 1 Lancelot vs Mordred:

    fighting("lancelot", "mordred", KNIGHTS)

    # knights["lancelot"]["hp"] -= knights["mordred"]["power"] \
    #     - knights["lancelot"]["protection"]
    # knights["mordred"]["hp"] -= knights["lancelot"]["power"] \
    #     - knights["mordred"]["protection"]
    #
    # # check if someone fell in battle
    # knights["lancelot"]["hp"] = check_hp_knight(knights["lancelot"]["hp"])
    # knights["mordred"]["hp"] = check_hp_knight(knights["mordred"]["hp"])

    # 2 Arthur vs Red Knight:

    fighting("arthur", "red_knight", KNIGHTS)

    # knights["arthur"]["hp"] -= knights["red_knight"]["power"] \
    #     - knights["arthur"]["protection"]
    # knights["red_knight"]["hp"] -= knights["arthur"]["power"] \
    #     - knights["red_knight"]["protection"]
    #
    # # check if someone fell in battle
    # knights["arthur"]["hp"] = check_hp_knight(knights["arthur"]["hp"])
    # knights["red_knight"]["hp"] = check_hp_knight(knights["red_knight"]["hp"])
    print(knights)
    # Return battle results:
    return {knights[name]["name"]: knights[name]["hp"] for name in knights}


print(battle(KNIGHTS))
