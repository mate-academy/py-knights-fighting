def change_stats(knight: dict) -> dict:
    protection = 0
    for arm in knight["armour"]:
        protection += arm["protection"]
    power = knight["power"]
    power += knight["weapon"]["power"]
    hp = knight["hp"]
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            power += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            protection += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            hp += knight["potion"]["effect"]["hp"]
    return {"name": knight.get("name"), "power": power,
            "hp": hp, "protection": protection}
