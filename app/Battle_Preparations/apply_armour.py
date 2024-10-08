def apply_armour(knight: dict) -> None:
    for stats in knight.values():
        stats["protection"] = 0
        for armour in stats["armour"]:
            stats["protection"] += armour["protection"]
