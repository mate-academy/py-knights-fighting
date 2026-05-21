def knights_preparing(knight: dict) -> None:
    knight["protection"] = 0
    if knight["armour"]:
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        for stat, value in effects.items():
            knight[stat] += value
