def apply_armour(knight_data: dict) -> dict:
    knight_data["protection"] = 0
    if knight_data["armour"]:
        for armour_dict in knight_data["armour"]:
            knight_data["protection"] += armour_dict["protection"]

    return knight_data


def apply_weapon(knight_data: dict) -> dict:
    knight_data["power"] += knight_data["weapon"]["power"]

    return knight_data


def apply_potion(knight_data: dict) -> dict:
    if knight_data["potion"] is not None:
        knight_stats = ["power", "hp", "protection"]
        for stat in knight_stats:
            if stat in knight_data["potion"]["effect"]:
                knight_data[stat] += knight_data["potion"]["effect"][stat]

    return knight_data
