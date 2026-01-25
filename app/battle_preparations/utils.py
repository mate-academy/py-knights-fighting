def apply_weapon(knights: dict) -> None:
    for knight, stats in knights.items():
        stats["power"] += stats["weapon"]["power"]


def apply_potion(knights: dict) -> None:
    for knight in knights.values():
        if knight["potion"] is not None:
            potion = knight["potion"]["effect"]
            if "power" in potion:
                knight["power"] += potion["power"]

            if "protection" in potion:
                knight["protection"] += potion["protection"]

            if "hp" in potion:
                knight["hp"] += potion["hp"]


def apply_armour(knights: dict) -> None:
    for stats in knights.values():
        stats["protection"] = 0
        for armour in stats["armour"]:
            stats["protection"] += armour["protection"]
