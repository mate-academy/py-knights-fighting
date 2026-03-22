from app.change_stats import change_stats
from app.Data import KNIGHTS


def battle(knights: dict) -> dict:
    result = {}
    for name in knights:
        change_stats(knights[name])
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]
    lancelot["hp"] -= (mordred["power"] - lancelot["protection"])
    mordred["hp"] -= (lancelot["power"] - mordred["protection"])
    arthur["hp"] -= (red_knight["power"] - arthur["protection"])
    red_knight["hp"] -= (arthur["power"] - red_knight["protection"])
    warriors = [lancelot, mordred, arthur, red_knight]
    for warrior in warriors:
        if warrior["hp"] < 0:
            warrior["hp"] = 0
        result[warrior["name"]] = warrior["hp"]

    return result


print(battle(KNIGHTS.KNIGHTS))
