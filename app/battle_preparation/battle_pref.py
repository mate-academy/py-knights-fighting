def battle_pref(knights: dict) -> dict:
    new_pref_knights = {}

    # loop for knight
    for knight in knights:
        each_kn = knights[knight]

        each_kn["protection"] = 0

        for armour_part in each_kn["armour"]:
            each_kn["protection"] += armour_part["protection"]

        # apply weapon
        each_kn["power"] += each_kn["weapon"]["power"]

        # apply potion if exist
        if each_kn["potion"] is not None:
            if "power" in each_kn["potion"]["effect"]:
                each_kn["power"]\
                    += each_kn["potion"]["effect"]["power"]

            if "protection" in each_kn["potion"]["effect"]:
                each_kn["protection"]\
                    += each_kn["potion"]["effect"]["protection"]

            if "hp" in each_kn["potion"]["effect"]:
                each_kn["hp"]\
                    += each_kn["potion"]["effect"]["hp"]

    # make dict {name: preferences}
    for knight_name in knights:
        new_pref_knights[knight_name] = knights[knight_name]

    return new_pref_knights
