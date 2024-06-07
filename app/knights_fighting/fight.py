from app.knights_fighting.knight import Knight


def all_fights(knights: dict) -> list:
    list_of_knights = [
        Knight(knights["lancelot"]),
        Knight(knights["mordred"]),
        Knight(knights["arthur"]),
        Knight(knights["red_knight"])
    ]
    for knight_fight in range(0, 4, 2):
        list_of_knights[knight_fight].modify_knight()
        list_of_knights[knight_fight + 1].modify_knight()
        fight(list_of_knights[knight_fight], list_of_knights[knight_fight + 1])

    return list_of_knights


def fight(fighter1: Knight, fighter2: Knight) -> tuple:
    fighter1.hp -= fighter2.power - fighter1.protection
    fighter2.hp -= fighter1.power - fighter2.protection
    check_for_defeat(fighter1)
    check_for_defeat(fighter2)
    return fighter1, fighter2


def check_for_defeat(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def get_result_of_all_fights(knights: dict) -> dict:
    all_knights = all_fights(knights)
    return {
        "Lancelot": all_knights[0].hp,
        "Arthur": all_knights[2].hp,
        "Mordred": all_knights[1].hp,
        "Red Knight": all_knights[3].hp
    }
