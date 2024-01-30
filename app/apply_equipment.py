def apply_armour(name: dict) -> None:
    name["protection"] = 0
    for part in name["armour"]:
        name["protection"] += part["protection"]
    return name["protection"]


def apply_weapon(name: dict) -> None:
    name["power"] += name["weapon"]["power"]
    return name["power"]


def apply_potion(name: dict) -> None:
    if name["potion"] is not None and "effect" in name["potion"]:
        potion_effect = name["potion"]["effect"]

        for attribute in ["power", "protection", "hp"]:
            if attribute in potion_effect:
                name[attribute] += potion_effect[attribute]
