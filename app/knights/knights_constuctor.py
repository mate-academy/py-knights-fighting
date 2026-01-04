from app.knights.knight import Knight


def knights_constructor(knights: {dict}) -> dict:
    knights_list = {}
    for knight in knights.values():
        knight_model = Knight(
            name=knight["name"],
            hp=knight["hp"],
            power=knight["power"])

        knight_model.health_points(
            armours=knight["armour"],
            potion=knight["potion"],
            weapon=knight["weapon"])
        knights_list[knight_model.name] = knight_model
    return knights_list
