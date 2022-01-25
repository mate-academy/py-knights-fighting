def feature_count(knightsConfig, knight_2):
    result = knightsConfig[knight_2]
    result["protection"] = sum(armour["protection"]
                               for armour in result["armour"])
    result["power"] += result["weapon"]["power"]

    stats = ("protection", "power", "hp")

    if result["potion"] is not None:
        for statistic in stats:
            if statistic in result["potion"]["effect"]:
                result[statistic] += result["potion"]["effect"][statistic]

    return result
