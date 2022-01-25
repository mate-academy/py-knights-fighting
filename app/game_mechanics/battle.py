# from app.game_mechanics.dice import modifying
# from app.game_mechanics.dice import rolling
from app.npc.knights import fighters

lancelot = fighters["lancelot"]
mordred = fighters["mordred"]
arthur = fighters["arthur"]
red_knight = fighters["red_knight"]


def battle(*args):
    # 1 Lancelot vs Mordred:

    # lancelot["power"] = modifying(rolling(), lancelot["power"])
    # mordred["power"] = modifying(rolling(), mordred["power"])

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:

    # arthur["power"] = modifying(rolling(), arthur["power"])
    # red_knight["power"] = modifying(rolling(), red_knight["power"])

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return ({lancelot["name"]: lancelot["hp"],
             arthur["name"]: arthur["hp"],
             mordred["name"]: mordred["hp"],
             red_knight["name"]: red_knight["hp"]})
