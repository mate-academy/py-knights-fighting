def apply_stats(knight: dict) -> None:
    knight["protection"] = sum(arm["protection"] for arm in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value
