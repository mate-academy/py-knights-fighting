import app.knight as knight
from app.settings import KNIGHTS


def battle(knights_сonfig: dict) -> dict:
    # PREPARATIONS:

    # lancelot
    lancelot = knights_сonfig["lancelot"]
    # lancelot_obj = knight.Knight(lancelot)
    knight.apply_gear(lancelot)

    # arthur
    arthur = knights_сonfig["arthur"]
    knight.apply_gear(arthur)

    # mordred
    mordred = knights_сonfig["mordred"]
    knight.apply_gear(mordred)

    # red_knight
    red_knight = knights_сonfig["red_knight"]
    knight.apply_gear(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    knight.duel(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    knight.duel(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
