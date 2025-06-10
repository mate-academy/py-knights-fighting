def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += (
                knight)["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
