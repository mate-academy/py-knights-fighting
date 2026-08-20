def prepare_knight(knight: dict) -> dict:
    protection = 0

    for armour_part in knight["armour"]:
        protection += armour_part["protection"]

    knight["protection"] = protection
    knight["power"] += knight["weapon"]["power"]

    potion = knight["potion"]

    if potion is not None:
        for stat, value in potion["effect"].items():
            knight[stat] += value

    return knight
