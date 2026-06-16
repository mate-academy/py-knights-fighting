from app.characters.knights import Knight


def parse(config: dict) -> dict:
    result = {}

    for character in config.values():
        power = character["power"]
        hp = character["hp"]
        armour = 0

        if character["armour"]:
            for part in character["armour"]:
                armour += part["protection"]

        if character["weapon"]:
            power += character["weapon"]["power"]

        if character["potion"]:
            if "power" in character["potion"]["effect"]:
                power += character["potion"]["effect"]["power"]

            if "protection" in character["potion"]["effect"]:
                armour += character["potion"]["effect"]["protection"]

            if "hp" in character["potion"]["effect"]:
                hp += character["potion"]["effect"]["hp"]

        name = character["name"]
        knight = Knight(name, power, hp, armour)
        result[name] = knight

    return result
