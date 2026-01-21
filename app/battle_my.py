from app.class_knight import Knight


def one_on_one(first_knight: Knight, second_knight: Knight) -> dict:
    result = {}
    knight1 = first_knight
    knight2 = second_knight
    knight1.hp -= knight2.power - knight1.armour
    knight2.hp -= knight1.power - knight2.armour
    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0
    result[knight1.name] = knight1.hp
    result[knight2.name] = knight2.hp
    return result
