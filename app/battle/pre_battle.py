def battle(knights_one: dict) -> dict:
    # BATTLE PREPARATIONS:
    for knight in knights_one:
        knight = knights_one[knight]

    # apply armour
        knight["protection"] = 0

        for armour_in in knight["armour"]:
            knight["protection"] += armour_in["protection"]

        # apply weapon
        knight["power"] += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"]:
            for strength in knight["potion"]["effect"]:
                knight[strength] += knight["potion"]["effect"][strength]

    lancelot = knights_one["lancelot"]
    mordred = knights_one["mordred"]
    arthur = knights_one["arthur"]
    red_knight = knights_one["red_knight"]

    lancelot["hp"] -= mordred["power"] - knights_one["lancelot"]["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # dict of result
    result_dict = {}

    # check if someone fell in battle
    for knight in knights_one:
        if knights_one[knight]["hp"] <= 0:
            knights_one[knight]["hp"] = 0
        result_dict[knights_one[knight]["name"]] = knights_one[knight]["hp"]

    # Return battle results:
    return result_dict
