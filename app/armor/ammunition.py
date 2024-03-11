def ammunition(knight: dict) -> dict:
    # Initialize protection to 0
    knight["protection"] = 0

    # Calculate protection based on armour
    for part in knight["armour"]:
        knight["protection"] += part["protection"]

    # Add weapon power to the knight's power
    knight["power"] += knight["weapon"]["power"]

    # Apply potion effects if a potion is present
    if knight["potion"] is not None:
        stat_list = ["power", "hp", "protection"]
        for stat in stat_list:
            if stat in knight["potion"]["effect"]:
                knight[stat] += knight["potion"]["effect"][stat]

    # Return the calculated stats in a dictionary
    return {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": knight["protection"]
    }
