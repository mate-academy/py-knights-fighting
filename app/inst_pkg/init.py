from app.inst_pkg.knights import Knight


def initiation(knight_info: dict) -> Knight:
    power = knight_info["power"] + knight_info["weapon"]["power"]
    hp = knight_info["hp"]
    protection = 0
    if knight_info["potion"] is not None:
        if "power" in knight_info["potion"]["effect"]:
            power += knight_info["potion"]["effect"]["power"]
        if "hp" in knight_info["potion"]["effect"]:
            hp += knight_info["potion"]["effect"]["hp"]
        if "protection" in knight_info["potion"]["effect"]:
            protection += knight_info["potion"]["effect"]["protection"]
    if knight_info["armour"] != []:
        for armour in knight_info["armour"]:
            protection += armour["protection"]
    # print(Knight(knight_info["name"], power, hp, protection))
    return Knight(knight_info["name"], power, hp, protection)
