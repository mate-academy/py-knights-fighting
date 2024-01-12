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
        for key in knight["potion"]["effect"]:
            knight[key] += knight["potion"]["effect"][key]
