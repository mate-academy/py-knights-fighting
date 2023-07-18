def apply_armor_and_weapon(knight: dict) -> None:
    knight["protection"] = sum(armor["protection"]
                               for armor in knight["armour"])
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def prepare_knight(knight: dict) -> None:
    apply_armor_and_weapon(knight)
    apply_potion(knight)
