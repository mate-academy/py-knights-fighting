def apply_armour(knights: dict) -> None:
    for stats in knights.values():
        stats["protection"] = 0
        for armour in stats["armour"]:
            stats["protection"] += armour["protection"]
