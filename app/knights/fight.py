from app.knights.base_class import Knight


def fight(knight_one: Knight, knight_two: Knight) -> dict:
    knight_one.hp -= knight_two.power - knight_one.protection
    knight_two.hp -= knight_one.power - knight_two.protection

    for knight in (knight_one, knight_two):
        if knight.hp <= 0:
            knight.hp = 0

    return {
        knight_one.name: knight_one.hp,
        knight_two.name: knight_two.hp
    }
