from settings.data import KNIGHTS
from app.battle_implement.implementation import create_knight
from app.battle_implement.battle_process import battle, battles_result


def main(knights_dict):
    knights = [create_knight(knights_dict.get(knight)) for knight in knights_dict]

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]
    battle(lancelot, mordred)
    battle(arthur, red_knight)

    return battles_result(knights)


print(main(KNIGHTS))