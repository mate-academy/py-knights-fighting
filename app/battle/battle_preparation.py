from app.participants.knight import Knight


def prepare_the_knight(knight: Knight) -> None:
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()
