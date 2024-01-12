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
        for key, value in knight["potion"]["effect"].items():
            knight[key] += value
