def check_hp(hp: int) -> int:
    # check if someone fell in battle
    return hp if hp > 0 else 0


def apply_potion(knights_list: list, knight: str) -> None:
    # apply armour
    knights_list[knight]["protection"] = 0
    for index in knights_list[knight]["armour"]:
        knights_list[knight]["protection"] += index["protection"]

    # apply weapon
    knights_list[knight]["power"] += knights_list[knight]["weapon"]["power"]

    if knights_list[knight]["potion"] is not None:
        potion_effect = knights_list[knight]["potion"]["effect"]
        for value in ["power", "protection", "hp"]:
            if value in potion_effect:
                knights_list[knight][value] += potion_effect[value]
