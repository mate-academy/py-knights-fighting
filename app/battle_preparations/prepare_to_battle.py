from app.knight.knight_class import Knight


def prepare_to_battle(knights: dict) -> list:
    knights_instances = [
        Knight(knights[knight]["name"],
               knights[knight]["power"],
               knights[knight]["hp"],
               knights[knight]["armour"],
               knights[knight]["weapon"],
               knights[knight]["potion"])
        for knight in knights
    ]

    return knights_instances
