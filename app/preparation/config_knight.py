def config_knight(all_knights: dict) -> dict:
    for person in all_knights.items():
        # apply armour
        person[1]["protection"] = 0
        for armour in person[1]["armour"]:
            person[1]["protection"] += armour["protection"]

        # apply weapon
        person[1]["power"] += person[1]["weapon"]["power"]

        # apply potion
        if person[1]["potion"] is not None:
            for potion in person[1]["potion"]["effect"]:
                if potion in person[1]["potion"]["effect"]:
                    person[1][potion] += person[1]["potion"]["effect"][potion]

    return all_knights
