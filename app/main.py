from app.knights import knights
from app.preparation import preparation


@preparation
def battle(members: dict) -> dict:

    # 1 Lancelot vs Mordred:
    members["lancelot"]["hp"] -= (
        members["mordred"]["power"] - members["lancelot"]["protection"]
    )
    members["mordred"]["hp"] -= (
        members["lancelot"]["power"] - members["mordred"]["protection"]
    )

    # 2 Arthur vs Red Knight:
    members["arthur"]["hp"] -= (
        members["red_knight"]["power"] - members["arthur"]["protection"]
    )
    members["red_knight"]["hp"] -= (
        members["arthur"]["power"] - members["red_knight"]["protection"]
    )

    # check if someone fell in battle
    for knight, attributes in members.items():
        if attributes["hp"] <= 0:
            attributes["hp"] = 0

    # Return battle results:
    return {attributes["name"]: attributes["hp"]
            for _, attributes in members.items()}


print(battle(knights))
