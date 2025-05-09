# apply armour
def apply_armour(warrior: dict) -> int:
    warrior["protection"] = 0
    for arms in warrior["armour"]:
        warrior["protection"] += arms["protection"]

    return warrior["protection"]


# apply weapon
def apply_weapon(warrior: dict) -> int:
    warrior["power"] += warrior["weapon"]["power"]

    return warrior["power"]


# apply potion if exist
def apply_potion(warrior: dict) -> None:
    if warrior["potion"] is not None:
        if "power" in warrior["potion"]["effect"]:
            warrior["power"] += warrior["potion"]["effect"]["power"]

        if "protection" in warrior["potion"]["effect"]:
            warrior["protection"] += (
                warrior)["potion"]["effect"]["protection"]

        if "hp" in warrior["potion"]["effect"]:
            warrior["hp"] += warrior["potion"]["effect"]["hp"]
