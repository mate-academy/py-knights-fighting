def config_knight(all_knights: dict) -> dict:
    knight_dict = {}
    for name, stats in all_knights.items():
        knight_dict.update({name: stats})
        # apply armour
        stats["protection"] = 0
        for armour in stats["armour"]:
            stats["protection"] += armour["protection"]

        # apply weapon
        stats["power"] += stats["weapon"]["power"]

        # apply potion
        if stats["potion"] is not None:
            for potion in stats["potion"]["effect"]:
                if potion in stats["potion"]["effect"]:
                    stats[potion] += stats["potion"]["effect"][potion]

    return knight_dict
