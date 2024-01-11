def prepare_to_battle(knight: dict) -> None:
    knight["protection"] = 0

    # apply armour
    if knight["armour"] is not None:
        for protect in knight["armour"]:
            knight["protection"] += protect["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight[
                "potion"
            ]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
