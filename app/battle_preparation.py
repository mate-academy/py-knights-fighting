def prepare(knights: dict) -> None:

    for knight, stats in knights.items():
        stats["protection"] = 0
        stats["power"] += stats["weapon"]["power"]

        for arm in stats["armour"]:
            stats["protection"] += arm["protection"]

        if stats["potion"] is not None:
            if "power" in stats["potion"]["effect"]:
                stats["power"] += stats["potion"]["effect"]["power"]
            if "protection" in stats["potion"]["effect"]:
                stats["protection"] += stats["potion"]["effect"]["protection"]
            if "hp" in stats["potion"]["effect"]:
                stats["hp"] += stats["potion"]["effect"]["hp"]
