def calculate_power(potion: dict, knihgt_power: int) -> int:
    if potion is not None and "power" in potion["effect"]:
        knihgt_power += potion["effect"]["power"]
    return knihgt_power
