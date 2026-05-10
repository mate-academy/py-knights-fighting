def stats(knights_config: dict) -> dict:
    knights_stats = {}
    for key, value in knights_config.items():
        effect_list = {"power": 0, "protection": 0, "hp": 0}
        if value["potion"] is not None:
            for effect in effect_list.keys():
                if effect in value["potion"]["effect"]:
                    effect_list[effect] = value["potion"]["effect"][effect]
        name = key
        hp = value["hp"] + effect_list["hp"]
        power = \
            value["power"] + value["weapon"]["power"] + effect_list["power"]
        protection = protection_calculation(value) + effect_list["protection"]
        stats_one_knight = \
            {"hp": hp, "power": power, "protection": protection}
        knights_stats[name] = stats_one_knight
    return knights_stats


def protection_calculation(knights_config: dict) -> int:
    protection = 0
    for item in knights_config["armour"]:
        protection += item["protection"]
    return protection
