from app.data.knight_data import KNIGHTS
from app.battle.preparation import preparations
from app.battle.fighting import fighting
from app.battle.results import results


def battle(data: dict) -> dict:
    # Preparation for battle
    for name in KNIGHTS:
        preparations(data, name)

    # The fight
    fighting("lancelot", "mordred", data)
    fighting("arthur", "red_knight", data)

    # Results of the fight
    return {
        results(data, knight)[0]: results(data, knight)[1]
        for knight in data
    }


print(battle(KNIGHTS))
