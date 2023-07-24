from app.data.knight_data import KNIGHTS
from app.battle.preparation import preparations
from app.battle.fighting import fighting
from app.battle.results import results


def battle(data: dict) -> dict:
    """PREPARATION"""
    for name in KNIGHTS:
        preparations(data, name)

    """FIGHTING"""
    fighting("lancelot", "mordred", data)
    fighting("arthur", "red_knight", data)

    """RESULTS"""
    return {
        results(data, knight)[0]: results(data, knight)[1]
        for knight in data
    }


print(battle(KNIGHTS))
