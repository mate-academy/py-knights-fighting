def calculations(characteristics: dict) -> dict:
    power = characteristics["weapon"]["power"]
    hp = 0
    protection = 0
    for armour_set in characteristics["armour"]:
        protection += armour_set["protection"]
    if characteristics["potion"] is not None:
        if "power" in characteristics["potion"]["effect"]:
            power += characteristics["potion"]["effect"]["power"]
        if "hp" in characteristics["potion"]["effect"]:
            hp = characteristics["potion"]["effect"]["hp"]
        if "protection" in characteristics["potion"]["effect"]:
            protection += characteristics["potion"]["effect"]["protection"]
    return {"power": power, "hp": hp, "protection": protection}
