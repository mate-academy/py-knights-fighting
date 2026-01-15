from app.knight.one_knight import Knight


def armour_preparation(knight: Knight) -> int:
    new_protection = sum([i["protection"] for i in knight.armour])
    knight.protection = new_protection
    return knight.protection
