def check_hp(hp: int) -> int:
    # check if someone fell in battle
    if hp <= 0:
        hp = 0
    return hp


def apply_potion(knights_list: list, kn: str) -> None:
    # apply armour
    knights_list[kn]["protection"] = 0
    for knight in knights_list[kn]["armour"]:
        knights_list[kn]["protection"] += knight["protection"]

    # apply weapon
    knights_list[kn]["power"] += knights_list[kn]["weapon"]["power"]

    if knights_list[kn]["potion"] is not None:
        potion_effect = knights_list[kn]["potion"]["effect"]

        if "power" in potion_effect:
            knights_list[kn]["power"] += potion_effect["power"]

        if "protection" in potion_effect:
            knights_list[kn]["protection"] += potion_effect["protection"]

        if "hp" in potion_effect:
            knights_list[kn]["hp"] += potion_effect["hp"]
