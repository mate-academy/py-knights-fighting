from app.knight import Knight
from app.fight import fight_between


def battle(knights: dict) -> dict:
    knight1 = Knight(knights["lancelot"])
    knight2 = Knight(knights["arthur"])
    knight3 = Knight(knights["red_knight"])
    knight4 = Knight(knights["mordred"])
    all_knights = [knight1, knight2, knight3, knight4]

    fight_between(knight1, knight4)
    fight_between(knight2, knight3)

    return {knight.name: knight.hp for knight in all_knights}
