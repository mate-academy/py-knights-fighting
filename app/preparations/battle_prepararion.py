from app.knight.create_knight import Knight


def applied_equipments(knight: Knight) -> None:

    # apply armour
    if knight.armour:
        knight.apply_armour()

    # apply weapon
    knight.apply_weapon()

    # apply potion if exist
    if knight.potion is not None:
        knight.apply_potion()
