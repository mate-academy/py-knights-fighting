from app.knights.data import Knight


def damage(knight: Knight, other_knight: Knight) -> None:
    knight.hp -= other_knight.power - knight.protection
    other_knight.hp -= knight.power - other_knight.protection
