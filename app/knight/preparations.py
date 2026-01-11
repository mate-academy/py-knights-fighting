from app.knight.knight import Knight


def prepare_knight_to_battle(knight: Knight) -> None:
    # apply armour
    knight.apply_armour()

    # apply weapon
    knight.apply_weapon()

    # apply potion if exist
    knight.apply_potion()
