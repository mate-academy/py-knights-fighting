def check_hp(hp: int) -> int:
    # check if someone fell in battle
    return hp if hp > 0 else 0


def apply_potion(knights_list: list, name: str) -> None:
    # apply armour
    name["protection"] = 0
    for index in name["armour"]:
        name["protection"] += index["protection"]

    # apply weapon
    name["power"] += name["weapon"]["power"]

    if name["potion"] is not None:
        potion_effect = name["potion"]["effect"]
        for value in ["power", "protection", "hp"]:
            if value in potion_effect:
                name[value] += potion_effect[value]
