def first_battle(lancelot, mordred):
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    return lancelot, mordred


def second_battle(arthur, red_knight):
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return arthur, red_knight
