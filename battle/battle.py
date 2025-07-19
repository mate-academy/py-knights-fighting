from battle.knight import Knight


def create_knight(knight: dict) -> dict:
    knight = Knight(**knight)
    return knight.calculate_total_power()


def battle(knights: dict) -> dict:
    lancelot = create_knight(knights["lancelot"])
    arthur = create_knight(knights["arthur"])
    mordred = create_knight(knights["mordred"])
    red_knight = create_knight(knights["red_knight"])

    # 1 Lancelot vs Mordred
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # 2 Arthur vs Red Knight
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in [lancelot, arthur, mordred, red_knight]:
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
