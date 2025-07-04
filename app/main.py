from app.knight_setup.knight_data import KNIGHTS
from app.knight_setup.battle_preparation import Knight
from app.battle.battle import Battle


def battle(knights: dict) -> dict:
    lancelot = Knight(knight_data=knights["lancelot"])
    arthur = Knight(knight_data=knights["arthur"])
    mordred = Knight(knight_data=knights["mordred"])
    red_knight = Knight(knight_data=knights["red_knight"])

    Battle.vs(lancelot, mordred)

    Battle.vs(arthur, red_knight)

    return Battle.battle_results([lancelot, arthur, mordred, red_knight])


print(battle(KNIGHTS))
