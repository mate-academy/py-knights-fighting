from app.classes.knight import Knight


def fight(k_1: Knight, k_2: Knight) -> None:
    attack(k_1, k_2)
    if_died(k_1)
    if_died(k_2)


def attack(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection


def if_died(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def results(k1: Knight, k2: Knight, k3: Knight, k4: Knight) -> dict:
    return {
        k1.name: k1.hp,
        k2.name: k2.hp,
        k3.name: k3.hp,
        k4.name: k4.hp,
    }
