from app import battle_preparation


def fight(knights: dict) -> dict:

    battle_preparation.prepare(knights)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight, stats in knights.items():
        if stats["hp"] <= 0:
            stats["hp"] = 0

    return {stats["name"]: stats["hp"] for knight, stats in knights.items()}
