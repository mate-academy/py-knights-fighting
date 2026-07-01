def apply_armour(knight: dict) -> None:
    knight["protection"] = 0

    for temp in knight["armour"]:
        knight["protection"] += temp["protection"]
