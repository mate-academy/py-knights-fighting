def prepare_knights(knights_config: dict) -> dict:

    knights = {}

    for knight in knights_config.values():
        hp = knight["hp"]
        power = knight["power"] + knight["weapon"]["power"]
        protection = 0

        if knight["armour"]:
            protection += sum([arm["protection"] for arm in knight["armour"]])

        if knight["potion"] is not None:
            if "hp" in knight["potion"]["effect"]:
                hp += knight["potion"]["effect"]["hp"]
            if "power" in knight["potion"]["effect"]:
                power += knight["potion"]["effect"]["power"]
            if "protection" in knight["potion"]["effect"]:
                protection += knight["potion"]["effect"]["protection"]

        knights[knight["name"]] = hp, power, protection

    return knights
