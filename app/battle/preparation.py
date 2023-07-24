from app.support.support_functions import apply


def preparations(data: dict, name: str) -> None:
    knight_name = data[name]

    # apply armour
    knight_name["protection"] = 0

    for part in knight_name["armour"]:
        knight_name["protection"] += part["protection"]

    # apply weapon
    knight_name["power"] += knight_name["weapon"]["power"]

    # apply potion if exist
    if knight_name["potion"]:
        for potion in ("power", "protection", "hp"):
            apply(potion, knight_name)
