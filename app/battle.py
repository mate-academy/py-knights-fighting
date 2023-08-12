from app.knight_class import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0


def results(knights: list[Knight]) -> dict:
    return {knight.name: knight.hp for knight in knights}
