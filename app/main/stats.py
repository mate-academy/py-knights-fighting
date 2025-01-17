def calculate_stats(knight: dict) -> None:
    knight["protection"] = sum(arm["protection"] for arm in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"]:
        effects = knight["potion"]["effect"]
        knight["power"] += effects.get("power", 0)
        knight["protection"] += effects.get("protection", 0)
        knight["hp"] += effects.get("hp", 0)
