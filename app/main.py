from app.knight import Knight
from app.knights_dict import KNIGHTS


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    return Knight.duel(lancelot, mordred) | Knight.duel(arthur, red_knight)


print(battle(KNIGHTS))
