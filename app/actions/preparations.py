def prepare(character: dict) -> None:

    character["protection"] = 0
    for am in character["armour"]:
        character["protection"] += am["protection"]

    # apply weapon
    character["power"] += character["weapon"]["power"]

    # apply potion if exist
    if character["potion"] is not None:
        if "power" in character["potion"]["effect"]:
            character["power"] += character["potion"]["effect"]["power"]

        if "protection" in character["potion"]["effect"]:
            character["protection"] \
                += character["potion"]["effect"]["protection"]

        if "hp" in character["potion"]["effect"]:
            character["hp"] += character["potion"]["effect"]["hp"]
