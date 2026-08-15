def prepare_knight(knight: dict) -> None:
    knight["protection"] = 0

    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]


def fight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: dict) -> dict:

    for knight_key in ["lancelot", "arthur", "mordred", "red_knight"]:
        prepare_knight(knights_config[knight_key])

    fight(knights_config["lancelot"], knights_config["mordred"])
    fight(knights_config["arthur"], knights_config["red_knight"])

    return {
        knight["name"]: knight["hp"]
        for knight in knights_config.values()
    }
