def apply_upgrades(knight: dict) -> None:
    # Apply armour
    knight["protection"] = sum(
        a["protection"] for a in knight.get("armour", []))

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if exists
    potion = knight.get("potion")
    if potion:
        effect = potion.get("effect", {})
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def builds(knights: dict) -> None:
    for knight in knights.values():
        apply_upgrades(knight)
