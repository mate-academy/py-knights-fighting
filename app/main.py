from app.Knight import Knight
from app.KnightList import KNIGHTS
from app.Tournament import duels


def battle(contender_dict: dict) -> dict:
    contenders = Knight.prepare_to_battle(contender_dict)
    score = duels(contenders)
    return score


print(battle(KNIGHTS))
