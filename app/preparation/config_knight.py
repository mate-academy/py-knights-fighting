def config_knight(all_knights: dict) -> dict:
    for knight in all_knights:
        person = all_knights[knight]
        all_knights.update({knight: person})
        # apply armour
        person["protection"] = 0
        for armour in person["armour"]:
            person["protection"] += armour["protection"]

        # apply weapon
        person["power"] += person["weapon"]["power"]

        # apply potion
        if person["potion"] is not None:
            if "power" in person["potion"]["effect"]:
                person["power"] += person["potion"]["effect"]["power"]

            if "protection" in person["potion"]["effect"]:
                person["protection"] += person["potion"]["effect"]["protection"]

            if "hp" in person["potion"]["effect"]:
                person["hp"] += person["potion"]["effect"]["hp"]

    return all_knights
