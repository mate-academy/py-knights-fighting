from app.knights_fighting.knight import Knight


def all_fights(knights: dict) -> tuple:
    knight1, knight2 = Knight(knights["lancelot"]), Knight(knights["mordred"])
    knight1.modify_knight()
    knight2.modify_knight()
    fight(knight1, knight2)
    print(knight1.get_hp(), knight1.get_power(), knight1.get_protection())
    print(knight2.get_hp(), knight2.get_power(), knight2.get_protection())
    knight3, knight4 = Knight(knights["arthur"]), Knight(knights["red_knight"])
    knight3.modify_knight()
    knight4.modify_knight()
    fight(knight3, knight4)
    return knight1, knight2, knight3, knight4


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
        "Lancelot": all_knights[0].get_hp(),
        "Arthur": all_knights[2].get_hp(),
        "Mordred": all_knights[1].get_hp(),
        "Red Knight": all_knights[3].get_hp()
    }
