def warrior(knight: dict) -> dict:
    # apply armour
    knight["protection"] = sum(
        [armour["protection"] for armour in knight["armour"]]
    )

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    herb = knight["potion"]

    if herb is not None:
        effect = herb["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)

    return {
        "power": knight["power"],
        "protection": knight["protection"],
        "hp": knight["hp"],
        "name": knight["name"]
    }
