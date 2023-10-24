def apply_everything(name_of_knight: str, knights_config: dict) -> dict:
    knight = knights_config[name_of_knight].copy()

    # Apply armor
    knight["protection"] = max(
        0, sum(item["protection"] for item in knight["armour"])
    )

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if it exists
    if knight["potion"]:
        potion = knight["potion"]
        effect = potion.get("effect", {})

        if "power" in effect:
            knight["power"] += effect["power"]
        if "protection" in effect:
            knight["protection"] += effect["protection"]
        if "hp" in effect:
            knight["hp"] += effect["hp"]

    return knight
