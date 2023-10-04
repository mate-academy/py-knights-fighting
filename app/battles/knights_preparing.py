def preparing(temp_knight: dict) -> dict:
    # apply armour
    temp_knight["protection"] = sum(
        [armour["protection"] for armour in temp_knight["armour"]]
    )
    # apply weapon, potion if exist
    temp_knight["power"] += temp_knight["weapon"]["power"]
    potion = temp_knight["potion"]
    if potion is not None:
        impact = potion["effect"]
        temp_knight["power"] += impact.get("power", 0)
        temp_knight["protection"] += impact.get("protection", 0)
        temp_knight["hp"] += impact.get("hp", 0)

    return {
        "power": temp_knight["power"],
        "protection": temp_knight["protection"],
        "hp": temp_knight["hp"],
        "name": temp_knight["name"]
    }
