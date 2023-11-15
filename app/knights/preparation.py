from app.knights.knight import Knight


def prepare_knights(knights_data: dict) -> list[Knight]:
    knights = [Knight(**knights_data[person]) for person in knights_data]
    for knight in knights:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    return knights
