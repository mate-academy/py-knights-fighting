from copy import deepcopy


def prepare_knight(knight: dict) -> dict:
    knight = deepcopy(knight)

    # Apply armour
    knight["protection"] = 0

    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion
    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value

    return knight
