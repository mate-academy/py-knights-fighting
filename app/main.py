from app.battle_knights.battle import BattleF
from app.battle_knights.knights_dict import knights


def battle(dict_person=knights):
    total_hps = {}
    battlefield = BattleF(knights_d=dict_person)
    battlefield = battlefield.total_hp()
    for knight_k, value in battlefield.items():
        if value <= 0:
            value = 0
        total_hps[knights[knight_k]["name"]] = value
    return total_hps
