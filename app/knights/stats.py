def calculate_knight_stats(curr_knight: dict) -> dict:

    # apply armour
    curr_knight["protection"] = 0
    for part in curr_knight["armour"]:
        curr_knight["protection"] += part["protection"]

    # apply weapon
    curr_knight["power"] += curr_knight["weapon"]["power"]

    # apply potion if exist
    if curr_knight["potion"] is not None:
        stat_list = ["power", "protection", "hp"]
        for stat in stat_list:
            if stat in curr_knight["potion"]["effect"]:
                curr_knight[stat] += curr_knight["potion"]["effect"][stat]

    return {
        "name": curr_knight["name"],
        "hp": curr_knight["hp"],
        "power": curr_knight["power"],
        "protection": curr_knight["protection"]
    }
