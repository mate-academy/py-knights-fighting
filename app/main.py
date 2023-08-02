from app.knights.knights_info import KNIGHTS
from app.knights.knights_stats import warrior


def battle(knights: dict) -> dict:
    results = {}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for first, second in pairs:
        first_stats = warrior(knights[first])
        second_stats = warrior(knights[second])

        first_stats["hp"] -= second_stats["power"] - first_stats["protection"]
        second_stats["hp"] -= first_stats["power"] - second_stats["protection"]

        if first_stats["hp"] <= 0:
            first_stats["hp"] = 0

        if second_stats["hp"] <= 0:
            second_stats["hp"] = 0

        results[first_stats["name"]] = first_stats["hp"]
        results[second_stats["name"]] = second_stats["hp"]

    return results


print(battle(KNIGHTS))
