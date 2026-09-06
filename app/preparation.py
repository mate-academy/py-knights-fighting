def prepare_knight(knight: dict) -> None:
    knight["protection"] = sum(
        armour["protection"] for armour in knight["armour"]
    )
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]

        knight["power"] += effects.get("power", 0)
        knight["protection"] += effects.get("protection", 0)
        knight["hp"] += effects.get("hp", 0)
