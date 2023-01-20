def get_protection(knight: dict) -> int:
    knight_protection = 0
    for arm_elem in knight["armour"]:
        knight_protection += arm_elem["protection"]

    if knight["potion"] is not None:
        if "protection" in knight["potion"]["effect"]:
            knight_protection += knight["potion"]["effect"]["protection"]
    return knight_protection


def get_power(knight: dict) -> int:
    knight_power = knight["power"] + knight["weapon"]["power"]

    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight_power += knight["potion"]["effect"]["power"]
    return knight_power


def get_hp(knight: dict) -> int:
    knight_hp = knight["hp"]

    if knight["potion"] is not None:
        if "hp" in knight["potion"]["effect"]:
            knight_hp += knight["potion"]["effect"]["hp"]
    return knight_hp


def get_name(knight: dict) -> str:
    knight_name = knight["name"]
    return knight_name
