def battle_preparation(config: dict) -> tuple:
    name = config["name"]
    hp = config["hp"]

    # apply weapon
    power = config["power"] + config["weapon"]["power"]

    # apply armour
    protection = 0
    for i in config["armour"]:
        protection += i["protection"]

    # apply potion if exist
    if config["potion"] is not None:
        effect = config["potion"]["effect"]

        if "power" in effect:
            power += effect["power"]

        if "protection" in effect:
            protection += effect["protection"]

        if "hp" in effect:
            hp += effect["hp"]

    return name, hp, power, protection
