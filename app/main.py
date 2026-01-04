from app.preparation import preparation


@preparation
def battle(knights: dict) -> dict:

    # 1 Lancelot vs Mordred:
    knights["lancelot"]["hp"] -= (
        knights["mordred"]["power"]
        - knights["lancelot"]["protection"]
    )
    knights["mordred"]["hp"] -= (
        knights["lancelot"]["power"]
        - knights["mordred"]["protection"]
    )

    # 2 Arthur vs Red Knight:
    knights["arthur"]["hp"] -= (
        knights["red_knight"]["power"]
        - knights["arthur"]["protection"]
    )
    knights["red_knight"]["hp"] -= (
        knights["arthur"]["power"]
        - knights["red_knight"]["protection"]
    )

    # check if someone fell in battle:
    for knight, attributes in knights.items():
        if attributes["hp"] <= 0:
            attributes["hp"] = 0

    # Return battle results:
    return {
        attributes["name"]: attributes["hp"]
        for _, attributes in knights.items()
    }
