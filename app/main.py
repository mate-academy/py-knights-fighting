from app.divison.initiation import init
from app.divison.configs import KNIGHTS


def battle(knight : dict) -> dict:
    knight = init(knight)

    lancelot = knight["lancelot"]
    arthur = knight["arthur"]
    mordred = knight["mordred"]
    red_knight = knight["red_knight"]

    # 1 Lancelot vs Mordred
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


result = battle(KNIGHTS)
print(result)
