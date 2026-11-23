def prepare_knight(knight: dict) -> None:
    knight["protection"] = sum(
        armour["protection"]
        for armour in knight["armour"]
    )

    knight["power"] += knight["weapon"]["power"]

    potion = knight["potion"]
    if potion is None:
        return

    effects = potion["effect"]

    knight["power"] += effects.get("power", 0)
    knight["protection"] += effects.get("protection", 0)
    knight["hp"] += effects.get("hp", 0)


def prepare_knights(knights: dict) -> None:
    for knight in knights.values():
        prepare_knight(knight)
