def change_stats(knights: dict) -> dict:
    knights["protection"] = 0
    for arm in knights["armour"]:
        knights["protection"] += arm["protection"]
    knights["power"] += knights["weapon"]["power"]
    if knights["potion"] is not None:
        if "power" in knights["potion"]["effect"]:
            knights["power"] += knights["potion"]["effect"]["power"]
        if "protection" in knights["potion"]["effect"]:
            knights["protection"] += knights["potion"]["effect"]["protection"]
        if "hp" in knights["potion"]["effect"]:
            knights["hp"] += knights["potion"]["effect"]["hp"]
    return knights
