from app.Knight.knight import Knight


def preparation(knights: dict) -> list:
    knights_list = []

    for knight in knights.values():
        person = Knight(knight["name"], knight["power"], knight["hp"])
        person.get_weapon(knight)
        person.get_armour(knight)
        person.get_potion(knight)
        knights_list.append(person)

    return knights_list
