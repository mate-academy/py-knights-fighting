def potion_effect(potion: dict) -> list:
    hp = 0
    protection = 0
    power = 0
    if potion is not None:
        if "power" in potion["effect"]:
            power += potion["effect"]["power"]

        if "protection" in potion["effect"]:
            protection += potion["effect"]["protection"]

        if "hp" in potion["effect"]:
            hp += potion["effect"]["hp"]
    return [hp, protection, power]
