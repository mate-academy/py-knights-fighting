def battle(
        lancelot: dict,
        arthur: dict,
        mordred: dict,
        red_knight: dict
) -> dict:
    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    knight_hp(lancelot)

    knight_hp(mordred)

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    knight_hp(arthur)

    knight_hp(red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def knight_hp(knight: dict) -> None:
    if knight["hp"] <= 0:
        knight["hp"] = 0
