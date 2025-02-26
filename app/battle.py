from app.litsar import calculate_stats


def battle(knights: dict) -> dict:
    stats = {}
    for key, knight in knights.items():
        stats[key] = calculate_stats(knight)

    stats["lancelot"]["hp"] -= (
        stats["mordred"]["power"] - stats["lancelot"]["protection"]
    )
    stats["mordred"]["hp"] -= (
        stats["lancelot"]["power"] - stats["mordred"]["protection"]
    )

    if stats["lancelot"]["hp"] < 0:
        stats["lancelot"]["hp"] = 0
    if stats["mordred"]["hp"] < 0:
        stats["mordred"]["hp"] = 0

    stats["arthur"]["hp"] -= (
        stats["red_knight"]["power"] - stats["arthur"]["protection"]
    )
    stats["red_knight"]["hp"] -= (
        stats["arthur"]["power"] - stats["red_knight"]["protection"]
    )

    if stats["arthur"]["hp"] < 0:
        stats["arthur"]["hp"] = 0
    if stats["red_knight"]["hp"] < 0:
        stats["red_knight"]["hp"] = 0

    return {
        stats["lancelot"]["name"]: stats["lancelot"]["hp"],
        stats["arthur"]["name"]: stats["arthur"]["hp"],
        stats["mordred"]["name"]: stats["mordred"]["hp"],
        stats["red_knight"]["name"]: stats["red_knight"]["hp"],
    }
