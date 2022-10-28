def get_ready(knights_config: dict) -> dict:
    for person in knights_config.keys():
        king = knights_config[person]
        king["protection"] = 0

        for part in king["armour"]:
            king["protection"] += part["protection"]

        if king["potion"] is not None:
            for effect in king["potion"]["effect"]:
                king[effect] += king["potion"]["effect"][effect]

        king["power"] += king["weapon"]["power"]
    return knights_config
