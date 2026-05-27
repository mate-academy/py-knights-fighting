from app.warriors.knights import Knight


def conducting_battle(knight_one: Knight, knight_two: Knight) -> None:

    dmg_to_knight_one = knight_two.power - knight_one.protection
    knight_one.hp -= dmg_to_knight_one

    dmg_to_knight_two = knight_one.power - knight_two.protection
    knight_two.hp -= dmg_to_knight_two

    if knight_one.hp <= 0:
        knight_one.hp = 0

    if knight_two.hp <= 0:
        knight_two.hp = 0
