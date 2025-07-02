from app.knight_setup.knight_data import KNIGHTS
from app.knight_setup.battle_preparation import Knight
from app.battle.battle import Battle


def battle(knights: dict) -> dict:
    all_knight_instances = \
        [Knight(knight_data=value) for value in knights.values()]
    lancelot = all_knight_instances[0]
    arthur = all_knight_instances[1]
    mordred = all_knight_instances[2]
    red_knight = all_knight_instances[3]

    Battle.vs(lancelot, mordred)

    Battle.vs(arthur, red_knight)

    return Battle.battle_results(all_knight_instances)


print(battle(KNIGHTS))
