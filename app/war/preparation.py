from app.warrior.knight import Knight


def preparation_to_fight(knight: Knight) -> None:
    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()
