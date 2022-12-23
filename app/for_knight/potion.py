def apply_potion(fighter: dict) -> None:
    if fighter["potion"] is not None:
        if "power" in fighter["potion"]["effect"]:
            fighter["power"] += fighter["potion"]["effect"]["power"]

        if "protection" in fighter["potion"]["effect"]:
            fighter["protection"] += fighter["potion"]["effect"]["protection"]

        if "hp" in fighter["potion"]["effect"]:
            fighter["hp"] += fighter["potion"]["effect"]["hp"]
