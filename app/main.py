from app.kamelot.knights_dict import KNIGHTS
from app.kamelot.knight import Knight
from app.kamelot.fighting import duel, standings


def battle(knights_config: dict) -> dict:
    knights_list = Knight.init_from_dict(knights_config)

    lancelot, arthur, mordred, red_knight = knights_list

    _ = duel(lancelot, mordred)
    _ = duel([arthur, red_knight])

    results = standings(lancelot, arthur, mordred, red_knight)

    return results


print(battle(KNIGHTS))
