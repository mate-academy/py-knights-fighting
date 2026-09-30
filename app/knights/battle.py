from app.knights.knights import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    damage_first_knight = knight2.power - knight1.protection
    damage_second_knight = knight1.power - knight2.protection
    if damage_first_knight > 0:
        knight1.hp -= damage_first_knight
    if damage_second_knight > 0:
        knight2.hp -= damage_second_knight

    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0
