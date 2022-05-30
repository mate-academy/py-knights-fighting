from app.npc.knights import fighters

lancelot = fighters["lancelot"]
mordred = fighters["mordred"]
arthur = fighters["arthur"]
red_knight = fighters["red_knight"]


def battle(*args):
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return ({lancelot["name"]: lancelot["hp"],
             arthur["name"]: arthur["hp"],
             mordred["name"]: mordred["hp"],
             red_knight["name"]: red_knight["hp"]})
