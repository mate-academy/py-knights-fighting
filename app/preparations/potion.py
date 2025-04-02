def count_potion(person: dict) -> None:
    if "power" in person["potion"]["effect"]:
        person["power"] += person["potion"]["effect"]["power"]

    if "protection" in person["potion"]["effect"]:
        person["protection"] += person["potion"]["effect"]["protection"]

    if "hp" in person["potion"]["effect"]:
        person["hp"] += person["potion"]["effect"]["hp"]
