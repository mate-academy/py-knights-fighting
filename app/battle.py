from app.class_knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= (knight2.power - knight1.protection)
    knight2.hp -= (knight1.power - knight2.protection)


def check_hp(knights: dict[Knight]) -> None:
    for knight in knights.values():
        if knight.hp <= 0:
            knight.hp = 0
