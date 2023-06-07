def calculate_knight_stats(current_knight: dict) -> dict:

    # apply armour
    current_knight["protection"] = 0
    for part in current_knight["armour"]:
        current_knight["protection"] += part["protection"]

    # apply weapon
    current_knight["power"] += current_knight["weapon"]["power"]

    # apply potion if exist
    if current_knight["potion"] is not None:
        stat_list = ["power", "protection", "hp"]
        for stat_unit in stat_list:
            if stat_unit in current_knight["potion"]["effect"]:
                current_knight[stat_unit] += current_knight["potion"]["effect"][stat_unit]

    return {
        "name": current_knight["name"],
        "hp": current_knight["hp"],
        "power": current_knight["power"],
        "protection": current_knight["protection"]
    }
