def apply_armour(knight: dict) -> None:
    knight["protection"] = sum(
        armour["protection"]
        for armour in knight["armour"]
    )


def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict) -> None:
    if knight["potion"] is not None:
        for effect_key, effect_value in knight["potion"]["effect"].items():
            if effect_key in knight:
                knight[effect_key] += effect_value


def preparation(*knights: dict) -> None:
    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
