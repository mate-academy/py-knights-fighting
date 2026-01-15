def change_in_characteristics(knights_configs: dict) -> dict:
    knights_configs["protection"] = 0
    for armour_protection in knights_configs["armour"]:
        knights_configs["protection"] += armour_protection["protection"]

    knights_configs["power"] += knights_configs["weapon"]["power"]

    if knights_configs["potion"] is not None:
        if "power" in knights_configs["potion"]["effect"]:
            knights_configs["power"] += (
                knights_configs)["potion"]["effect"]["power"]

        if "protection" in knights_configs["potion"]["effect"]:
            knights_configs["protection"] += (
                knights_configs)["potion"]["effect"]["protection"]

        if "hp" in knights_configs["potion"]["effect"]:
            knights_configs["hp"] += (
                knights_configs)["potion"]["effect"]["hp"]
    return knights_configs
