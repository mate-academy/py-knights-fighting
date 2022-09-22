def prepare(knights_config: dict, knight: str) -> dict:
    current_knight = knights_config[knight]

    current_knight["protection"] = 0
    for armour_part in current_knight["armour"]:
        current_knight["protection"] += armour_part["protection"]
    current_knight["power"] += current_knight["weapon"]["power"]

    if current_knight["potion"] is not None:
        potion_effects = ["power", "protection", "hp"]
        for effect in potion_effects:
            if effect in current_knight["potion"]["effect"]:
                new_effect = current_knight["potion"]["effect"][effect]
                current_knight[effect] += new_effect

    return current_knight
