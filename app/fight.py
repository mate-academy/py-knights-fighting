from app.knight.one_knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> dict:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
    battle_result_hp = {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp
    }
    return battle_result_hp
