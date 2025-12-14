from app.domain.knight import Knight


def create_knight(config: dict) -> Knight:
    """
    Creates a knight based on the configuration.
    Calculates final combat statistics.
    """

    name = config.get("name")
    hp = config.get("hp")
    power = config.get("power")
    protection = 0

    for armor in config["armour"]:
        protection += armor["protection"]

    power += config["weapon"]["power"]

    if config["potion"] is not None:
        if "power" in config["potion"]["effect"]:
            power += config["potion"]["effect"]["power"]

        if "protection" in config["potion"]["effect"]:
            protection += config["potion"]["effect"]["protection"]

        if "hp" in config["potion"]["effect"]:
            hp += config["potion"]["effect"]["hp"]

    knight = Knight(name, hp, power, protection)

    return knight
