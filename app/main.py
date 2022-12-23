from app.knights_points.lancelot import lencelot_points
from app.knights_points.red_knight import red_knight_points
from app.knights_points.arthur import arthur_points
from app.knights_points.mordred import mordred_points
from app.knights_points.knights import KNIGHTS


def battle(knights: dict) -> dict:
    # lancelot
    lancelot = lencelot_points(knights["lancelot"])
    # arthur
    arthur = arthur_points(knights["arthur"])
    # mordred
    mordred = mordred_points(knights["mordred"])
    # red_knight
    red_knight = red_knight_points(knights["red_knight"])
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


print(battle(KNIGHTS))
