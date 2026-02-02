from app.knight.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power - knight1.protection)
    knight2.take_damage(knight1.power - knight2.protection)