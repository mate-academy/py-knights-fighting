def apply_armour(knight: dict) -> None:
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]


def battle_preparations(*knights) -> None:
    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
