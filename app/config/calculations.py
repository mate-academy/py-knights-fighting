def power(characteristics: dict) -> int:
    weapon = characteristics["weapon"]["power"]
    if characteristics["potion"] is not None:
        if "power" in characteristics["potion"]["effect"]:
            potion = characteristics["potion"]["effect"]["power"]
            return potion + weapon
    return weapon


def hp(characteristics: dict) -> int:
    if characteristics["potion"] is not None:
        if "hp" in characteristics["potion"]["effect"]:
            return characteristics["potion"]["effect"]["hp"]
    return 0


def protection(characteristics: dict) -> int:
    protection = 0
    for a_set in characteristics["armour"]:
        protection += a_set["protection"]
    if characteristics["potion"] is not None:
        if "protection" in characteristics["potion"]["effect"]:
            potion = characteristics["potion"]["effect"]["protection"]
            return potion + protection
    return protection
