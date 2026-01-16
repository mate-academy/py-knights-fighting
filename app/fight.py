from app import battle_preparation


def fight(knights: dict) -> dict:

    battle_preparation.prepare(knights)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    pairs = [[lancelot, mordred],
             [mordred, lancelot],
             [arthur, red_knight],
             [red_knight, arthur]]

    for fighter1, fighter2 in pairs:
        fighter1["hp"] -= fighter2["power"] - fighter1["protection"]

    for knight, stats in knights.items():
        if stats["hp"] <= 0:
            stats["hp"] = 0

    return {stats["name"]: stats["hp"] for knight, stats in knights.items()}
