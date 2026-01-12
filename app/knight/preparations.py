from app.knight.knight import Knight


def prepare_knight_to_battle(knight: Knight) -> None:
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()
