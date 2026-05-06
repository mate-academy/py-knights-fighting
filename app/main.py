def get_knight_stats(knight: dict) -> dict:
    stats = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"] + knight["weapon"]["power"],
        "protection": sum(
            part["protection"] for part in knight["armour"]
        ),
    }

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            stats[stat] += value

    return stats


def fight(first: dict, second: dict) -> None:
    first["hp"] -= second["power"] - first["protection"]
    second["hp"] -= first["power"] - second["protection"]

    first["hp"] = max(first["hp"], 0)
    second["hp"] = max(second["hp"], 0)


def battle(knights_config: dict) -> dict:
    lancelot = get_knight_stats(knights_config["lancelot"])
    arthur = get_knight_stats(knights_config["arthur"])
    mordred = get_knight_stats(knights_config["mordred"])
    red_knight = get_knight_stats(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
