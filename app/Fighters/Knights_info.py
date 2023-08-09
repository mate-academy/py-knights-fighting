def count_armours_protection(armours: list) -> int:
    current_protection = 0
    for armour_part in armours:
        current_protection += armour_part["protection"]
    return current_protection


def fill_knight_info(knight_dict: dict) -> dict:
    knight_protection = count_armours_protection(knight_dict["armour"])

    current_knight = {
        "name": knight_dict["name"],
        "power": knight_dict["power"],
        "hp": knight_dict["hp"],
        "protection": knight_protection
    }

    # apply weapon
    current_knight["power"] += knight_dict["weapon"]["power"]

    # apply potion if exist
    if knight_dict["potion"] is not None:
        apply_potion(current_knight, knight_dict["potion"]["effect"])

    return current_knight


def apply_potion(current_knight: dict, potion_effect: dict) -> None:
    if potion_effect.get("power"):
        current_knight["power"] += potion_effect["power"]

    if potion_effect.get("hp"):
        current_knight["hp"] += potion_effect["hp"]

    if potion_effect.get("protection"):
        current_knight["protection"] += potion_effect["protection"]
