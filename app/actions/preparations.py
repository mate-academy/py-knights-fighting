def prepare(character: dict) -> None:

    character["protection"] = 0
    for am in character["armour"]:
        character["protection"] += am["protection"]

    # apply weapon
    character["power"] += character["weapon"]["power"]

    # apply potion if exist
    if character["potion"] is not None:
        for key in character["potion"]["effect"]:
            character[key] += character["potion"]["effect"][key]
