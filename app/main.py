from app.knights.data import Knight
from app.battle.combat import combat


def battle(knights: dict) -> dict:
    # create every knight
    for knight in knights:
        Knight(knights[knight])
    # this return combat results
    return combat(Knight.dict_of_knights)
