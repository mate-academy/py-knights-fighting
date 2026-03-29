def set_protection(knight: dict) -> dict:
    knight["protection"] = 0
    for arm in knight["armour"]:
        knight["protection"] += arm["protection"]
    return knight


def add_weapon(knight: dict) -> dict:
    knight["power"] += knight["weapon"]["power"]
    return knight


def set_potion(knight: dict) -> dict:
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
    return knight


def preparations(knights: dict) -> dict:

    knights_dict = {}
    for name, knight in knights.items():
        # Here we prepare all the knights for battle
        set_protection(knight)
        add_weapon(knight)
        knight_for_battle = set_potion(knight)
        knights_dict[name] = knight_for_battle
    return knights_dict
