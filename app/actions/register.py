from app.people.knight import Knight


def register_knights(knights: dict) -> list:
    registered_knights = []
    for person in knights:
        new_register = Knight(
            knights[person]["name"],
            knights[person]["power"],
            knights[person]["hp"],
            knights[person]["armour"],
            knights[person]["weapon"],
            knights[person]["potion"]
        )
        registered_knights.append(new_register)

    return registered_knights
