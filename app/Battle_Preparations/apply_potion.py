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
