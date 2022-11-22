def battle_pref(knights: dict) -> dict:
    new_pref_knights = {}

    # loop for knight
    for knight in knights:
        knight_in_dict = knights[knight]

        knight_in_dict["protection"] = 0

        for armour_part in knight_in_dict["armour"]:
            knight_in_dict["protection"] += armour_part["protection"]

        # apply weapon
        knight_in_dict["power"] += knight_in_dict["weapon"]["power"]

        # apply potion if exist
        if knight_in_dict["potion"] is not None:
            potion_eff = knight_in_dict["potion"]["effect"]

            if "power" in potion_eff:
                knight_in_dict["power"] += potion_eff["power"]

            if "protection" in potion_eff:
                knight_in_dict["protection"] += potion_eff["protection"]

            if "hp" in potion_eff:
                knight_in_dict["hp"] += potion_eff["hp"]

    for knight_name in knights:
        new_pref_knights[knight_name] = knights[knight_name]

    return new_pref_knights
