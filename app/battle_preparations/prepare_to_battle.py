from app.knight.knight_class import Knight


def preparations(knights: dict) -> list:
    knights_instances = [
        Knight(knights[knight]["name"],
               knights[knight]["power"],
               knights[knight]["hp"])
        for knight in knights
    ]

    for knight_inst in knights_instances:
        knight_inst.apply_armor(knights)

    for knight_inst in knights_instances:
        knight_inst.equip_weapon(knights)

    for knight_inst in knights_instances:
        knight_inst.use_potion(knights)

    return knights_instances
