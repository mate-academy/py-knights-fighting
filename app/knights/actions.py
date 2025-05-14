def apply_weapon(knight: dict) -> None:
    knight["power"] += knight["weapon"]["power"]


def apply_armour(knight: dict) -> None:
    knight["protection"] = sum(
        element["protection"] for element in knight["armour"]
    )


def apply_potion(knight: dict) -> None:
    potion = knight.get("potion")

    if potion:
        effect = potion.get("effect", {})
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)
