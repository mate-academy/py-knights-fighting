from app.data import KNIGHTS
from app.battle_implement.implementation import create_knight
from app.battle_implement.battle_process import battle_process, battles_result


def battle(knights_dict: dict) -> dict:
    knights = [create_knight(knights_dict.get(knight))
               for knight in knights_dict]

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]
    battle_process(lancelot, mordred)
    battle_process(arthur, red_knight)

    return battles_result(knights)


if __name__ == "__main__":
    print(battle(KNIGHTS))
