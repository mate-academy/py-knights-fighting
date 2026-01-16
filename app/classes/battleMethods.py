from app.classes.knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:
    attack(knight_1, knight_2)
    check_dead(knight_1)
    check_dead(knight_2)


def attack(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection


def check_dead(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def get_results(knight_1: Knight,
                knight_2: Knight,
                knight_3: Knight,
                knight_4: Knight) -> dict:
    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp,
        knight_3.name: knight_3.hp,
        knight_4.name: knight_4.hp,
    }
