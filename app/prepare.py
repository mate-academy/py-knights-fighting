def prepare_knight_stats(knight: dict) -> dict:
    stats = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": 0,
    }

    stats["power"] += knight["weapon"]["power"]

    if knight.get("armour"):
        for item in knight["armour"]:
            stats["protection"] += item["protection"]

    if knight.get("potion") and knight["potion"] is not None:
        for key, value in knight["potion"]["effect"].items():
            stats[key] += value

    return stats
