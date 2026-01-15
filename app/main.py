from app.knights import prepare_knight


def battle(knights_config: dict) -> dict:
    knights = {name: knight for name, knight in knights_config.items()}

    for knight in knights.values():
        prepare_knight(knight)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knights.values():
        if knight["hp"] < 0:
            knight["hp"] = 0

    return {knight["name"]: knight["hp"] for knight in knights.values()}
