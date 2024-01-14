def potion_check(potion: dict) -> tuple:
    power = 0
    hp = 0
    protection = 0
    if "power" in potion["effect"]:
        power = potion["effect"]["power"]
    if "hp" in potion["effect"]:
        hp = potion["effect"]["hp"]
    if "protection" in potion["effect"]:
        protection = potion["effect"]["protection"]

    return potion["name"], power, hp, protection
