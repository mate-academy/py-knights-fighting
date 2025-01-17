from app.main.stats import calculate_stats
from app.main.fight import fight


def battle(knights: dict) -> dict:
    for knight_name in knights:
        calculate_stats(knights[knight_name])

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight["name"]: knight["hp"] for knight in knights.values()}
