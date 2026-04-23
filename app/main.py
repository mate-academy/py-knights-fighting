from app.Knights.lancelot import lancelot_preparation, knights_lancelot
from app.Knights.arthur import arthur_preparation, knights_arthur
from app.Knights.morder import mordred_preparation, knights_mordred
from app.Knights.red_knight import red_knights_preparation, knights_red


def battle(knights_config: dict) -> dict:
    lancelot = lancelot_preparation(knights_config)
    arthur = arthur_preparation(knights_config)
    red_knight = red_knights_preparation(knights_config)
    mordred = mordred_preparation(knights_config)
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


knights_config = {
    "lancelot": knights_lancelot["lancelot"],
    "arthur": knights_arthur["arthur"],
    "red_knight": knights_red["red_knight"],
    "mordred": knights_mordred["mordred"]
}

print(battle(knights_config))
