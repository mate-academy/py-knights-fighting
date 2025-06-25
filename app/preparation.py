def preparation(dictionary_knights: dict) -> list[dict]:
    lancelot = dictionary_knights["lancelot"]
    arthur = dictionary_knights["arthur"]
    mordred = dictionary_knights["mordred"]
    red_knight = dictionary_knights["red_knight"]
    lst_knights = [lancelot, arthur, mordred, red_knight]
    for knight in lst_knights:
        knight["protection"] = 0
        for defend in knight["armour"]:
            knight["protection"] += defend["protection"]
        knight["power"] += knight["weapon"]["power"]
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += (
                    knight)["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
    return lst_knights
