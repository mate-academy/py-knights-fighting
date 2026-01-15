from app.knights import Knight


def fight(knight_1: Knight, knight_2: Knight) -> dict:
    knight_1.hp = max(0, knight_1.hp - (knight_2.power - knight_1.armour))
    knight_2.hp = max(0, knight_2.hp - (knight_1.power - knight_2.armour))

    return {knight_1.name: knight_1.hp, knight_2.name: knight_2.hp}
