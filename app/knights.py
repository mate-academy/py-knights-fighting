def apply_armor_and_weapon(knight: dict) -> None:
    knight["protection"] = sum(armor["protection"]
                               for armor in knight["armour"])
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        for key in ["power", "protection", "hp"]:
            knight[key] += effect.get(key, 0)


def prepare_knight(knight: dict) -> None:
    apply_armor_and_weapon(knight)
    apply_potion(knight)
