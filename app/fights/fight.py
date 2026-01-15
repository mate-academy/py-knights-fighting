from app.knights.knight import Knight


def fight(knight_one: Knight, knight_two: Knight) -> dict:
    damage_one = knight_one.power - knight_two.protection
    damage_two = knight_two.power - knight_one.protection

    knight_one.hp -= damage_two
    knight_two.hp -= damage_one

    knight_one.hp = max(knight_one.hp, 0)
    knight_two.hp = max(knight_two.hp, 0)

    battle_result = {
        knight_one.name: knight_one.hp,
        knight_two.name: knight_two.hp
    }
    return battle_result
