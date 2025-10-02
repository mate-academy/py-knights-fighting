from app.models import Knight


def create_knight(data: dict) -> Knight:
    return Knight(
        name=data["name"],
        hp=data["hp"],
        power=data["power"],
        armour=data["armour"],
        weapon=data["weapon"],
        potion=data["potion"],
    )


def battle(knights_config: dict) -> dict:
    knight_keys = ("lancelot", "arthur", "mordred", "red_knight")

    knights = {k: create_knight(knights_config[k]) for k in knight_keys}

    for knight in knights.values():
        knight.prepare()

    knights["lancelot"].damage(knights["mordred"].power)
    knights["mordred"].damage(knights["lancelot"].power)

    # Second pair
    knights["arthur"].damage(knights["red_knight"].power)
    knights["red_knight"].damage(knights["arthur"].power)

    # Return result
    return {knight.name: knight.hp for knight in knights.values()}
