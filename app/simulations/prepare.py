from app.models.knight_class import Knight


def prepare_knight(knight: Knight) -> Knight:
    return knight.apply_armor().apply_weapon().apply_potion()
