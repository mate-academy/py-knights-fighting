def equipment(knightsconfig: dict) -> dict:
    result = {}
    for hero in knightsconfig:
        character = knightsconfig[hero]
        name = character["name"]
        power = character["power"]
        armour = character["armour"]
        hero_hp = character["hp"]
        armour = 0

        # apply armour
        if character["armour"] is not []:

            for equipment in character["armour"]:
                armour += equipment["protection"]

        # apply weapon
        power += character["weapon"]["power"]

        # apply potion if exist
        if character["potion"] is not None:
            if "power" in character["potion"]["effect"]:
                power += character["potion"]["effect"]["power"]
            if "protection" in character["potion"]["effect"]:
                armour += character["potion"]["effect"]["protection"]
            if "hp" in character["potion"]["effect"]:
                hero_hp += character["potion"]["effect"]["hp"]
        result[hero] = {"name": name, "hp": hero_hp,
                        "armour": armour, "power": power}
    return result
