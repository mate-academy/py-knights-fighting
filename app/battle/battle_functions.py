from app.knights.knight_class import Knight


def perform_fight(knight_1: Knight, knight_2: Knight) -> None:

    damage_for_first_knight = knight_2.power - knight_1.protection
    damage_for_second_knight = knight_1.power - knight_2.protection
    knight_1.hp -= max(0, damage_for_first_knight)
    knight_2.hp -= max(0, damage_for_second_knight)


def show_result_battle(knight: Knight) -> None:

    knight.hp = max(0, knight.hp)
