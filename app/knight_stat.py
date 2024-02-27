def calculate_knight_stat(knight: dict) -> dict:
    knight["protection"] = 0

    for part in knight["armour"]:
        knight["protection"] += part["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        stat_list = ["power", "hp", "protection"]
        for stat in stat_list:
            if stat in knight["potion"]["effect"]:
                knight[stat] += knight["potion"]["effect"][stat]

    return {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": knight["protection"]
    }
