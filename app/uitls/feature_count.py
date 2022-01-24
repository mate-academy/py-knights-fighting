def feature_count(knightsConfig, knight_2):
    result = knightsConfig[knight_2]
    result["protection"] = sum(a["protection"] for a in result["armour"])
    result["power"] += result["weapon"]["power"]

    if result["potion"] is not None:
        if "power" in result["potion"]["effect"]:
            result["power"] += result["potion"]["effect"]["power"]

        if "protection" in result["potion"]["effect"]:
            result["protection"] += result["potion"]["effect"]["protection"]

        if "hp" in result["potion"]["effect"]:
            result["hp"] += result["potion"]["effect"]["hp"]

    return result
