def knight_stat(knight: dict) -> tuple:
    hp = 0
    power = 0
    hp += knight["hp"]
    power += knight["power"] + knight["weapon"]["power"]
    for armour in knight["armour"]:
        hp += armour["protection"]
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            power += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            hp += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            hp += knight["potion"]["effect"]["hp"]
    return (hp, power)
