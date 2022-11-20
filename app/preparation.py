def set_stats_hero(knights_config: dict) -> dict:
    for person in knights_config:
        knight = knights_config[person]
        knight["protection"] = 0

        for part in knight["armour"]:
            knight["protection"] += part["protection"]

        if knight["potion"] is not None:
            for effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]

        knight["power"] += knight["weapon"]["power"]
    return knights_config
