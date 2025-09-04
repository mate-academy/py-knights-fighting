from typing import Dict, Any

from app.participants import KNIGHTS
from app.preparations import prepare_knight


def battle(knights_config: Dict[str, Any]) -> dict:

    # BATTLE PREPARATIONS:
    lancelot = knights_config["lancelot"]
    prepare_knight(lancelot)

    arthur = knights_config["arthur"]
    prepare_knight(arthur)

    mordred = knights_config["mordred"]
    prepare_knight(mordred)

    red_knight = knights_config["red_knight"]
    prepare_knight(red_knight)

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


if __name__ == "__main__":
    print(battle(KNIGHTS))
